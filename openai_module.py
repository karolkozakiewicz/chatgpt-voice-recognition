import os
import openai

import requests

openai.api_key = ""

class Openai_Model:
    
    def __init__(self) -> None:
        pass
    
    def ask_question(self, question):
        answer = openai.Completion.create(engine="text-davinci-003",
                                        prompt=str(question),
                                        max_tokens=150,
                                        temperature=0.9)
        return answer['choices'][0]['text'][:3].replace("\n", "") + answer['choices'][0]['text'][3:]
        
    def main(self):
        while True:
            question = str(input())
            print(self.ask_question(question))
        
    
