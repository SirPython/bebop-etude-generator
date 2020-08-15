import random
from abc_notation import ABCNotator
import music

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
        chord_notes.append(random.choice(music.get_chord_tones(chord)))

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
            f.write(abc.note(music.cvt_num(note)))
