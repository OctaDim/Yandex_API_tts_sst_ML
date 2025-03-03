import boto3

from configs.settings import BOTO_V3_CONFIGS
from configs.yandex_credentials import (
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


class BotoS3Session:

    def __init__(self,
                 aws_access_key_id: str = AWS_ACCESS_KEY_ID,
                 aws_secret_access_key: str = AWS_SECRET_ACCESS_KEY,
                 service_name: str = BOTO_V3_CONFIGS.SERVICE_NAME,
                 endpoint_url: str = BOTO_V3_CONFIGS.ENDPOINT_URL):
        self.service_name = service_name
        self.endpoint_url = endpoint_url
        self.__aws_access_key_id = aws_access_key_id
        self.__aws_secret_access_key = aws_secret_access_key
        self.s3_session = None

    def __enter__(self):
        session = boto3.session.Session(
            aws_access_key_id=self.__aws_access_key_id,
            aws_secret_access_key=self.__aws_secret_access_key)
        self.s3_session = session.client(service_name=self.service_name,
                                         endpoint_url=self.endpoint_url)
        print(f"Boto s3 session created: "
              f"service_name: {self.service_name}, "
              f"endpoint_url: {self.endpoint_url}")
        return self.s3_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s3_session.close()
        print(f"Boto s3 session closed")
