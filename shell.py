import json


def format_prompt(prompt: str) -> str:
    """A function to format the prompt according to escape codes."""
    prompt = prompt.replace("$u", username).replace("$h", hostname)
    return prompt


# Open the config file and read from it.
with open("config.json", "r") as f:
    data: dict = json.load(f)
    username: str = data["username"]
    hostname: str = data["hostname"]
    prompt: str = data["prompt"]

# Program Mainloop.
while True:
    command = str(input(prompt))
