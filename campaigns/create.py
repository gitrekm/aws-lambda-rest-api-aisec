import json
import logging
import os
import time
import uuid
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(datetime.utcnow().timestamp())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'creationDate': timestamp,
        'updatedAt': timestamp,
        'status': str(uuid.uuid1()),
        'etat': str(uuid.uuid1()),
        'campaignName': str(uuid.uuid1()),
        'startDate': str(uuid.uuid1()),
        'aPI': str(uuid.uuid1()),
        'parcours': str(uuid.uuid1()),
        'plateform': str(uuid.uuid1()),
        'targetEnvironment': str(uuid.uuid1()),
        'owner': str(uuid.uuid1()),
        'projectName': str(uuid.uuid1()),
        'withNotification': str(uuid.uuid1()),
        'dureeexec': str(uuid.uuid1()),

    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
