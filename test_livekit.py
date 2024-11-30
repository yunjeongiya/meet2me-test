import asyncio
import websockets
import requests
import json
import random

# 서버 URL
SERVER_URL = "http://ec2-3-93-131-99.compute-1.amazonaws.com:8080"  # 내가 만든 서버의 주소
LIVEKIT_URL = "wss://meet2me-v1cyuau7.livekit.cloud"  # LiveKit WebSocket 서버 주소

# 테스트 설정
NUM_ROOMS = 100  # 생성할 방의 개수
PARTICIPANTS_PER_ROOM = 4  # 방당 참가자 수


def generate_random_name():
    """랜덤 참가자 이름 생성"""
    return f"user_{random.randint(1000, 9999)}"


def create_room():
    """방 생성 요청"""
    response = requests.post(f"{SERVER_URL}/rooms")
    if response.status_code == 200:
        room_id = response.json().get("roomId")
        print(f"Room created: {room_id}")
        return room_id
    else:
        print(f"Failed to create room: {response.status_code} - {response.text}")
        return None


def create_participant(room_id, username):
    """참가자 생성 요청"""
    payload = {"username": username}
    response = requests.post(f"{SERVER_URL}/rooms/{room_id}/tokens", json=payload)
    if response.status_code == 200:
        token = response.json().get("token")
        print(f"Participant created: Room={room_id}, Username={username}, Token={token}")
        return token
    else:
        print(f"Failed to create participant: {response.status_code} - {response.text}")
        return None


async def connect_to_livekit(room_id, participant_name, token):
    """LiveKit WebSocket에 참가자 연결"""
    async with websockets.connect(LIVEKIT_URL) as websocket:
        connect_message = {
            "type": "connect",
            "room": room_id,
            "participant": participant_name,
            "token": token
        }
        await websocket.send(json.dumps(connect_message))
        print(f"Connected to LiveKit: Room={room_id}, Participant={participant_name}")

        # 메시지 수신 대기
        try:
            async for message in websocket:
                print(f"Message from Room {room_id}: {message}")
        except websockets.ConnectionClosed:
            print(f"Disconnected: Room={room_id}, Participant={participant_name}")


async def test_livekit():
    """전체 테스트 실행"""
    tasks = []

    # 방 생성 및 참가자 추가
    for _ in range(NUM_ROOMS):
        room_id = create_room()
        if not room_id:
            continue

        for _ in range(PARTICIPANTS_PER_ROOM):
            username = generate_random_name()
            token = create_participant(room_id, username)
            if token:
                tasks.append(connect_to_livekit(room_id, username, token))

    # LiveKit WebSocket에 참가자 연결
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(test_livekit())
