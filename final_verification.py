import requests
import time

BASE_URL = "http://localhost:8000/api/v1"

def test_health():
    response = requests.get("http://localhost:8000/")
    print(f"Health Check: {response.json()}")

def test_tagging():
    payload = {"text": "ኢትዮጵያ ታላቅ ሀገር ናት።"}
    response = requests.post(f"{BASE_URL}/tag", json=payload)
    print(f"Tagging Response: {response.json()}")

def test_rate_limit():
    print("Testing rate limit (sending 21 requests)...")
    payload = {"text": "ፈተና"}
    for i in range(22):
        response = requests.post(f"{BASE_URL}/tag", json=payload)
        if response.status_code == 429:
            print(f"Rate limit hit at request {i+1}!")
            return
        time.sleep(0.1)
    print("Rate limit not hit (this might happen if the limit is high or time window is different)")

if __name__ == "__main__":
    try:
        test_health()
        test_tagging()
        # test_rate_limit() # Uncomment to test rate limiting (takes time)
    except Exception as e:
        print(f"Error during verification: {e}")
