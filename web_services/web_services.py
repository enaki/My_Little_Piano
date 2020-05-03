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
import pigpio


# create an instance of the pigpio library
pi = pigpio.pi()

# define the pin used by the Buzzer
# this is GPIO12, which is pin 32
buzzer = 12

# create an instance of flask
app = Flask(__name__, template_folder='../templates')

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
    pi.hardware_PWM(buzzer, octave_array[octave - 1][0], 500000)

    # send a message to the user
    return 'ok'


@app.route('/cs_note')
def cs_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][1], 500000)

    # send a message to the user
    return 'ok'


@app.route('/d_note')
def d_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][2], 500000)

    # send a message to the user
    return 'ok'


@app.route('/ds_note')
def ds_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][3], 500000)

    # send a message to the user
    return 'ok'


@app.route('/e_note')
def e_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][4], 500000)

    # send a message to the user
    return 'ok'


@app.route('/f_note')
def f_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][5], 500000)

    # send a message to the user
    return 'ok'


@app.route('/fs_note')
def fs_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][6], 500000)

    # send a message to the user
    return 'ok'


@app.route('/g_note')
def g_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][7], 500000)

    # send a message to the user
    return 'ok'


@app.route('/gs_note')
def gs_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][8], 500000)

    # send a message to the user
    return 'ok'


@app.route('/a_note')
def a_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][9], 500000)

    # send a message to the user
    return 'ok'


@app.route('/as_note')
def as_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][10], 500000)

    # send a message to the user
    return 'ok'


@app.route('/b_note')
def b_note():
    # play the note on the buzzer
    pi.hardware_PWM(buzzer, octave_array[octave - 1][11], 500000)
    print(octave)
    # send a message to the user
    return 'ok'


@app.route('/off')
def off():
    # turn off the buzzer
    pi.hardware_PWM(buzzer, 0, 0)

    # send a message to the user
    return 'ok'


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