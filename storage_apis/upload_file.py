import requests

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'file': open('sample_new.txt', 'rb'),
}

response = requests.post('http://3.71.186.106/upload', headers=headers, files=files)

print("File Uploaded successfully ")