import uvicorn
from fastapi import File, UploadFile, FastAPI, Query
from fastapi.responses import FileResponse
import boto3
from botocore.exceptions import ClientError
import io


app = FastAPI()

def upload_file(bucket: str, folder: str, file_as_binary: str, file_name: str):
    """ uploads file to S3
    Args:
        bucket str: S3 Bucket Name
        folder str: Subpath in S3 of file
        file_as_binary str: data of file in binary string
        file_name str: filename to upload on S3.
    """
    s3_client = boto3.client('s3')
    file_as_binary = io.BytesIO(file_as_binary)
    key = folder+"/"+file_name
    try:
        s3_client.upload_fileobj(file_as_binary, bucket, key)
    except ClientError as e:
        print(e)

        return False
    return True


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """ Api takes Multipart file as input and uploades the file to S3.
    Args:
        file File: Multipart file
    """
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)

        #get file as binary
        file_binary = open(file.filename, "rb").read()
        #uploading file
        upload_file("ts-tasks", "upload_data", file_binary, file.filename)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}


@app.get('/list_files_s3')
def list_files_s3() -> list:
    """ Get files from S3 and return the list
    Returns: List of s3 files        
    """   
    session = boto3.Session()
    s3_prefix="upload_data/"
    list_of_files = []
    s3 = session.resource('s3')
    my_bucket = s3.Bucket('ts-tasks')
    for my_bucket_object in my_bucket.objects.all():
        s3_object = my_bucket_object.key.replace(s3_prefix, "")
        if s3_object:
            list_of_files.append(s3_object)
    return {"list_of_s3_files": list_of_files}


def download_file_from_s3(key: str):
    """ Downloads specific file from S3.
    Args:
        key str: filename to download from S3.
    """
    s3_prefix="upload_data/"
    s3 = boto3.resource('s3')
    try:
        s3.Bucket('ts-tasks').download_file(f"{s3_prefix}{key}", f"downloads/{key}")
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


@app.get('/download_file')
async def download_file(file_name:str):
    """ Api to download the file on user's local box.
    Args:
        file_name str: filename which needs to download from S3.
    """
    download_file_from_s3(file_name)
    file_path = f"downloads/{file_name}"
    return FileResponse(path=file_path, filename=file_path)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


