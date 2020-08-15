"""
Notes and tones will be represented by numbers, but notes != tones.

A note will always be in the range 0-11, and describes 1 of 12 notes in western
music.

A tone can be any integer. It corresponds to a note and an octave.
"""

import random
from math import floor

def cvt_num(num, accid="flat"):


    return note

def tone2note(tone):
    return tone % 12

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
def pick_octv(note, prev=None, range=(-2, 30)):
    if prev == None:
        octvs = []
        # The lowest octave
        tone = note - (12 * floor((note - range[0]) / 12))

        while tone <= range[1]:
            octvs.append(tone)
            tone += 12

        return random.choice(octvs)
    else:
        intvl = abs(note - prev)
        up = True if intvl > abs(note+12 - prev) else False

        if up:
            # If the interval is supposed to go up but it would go out of range,
            # then set it downwards instead.
            up = up and prev + intvl < range[1]
        else:
            up = up or prev - intvl < range[0]

        return prev + (intvl * (1 if up else -1))