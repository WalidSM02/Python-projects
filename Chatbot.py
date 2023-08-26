from time import ctime
import json
from difflib import get_close_matches

""" Created a function called load_knowladge_base() to
 open a json file in the same folder"""

def load_knowladge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file) #<----Load the json file as dictionary.
    return data

""" Created a function called save_knowladge_base() to write an existing json file.
    This will help to store new answers from the user"""

def save_knowladge_base(file_path:str, data:dict):
    with open(file_path,"w") as file:
        json.dump(data, file, indent=2) #<---Store the datum as dictionary in json file.

""" Created a function called find_best_matches() to get the best similar question with 60% acuuracy"""        

def find_best_matches(user_question:str, questions:list[str]) -> str| None:
    matches:list = get_close_matches(user_question, questions, n=1, cutoff = 0.6)
    return matches[0] if matches else None
""" Created a function called get_answer_for_question() to get the answer. This could return None."""

def get_answer_for_question(question:str, knowladge_base: dict) -> str| None:
    for i in knowladge_base["question"]:
        if i["question"]== question:
            return i["answer"]
      
def chatbot():
    
    knowladge_base: dict = load_knowladge_base('knowladge_base.json') #<- Load the json file.
    
    while True:
        
        #Create a variable called user_input to take the inputs from the user.
        
        user_input: str = input("\nYou : ")
        # if statement for quitting the process/ while loop.
        if user_input.lower() == 'quit':
            print("Thank you for using me 💖")
            print("""
                  Programmed by:
                      SM Walid
                      Data scientist at Datacamp.
                      Date:%s
                  """%ctime())
            break
        best_matches: str = find_best_matches(user_input, [i["question"] for i in knowladge_base['question']])
        
        # if best_matches is a string.
        if best_matches:
            answer: str = get_answer_for_question(best_matches, knowladge_base)
            print(f'Bot : {answer}') #<- formating an answer.
        # if best_matches is None.
        else:
            print("Bot : I don\'t understand. Can you teach me?")
            new_answer:str = input(" Type answer or type 'skip' to skip \n>>>>>> ")
            if new_answer != "skip":
                # knowladge_base['question'] is a list type which will append a dictionary as object.
                knowladge_base['question'].append({'question': user_input, 'answer':new_answer})
                save_knowladge_base('knowladge_base.json', knowladge_base)
                print("Thank you for teaching.")
        
if __name__ == '__main__':
    chatbot()
    