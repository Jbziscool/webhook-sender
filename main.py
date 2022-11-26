import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


hook = os.getenv('webhook')



while True:
    message = input(f'Webhook msg: ')
    
    
    json={
    "content": message,
    "embeds": None,
    "attachments": []
}
    requests.post(hook,json=json)

