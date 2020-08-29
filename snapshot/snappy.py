import boto3
import os

os.environ['AWS_DEFAULT_REGION'] = "us-east-2"

if __name__ == '__main__':
    session = boto3.Session(profile_name='WS-000G-role_DEVOPS')
    ec2 = session.resource('ec2')

    for i in ec2.instances.all():
        print(i)
