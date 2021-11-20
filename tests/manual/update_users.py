from pprint import pprint
import requests

TEST_USER_DATA = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Playing Tennis"
}

URL = "http://127.0.0.1:5000/users/2"


def update_user():
    out = requests.put(URL, json=TEST_USER_DATA)
    if out.status_code == 200:
        pprint(out.json())
    else:
        print("Something went wrong while trying to update")


if __name__ == "__main__":
    update_user()
