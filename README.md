# Chat Application Project

This project is a client-server chat application with anonymous messaging. The system measures quality attributes such as time behavior, recoverability, and maintainability through fitness functions.


### Files Overview

- **client.html**:  
  The front-end interface for users to interact with the chat application (client-side connection).
  
- **fitness_maintainability.py**:  
  A Python script to measure maintainability by analyzing code complexity. It uses cyclomatic complexity metrics to determine how easy it is to maintain the system.

- **fitness_recoverability.py**:  
  A Python script to evaluate the recoverability of the system, including how well the server and client can handle failures and restore connections.

- **fitness_time_behavior.py**:  
  A Python script designed to measure the time behavior of the system, specifically the response time for certain requests like message counts.

- **messages.json**:  
  A JSON file for storing messages that are transmitted between the server and clients.

- **server.py**:  
  The server-side logic responsible for handling client requests, transmitting messages, and maintaining the chat system's backend.

- **style.css**:  
  The stylesheet for the front-end client interface to define the visual appearance of the chat application.

---

## How to Run

1. Start the server by running the `server.py` file:
   ```bash
   python server.py
