# ts-task


Prerequisite: 
1. Install AWS CLI, 
sudo apt install awscli
2. docker and docker-compose

Steps for the task.
1. git clone , cd inside git directory
2. copy/download the data to src/dataset, 

- mkdir src/dataset
- export AWS_ACCESS_KEY_ID=<>
- export AWS_SECRET_ACCESS_KEY=<>
- export AWS_DEFAULT_REGION=eu-central-1
- aws s3 cp s3://career-builder-source/source_data/marketing_sample_for_careerbuilder_usa-careerbuilder_job_listing__20200401_20200630__30k_data.ldjson src/dataset/

3. 
 - docker-compose up -d
 - docker ps
 - docker logs jupyter-notebook
    - copy the URL,
    - replace the 127.0.0.1 from your public IP.
    - Example:
    - http://127.0.0.1:8888/lab?token=ef513ec40756ffb2fef37fc8b1b096a3202fc22103f069ef
    - http://3.68.160.135:8888/lab?token=ef513ec40756ffb2fef37fc8b1b096a3202fc22103f069ef



--------------------------------
--------------------------------

## STORAGE APIs

### Steps to Setup and Start server
#### 1. Launch EC2,
#### 2. Install python3, and pip3.
#### 3. install these requirements

```
    sudo apt-get update
    sudo apt install python3-pip
    pip3 install -r requirements.txt

    ---- requirements -----
    anyio==3.4.0
    asgiref==3.4.1
    certifi==2021.10.8
    charset-normalizer==2.0.9
    click==8.0.3
    fastapi==0.70.0
    h11==0.12.0
    idna==3.3
    pydantic==1.8.2
    python-dotenv==0.19.2
    requests==2.26.0
    sniffio==1.2.0
    starlette==0.16.0
    typing_extensions==4.0.1
    urllib3==1.26.7
    uvicorn==0.16.0
    -----------------------

```

#### 4. Install Nginx, and ssl certificate
```
sudo apt install nginx
sudo apt-get install openssl
cd /etc/nginx
sudo mkdir ssl
sudo openssl req -batch -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout /etc/nginx/ssl/server.key \
-out /etc/nginx/ssl/server.crt

cd /etc/nginx/sites-enabled/
sudo nano fastapi_nginx

server {
    listen 80;
    listen 443 ssl;
    ssl on;
    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    server_name 3.71.186.106;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

Note: 3.71.186.106 is the public IP of EC2.
Add inbound rule in EC2 for port 8000 (Custom TCP)


sudo service nginx restart
```

#### 5.Steps to Start the server

```
export AWS_ACCESS_KEY_ID=<>
export AWS_SECRET_ACCESS_KEY=<>
export AWS_DEFAULT_REGION=eu-central-1
```

To start the server hit this command.
add the storage_api.py file on EC2 and hit below command.
```
nohup python3 -u -m uvicorn storage_api:app > out_storage_api.log &
```


#### 6. Test The API
Go To this URL: http://3.71.186.106/docs
