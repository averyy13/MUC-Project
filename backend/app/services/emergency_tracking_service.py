from collections import defaultdict
from typing import DefaultDict

from fastapi import WebSocket


class EmergencyTrackingManager:

    def __init__(self):
        # emergency_id -> connected requester sockets
        self.requester_connections: DefaultDict[
            str,
            set[WebSocket]
        ] = defaultdict(set)

    async def connect_requester(
        self,
        emergency_id: str,
        websocket: WebSocket,
    ):
        await websocket.accept()

        self.requester_connections[
            emergency_id
        ].add(websocket)

    def disconnect_requester(
        self,
        emergency_id: str,
        websocket: WebSocket,
    ):
        connections = self.requester_connections.get(
            emergency_id
        )

        if not connections:
            return

        connections.discard(websocket)

        if not connections:
            self.requester_connections.pop(
                emergency_id,
                None
            )

    async def broadcast_location(
        self,
        emergency_id: str,
        message: dict,
    ):
        connections = self.requester_connections.get(
            emergency_id,
            set()
        )

        disconnected = []

        for websocket in connections:
            try:
                await websocket.send_json(message)
            except Exception:
                disconnected.append(websocket)

        for websocket in disconnected:
            self.disconnect_requester(
                emergency_id,
                websocket
            )


tracking_manager = EmergencyTrackingManager()