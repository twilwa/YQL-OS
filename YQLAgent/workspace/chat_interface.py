import os
from agent import Agent

class ChatInterface:
    def __init__(self):
        self.agent = Agent()

    def run(self):
        while True:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                break
            response = self.agent.handle_input(user_input)
            print(f"Agent: {response}")
