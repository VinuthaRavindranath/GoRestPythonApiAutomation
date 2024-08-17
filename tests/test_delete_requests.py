import allure
import pytest

from config.api_config import ApiUrls
from helpers import api_requests_wrapper
from req_res.request.GoRestRequests import GoRestRequests
from utils.common_utils import CommonUtility


class TestDeleteRequests:
    @allure.epic("Epic3: Delete request to delete user by Id")
    @allure.feature("TC#1 -   Delete user by Id")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Delete user by Id")
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_delete_users(self):
        post_response = api_requests_wrapper.post_request(ApiUrls.URL, None, GoRestRequests.CREATE_USER,
                                                          CommonUtility.get_custom_header(), 201)
        user_id = post_response['id']

        delete_response = api_requests_wrapper.delete_request(ApiUrls.url_user_by_id(user_id), None, None,
                                                              CommonUtility.get_custom_header())

        assert delete_response.status_code == 204, f"received {delete_response.status_code} but expected is 204"
