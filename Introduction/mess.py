import requests

def send_sms(number, message):
    url = "https://helobuy.shop/csms.php"
    params = {
        "key": "bft",      # তোমার দেয়া key
        "number": number,
        "message": message
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            print("✅ SMS Sent Successfully!")
            print("Server Response:", response.text)
        else:
            print("❌ Failed! Status Code:", response.status_code)
    except Exception as e:
        print("⚠️ Error:", str(e))


# Example usage:
if __name__ == "__main__":
    number = input("Enter number: ")
    message = input("Enter message: ")
    send_sms(number, message)
