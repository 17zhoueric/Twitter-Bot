import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

def quotes(api):
    file = open("tbotcb_edited.txt", "r")
    lines = file.readlines()
    logger.info("Printing one line from The Boy of the Cherry Blossoms") 
    api.update_status(lines[0])
    lines.pop(0)

def main():
    api = create_api()
    while True:
        quotes(api)
        logger.info("Waiting ... ")
        time.sleep(3600)

if __name__ == "__main__":
    main()

        
