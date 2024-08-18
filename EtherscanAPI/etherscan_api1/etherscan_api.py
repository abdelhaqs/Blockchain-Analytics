import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ApiKeyToken = os.getenv("ApiKeyToken")
address = "0xb65a2cbc549c08080b1d74137c4c9a5073d0fc73"
# Define your API key

url = "http://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
      "&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey=" + ApiKeyToken

response = requests.get(url)

address_content = response.json()
result = address_content.get("result")

for n, transaction in enumerate(result):
    hash = transaction.get("hash")
    tx_from = transaction.get("from")
    tx_to = transaction.get("to")
    value = transaction.get("value")
    confirmations = transaction.get("confirmations")

    print("Transaction ID: ", n)
    print("hash: ", hash)
    print("from: ", tx_from)
    print("to: ", tx_to)
    print("value: ", value)
    print("confirmations: ", confirmations)
    print("\n")