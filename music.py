def get_chord_tones(chord):
    note_ids = { "C": 0, "Db": 1, "C#": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
        "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10,
        "Bb": 10, "B": 11, "Cb": 11
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

def cvt_num(num, accid="flat"):
    note = ""

    if accid == "flat":
        note = ["C","_D","D","_E","E","F","_G","G","_A","A","_B","B"][num % 12]
    else:
        note = ["C","^C","D","^D","E","F","^F","G","^G","A","^G","B"][num % 12]

    if num > 12:
        note.lower()
    elif num < 0:
        note += ","

    return note
