import random

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
        tones.append((tones[0] + 3) % 11)
    else:
        tones.append((tones[0] + 4) % 11)

    # The fifth (look for + and 5)
    tones.append((tones[0] + 7) % 11)

    # The seventh
    if "7" in chord:
        if chord[ chord.find("7") - 1 ] == "M":
            tones.append((tones[0] + 11) % 11)
        else:
            tones.append((tones[0] + 10) % 11)

    for tone in tones:
        print(id_note[tone])
    print("*****")

    return tones

bebop_fluff = (
    (3, 2, 1),
    (2, 2, 1)
)

if __name__ == "__main__":
    chords = ("C", "F", "C", "C", "F", "F", "C", "C", "G", "F", "C", "G")

    chord_notes = []
    all_notes = []

    for chord in chords:
        chord_notes.append(random.choice(get_chord_tones(chord)))

    # The first note won't have any approaches
    all_notes.append(chord_notes[0])

    for chord_note in chord_notes[1:]:
        for mod in random.choice(bebop_fluff):
            all_notes.append( (chord_note + mod) % 11 )

        all_notes.append(chord_note)
