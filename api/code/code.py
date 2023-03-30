import boto3
import os
from common.configs import get_configs
# setting up aws session and environment
STAGE = os.getenv("STAGE", "DEV")
CONFIGS = get_configs(STAGE)
new_session = boto3.Session(aws_access_key_id=CONFIGS["AWS_ACCESS_KEY"],
                            aws_secret_access_key=CONFIGS['AWS_SECRET_ACCESS_KEY'],
                            aws_session_token=CONFIGS['SESSION_TOKEN'])
s3 = new_session.client('s3')


def str_hello_world() -> str:
    str = 'Hello, World!'
    return str


def list_s3_folder_contents(bucket: str, path: str) -> list:
    object_list = s3.list_objects_v2(
        Bucket=bucket,
        Prefix=path)
    key_array = []
    for vals in object_list['Contents']:
        if vals['Key'][len(vals['Key']) - 1] != '/':
            key_array.append(vals['Key'])
        else:
            print(f'This is the folder: {vals["Key"]}')
    return key_array


def run():
    list = list_s3_folder_contents(
        CONFIGS['PHOTO_BUCKET'], CONFIGS['PHOTO_PATH'])
    print(list)


if __name__ == '__main__':
    run()
