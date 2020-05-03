"""
 * Credits: www.plusivo.com
 *
 * Lesson 26: Piano
 *
 * The code below is created for the lesson "Piano"
 * where you will learn how to create a piano style, with one octave.
 * In HTML and using JavaScript we will call special functions that
 * will play a specific note on the buzzer when any key of the piano
 * is pressed.
 *
 * Make sure you connected the buzzer correctly, according to the guide.
 *
 * Before you run the code, do not forget to start the pigpiod daemon
 * using "sudo pigpiod".
 *
 * More information about the code can be found in the guide.
 """

# import the libraries used
import sys

import numpy as np
from web_services import web_services as web


# loads the octaves of the piano into the octave_array variable
def load_piano_octaves():
    import json
    try:
        with open("resources/piano_octaves.json") as json_file:
            data = json.load(json_file)
            web.octave_array = np.array([np.array([list(note.values())[0] for note in octave]) for octave in data.values()])
    except FileNotFoundError:
        return


def main():

    web.octave_array = None
    load_piano_octaves()
    if web.octave_array is None:
        return


    try:
        # we will run the app on port 5000
        # run(host='0.0.0.0', port='5000')
        web.app.debug = True
        web.app.run(host='0.0.0.0', port=5000)

    except KeyboardInterrupt:
        pass

    # stop the pwm signal
    web.pi.hardware_PWM(web.buzzer, 0, 0)


if __name__ == '__main__':
    main()

