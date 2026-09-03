import asyncio
import logging
from firebase_admin import messaging
logger = logging.getLogger(__name__)

class FCMService:
    @staticmethod
    async def send_emergency_notification(
        token: str,
        emergency_id: str,
        category_name: str,
        distance_meters: float,
    ):
        distance_km = distance_meters / 1000

        message = messaging.Message(
            notification=messaging.Notification(
                title="🚨 Emergency Request",
                body=(f"{category_name} emergency "
                    f"• {distance_km:.1f} km away"
                ),
            ),
            data={
                "type": "EMERGENCY_REQUEST",
                "emergency_id": emergency_id,
            },
            token=token,
        )

        try:
            # firebase_admin.messaging.send() is synchronous,so don't block the FastAPI event loop.
            response = await asyncio.to_thread(
                messaging.send,
                message,
            )
            logger.info(
                "FCM emergency notification sent successfully: %s",
                response,
            )
            return response
        except Exception:
            logger.exception(
                "Failed to send FCM emergency notification"
            )
            return None
        
    @staticmethod
    async def send_volunteer_arrived_notification(
        token: str,
        emergency_id: str,
    ):
        message = messaging.Message(
            data={
                "type": "VOLUNTEER_ARRIVED",
                "emergency_id": emergency_id,
                "title": "🚑 Volunteer Arrived",
                "body": "Your emergency volunteer has arrived.",
            },
            token=token,
        )
    
        try:
            response = await asyncio.to_thread(
                messaging.send,
                message,
            )
    
            logger.info(
                "Volunteer-arrived notification sent: %s",
                response,
            )
    
            return response
    
        except Exception:
            logger.exception(
                "Failed to send volunteer-arrived notification"
            )
            return None