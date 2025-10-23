from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logger
from socialMessageUtils import removeSlackChannel
import tokenUtils
import json

log = logger.setup_logger("slackClient")
SLACK_CHANNEL_KEY = "slack_channel"

def send(message):
    log.info(f"message -->{message}<--")
    
    channel_name = message[SLACK_CHANNEL_KEY]; 
    message = removeSlackChannel(message); 
    token = tokenUtils.load_stored_token()
    access_token = token["access_token"]
    messageAsString = json.dumps(message)

    log.debug(f"channel_name -->{channel_name}<--\n\r")
    log.debug(f"message -->{message}<--\n\r")
    log.debug(f"messageAsString -->{messageAsString}<--\n\r")
    log.debug(f"token -->{token}<--\n\r")
    log.debug(f"access_token -->{access_token}<--\n\r")
    
    client = WebClient(token=access_token)
    try:
        client.chat_postMessage(
            channel=channel_name,
            text=messageAsString
        )
    except SlackApiError as e:
        log.error(f"Error: {e}")    
