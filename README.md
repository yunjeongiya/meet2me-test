# LiveKit Performance Testing

This repository contains automated performance testing scripts for the LiveKit server, focusing on the interaction between the LiveKit WebSocket API and a custom backend server. It includes functionality for creating rooms, adding participants, and connecting to LiveKit WebSocket for real-time communication testing.

## Purpose

The goal of this repository is to test the scalability and performance of the LiveKit server when handling multiple rooms and users simultaneously. The tests ensure that the system can handle concurrent connections, manage multiple video streams, and maintain low latency and high frame rates.

## Features

- **Room Creation**: Automatically creates multiple rooms on the custom backend server.
- **User Creation**: Adds multiple users to each room and generates user tokens.
- **WebSocket Connection**: Connects each user to LiveKit WebSocket server using the generated tokens and room IDs.
- **Simulated Load**: Tests the LiveKit server by simulating the creation of 5 or more rooms, each with 4 participants.

## Prerequisites

Before running the test scripts, ensure that the following requirements are met:

1. **Custom Backend Server**:
    - The custom backend server must be running and accessible.
    - The server must provide APIs for room creation (`POST /rooms`) and participant token generation (`POST /rooms/{roomId}/tokens`).

2. **LiveKit Server**:
    - LiveKit WebSocket server must be running and accessible (default URL: `ws://localhost:7880`).
    - WebSocket port and token generation must be configured for testing.

3. **Python Environment**:
    - Python 3.6+ is required.
    - Install the necessary dependencies using `pip`.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/livekit-performance-testing.git
cd livekit-performance-testing
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Configure Server URLs and Token

In `test_livekit.py`, update the following variables with your server URLs and token information:

```python
SERVER_URL = "http://localhost:8080"  # Your custom backend server URL
LIVEKIT_URL = "ws://localhost:7880"   # LiveKit WebSocket server URL
BASE_TOKEN = "your-jwt-token"         # Your base JWT token for LiveKit
```

### 4. Run the Test Script

Execute the test script to simulate the load and connect participants to LiveKit:

```bash
python test_livekit.py
```

The script will create multiple rooms, add participants, and establish WebSocket connections to the LiveKit server. Messages and connection statuses will be printed to the console.

## Testing Scenarios

- **Room Creation**: Create rooms on the custom backend server and generate a unique room ID for each.
- **User Creation**: For each room, generate 4 user tokens and simulate users connecting to the LiveKit WebSocket server.
- **WebSocket Connections**: Each user will be connected to the LiveKit WebSocket server and participate in the room.
- **Scalability Test**: The script will test the ability of LiveKit to handle multiple concurrent connections and video streams in real-time.

## Output

The script will output the following:

- **Room IDs and Participant Names**: Printed after each room and participant is successfully created.
- **WebSocket Connection Status**: Each user's connection attempt and status will be logged.
- **Errors**: Any errors encountered during the process will be printed to the console.

## Requirements

- Python 3.6+
- `websockets` library for WebSocket connections.
- `requests` library for making HTTP requests to the custom backend server.
- Access to the custom backend server and LiveKit WebSocket server.
