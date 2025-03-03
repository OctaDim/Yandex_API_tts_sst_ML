#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Literal

from utils_Boto_s3.boto_s3_session_manager import BotoS3Session


def create_new_bucket_s3(bucket_name: str) -> None:
    with BotoS3Session() as s3_session:
        response = s3_session.create_bucket(Bucket=bucket_name)
        print(f"Bucket created [OK]: Bucket={bucket_name}, "
              f"response={response}, type(response)={type(response)}")
        return response


def upload_str_to_obj_storage_s3(
        bucket: str,
        body: str,
        key: str,  # distant path in bucket "folder/sub_folder/file.txt"
        storage_class: Literal["STANDARD", "COLD", "ICE"] = "STANDARD",
        extra_args: dict = None
) -> None:
    with BotoS3Session() as s3_session:
        response = s3_session.put_object(Bucket=bucket,
                                         Key=key,
                                         Body=body,
                                         StorageClass=storage_class,
                                         ExtraArgs=extra_args)
        print(f"Object put [OK]: Bucket={bucket}, Key={key}, "f"Body={body}, "
              f"StorageClass={storage_class}, ExtraArgs={extra_args}, "
              f"response={response}, type(response)={type(response)}")
        return response


def upload_file_to_obj_storage_s3(
        bucket: str,
        file_name: str,  # path to local file"/path/to/local/file.txt"
        key: str,  # distant path in bucket "folder/sub_folder/file.txt"
        storage_class: Literal["STANDARD", "COLD", "ICE"] = "STANDARD",
        extra_args: dict = None
) -> None:
    with BotoS3Session() as s3_session:
        response = s3_session.upload_file(Bucket=bucket,
                                          Filename=file_name,
                                          Key=key,
                                          StorageClass=storage_class,
                                          ExtraArgs=extra_args)
        print(f"Object put [OK]: Bucket={bucket}, Filename={file_name}, "
              f"Key={key}, StorageClass={storage_class}, ExtraArgs={extra_args}, "
              f"response={response}, type(response)={type(response)}")
        return response


def get_obj_from_obj_storage(bucket: str, key: str) -> List[dict]:
    with BotoS3Session() as s3_session:
        response_obj = s3_session.get_object(Bucket=bucket, Key=key)
        if "Body" in response_obj:
            body = response_obj["Body"].read()
            print(f"Object got [OK]: Bucket={bucket}, Key={key}, "
                  f"response_obj={response_obj}, "
                  f"type(response_obj)={type(response_obj)}, "
                  f"body={body}")
            return body


def get_objs_list_from_obj_storage(
        bucket: str,
        key: str,  # distant path in bucket "folder/sub_folder/file.txt"
) -> None:
    with BotoS3Session() as s3_session:
        response_objs = s3_session.list_objects(Bucket=bucket, Key=key)
        if "Contents" in response_objs:
            contents = response_objs["Contents"]
            print(f"Objects got [OK]: Bucket={bucket}, Key={key}, "
                  f"response_objs={response_objs}, "
                  f"type(response_objs)={type(response_objs)}, "
                  f"contents={contents}")
            return contents


def delete_objs_from_obj_storage(
        bucket: str,
        objects_keys: str,  # distant objs paths in bucket "folder/sub_folder/file.txt"
) -> None:
    with BotoS3Session() as s3_session:
        for_deletion = [{"Key": obj_key} for obj_key in objects_keys]
        response = s3_session.delete_objects(Bucket="bucket-name",
                                             Delete={"Objects": for_deletion})
        print(f"Objects got [OK]: Bucket={bucket}, "
              f"objects_keys={objects_keys}, for_deletion={for_deletion}, "
              f"response={response}, type(response)={type(response)}")
        return response
