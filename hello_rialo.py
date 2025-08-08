import requests

def ping_example():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        price = data["data"]["amount"]
        print(f"✅ Current Bitcoin Price (USD): ${price}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch data: {e}")

if __name__ == "__main__":
    print("🌐 Hello, Rialo! Fetching BTC price...")
    ping_example()
