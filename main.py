import random
from abc_notation import ABCNotator
import bebop

def generate_bebop_fluff(chord_note):
    bebop_fluff = (
        (3, 2, 1),
        (2, 2, 1),
        (-3, -2, -1),
        (-2, -2, -1)
    )

    ret = []

    for mod in random.choice(bebop_fluff):
        ret.append(chord_note + mod)
    ret.append(chord_note)

    return ret


if __name__ == "__main__":
    chords = ("C", "F", "C", "C", "F", "F", "C", "C", "G", "F", "C", "G")

    chord_tones = []
    all_tones = []

    for i, chord in enumerate(chords):
        note = random.choice(bebop.get_chord_notes(chord))

        chord_tones.append(
            bebop.pick_octv(
                note,
                chord_tones[i-1] if i > 0 else None
            )
        )

    all_tones.append(chord_tones[0])
    for tone in chord_tones[1:]:
        all_tones.extend(bebop.create_encl(tone))

    with open("output.abc", "w") as f:
        abc = ABCNotator()
        for tone in all_tones:
            abc.notate(tone)
        f.write(abc.score)

    """
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
            print(note)
            f.write(abc.note(bebop.cvt_num(note)))
    """