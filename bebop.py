"""
Notes and tones will be represented by numbers, but notes != tones.

A note will always be in the range 0-11, and describes 1 of 12 notes in western
music.

A tone can be any integer. It corresponds to a note and an octave.
"""

import random
from math import floor
import music

SAXOPHONE = (-2, 30)

"""
len(chord_tones) == len(chords)
"""
def create_encl(chord_tone, range=SAXOPHONE):
    # Temporarily split the flag while we generate enclosure notes
    chord_tone, flag = music.split_flag(chord_tone)

    encls = (
        (3, 2, 1),
        (-3, -2, -1),
        (1, -2, -1),
        (-1, 2, 1),
        (-2, 1, -1),
        (2, -1, 1)
    )

    encl = list(e + chord_tone for e in random.choice(encls))
    encl.append(chord_tone + flag)

    # Likely susceptible to edge cases, but if the enclosures become more
    # complex in the future, then this will be adjusted.
    for tone in encl:
        if tone < range[0]:
            encl = tuple(e + 12 for e in encl)
        elif tone > range[1]:
            encl = tuple(e - 12 for e in encl)

    return encl

"""
Converts a note into a tone by assingin an octave.

Picks the closest octave for the note based on the previous tone. If there is no
previous tone, a random octave is assigned.

The default range is that of the saxophone.
"""
def pick_octv(note, prev_tone=None, range=SAXOPHONE):
    if prev_tone == None:
        octvs = []
        # The lowest octave
        tone = note - (12 * floor((note - range[0]) / 12))

        while tone <= range[1]:
            octvs.append(tone)
            tone += 12

        return random.choice(octvs)
    else:
        prev_note = prev_tone % 12

        # The numerical difference in semitones
        intvl = abs(note - prev_note)

        # If the difference is greater than a tritone, then it can be
        # represented by a smaller interval
        intvl += -12 if intvl > 6 else 0

        # Flip the direction of the interval if the previous note is higher
        intvl *= 1 if note >= prev_note else -1

        # If the interval will go out of range, get the composite interval
        if prev_tone + intvl > range[1]:
            intvl -= 12
        elif prev_tone + intvl < range[0]:
            intvl += 12

        return prev_tone + intvl