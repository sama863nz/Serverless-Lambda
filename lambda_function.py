import json

from config import base_url
import requests

def lambda_handler(event, context):

    response = requests.get( url = base_url + '/todos/1')
    return {
        'statusCode': response.statusCode,
        'body': response.json()
    }

