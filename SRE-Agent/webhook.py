from fastapi import APIRouter
from pydantic import BaseModel

from logger import logger
from restart_service import restart_service
from verify_service import verify_service

router = APIRouter()


class WebhookPayload(BaseModel):
    service_name: str


@router.post("/webhook")
async def receive_webhook(payload: WebhookPayload):

    logger.info(f"Received Alert: {payload.model_dump()}")

    service_name = payload.service_name

    restarted = restart_service(service_name)

    if not restarted:
        return {
            "success": False,
            "message": f"Failed to restart {service_name}"
        }

    running = verify_service(service_name)

    if running:
        return {
            "success": True,
            "message": f"{service_name} restarted successfully"
        }

    return {
        "success": False,
        "message": f"{service_name} is not running after restart"
    }