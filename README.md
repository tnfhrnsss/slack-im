# im(identity management) service using slack-api

## Requirements

* python 3.x
* slack sdk
* jenkins 2.414.1 (optional)

# Usage

## Slack Setting

* You have to add **users:read , users:read:email** of Bot Token Scopes.
* And have to configure the slack bot token in the env.json file.

   ```
    {
        "slack_token": "xoxb-"
    }
   ```

# Run

* execute sync.py
  ```
   python sync.py ${API_URL}
  ```


### blog reference

For further reference, please consider the following sections:

* [blog](https://tnfhrnsss.github.io/docs/sub-projects/make_im_service_using_slack/)

