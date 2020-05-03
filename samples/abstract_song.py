import time

from raspberrypi_configurations import raspberrypi_configurations
from raspberrypi_configurations.raspberrypi_configurations import rgb_turn_off, start_rgb_led_by_note

pi = raspberrypi_configurations.pi
buzzer = raspberrypi_configurations.buzzer


class Song:
    def __init__(self, delay):
        self.delay = delay
        self.sequence_notes_frequencies = None
        self.sequence_notes = None
        self.sequence_delays = None
        self.sequence_awaits = None

    def play_sequence(self):
        # using the for loop we will play all the notes in the correct
        # order
        for i in range(0, len(self.sequence_notes_frequencies)):
            # play "i" note
            pi.hardware_PWM(buzzer, self.sequence_notes_frequencies[i], 500000)
            # turn on the led corresponding to the notes
            start_rgb_led_by_note(self.sequence_notes[i])

            # time for playing the "i" note
            time.sleep(self.sequence_delays[i])

            # turn off the buzzer
            pi.hardware_PWM(buzzer, 0, 0)
            # turn off the rgb led
            rgb_turn_off()

            time.sleep(self.sequence_awaits[i])