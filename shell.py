from json import load
from os import listdir
from os.path import isfile


def format_prompt(prompt: str) -> str:
    """A function to format the prompt according to escape codes."""
    prompt = prompt.replace("$u", username).replace("$h", hostname)
    return prompt


def find_program(paths: list, filename: str):
    # Search through the given paths for a file to execute.
    for path in paths:
        dir: list = listdir(path)

        for file in dir:
            # If the file is named the same, then run it.
            if file == filename:
                return f"{path}/{file}"

    # If the file cannot be found, return False.
    return False


# Open the config file and read from it.
with open("config.json", "r") as f:
    data: dict = load(f)
    username: str = data["username"]
    hostname: str = data["hostname"]
    prompt: str = data["prompt"]
    paths: list = data["paths"]

# Program Mainloop.
while True:
    command = str(input(prompt))
