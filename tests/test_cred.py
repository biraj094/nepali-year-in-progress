import pytest
from models import TwitterClient

def test_cred():
    twitter_client = TwitterClient()
    assert twitter_client.status == True

