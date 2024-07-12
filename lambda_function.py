import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-table')

def lambda_handler(event, context):
    # TODO implement
    try: 
        response=table.put_item(Item=event)
        # response = table.delete_item
        return table.scan
    except:
        raise

if __name__ == "__main__":
    event = {
        "name":"new entry test"
    }
    print(lambda_handler(event, None))