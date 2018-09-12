from collections import namedtuple
import os

import pytest
import requests
import yaml


def full_path(file):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file)


AccountDetails = namedtuple("AccountDetails", ["email", "password"])


# Configuration
API_URL = os.getenv("API_URL", "http://api:7000")

config_data = yaml.load(open(full_path("./common.yaml"), "r"))
FIRST_NAME = config_data["variables"]["test_account__password"]
LAST_NAME = config_data["variables"]["test_account__password"]
EMAIL = config_data["variables"]["test_account__email"]
PASSWORD = config_data["variables"]["test_account__password"]


@pytest.fixture(scope="session", name="jwt")
def login_and_create_jwt(create_account):
    login_url = API_URL + "/login"
    r = requests.post(
        login_url,
        json={"email": create_account.email, "password": create_account.password},
    )
    if r.status_code == 200:
        yield r.json()["jwt"]


@pytest.fixture(scope="session")
def create_account():
    test_account = AccountDetails(EMAIL, PASSWORD)
    exists_url = API_URL + "/users/exists"
    create_user_url = API_URL + "/users"

    r = requests.post(exists_url, json={"email": EMAIL})
    if r.status_code != 200:
        r = requests.post(
            create_user_url,
            json={
                "first_name": FIRST_NAME,
                "last_name": LAST_NAME,
                "email": EMAIL,
                "password": PASSWORD,
            },
        )

    yield test_account
