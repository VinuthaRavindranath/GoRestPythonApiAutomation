from helpers import api_requests_wrapper


class ApiUrls:
    URL = api_requests_wrapper.get_base_end_point() + "/public/v2/users"

    @staticmethod
    def url_user_by_id(user_id):
        return api_requests_wrapper.get_base_end_point() + f"/public/v2/users/{user_id}"
