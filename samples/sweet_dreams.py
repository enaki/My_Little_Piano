import array
from samples.abstract_song import Song


class SweetDreams(Song):
    def __init__(self, octave_1, octave_2, delay):
        super().__init__(delay)
        self.octave_1 = octave_1
        self.octave_2 = octave_2

    def play(self):
        self.sweet_dreams_sequence_1()
        self.sweet_dreams_sequence_2()
        self.sweet_dreams_sequence_3()

        self.sweet_dreams_sequence_1()
        self.sweet_dreams_sequence_2()
        self.sweet_dreams_sequence_4()

    def sweet_dreams_sequence_1(self, octave_1=None):
        o2 = octave_1 if octave_1 else self.octave_2
        delay = self.delay / 8

        # play every note indicated for delay1 (or delay2, or delay3)
        # seconds, then turn off the buzzer for delay4 seconds
        # then play the next note

        print("Sweet Dreams: first sequence")
        print("play: D D G D G_maj D G D")
        # create two arrays: one that stores the notes in order and
        # another that stores the playing time for each note
        self.sequence_notes_frequencies = array.array('i', [o2['c'], o2['c'], o2['g'], o2['c'], o2['gs'], o2['c'], o2['g'], o2['c']])
        self.sequence_notes = ['c', 'c', 'g', 'c', 'gs', 'c', 'g', 'c']
        self.sequence_delays = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits = array.array('f', [delay/4 for _ in range(len(self.sequence_notes_frequencies))])
        self.play_sequence()

    def sweet_dreams_sequence_2(self, octave_1=None, octave_2=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay / 8

        print("Sweet Dreams: second sequence")
        print("play: G_mag G_maj D_maj F")
        self.sequence_notes_frequencies = array.array('i', [o1['gs'], o1['gs'], o2['ds'], o2['f']])
        self.sequence_notes = ['gs', 'gs', 'ds', 'f']
        self.sequence_delays = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits = array.array('f', [delay/4 for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

    def sweet_dreams_sequence_3(self, octave_1=None, octave_2=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay / 8

        print("Sweet Dreams: third sequence")
        print("play: G G D D_maj")

        self.sequence_notes_frequencies = array.array('i', [o1['g'], o1['g'], o2['d'], o2['ds']])
        self.sequence_notes = ['g', 'g', 'd', 'ds']
        self.sequence_delays = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits = array.array('f', [delay/4 for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

    def sweet_dreams_sequence_4(self, octave_1=None, octave_2=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay / 8

        print("Sweet Dreams: forth sequence")
        print("play: G G D_maj D C")

        self.sequence_notes_frequencies = array.array('i', [o1['g'], o1['g'], o2['ds'], o2['d'], o2['c']])
        self.sequence_notes = ['g', 'g', 'ds', 'd', 'c']
        self.sequence_delays = array.array('f', [delay, delay, delay, delay, 4 * delay])
        self.sequence_awaits = array.array('f', [delay/4 for i_ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

