import random
from abc_notation import ABCNotator
import bebop

def boop(tone):
    return ("C","Db","D","Eb","E","F","F#","G","Ab", "A", "Bb", "B")[tone % 12]

if __name__ == "__main__":
    chords = ("C", "F", "C", "C", "F", "F", "C", "C", "G", "F", "C", "G")

    chord_tones = []
    all_tones = []

    for i, chord in enumerate(chords):
        note = random.choice(bebop.get_chord_notes(chord))


        ret = bebop.pick_octv(
            note,
            chord_tones[i-1] if i > 0 else None
        )

        print(f"input {boop(note)} ret {boop(ret)}\n")

        chord_tones.append(
            ret
        )

    all_tones.append(chord_tones[0])
    for tone in chord_tones[1:]:
        all_tones.extend(bebop.create_encl(tone))

    with open("output.abc", "w") as f:
        abc = ABCNotator()
        for tone in all_tones:
            abc.notate(tone)
        f.write(abc.score)