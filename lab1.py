class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FileManager(metaclass=SingletonMeta):
    def __init__(self):
        self.storage = None

    def set_storage(self, storage):
        self.storage = storage

    def upload_file(self, file_path, destination):
        if self.storage:
            self.storage.upload(file_path, destination)

    def download_file(self, file_name, destination):
        if self.storage:
            self.storage.download(file_name, destination)

class LocalDiskStorage:
    def upload(self, file_path, destination):
        with open(file_path, 'rb') as file:
            with open(destination, 'wb') as dest:
                dest.write(file.read())
        print(f"Uploaded {file_path} to {destination} on local disk.")

    def download(self, file_name, destination):
        with open(file_name, 'rb') as file:
            with open(destination, 'wb') as dest:
                dest.write(file.read())
        print(f"Downloaded {file_name} to {destination} on local disk.")

import boto3
import os

class S3Storage:
    def __init__(self, bucket_name):
        session = boto3.Session(profile_name='Dalitvi')
        self.s3 = session.client('s3')
        self.bucket_name = bucket_name

    def upload(self, file_path, destination):
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return
        self.s3.upload_file(file_path, self.bucket_name, destination)
        print(f"Uploaded {file_path} to {destination} on S3.")

    def download(self, file_name, destination):
        self.s3.download_file(self.bucket_name, file_name, destination)
        print(f"Downloaded {file_name} to {destination} from S3.")


if __name__ == "__main__":
    # Для локального диску
    file_manager = FileManager()
    local_storage = LocalDiskStorage()
    file_manager.set_storage(local_storage)
    file_manager.upload_file('example.txt', 'destination.txt')
    file_manager.download_file('destination.txt', 'downloaded_example.txt')

    # Для Amazon S3
    self.s3 = boto3.client('s3', profile_name='Dalitvi')
    s3_storage = S3Storage(bucket_name='lab1singleton')
    file_manager.set_storage(s3_storage)
    file_manager.upload_file('example.txt', 'example_s3.txt')
    file_manager.download_file('example_s3.txt', 'downloaded_example_s3.txt')
