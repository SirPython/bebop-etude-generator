from math import floor, isclose
import bebop
import music

#http://www.clivew.com/abc.php

class ABCNotator():
    def __init__(self):
        self.note_cnt = 0
        self.msr_cnt = 0
        self.accids = []
        self.last_tone = 0

        # Score saved as internal state so that the outer program does not need
        # to keep track of the score as it is being generated.
        self.score = f"""X: 1
T: Bebop Etude
C: Bebop Etude Generator
M: 4/4
K: C
L: 1/8
"""

    """
    Convers a tone into ABC notation. Applies commas and apostrophes to
    represent the octave. Accidentals are applied based on the previous tone
    notated (self.last_tone)
    """
    def cvt_tone(self, tone):
        tone, flag = music.split_flag(tone)
        note = ""

        # Use flats when going down, sharps when going up
        if self.last_tone > tone or isclose(flag, music.FLAT_FLAG):
            note = ("C","_D","D","_E","E","F","_G","G","_A","A","_B","B")[tone % 12]
        else:
            note = ("C","^C","D","^D","E","F","^F","G","^G","A","^A","B")[tone % 12]

        #print(f"{note} {flag}")

        # Stack on 's or ,s to change octave in ABC notation
        octvs = floor(abs(tone / 12)) + (1 if tone < 0 else 0)
        return note + ("'" if tone > 0 else ",") * octvs

    """
    Given a tone, writes it to the score in the state. Inserts spaces, vertical
    bars, and newlines as appropriate to differentiate 8th note groups,
    measures, and lines.
    """
    def notate(self, tone):
        # This is a note in the sense of notation
        note = self.cvt_tone(tone)
        self.last_tone = tone

        # If there's an accidental
        if len(note) > 1:
            self.accids.append(note[1])

        # If there's no accidental but the note has appeared before with one
        elif note in self.accids:
            note = f"={note}"

        if self.note_cnt == 8:
            self.note_cnt = 0
            self.accids = []
            self.msr_cnt += 1

            self.score += "|"
        elif self.note_cnt == 4:
            self.score += " "

        if self.msr_cnt == 4:
            self.msr_cnt = 0

            self.score += "\n"

        self.score += note
        self.note_cnt += 1