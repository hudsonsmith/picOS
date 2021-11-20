from json import load
from os import listdir


def isfile(filepath: str) -> bool:
    """A function to replace os.path.isfile in micropython."""
    try:
        open(filepath)
        return True

    except OSError:
        return False


def format_prompt(prompt: str) -> str:
    """A function to format the prompt according to escape codes."""
    prompt = prompt.replace("$u", username).replace("$h", hostname)
    return prompt


def find_program(paths: list, filename: str):
    """
    A function made to return the path to a program based on a list of dirs
    and a filename.
    """

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
    try:
        command = str(input(format_prompt(prompt)))

    # If the user hits ^C, continue the program without failing.
    except KeyboardInterrupt:
        # Print a newline to make sure the prompt does not get stacked on one line.
        print()
        continue

    # If the command is simply nothing, continue the loop.
    if command == "":
        continue

    # Find the file by formatting the command to look like a filename.
    file = find_program(paths, f"{command}.py")

    if file:
        try:
            exec(open(file).read())
        except KeyboardInterrupt:
            continue
    else:
        print(f"{command}: command not found")
