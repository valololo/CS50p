import requests
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    # Convert the command-line argument to a float
    bitcoin = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    # Make a request to the CoinCap API to get the current price of Bitcoin
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=34f0dd0607e107ea21bce2281d2396292a2a43cb45841d4d34bafebdc3dd59a8")
    content = response.json()
    price = content["data"]["priceUsd"]

    # Calculate the amount in USD
    amount = bitcoin * float(price)

    # Print the amount formatted as USD
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit(2)
