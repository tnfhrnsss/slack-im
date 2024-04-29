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
            users = slackUser.findAll()
            run_sync(users)
        except Exception as e:
            print("occur exception.!!", e)


def run_sync(users):
    for user in users:
        user_name = user["real_name"]
        profile = user["profile"]
        email = profile.get('email')

        email_id = email.split("@")[0]
        print(email_id)
        print("User {} registered successfully.".format(email_id))
        member.register(email_id, user_name)


execute()
