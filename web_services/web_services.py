# we have included the octave arrays in another array.
# this way we have created a matrix in which we can call the frequency by octave and
# note number as described in the next "illustration"
#
# |   |   | |   |   |   |   | |   | |   |   |
# |   |   | |   |   |   |   | |   | |   |   |frequency
# |   |   | |   |   |   |   | |   | |   |   |
# |   |C S| |D S|   |   |F S| |G S| |A S|   |
# |   | 1 | | 3 |   |   | 6 | | 8 | |10 |   |
# |   |___| |___|   |   |___| |___| |___|   |
# |     |     |     |     |     |     |     |
# |  C  |  D  |  E  |  F  |  G  |  A  |  B  |
# |  0  |  2  |  4  |  5  |  7  |  9  |  11 |
# -------------------------------------------

from flask import request, Flask, render_template, redirect, url_for, jsonify
from raspberrypi_configurations import raspberrypi_configurations as rasp

# create an instance of flask
from raspberrypi_configurations.raspberrypi_configurations import start_rgb_led_by_note

app = Flask(__name__, template_folder='../templates')

pi = rasp.pi
buzzer = rasp.buzzer

#defining the first octave to start with
octave = 1
octave_array = None



# define the route for the main page
@app.route('/')
def index():
    # at the '/' route we will return the index.html
    # template that is in the templates folder
    return render_template('index.html')


@app.route('/c_note')
def c_note():
    # play the note on the buzzer
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][0], 500000)
        start_rgb_led_by_note('c')

        # send a message to the user
        return 'ok'
    else:
        return 'not ok'


@app.route('/cs_note')
def cs_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][1], 500000)
        start_rgb_led_by_note('cs')

        return 'ok'
    else:
        return 'not ok'


@app.route('/d_note')
def d_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][2], 500000)
        start_rgb_led_by_note('d')
        return 'ok'
    else:
        return 'not ok'


@app.route('/ds_note')
def ds_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][3], 500000)
        start_rgb_led_by_note('ds')
        return 'ok'
    else:
        return 'not ok'


@app.route('/e_note')
def e_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][4], 500000)
        start_rgb_led_by_note('e')

        return 'ok'
    else:
        return 'not ok'


@app.route('/f_note')
def f_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][5], 500000)
        start_rgb_led_by_note('f')

        return 'ok'
    else:
        return 'not ok'


@app.route('/fs_note')
def fs_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][6], 500000)
        start_rgb_led_by_note('fs')
        return 'ok'
    else:
        return 'not ok'


@app.route('/g_note')
def g_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][7], 500000)
        start_rgb_led_by_note('g')
        return 'ok'
    else:
        return 'not ok'


@app.route('/gs_note')
def gs_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][8], 500000)
        start_rgb_led_by_note('gs')
        return 'ok'
    else:
        return 'not ok'


@app.route('/a_note')
def a_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][9], 500000)
        start_rgb_led_by_note('a')
        return 'ok'
    else:
        return 'not ok'


@app.route('/as_note')
def as_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][10], 500000)
        start_rgb_led_by_note('as')
        return 'ok'
    else:
        return 'not ok'


@app.route('/b_note')
def b_note():
    if rasp.is_buzzer_off:
        rasp.is_buzzer_off = False
        pi.hardware_PWM(buzzer, octave_array[octave - 1][11], 500000)
        start_rgb_led_by_note('b')
        return 'ok'
    else:
        return 'not ok'


@app.route('/off')
def off():
    if not rasp.is_buzzer_off and not rasp.is_buzzer_used_locally:
        # turn off the buzzer
        pi.hardware_PWM(buzzer, 0, 0)
        rasp.rgb_turn_off()
        rasp.is_buzzer_off = True
        return 'ok'
    else:
        return 'not ok'


@app.route('/set_octave', methods=['POST'])
def set_octave():
    global octave
    octave = int(request.form['octave'])
    # send a message to the user
    return 'ok'


@app.route('/refresh', methods=['GET'])
def refresh():
    # send the value to the client
    return jsonify({'octave': octave})