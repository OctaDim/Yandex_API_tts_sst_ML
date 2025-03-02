import boto3

from configs.settings import BOTO_V3_CONFIGS


class BotoS3Session:

    def __init__(self,
                 service_name: str = BOTO_V3_CONFIGS.SERVICE_NAME,
                 endpoint_url: str = BOTO_V3_CONFIGS.ENDPOINT_URL):
        self.service_name = service_name
        self.endpoint_url = endpoint_url
        self.s3_session = None

    def __enter__(self):
        session = boto3.session.Session()
        self.s3_session = session.client(service_name=self.service_name,
                                         endpoint_url=self.endpoint_url)
        return self.s3_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s3_session.close()
