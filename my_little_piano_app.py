"""
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
import threading
import numpy as np

from samples.coffin_dance import CoffinDance
from samples.sweet_dreams import SweetDreams
from samples.smells_like_teen_spirit import SmellsLikeTennSpirit
from web_services import web_services as web
from raspberrypi_configurations import raspberrypi_configurations as rasp

running_flag = True


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
    web.octave_array = np.array([np.array(list(octave.values())) for octave in data.values()])


def local_input_piano_samples():
    global running_flag
    try:
        data = get_piano_octaves_json()
        sweet_dreams = SweetDreams(data['octave_4'], data['octave_5'], 3)
        smells_like_teen_spirits = SmellsLikeTennSpirit(data['octave_4'], data['octave_5'], data['octave_6'], 1.2)
        coffin_dance = CoffinDance(data['octave_4'], data['octave_5'], 1.2)
        print("Loaded piano json for local input. Thread: {}".format(threading.current_thread()))
        while running_flag:
            # if the first button was pressed, play the first song
            if rasp.GPIO.input(rasp.button1) == rasp.GPIO.LOW and rasp.is_buzzer_off:
                rasp.is_buzzer_off = False
                rasp.is_buzzer_used_locally = True
                sweet_dreams.play()
                rasp.is_buzzer_off = True
                rasp.is_buzzer_used_locally = False

            # if the second button was pressed, play the second song
            if rasp.GPIO.input(rasp.button2) == rasp.GPIO.LOW and rasp.is_buzzer_off:
                rasp.is_buzzer_off = False
                rasp.is_buzzer_used_locally = True
                smells_like_teen_spirits.play()
                rasp.is_buzzer_off = True
                rasp.is_buzzer_used_locally = False

            # if the second button was pressed, play the second song
            if rasp.GPIO.input(rasp.button3) == rasp.GPIO.LOW and rasp.is_buzzer_off:
                rasp.is_buzzer_off = False
                rasp.is_buzzer_used_locally = True
                coffin_dance.play()
                rasp.is_buzzer_off = True
                rasp.is_buzzer_used_locally = False
    except (RuntimeError, OSError, AttributeError, KeyboardInterrupt):
        print("Unexpected event in the main thread. Exiting thread {}".format(threading.current_thread()))
    finally:
        print("Thread {} stopped.".format(threading.current_thread()))


def main():
    global running_flag
    web.octave_array = None
    local_input_thread = None
    load_piano_octaves()
    if web.octave_array is None:
        return

    try:
        # we will run the app on port 5000
        # run(host='0.0.0.0', port='5000')
        local_input_thread = threading.Thread(target=local_input_piano_samples)
        local_input_thread.daemon = True
        local_input_thread.start()

        web.app.debug = False
        web.app.use_reloader = False
        web.app.run(host='0.0.0.0', port=5000)

    except KeyboardInterrupt:
        pass
    finally:
        #stop the local thread
        running_flag = False

        # stop the pwm signal
        rasp.pi.hardware_PWM(web.buzzer, 0, 0)
        rasp.rgb_led_configure()
        rasp.GPIO.cleanup()

        # stop the connection with the daemon
        rasp.pi.stop()


if __name__ == '__main__':
    main()

