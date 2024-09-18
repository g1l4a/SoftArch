import requests
import time
import threading


MESSAGE_COUNT_URL = "http://localhost:5000/messages/count"

def check_response_time():
    start_time = time.time()
    response = requests.get(MESSAGE_COUNT_URL)
    end_time = time.time()
    response_time = end_time - start_time
    return response_time

def test_time_behavior(num_requests=10):
    threads = []
    response_times = []

    for _ in range(num_requests):
        thread = threading.Thread(target=lambda: response_times.append(check_response_time()))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    max_response_time = max(response_times)

    print(f"Maximum response time: {max_response_time:.2f} seconds")


test_time_behavior()
