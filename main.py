import random

class Note:
    ONE = ("A")
    TWO = ("A#", "Bb")
    THREE = ("B")
    FOUR = ("C")
    FIVE = ("C#", "Db")
    SIX = ("D")
    SEVEN = ("D#", "Eb")
    EIGHT = ("E")
    NINE = ("F")
    TEN = ("F#", "Gb")
    ELEVEN = ("G")
    TWELVE = ("G#", "Ab")

note_ids = { "A": 0, "Bb": 1, "A#": 1, "B": 2, "Cb": 2, "C": 3, "Db": 4,
    "C#": 4, "D": 5, "Eb": 6, "D#": 6, "E": 7, "F": 8, "F#": 9, "Gb": 9,
    "G": 10, "Ab": 11, "G#": 11
}

id_note = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab"]

def get_chord_tones(chord):
    '''
    1. read the root
    2. look for a - or a +
    3. find the triad notes
    4. look for a 7, and preceding M
    5. look for 9, 11, and 13, looking for b or # preceding
    '''
    tones = []

    # The root
    if chord[1] == 'b' or chord [1] == '#':
        tones.append(note_ids[chord[:2]])
    else:
        tones.append(note_ids[chord[0]])

    # The third
    if "-" in chord:
        tones.append(notes_ids[ (tones[0] + 3) % 11 ])
    else:
        tones.append(notes_ids[ (tones[0] + 4) % 11 ])

    # The fifth
    tones.append(note_ids[ (tones[0] + 7) % 11 ])

    # The seventh
    if "7" in chord:
        if chord[ chord.find("7") - 1 ] == "M":
            tones.append(note_ids[ (tones[0] + 11) % 11 ])
        else:
            tones.append(note_ids[ (tones[0] + 10) % 11 ]

'''
1. get next chord's tones
2. choose an approach
3. write the approach notes on beats 1+, 2, and 2+
4. write the chord tone on beat 3
'''

if __name__ == "__main__":
    chord_notes = []
    all_notes = []

    for chord in chords:
        chord_tones.append(random.choose(get_chord_tones(chord)))
