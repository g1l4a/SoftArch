# time_behavior_test.py
import requests
import time

start_time = time.time()

response = requests.get('http://localhost:5000/messages/count')
end_time = time.time()

response_time = end_time - start_time
print(f"Response time: {response_time:.4f} seconds")
print(f"Message count: {response.json()['count']}")
