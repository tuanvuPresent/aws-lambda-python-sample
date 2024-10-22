import pytest

from lambda_functions.api import export_file


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{"test": "body"}',
    }


def test_lambda_handler(apigw_event):
    ret = export_file.lambda_handler(apigw_event, "")
    assert ret['statusCode'] == 200
    assert ret['headers']['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    assert 'Content-Disposition' in ret['headers']
    assert len(ret['body']) > 0
