def flag(chord_tones, chords):
    flats = ("C","F","Bb","Eb","Ab","Db")

    ret = []

    # Add a "flag" to all chord tones. This will come into play when rendering
    # the notation for the tone. All notes with a flat flag will get a b, all
    # with a sharp flag will get a sharp (unless the tone requires neither).
    # This way we don't end up with instances like an A# over a C7 chord.
    for i, tone in enumerate(chord_tones):
        ret.append(
            tone + FLAT_FLAG if parse_root(chords[i]) in flats
            else   SHARP_FLAG
        )

    return ret

def parse_root(chord):
    if len(chord) > 1 and (chord[1] == 'b' or chord [1] == '#'):
        return chord[:2]
    else:
        return chord[0]

def parse_chord(chord):
    note_ids = { "C": 0, "Db": 1, "C#": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
        "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10,
        "Bb": 10, "B": 11, "Cb": 11
    }

    notes = []

    notes.append(note_ids[parse_root(chord)])

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