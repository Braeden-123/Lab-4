import requests
from pydantic import ValidationError

token = "0"
numquestions = 1
categoryid = 0
difficulty = "easy"

get_token_api_url = "https://opentdb.com/api_token.php?command=request"

base_api_url = (f"https://opentdb.com/api.php?amount={numquestions}&category={categoryid}&difficulty={difficulty}&token={token}")

category_lookup_url = "https://opentdb.com/api_category.php"

category_number_questions_url = "https://opentdb.com/api_count.php?category="

def GetToken():
    response = requests.get(get_token_api_url)
    if response.status_code == 200:
        token = response.json().get('token')
    else:
        print(response.status_code)

def GetCategoryIDs():
    response = requests.get("https://opentdb.com/api_category.php")
    if response.status_code == 200:
        data = response.json()
        for category in data["trivia_categories"]:
            category_id = category["id"]
            category_name = category["name"]
            print(f"ID: {category_id}, Category: {category_name}") 
    else:
        print(response.status_code)

def MakeTheQuiz():
    global numquestions, categoryid, difficulty
    try:
        numquestions = int(input("Input the amount of questions for the quiz: "))
        categoryid = int(input("Input the category id: "))
        difficulty = input("Enter the difficulty easy, medium, or hard: ")
    except:
          print("An invald input.")

    if token == "0":
         GetToken()
    
    api_url = f"{base_api_url}?amount={numquestions}&category={categoryid}&difficulty={difficulty}&token={token}"


    


def menu():
       while True:
              print("1. View the categories and their ids")
              print("2. Make a trivia quiz")
              print("5. Exit")
              choice = input("Enter your choice: ")
              try:
                     match int(choice):
                            case 1:
                               GetCategoryIDs()
                            case 2:
                               MakeTheQuiz()
                            case 5:
                                   print("Exiting")
                                   break
                            case _:
                                   print("Invalid choice.")
                                   break
              except:
                     print("An error has occured.")

if __name__ == "__main__":
     menu()