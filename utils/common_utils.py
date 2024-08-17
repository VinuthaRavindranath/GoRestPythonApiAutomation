import random
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()


class CommonUtility:

    @staticmethod
    def get_custom_header():
        bearer_token = os.getenv("token")
        headers = {"Authorization": f"Bearer {bearer_token}",
                   "Content-Type": "application/json"}
        return headers

    @staticmethod
    def get_unique_email():
        random_number = random.randint(1000, 99999)
        email = f"test_automation{random_number}@gmail.com"
        return email
