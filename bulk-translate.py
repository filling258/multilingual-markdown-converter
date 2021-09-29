
import openai, tiktoken, time

# Setup initialisation parameters
input_language = "english"
output_language = [
    "french",
    "german",
    "italian",
    "spanish",
    "japanese",
    "korean",
    "chinese_simplified",
    "russian",
    "portuguese",
]
input_paths = ["data/input.txt", "data/input.txt"]
output_paths = ["data/input.txt", "data/input.txt"]
format = "markdown (possibly including front-matter)"  # any special formatting considerations (e.g. .arb file, markdown, json, plain text, or multiple)
split_string = "\n\n"  # the split string used to segment the chunks within the text.
# TODO: whether to persist the chunks to a file or not
persist_chunks = False


# Import the files to be translated
file_contents = []
for path in input_paths:
    with open(path, "r") as f:
        file_contents.append(f.read())

# Simple test to get an idea of the length of the text and token cost