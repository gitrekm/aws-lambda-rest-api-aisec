import os
import json

from campaigns import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def etat(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'etat': event['pathParameters']['etat']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
