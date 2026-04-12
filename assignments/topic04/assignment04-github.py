# This program will read a file from a public GitHub repository,
# replace all instances of "Andrew" with "Orla" and push the changes back to my repo, using authorisation.

import requests
import base64
import config

# config.py added to gitignore so API token not pushed to GitHub

# Source public repo (no authorisation/token required): https://github.com/andrewbeattycourseware
source_owner = "andrewbeattycourseware"
source_repo  = "wsaa-courseware"
source_file  = "code/Topic03-apis/bookapidao.py"

# Destination (my repo) details loaded from config.py
dest_owner = config.Destination_owner
dest_repo  = config.Destination_repo
dest_file  = config.Destination_file

# Define authorisation header using token from config.py
headers = {
    "Authorization": f"token {config.GitHub_token}",
    "Accept": "application/vnd.github+json"
}

def get_file_from_source():
    #Read the file from Andrew's public repo
    url = f"https://api.github.com/repos/{source_owner}/{source_repo}/contents/{source_file}"
    
    # No authorisation needed for public repo
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Decode base64 GitHub file
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content

def replace_name(content):
    # Replace all instances of 'Andrew' with my name "Orla"
    return content.replace("Andrew", "Orla") 

def push_to_my_repo(new_content):
    # Push the updated file to my own assignments repo
    url = f"https://api.github.com/repos/{dest_owner}/{dest_repo}/contents/{dest_file}"

    # Check if file already exists in my repo (need Secure Hash Alogrithm - SHA- to update it)
    sha = None
    check = requests.get(url, headers=headers)
    if check.status_code == 200:
        sha = check.json()["sha"]  # file exists, grab its SHA so it can replace this file with the new content

    # GitHub requires content to be base64 encoded when pushing 
    encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")

    # Build the commit content with message and encoded file content
    payload = {
        "message": "Assignment 04 - replaced Andrew with my name",
        "content": encoded
    }

    # Include SHA if updating an existing file
    if sha:
        payload["sha"] = sha

    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    print("File successfully pushed to my repo.")

if __name__ == "__main__":
    # Step 1: Read the file from Andrew's repo
    content = get_file_from_source()
    print("File read successfully.")

    # Step 2: Replace the name
    updated = replace_name(content)
    print("Name replaced successfully.")

    # Step 3: Push to my own repo
    push_to_my_repo(updated)

