from datetime import datetime
from flask import abort
import boto3
from botocore.exceptions import ClientError

client = boto3.client('ssm')


def get_paginated_list(count: int, start: int, limit: int, url: str) -> object:
    if count < start or limit < 0:
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


def get_pwd() -> str:
    try:
        response = client.get_parameter(
            Name='MONGODB_PWD',
            WithDecryption=True)
        pwd = response['Parameter']['Value']
    except ClientError as error:
        print(error.response['Error']['Code'])
        raise
    return pwd


def get_username() -> str:
    try:
        response = client.get_parameter(
            Name='MONGODB_USERNAME')
        username = response['Parameter']['Value']
    except ClientError as error:
        print(error.response['Error']['Code'])
        raise
    return username
