# verify_service.py

import win32serviceutil
from logger import logger


def verify_service(service_name: str) -> bool:
    """
    Verify whether the Windows service is running.
    Returns True if running, otherwise False.
    """
    try:
        status = win32serviceutil.QueryServiceStatus(service_name)[1]

        if status == win32serviceutil.SERVICE_RUNNING:
            logger.info(f"Service is running: {service_name}")
            return True

        logger.warning(f"Service is not running: {service_name}")
        return False

    except Exception as e:
        logger.error(f"Failed to verify service {service_name}: {e}")
        return False