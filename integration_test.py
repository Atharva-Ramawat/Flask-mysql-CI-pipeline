import requests
import re
import sys

# The URL of our Docker container
url = "http://localhost:5000"

def get_visit_count():
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Server returned {response.status_code}")
            return None
        
        # Extract the number from "Hello! I have been visited X times."
        text = response.text
        match = re.search(r'visited (\d+) times', text)
        if match:
            return int(match.group(1))
        return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def run_test():
    print("Test 1: Getting initial count...")
    count_1 = get_visit_count()
    if count_1 is None:
        sys.exit(1) # Fail
    print(f"Initial Count: {count_1}")

    print("Test 2: Refreshing page to increase count...")
    count_2 = get_visit_count()
    if count_2 is None:
        sys.exit(1) # Fail
    print(f"New Count: {count_2}")

    # THE QUALITY CHECK
    if count_2 == count_1 + 1:
        print("SUCCESS: Visitor count increased correctly! ✅")
        sys.exit(0) # Pass
    else:
        print(f"FAILURE: Count did not increase! (Expected {count_1 + 1}, got {count_2}) ❌")
        sys.exit(1) # Fail

if __name__ == "__main__":
    run_test()