import random

def generate_header(key="C", meter="4/4"):
    return f"""X: 1
T: 1
C: Bebop Etude Generator
M: {meter}
K: {key}
"""

def get_chord_tones(chord):


'''
1. get next chord's tones
2. choose an approach
3. write the approach notes on beats 1+, 2, and 2+
4. write the chord tone on beat 3
'''

if __name__ == "__main__":
    # An array of only the chord tones
    chord_tones = []

    # An array of the chord tones + the approaches in between
    notes = []

    for chord in chords:
        chord_tones.append(random.choose(get_chord_tones(chord)))

    with open("output.abc", "w") as f:
        f.write(generate_header())
