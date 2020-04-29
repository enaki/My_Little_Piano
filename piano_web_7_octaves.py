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

from flask import request, Flask, render_template, redirect, url_for, jsonify
import pigpio
import numpy as np

# create an instance of the pigpio library
pi = pigpio.pi()

# define the pin used by the Buzzer
# this is GPIO12, which is pin 32
buzzer = 12

# declare variables that will hold the frequencies of the
# notes from the sixth octave
c1 = 33
cs1 = 35
d1 = 37
ds1 = 39
e1 = 41
f1 = 44
fs1 = 46
g1 = 49
gs1 = 52
a1 = 55
as1 = 58
b1 = 62
c2 = 65
cs2 = 69
d2 = 73
ds2 = 78
e2 = 82
f2 = 87
fs2 = 93
g2 = 98
gs2 = 104
a2 = 110
as2 = 117
b2 = 123
c3 = 131
cs3 = 139
d3 = 147
ds3 = 156
e3 = 165
f3 = 175
fs3 = 185
g3 = 196
gs3 = 208
a3 = 220
as3 = 233
b3 = 247
c4 = 262
cs4 = 277
d4 = 294
ds4 = 311
e4 = 330
f4 = 349
fs4 = 370
g4 = 392
gs4 = 415
a4 = 440
as4 = 466
b4 = 494
c5 = 523
cs5 = 554
d5 = 587
ds5 = 622
e5 = 659
f5 = 698
fs5 = 740
g5 = 784
gs5 = 831
a5 = 880
as5 = 932
b5 = 988
c6 = 1047
cs6 = 1109
d6 = 1175
ds6 = 1245
e6 = 1319
f6 = 1397
fs6 = 1480
g6 = 1568
gs6 = 1661
a6 = 1760
as6 = 1865
b6 = 1976
c7 = 2093
cs7 = 2217
d7 = 2349
ds7 = 2489
e7 = 2637
f7 = 2794
fs7 = 2960
g7 = 3136
gs7 = 3322
a7 = 3520
as7 = 3729
b7 = 3951

# declare a variable that will store the current octave
octave = 1

# create arrays with the notes for each octave (in order)
octave1 = np.array([c1, cs1, d1, ds1, e1, f1, fs1, g1, gs1, a1, as1, b1])
octave2 = np.array([c2, cs2, d2, ds2, e2, f2, fs2, g2, gs2, a2, as2, b2])
octave3 = np.array([c3, cs3, d3, ds3, e3, f3, fs3, g3, gs3, a3, as3, b3])
octave4 = np.array([c4, cs4, d4, ds4, e4, f4, fs4, g4, gs4, a4, as4, b4])
octave5 = np.array([c5, cs5, d5, ds5, e5, f5, fs5, g5, gs5, a5, as5, b5])
octave6 = np.array([c6, cs6, d6, ds6, e6, f6, fs6, g6, gs6, a6, as6, b6])
octave7 = np.array([c7, cs7, d7, ds7, e7, f7, fs7, g7, gs7, a7, as7, b7])

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

octave_array = np.array([octave1, octave2, octave3, octave4, octave5, octave6, octave7])

app = Flask(__name__, template_folder='templates')

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


try:
    # we will run the app on port 5000
    #run(host='0.0.0.0', port='5000')
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

except KeyboardInterrupt:
    pass

# stop the pwm signal
pi.hardware_PWM(buzzer, 0, 0)
