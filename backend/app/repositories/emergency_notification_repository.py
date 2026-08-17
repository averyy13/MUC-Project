from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.emergency_notification import EmergencyNotification
from app.models.enums import NotificationStatus


class EmergencyNotificationRepository:

    @staticmethod
    async def create_batch(
        db: AsyncSession,
        emergency_request_id,
        volunteers,
        batch_number: int,
    ):

        notifications = []

        for index, volunteer in enumerate(volunteers, start=1):
            notification = EmergencyNotification(
                emergency_request_id=emergency_request_id,
                volunteer_id=volunteer["volunteer_id"],
                notification_order=index,
                batch_number=batch_number,
                status=NotificationStatus.PENDING,
            )

            db.add(notification)
            notifications.append(notification)

        await db.flush()
        return notifications


    @staticmethod
    async def get_for_volunteer(
        db: AsyncSession,
        emergency_request_id,
        volunteer_id,
    ):

        result = await db.execute(
            select(EmergencyNotification).where(
                EmergencyNotification.emergency_request_id == emergency_request_id,
                EmergencyNotification.volunteer_id == volunteer_id,
            )
        )

        return result.scalar_one_or_none()


    @staticmethod
    async def mark_accepted(
        db: AsyncSession,
        notification: EmergencyNotification,
    ):

        notification.status = NotificationStatus.ACCEPTED
        notification.responded_at = datetime.now(timezone.utc)

        await db.flush()


    @staticmethod
    async def cancel_other_pending(
        db: AsyncSession,
        emergency_request_id,
        accepted_volunteer_id,
    ):

        result = await db.execute(
            select(EmergencyNotification).where(
                EmergencyNotification.emergency_request_id == emergency_request_id,
                EmergencyNotification.volunteer_id != accepted_volunteer_id,
                EmergencyNotification.status == NotificationStatus.PENDING,
            )
        )

        notifications = result.scalars().all()

        for notification in notifications:
            notification.status = NotificationStatus.DECLINED

        await db.flush()