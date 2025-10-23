# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
import logger
from socialMessageUtils import removeSlackChannel
import tokenUtils

log = logger.setup_logger("slackClient")
SLACK_CHANNEL_KEY = "slack_channel"

def send(message):
    log.info(f"message -->{message}<--")
    
    channel_name = message[SLACK_CHANNEL_KEY]; 
    message = removeSlackChannel(message); 
    access_token = tokenUtils.load_stored_token()

    log.info(f"channel_name -->{channel_name}<--\n\r")
    log.info(f"message -->{message}<--\n\r")
    log.info(f"access_token -->{access_token}<--\n\r")
    # client = WebClient(token=access_token)
    # try:
    #     client.chat_postMessage(
    #         channel=channel_name,
    #         text=message
    #     )
    # except SlackApiError as e:
    #     log.error(f"Error: {e}")    
