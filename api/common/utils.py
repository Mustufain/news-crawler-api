from datetime import datetime
from flask import abort
import boto3
from botocore.exceptions import ClientError

ssm = boto3.client('ssm', region_name='us-east-1')


def get_paginated_list(count: int, start: int, limit: int, url: str) -> dict:
    if count < start or limit < 0 or start < 0:
        abort(404)
    links = {}
    if start == 1:
        prev_url = None
    else:
        prev_start = max(1, start - limit)
        prev_limit = start - 1
        prev_url = f'/news?start={prev_start}&limit={prev_limit}'

    if start + limit > count:
        next_url = None
    else:
        next_start = start + limit
        next_url = f'/news?start={next_start}&limit={limit}'
    if next_url:
        links['next'] = next_url
    if prev_url:
        links['prev'] = prev_url
    links['start'] = start
    links['limit'] = limit
    links['count'] = count
    links['base'] = url
    return links


def to_datetime(date: str) -> datetime:

    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        abort(404)
    return date


def get_ssm_parameter(name: str, with_decryption=False) -> str:
    try:
        response = ssm.get_parameter(
            Name=name,
            WithDecryption=with_decryption)
        parameter = response['Parameter']['Value']
    except ClientError as error:
        print(error.response['Error']['Code'])
        raise
    return parameter

