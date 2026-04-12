# WSAA Assignments
## Author: Orla Woods

This repository contains weekly assignments for the Web Services and Applications (WSAA) module at ATU. Each assignment involves interacting with external APIs or web services using Python.

## Assignment 2 - Card Draw
**File:** `deckofcards.py`

### Description
A program that simulates dealing 5 cards from a shuffled deck using the [Deck of Cards API](https://deckofcardsapi.com/). It checks the hand for special combinations and congratulates the user.

### How it works
1. Calls the Deck of Cards API to shuffle a new deck and retrieve a deck ID
2. Draws 5 cards using the deck ID
3. Prints the value and suit of each card
4. Checks the hand for:
   - Pair
   - Three of a kind
   - Straight (5 consecutive values)
   - Flush (all same suit)

### How to run
```bash
python deckofcards.py
```

---

## Assignment 3 - CSO Data Retrieval
**File:** `assignment03-cso.ipynb`

### Description
A Jupyter notebook that retrieves the "Exchequer Account (Historical Series)" dataset from the Central Statistics Office (CSO) API and saves it to a local JSON file.

### How it works
1. Calls the CSO PxStat API for dataset `FIQ02` (Exchequer Account Historical Series)
2. Returns data in JSON-stat 2.0 format 
3. Saves the response to `cso.json` with indented formatting for readable

### How to run
```bash
jupyter nbconvert --to notebook --execute assignment03-cso.ipynb
```
Or open in VS Code and click **Run All**.

### Output
A file called `cso.json` will be created in the same directory.

---

## Assignment 4 - GitHub API
**Files:** `assignment04-github.py`, `getrepoinformation.py`

### Description
Two programs that interact with the GitHub API:

1. **`assignment04-github.py`** — Reads a file from a public GitHub repository, replaces all instances of "Andrew" with "Orla", and pushes the updated file back to a private repository using a personal access token.

2. **`wsaa-code.json`** — Retrieved by a helper script that reads the contents of Andrew's course material repository and saves it locally as a JSON file.

### How it works - assignment04-github.py
1. Reads `getrepoinformation.py` from [andrewbeattycourseware/wsaa-courseware](https://github.com/andrewbeattycourseware/wsaa-courseware) (public repo, no token needed)
2. Replaces all instances of "Andrew" with "Orla"
3. Checks if the file already exists in the destination repo (retrieves SHA if it does)
4. Pushes the updated file to the destination repo using the GitHub API

### Security
This program uses a `config.py` file to store sensitive credentials. This file is listed in `.gitignore` and is **never pushed to GitHub**.

`config.py` should contain:
```python
GitHub_token      = "your_token_here"
Destination_owner = "your_github_username"
Destination_repo  = "your_repo_name"
Destination_file  = "path/to/output/file.py"
```

### How to run
```bash
python assignment04-github.py
```

### Expected output
