import boto3
import json

ec2 = boto3.resource('ec2', region_name='us-east-1')
def lambda_handler(event, context):
    instances = ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        },
        {
            'Name': 'tag:environment',
            'Values':['dev']
        }
    ])
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).stop()
        print("Instance ID is started :- "+instance.id)
    return "success"