from utils.common_utils import CommonUtility


class GoRestRequests:
    CREATE_USER = {
        "name": "automation user",
        "gender": "male",
        "email": f"{CommonUtility.get_unique_email()}",
        "status": "active"
    }

    UPDATE_USER = {
        "name": "automation user updated",
        "status": "inactive"
    }
