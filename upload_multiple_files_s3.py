#how to upload multiple files to S3 bucket
import os
import glob

cwd=os.getcwd()

cwd=cwd+"/upload/"

files=glob.glob(cwd+"*.txt")

files

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=text,
    Bucket="kparham-bucket-test-boto3",
    Key=file.split("/")[-1])