HISTORY_FILE = "history.txt"

def save_history (entry):
    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")

def read_history ():
    try:
        with open(HISTORY_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
