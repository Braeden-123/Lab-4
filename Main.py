import requests
from pydantic import ValidationError

get_token_api_url = "https://opentdb.com/api_token.php?command=request"

base_api_url = "https://opentdb.com/api.php?amount=&category=&difficulty=&type=&token="

category_lookup_url = "https://opentdb.com/api_category.php"

category_number_questions_url = "https://opentdb.com/api_count.php?category="

response = requests.get(get_token_api_url)

if response.status_code == 200:
    token = response.json().get('token')
    print(token)
else:
    print(response.status_code)

