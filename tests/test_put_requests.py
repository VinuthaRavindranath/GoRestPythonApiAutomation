import allure
import pytest

from config.api_config import ApiUrls
from helpers import api_requests_wrapper
from req_res.request.GoRestRequests import GoRestRequests
from utils.common_utils import CommonUtility


class TestPutRequests:

    @allure.epic("Epic3: Put request to update user by Id")
    @allure.feature("TC#1 -   Update user by Id")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Update user by Id")
    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_update_users(self):
        post_response = api_requests_wrapper.post_request(ApiUrls.URL, None, GoRestRequests.CREATE_USER,
                                                          CommonUtility.get_custom_header(), 201)
        user_id = post_response.json()['id']

        put_response = api_requests_wrapper.put_request(ApiUrls.url_user_by_id(user_id), None,
                                                        GoRestRequests.UPDATE_USER,
                                                        CommonUtility.get_custom_header(), 200)
        user_id = put_response.json()['id']
        name = put_response.json()['name']
        status = put_response.json()['status']

        get_response = api_requests_wrapper.get_request(ApiUrls.url_user_by_id(user_id), None,
                                                        CommonUtility.get_custom_header(), 200)

        assert post_response.status_code == 201, f"expected status code as 201 but got {post_response.status_code}"
        assert put_response.status_code == 200, f"expected status code as 200 but got {put_response.status_code}"
        assert get_response.status_code == 200, f"expected status code as 201 but got {get_response.status_code}"
        assert name == get_response.json()['name'], f"expected {name}but got {get_response.json()['name']}"
        assert status == get_response.json()['status'], f"expected {status}but got {get_response.json()['status']}"
