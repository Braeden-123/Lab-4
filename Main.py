import requests
from pydantic import ValidationError
import time
import random

get_token_api_url = "https://opentdb.com/api_token.php?command=request"

base_api_url = (f"https://opentdb.com/api.php")

category_lookup_url = "https://opentdb.com/api_category.php"

category_number_questions_url = "https://opentdb.com/api_count.php?category="

def GetToken():
    response = requests.get(get_token_api_url)
    if response.status_code == 200:
        token = response.json().get('token')
        return token
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
    question_number = 1
    score = 0
    try:
        numquestions = int(input("Input the amount of questions for the quiz: "))
        categoryid = int(input("Input the category id: "))
        difficulty = input("Enter the difficulty easy, medium, or hard: ")
    except:
          print("An invald input.")
    token = GetToken()
    print("Sleeping for 5 seconds to not get api rate limited...")
    time.sleep(5)
    api_url = f"{base_api_url}?amount={numquestions}&category={categoryid}&difficulty={difficulty}&type=multiple&token={token}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for question in data['results']:
            question_text = question['question']
            correct_answer = question['correct_answer']
            incorrect_answers = question['incorrect_answers']
            answers = incorrect_answers + [correct_answer]
            random.shuffle(answers)
            print(f"\nQuestion {question_number}: {question_text}")
            answer_options = {}
            option_labels = ['A', 'B', 'C', 'D']
            for i in range(len(answers)):
                label = option_labels[i]
                answer_options[label] = answers[i]
                print(f"{label}. {answers[i]}")

            while True:
                user_answer_label = input("Your choice (A, B, C, D): ").upper()
                if user_answer_label in answer_options:
                    user_answer = answer_options[user_answer_label]
                    break
                else:
                    print("Not an option")
            if user_answer == correct_answer:
                print("Correct!")
                score = score + 1
            else:
                print(f"The correct answer was {correct_answer}")
            question_number += 1
        print(f"Trivia quiz completed! You scored {score}/{numquestions}!")
    else:
        print(response.status_code)

def menu():
       while True:
              print("1. View the categories and their ids")
              print("2. Make a trivia quiz")
              print("3. Exit")
              choice = input("Enter your choice: ")
              try:
                     match int(choice):
                            case 1:
                               GetCategoryIDs()
                            case 2:
                               MakeTheQuiz()
                            case 3:
                                   print("Exiting")
                                   break
                            case _:
                                   print("Invalid choice.")
                                   break
              except:
                     print("An error has occured.")

if __name__ == "__main__":
     menu()