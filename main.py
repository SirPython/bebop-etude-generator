import random
from abc_notation import ABCNotator
import bebop
import music

def boop(tone):
    return ("C","Db","D","Eb","E","F","F#","G","Ab", "A", "Bb", "B")[tone % 12]

if __name__ == "__main__":
    chords = (
        "C7","C7","F7","F7","C7","C7","C7","C7",
        "F","F","F","F","C","C","C","C",
        "G","G","F","F","C","C","G","G"
    )

    chord_tones = []
    all_tones = []

    for i, chord in enumerate(chords):
        note = random.choice(music.parse_chord(chord))

        chord_tones.append(
            bebop.pick_octv(
                note,
                chord_tones[i-1] if i > 0 else None
            )
        )

    chord_tones = music.flag(chord_tones, chords)

    all_tones.append(chord_tones[0])
    for tone in chord_tones[1:]:
        all_tones.extend(bebop.create_encl(tone))

    all_tones.extend(bebop.create_encl(chord_tones[0]))

    with open("output.abc", "w") as f:
        abc = ABCNotator()
        for tone in all_tones:
            abc.notate(tone)
        f.write(abc.score)