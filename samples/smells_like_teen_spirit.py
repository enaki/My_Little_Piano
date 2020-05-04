import array
from samples.abstract_song import Song
import time


class SmellsLikeTennSpirit(Song):
    def __init__(self, octave_1, octave_2, octave_3, delay):
        super().__init__(delay)
        self.octave_1 = octave_1
        self.octave_2 = octave_2
        self.octave_3 = octave_3

    def play(self):
        self.smells_lite_teen_spirit_sequence_1()
        self.smells_lite_teen_spirit_sequence_1()
        self.smells_lite_teen_spirit_sequence_2(self.octave_1, self.octave_2)
        self.smells_lite_teen_spirit_sequence_3(self.octave_1, self.octave_2)
        self.smells_lite_teen_spirit_sequence_4(self.octave_1, self.octave_2)
        self.smells_lite_teen_spirit_sequence_5(self.octave_1, self.octave_2)
        self.smells_lite_teen_spirit_sequence_6(octave_1=self.octave_1)
        self.smells_lite_teen_spirit_sequence_6(octave_1=self.octave_1)

        self.smells_lite_teen_spirit_sequence_4()
        self.smells_lite_teen_spirit_sequence_5(rising_octave=True)
        self.smells_lite_teen_spirit_sequence_6()
        self.smells_lite_teen_spirit_sequence_6()
        self.smells_lite_teen_spirit_sequence_6()
        self.smells_lite_teen_spirit_sequence_6(last_delay=6)

    def smells_lite_teen_spirit_sequence_1(self, octave_1=None, octave_2=None, octave_3=None):
        o1 = octave_1 if octave_1 else self.octave_1
        o2 = octave_2 if octave_2 else self.octave_2
        o3 = octave_3 if octave_3 else self.octave_3
        delay = self.delay/8

        print("Smells Like Teen Spirits: first sequence")
        print("play: F F C F A_maj A_maj A_maj A_maj G_maj G_maj G_maj G_maj C_maj C_maj C_maj C")

        self.sequence_notes_frequencies = array.array('i', [o1['f'], o1['f'], o3['c'], o3['f'], o1['as'],  o1['as'], o1['as'], o1['as'],
                                        o1['gs'], o1['gs'], o1['gs'], o1['gs'], o2['cs'], o2['cs'], o2['cs'], o2['c']])
        self.sequence_notes = ['f', 'f', 'c', 'f', 'as', 'as', 'as', 'as', 'gs', 'gs', 'gs', 'gs', 'cs', 'cs', 'cs', 'c']
        self.sequence_delays = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

    def smells_lite_teen_spirit_sequence_2(self, octave_1=None, octave_2=None):
        o2 = octave_1 if octave_1 else self.octave_2
        o3 = octave_2 if octave_2 else self.octave_3
        delay = self.delay / 8

        time.sleep(delay * 2)

        print("Smells Like Teen Spirits: second sequence")
        print("play: C D_maj F G_maj F D_maj C_maj C")

        self.sequence_notes_frequencies = array.array('i', [o3['c'], o3['ds'], o3['f'], o2['gs'], o3['f'], o3['ds'], o3['cs'], o3['c']])
        self.sequence_notes = ['c', 'ds', 'f', 'gs', 'f', 'ds', 'cs', 'c']
        self.sequence_delays = array.array('f', [delay, delay*2, delay*2, delay*5, delay*2, delay*3/4, delay*3/4, delay*4])
        self.sequence_awaits = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

    def smells_lite_teen_spirit_sequence_3(self, octave_1=None, octave_2=None):
        o2 = octave_1 if octave_1 else self.octave_2
        o3 = octave_2 if octave_2 else self.octave_3
        delay = self.delay / 8
        print("Smells Like Teen Spirits: third sequence")
        print("play: C C G_maj G_maj C A_maj G_maj G")
        self.sequence_notes_frequencies = array.array('i',
                                       [o3['c'], o3['c'], o2['gs'], o2['gs'], o3['c'], o2['as'], o2['gs'], o2['g']])
        self.sequence_notes = ['c', 'c', 'gs', 'gs', 'c', 'as', 'gs', 'g']
        self.sequence_delays = array.array('f',
                                        [delay, delay*4, delay, delay * 5, delay * 2, delay*3/4, delay*3/4, delay*4])
        self.sequence_awaits = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])

        self.play_sequence()

    def smells_lite_teen_spirit_sequence_4(self, octave_1=None, octave_2=None):
        o2 = octave_1 if octave_1 else self.octave_2
        o3 = octave_2 if octave_2 else self.octave_3
        delay = self.delay / 8

        print("Smells Like Teen Spirits: forth sequence")
        print("play: C D_maj F G_maj G_maj F D_maj C_maj C")
        self.sequence_notes_frequencies = array.array('i', [o3['c'], o3['ds'], o3['f'], o2['gs'], o2['gs'], o3['f'], o3['ds'], o3['cs'], o3['c']])
        self.sequence_notes = ['c', 'ds', 'f', 'gs', 'gs', 'f', 'ds', 'cs', 'c']
        self.sequence_delays = array.array('f', [delay, delay*2, delay*2, delay*4, delay, delay*2, delay*3/4, delay*3/4, delay*4])
        self.sequence_awaits = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits[4] *= 3/4
        self.play_sequence()

    def smells_lite_teen_spirit_sequence_5(self, octave_1=None, octave_2=None, rising_octave=False):
        o2 = octave_1 if octave_1 else self.octave_2
        o3 = octave_2 if octave_2 else self.octave_3
        delay = self.delay / 8

        print("Smells Like Teen Spirits: fifth sequence")
        print("play: C_maj C A_maj G_maj G_maj C A_maj G_maj G")
        if rising_octave:
            self.sequence_notes_frequencies = array.array('i', [o3['cs'], o3['c'], o2['as'], o2['gs'], o2['gs'], o3['c'], o3['as'], o3['gs'], o3['g']])
        else:
            self.sequence_notes_frequencies = array.array('i', [o3['cs'], o3['c'], o2['as'], o2['gs'], o2['gs'], o3['c'], o2['as'], o2['gs'], o2['g']])
        self.sequence_notes = ['cs', 'c', 'as', 'gs', 'gs', 'c', 'as', 'gs', 'g']
        self.sequence_delays = array.array('f', [delay, delay*7/2, delay, delay * 7/2, delay, delay * 2, delay*3/4, delay*3/4, delay * 4])
        self.sequence_awaits = array.array('f', [delay for _ in range(len(self.sequence_notes_frequencies))])
        self.sequence_awaits[4] *= 3 / 4

        self.play_sequence()

    def smells_lite_teen_spirit_sequence_6(self, octave_1=None, last_delay=2):
        o3 = octave_1 if octave_1 else self.octave_3
        delay = self.delay / 8

        print("Smells Like Teen Spirits: sixth sequence")
        print("play: C C G_maj G_maj C A_maj G_maj G")

        self.sequence_notes_frequencies = array.array('i',
                                       [o3['gs'], o3['g'], o3['gs'], o3['g'], o3['gs'], o3['g'], o3['gs'], o3['g'], o3['g'], o3['f']])
        self.sequence_notes = ['gs', 'g', 'gs', 'g', 'gs', 'g', 'gs', 'g', 'g', 'f' if last_delay==2 else 'c']
        self.sequence_delays = array.array('f',
                                        [delay, delay*4, delay, delay * 4, delay, delay * 2, delay, delay, delay, delay * last_delay])
        self.sequence_awaits = array.array('f', [delay*3/4, delay, delay*3/4, delay, delay*3/4, delay, delay*3/4, delay/2, delay*3/4, delay])

        self.play_sequence()