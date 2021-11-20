from pprint import pprint
import requests

URL = "http://127.0.0.1:5000/users"


def deactivate_user_by_id(user_id):
    url = "%s/%s" % (URL, user_id)
    out = requests.delete(url)
    if out.status_code == 200:
        pprint(out.json())
    else:
        print("Something went wrong while trying to delete.")


if __name__ == "__main__":
    deactivate_user_by_id(2)
