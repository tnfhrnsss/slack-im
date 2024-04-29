import json
from slack_sdk import WebClient

with open('../config/env.json') as f:
    config = json.load(f)

def findAll():
    slack_token = config['slack_token']
    client = WebClient(token=slack_token)

    response = client.users_list()
    filtered_users = []

    if response["ok"]:
        users = response["members"]
        for user in users:
            deleted = user["deleted"]
            isBot = user["is_bot"]
            if deleted == True or isBot == True:
                continue

            isEmailConfirmed = user["is_email_confirmed"]
            if isEmailConfirmed == False:
                continue

            filtered_users.append(user)
        return filtered_users
    else:
        print("Failed to fetch users from Slack.")