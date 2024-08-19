import allure
import pytest

from config.api_config import ApiUrls
from helpers import api_requests_wrapper
from utils.common_utils import CommonUtility


class TestGetRequests:

    @allure.epic("Epic1: Get request to fetch all users")
    @allure.feature("TC#1 -  Fetch all users")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Fetch all users")
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_get_users(self):
        response = api_requests_wrapper.get_request(ApiUrls.URL, None, CommonUtility.get_custom_header(), 200)
        first_user_id = response.json()[0]['id']
        email = response.json()[0]['email']

        assert response.status_code == 200, f"expected status code as 200 but got {response.status_code}"
        assert first_user_id is not None
        assert email.count('@') == 1, " invalid email-id"

    @allure.epic("Epic1: Get request to fetch user by Id")
    @allure.feature("TC#2 -  fetch user by Id")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("fetch user by Id")
    @pytest.mark.smoke
    @pytest.mark.order(2)
    def test_get_user_by_id(self):
        response_all_users = api_requests_wrapper.get_request(ApiUrls.URL, None, CommonUtility.get_custom_header(),
                                                              200)
        first_user_id = response_all_users.json()[0]['id']
        email = response_all_users.json()[0]['email']
        response_user = api_requests_wrapper.get_request(ApiUrls.url_user_by_id(first_user_id), None,
                                                         CommonUtility.get_custom_header(), 200)

        assert response_user.status_code == 200, f"expected status code as 200 but got {response_user.status_code}"
        assert first_user_id == response_user.json()[
            'id'], f"got {first_user_id} but expected is {response_user.json()['id']} "
        assert email == response_user.json()['email'], f"got {email} but expected is {response_user.json()['email']} "
