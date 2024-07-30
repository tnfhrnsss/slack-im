import http.client
import os
import sys
import slackUser
import member

print(sys.argv[1])

api_url = sys.argv[1]


def execute():
    if len(api_url) == 0:
        print("api path is null.")
    else:
        try:
            run_sync(find_users())
        except http.client.IncompleteRead as e:
            print("IncompleteRead error occurred exception.!!", e)
            run_sync(find_users())
        except Exception as e:
            print("occur exception.!!", e)


def find_users():
    return slackUser.findAll()


def run_sync(users):
    for user in users:
        user_name = user["real_name"]
        profile = user["profile"]
        email = profile.get('email')

        email_id = email.split("@")[0]
        print("target email_id {}.".format(email_id))
        member.register(email_id, user_name)


execute()
