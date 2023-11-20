import requests

def generate_random_sentence():
    # use API to generate random sentence

    response = requests.get("https://api.quotable.io/random")
    data = response.json()

    sentence = data["content"]

    return sentence

def write_to_file(sentence, filename="randomsentence.txt"):
    # write random sentence to file
    with open(filename, "w") as file:
        file.write(sentence)

def read_from_file(filename="randomsentence.txt"):
    # read random sentence from file
    # this function can be erased if you are using another program to read the text file
    with open(filename, "r") as file:
        sentence = file.read()

        return sentence

