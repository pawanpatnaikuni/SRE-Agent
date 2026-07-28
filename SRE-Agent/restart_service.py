# restart_service.py

import win32serviceutil
from logger import logger


def restart_service(service_name: str) -> bool:
    """
    Restart the given Windows service.
    Returns True if restart command succeeds, otherwise False.
    """
    try:
        logger.info(f"Restarting service: {service_name}")

        win32serviceutil.RestartService(service_name)

        logger.info(f"Restart command sent successfully for: {service_name}")
        return True

    except Exception as e:
        logger.error(f"Failed to restart service {service_name}: {e}")
        return False