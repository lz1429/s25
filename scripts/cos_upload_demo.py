#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = '66666666666666666666666'  # 替换为用户的 secretId
secret_key = '66666666666666666666666'  # 替换为用户的 secretKey

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.upload_file(
    Bucket='wangyang-1251317460',
    LocalFilePath='code.png',  # 本地文件的路径
    Key='p1.png'  # 上传到桶之后的文件名
)
print(response['ETag'])
