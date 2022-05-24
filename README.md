# ts-task


Prerequisite: 
1. Install AWS CLI, 
sudo apt install awscli
2. docker and docker-compose

Steps for the task.
1. git clone , cd inside git directory
2. copy/download the data to src/dataset, 

mkdir src/dataset
export AWS_ACCESS_KEY_ID=<>
export AWS_SECRET_ACCESS_KEY=<>
export AWS_DEFAULT_REGION=eu-central-1
aws s3 cp s3://career-builder-source/source_data/marketing_sample_for_careerbuilder_usa-careerbuilder_job_listing__20200401_20200630__30k_data.ldjson src/dataset/

3. 
 3.1 docker-compose up -d
 3.2 docker ps
 3.3 docker logs jupyter-notebook
    - copy the URL,
    - replace the 127.0.0.1 from your public IP.
    - Example:
    - http://127.0.0.1:8888/lab?token=ef513ec40756ffb2fef37fc8b1b096a3202fc22103f069ef
    - http://3.68.160.135:8888/lab?token=ef513ec40756ffb2fef37fc8b1b096a3202fc22103f069ef
