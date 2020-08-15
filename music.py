def get_chord_tones(chord):
    note_ids = { "A": 0, "Bb": 1, "A#": 1, "B": 2, "Cb": 2, "C": 3, "Db": 4,
        "C#": 4, "D": 5, "Eb": 6, "D#": 6, "E": 7, "F": 8, "F#": 9, "Gb": 9,
        "G": 10, "Ab": 11, "G#": 11
    }

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

def cvt_num(num):
    id_note = ["A", "_B", "B", "C", "_D", "D", "_E", "E", "F", "^F", "G",
        "_A"]

    return id_note[num]
