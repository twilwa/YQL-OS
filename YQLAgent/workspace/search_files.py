import os

def search_files(query, tools_directory):
    search_results = []
    for root, _, files in os.walk(tools_directory):
        for file in files:
            if query.lower() in file.lower():
                search_results.append(os.path.join(root, file))
    return search_results
