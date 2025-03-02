#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Literal

from utils_Boto_s3.s3_session_manager import BotoS3Session


def create_new_bucket_s3(bucket_name: str) -> None:
    with BotoS3Session() as s3_session:
        s3_session.create_bucket(Bucket=bucket_name)


def upload_str_to_obj_storage_s3(
        bucket: str,
        body: str,
        key: str,  # distant path in bucket "folder/sub_folder/file.txt"
        storage_class: Literal["STANDARD", "COLD", "ICE"] = "STANDARD",
        extra_args: dict = None
) -> None:
    with BotoS3Session() as s3_session:
        s3_session.put_object(
            Bucket=bucket, Key=key, Body=body,
            StorageClass=storage_class, ExtraArgs=extra_args)


def upload_file_to_obj_storage_s3(
        bucket: str,
        file_name: str,  # path to local file"/path/to/local/file.txt"
        key: str,  # distant path in bucket "folder/sub_folder/file.txt"
        storage_class: Literal["STANDARD", "COLD", "ICE"] = "STANDARD",
        extra_args: dict = None
) -> None:
    with BotoS3Session() as s3_session:
        s3_session.upload_file(
            Bucket=bucket, Filename=file_name, Key=key,
            StorageClass=storage_class, ExtraArgs=extra_args)


def get_objs_list_from_obj_storage(bucket: str, prefix: str) -> List[dict]:
    with BotoS3Session() as s3_session:
        response = s3_session.list_objects(Bucket=bucket, Prefix=prefix)
        if "Contents" in response:
            return response["Contents"]

# def delete_objs_from_obj_storage(bucket_name: str, obj_key: str):
#     forDeletion = [{"Key": "object_name"}, {"Key": "script/py_script.py"}]
#     response = s3.delete_objects(Bucket="bucket-name", Delete={"Objects": forDeletion})
#

# def get_objs_from_obj_storage(
#         bucket: str,
#         key: str,  # distant path in bucket "folder/sub_folder/file.txt"
# ) -> None:
#     with BotoS3Session() as s3_session:
#         get_object_response = s3_session.get_object(Bucket="bucket-name", Key="py_script.py")
#         print(get_object_response["Body"].read())
