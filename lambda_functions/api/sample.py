import json

from share.utils import sample_func


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hi there',
            'data': sample_func()
        }),
    }
