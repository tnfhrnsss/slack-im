import sys
import requests

api_url = sys.argv[1]

def register(user_id, user_name):
    if len(user_id) == 0:
        print("user_id is null. {}", user_name)

    headers = {
        'X-Attic-User': 'admin',
        'X-Attic-Role': 'manageMember'
    }
    payload = {"userId": user_id, "name": user_name, "password": "1", "roleGroupId": "ADMIN", "centerIds":["spectra"]}
    response = requests.post(api_url, headers=headers, json=payload)

    if response.ok:
        print("User {} registered successfully.".format(user_name))
    else:
        print("Failed to register user .{}.".format(user_name))