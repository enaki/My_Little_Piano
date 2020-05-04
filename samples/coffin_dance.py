import array
from samples.abstract_song import Song
import time


class CoffinDance(Song):
    def __init__(self, octave_1, octave_2, delay):
        super().__init__(delay)
        self.octave_1 = octave_1
        self.octave_2 = octave_2

    def play(self):
        self.coffin_dance_sequence_header()
        self.coffin_dance_sequence_1()
        self.coffin_dance_sequence_2()
        self.coffin_dance_sequence_2()
        self.coffin_dance_sequence_1()
        self.coffin_dance_sequence_2()
        self.coffin_dance_sequence_2(play_last_note=False)
        self.coffin_dance_sequence_3()

    def coffin_dance_sequence_header(self, octave_1=None):
        o1 = octave_1 if octave_1 else self.octave_1
        delay = self.delay/8

        print("Coffin Dance: header sequence")
        print("play: B A G_maj E F_maj")

        self.sequence_notes_frequencies = array.array('i', [o1['b'], o1['a'], o1['gs'], o1['e'], o1['fs']])
        self.sequence_notes = ['b', 'a', 'gs', 'e', 'fs']
        self.sequence_delays = array.array('f', [delay, delay, delay, delay, delay*2])
        self.sequence_awaits = array.array('f', [delay/2, delay/2, delay/2, delay/2, delay])
        self.play_sequence()

    def coffin_dance_sequence_1(self, octave_1=None, octave_2=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay/8

        print("Coffin Dance: first sequence")
        print("play: F_maj C_maj B A G_maj G_maj G_maj B A G_maj F_maj")

        self.sequence_notes_frequencies = array.array('i', [o1['fs'], o2['cs'], o1['b'], o1['a'],  o1['gs'], o1['gs'], o1['gs'],
                                        o1['b'], o1['a'], o1['gs'], o1['fs']])
        self.sequence_notes = ['fs', 'cs', 'b', 'a', 'gs', 'gs', 'gs', 'b', 'a', 'gs', 'fs']
        self.sequence_delays = array.array('f', [delay, delay, delay*2, delay*2, delay*2, delay, delay, delay*2, delay, delay, delay*2])
        self.sequence_awaits = array.array('f', [delay/2, delay/2, delay, delay, delay, delay/2, delay/2, delay, delay/2, delay/2, delay])

        self.play_sequence()

    def coffin_dance_sequence_2(self, octave_1=None, octave_2=None, play_last_note=True):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay/8

        if play_last_note:
            print("Coffin Dance: second sequence")
            print("play: F_maj A G_maj A G_maj A F_maj")

            self.sequence_notes_frequencies = array.array('i', [o1['fs'], o2['a'], o2['gs'], o2['a'], o2['gs'],  o2['a'], o1['fs']])
            self.sequence_notes = ['fs', 'a', 'gs', 'a', 'gs', 'a', 'fs']
            self.sequence_delays = array.array('f', [delay, delay, delay, delay, delay, delay, delay*2])
            self.sequence_awaits = array.array('f', [delay/2, delay/2, delay/2, delay/2, delay/2, delay/2, delay])
        else:
            print("Coffin Dance: second sequence (without last note)")
            print("play: F_maj A G_maj A G_maj A")

            self.sequence_notes_frequencies = array.array('i', [o1['fs'], o2['a'], o2['gs'], o2['a'], o2['gs'], o2['a']])
            self.sequence_notes = ['fs', 'a', 'gs', 'a', 'gs', 'a']
            self.sequence_delays = array.array('f', [delay, delay, delay, delay, delay, delay])
            self.sequence_awaits = array.array('f', [delay / 2, delay / 2, delay / 2, delay / 2, delay / 2, delay / 2])
        self.play_sequence()

    def coffin_dance_sequence_3(self, octave_1=None, octave_2=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        delay = self.delay/8

        print("Coffin Dance: third sequence")
        print("play: A A A A C C C C B B B B E E E E E_maj E_maj E_maj E_maj E_maj E_maj E_maj E_maj E_maj E_maj E_maj E_maj")

        self.sequence_notes_frequencies = array.array('i', [o1['a'], o1['a'], o1['a'], o1['a'],
                                                            o2['cs'], o2['cs'], o2['cs'], o2['cs'],
                                                            o1['b'], o1['b'], o1['b'], o1['b'],
                                                            o2['e'], o2['e'], o2['e'], o2['e'],
                                                            o2['fs'], o2['fs'], o2['fs'], o2['fs'],
                                                            o2['fs'], o2['fs'], o2['fs'], o2['fs'],
                                                            o2['fs'], o2['fs'], o2['fs'], o2['fs']])
        self.sequence_notes = ['a', 'a', 'a', 'a',
                               'c', 'c', 'c', 'c',  # we put 'c' this here because i want to display red c's color instead of cyan of cs
                               'b', 'b', 'b', 'b',
                               'e', 'e', 'e', 'e',
                               'fs', 'fs', 'fs', 'fs',
                               'fs', 'fs', 'fs', 'fs',
                               'fs', 'fs', 'fs', 'fs']
        self.sequence_delays = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits = array.array('f', [delay/2 for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()