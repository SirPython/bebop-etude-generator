import random
from abc_notation import ABCNotator

note_ids = { "A": 0, "Bb": 1, "A#": 1, "B": 2, "Cb": 2, "C": 3, "Db": 4,
    "C#": 4, "D": 5, "Eb": 6, "D#": 6, "E": 7, "F": 8, "F#": 9, "Gb": 9,
    "G": 10, "Ab": 11, "G#": 11
}

id_note = ["=A", "_B", "=B", "=C", "_D", "=D", "_E", "=E", "=F", "^F", "=G",
    "_A"]

def get_chord_tones(chord):
    tones = []

    # The root (first note name)
    if len(chord) > 1 and (chord[1] == 'b' or chord [1] == '#'):
        tones.append(note_ids[chord[:2]])
    else:
        tones.append(note_ids[chord[0]])

    # The third (look for M and -)
    if "-" in chord:
        tones.append((tones[0] + 3) % 12)
    else:
        tones.append((tones[0] + 4) % 12)

    # The fifth (look for + and 5)
    tones.append((tones[0] + 7) % 12)

    # The seventh
    if "7" in chord:
        if chord[ chord.find("7") - 1 ] == "M":
            tones.append((tones[0] + 11) % 12)
        else:
            tones.append((tones[0] + 10) % 12)

    return tones


def generate_bebop_fluff(chord_note):
    bebop_fluff = (
        (3, 2, 1),
        (2, 2, 1)
    )

    ret = []

    for mod in random.choice(bebop_fluff):
        ret.append( (chord_note + mod) % 12 )
    ret.append(chord_note)

    return ret


if __name__ == "__main__":
    chords = ("C", "F", "C", "C", "F", "F", "C", "C", "G", "F", "C", "G")

    chord_notes = []
    all_notes = []

    for chord in chords:
        chord_notes.append(random.choice(get_chord_tones(chord)))

    # The first note won't have any approaches
    all_notes.append(chord_notes[0])

    for chord_note in chord_notes[1:]:
        all_notes.extend(generate_bebop_fluff(chord_note))

    # The last approaches go back around to the first chord
    all_notes.extend(generate_bebop_fluff(chord_notes[0]))

    with open("output.abc", "w") as f:
        abc = ABCNotator()
        f.write(abc.header())

        for note in all_notes:
            f.write(abc.note(id_note[note]))
