import numpy as np


# get the json piano octaves
def get_piano_octaves_json():
    import json
    try:
        with open("resources/piano_octaves.json") as json_file:
            data = json.load(json_file)
            return data

    except FileNotFoundError:
        print("File not Found")


# loads the octaves of the piano into the octave_array variable
def load_piano_octaves():
    data = get_piano_octaves_json()
    return np.array([np.array(list(octave.values())) for octave in data.values()])