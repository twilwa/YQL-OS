import os
from search_files import search_files
from evaluate_search_results import evaluate_search_results
from fill_in_the_blanks import fill_in_the_blanks
from approve_code import approve_code

class Agent:
    def __init__(self):
        self.tools_directory = os.path.join(os.getcwd(), "tools")
        self.workspace_directory = os.path.join(os.getcwd(), "workspace")

    def handle_input(self, user_input):
        search_results = search_files(user_input, self.tools_directory)
        tool_to_use = evaluate_search_results(search_results)
        if tool_to_use is None:
            tool_to_use = fill_in_the_blanks(user_input)
        code = approve_code(tool_to_use)
        return code
