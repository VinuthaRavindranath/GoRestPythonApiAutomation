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
        user_id = post_response.json()['id']
        user_email = post_response.json()['email']
        get_response = api_requests_wrapper.get_request(ApiUrls.url_user_by_id(user_id), None,
                                                        CommonUtility.get_custom_header(), 200)

        assert post_response.status_code == 201, f"expected status code as 201 but got {post_response.status_code}"
        assert get_response.status_code == 200, f"expected status code as 200 but got {get_response.status_code}"
        assert user_id == get_response.json()['id'], f"expected {user_id}but got {get_response.json()['id']}"
        assert user_email == get_response.json()[
            'email'], f"expected {user_email}but got {get_response.json()['email']}"
