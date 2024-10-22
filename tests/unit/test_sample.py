import json

import pytest

from lambda_functions.api import sample


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{"test": "body"}',
    }


def test_lambda_handler(apigw_event):
    ret = sample.lambda_handler(apigw_event, "")
    body = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert 'message' in body
    assert 'data' in body
    assert body['message'] == "Hi there"
    assert body['data'] == 100
