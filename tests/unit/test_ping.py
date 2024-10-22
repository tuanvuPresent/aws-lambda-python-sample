import json

import pytest

from lambda_functions.api import ping


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{"test": "body"}',
    }


def test_lambda_handler(apigw_event):
    ret = ping.lambda_handler(apigw_event, "")
    body = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert body == "Hi there"
