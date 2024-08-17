import allure
import pytest

from config.api_config import ApiUrls
from helpers import api_requests_wrapper
from req_res.request.GoRestRequests import GoRestRequests
from utils.common_utils import CommonUtility


class TestPostRequests:

    @allure.epic("Epic2: Post request to create new user")
    @allure.feature("TC#1 - Create a new user")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Create a new user")
    @pytest.mark.smoke
    @pytest.mark.order(3)
    def test_create_users(self):
        post_response = api_requests_wrapper.post_request(ApiUrls.URL, None, GoRestRequests.CREATE_USER,
                                                          CommonUtility.get_custom_header(), 201)
        user_id = post_response['id']
        user_email = post_response['email']
        get_response = api_requests_wrapper.get_request(ApiUrls.url_user_by_id(user_id), None,
                                                        CommonUtility.get_custom_header(), 200)
        assert user_id == get_response['id'], f"expected {user_id}but got {get_response['id']}"
        assert user_email == get_response['email'], f"expected {user_email}but got {get_response['email']}"
