import requests
import time
import subprocess
import os

SERVER_URL = "http://localhost:5000"
MESSAGE_COUNT_URL = f"{SERVER_URL}/messages/count"

def get_message_count():
    try:
        response = requests.get(MESSAGE_COUNT_URL)
        return response.json().get('count', 0)
    except requests.exceptions.ConnectionError:
        return None

def test_recoverability():
    initial_count = get_message_count()

    if initial_count is None:
        print("Server is unavailable for measurement.")
        return

    print(f"Messages before restart: {initial_count}")

    start_time = time.time()
    subprocess.Popen(["flask", "--app", "server.py", "run", "--host=0.0.0.0", "--port=5000"])
    while True:
        restored_count = get_message_count()
        if restored_count is not None:
            break

    recovery_time = time.time() - start_time
    print(f"Server recovery time: {recovery_time:.2f} seconds")

    if restored_count == initial_count:
        print(f"Messages successfully restored, count: {restored_count}")
    else:
        print(f"Message restoration error. Expected {initial_count}, but received {restored_count}.")


test_recoverability()
