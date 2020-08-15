"""
Notes and tones will be represented by numbers, but notes != tones.

A note will always be in the range 0-11, and describes 1 of 12 notes in western
music.

A tone can be any integer. It corresponds to a note and an octave.
"""

import random
from math import floor

def get_chord_notes(chord):
    note_ids = { "C": 0, "Db": 1, "C#": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
        "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10,
        "Bb": 10, "B": 11, "Cb": 11
    }

    notes = []

    # The root (first note name)
    if len(chord) > 1 and (chord[1] == 'b' or chord [1] == '#'):
        notes.append(note_ids[chord[:2]])
    else:
        notes.append(note_ids[chord[0]])

    # The third (look for M and -)
    if "-" in chord:
        notes.append((notes[0] + 3) % 12)
    else:
        notes.append((notes[0] + 4) % 12)

    # The fifth (look for + and 5)
    notes.append((notes[0] + 7) % 12)

    # The seventh
    if "7" in chord:
        if chord[ chord.find("7") - 1 ] == "M":
            notes.append((notes[0] + 11) % 12)
        else:
            notes.append((notes[0] + 10) % 12)

    return notes

def pick_encl():
    pass

"""
Converts a note into a tone by assingin an octave.

Picks the closest octave for the note based on the previous tone. If there is no
previous tone, a random octave is assigned.

The default range is that of the saxophone.
"""
def pick_octv(note, prev_tone=None, range=(-2, 30)):
    if prev_tone == None:
        print("picking random")
        octvs = []
        # The lowest octave
        tone = note - (12 * floor((note - range[0]) / 12))

        while tone <= range[1]:
            octvs.append(tone)
            tone += 12

        return random.choice(octvs)
    else:
        prev_note = prev_tone % 12

        # The shortest interval in semitones
        intvl = abs(note - prev_note)
        intvl += -12 if intvl > 6 else 0
        intvl *= 1 if note >= prev_note else -1

        print(f"the shortest interval between {prev_note} and {note} is {intvl} semitones\n")

        if prev_tone + intvl > range[1] or prev_tone + intvl < range[0]:
            intvl *= -1

        return prev_tone + intvl