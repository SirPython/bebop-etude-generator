import random
from math import floor
import http.server
import urllib.parse

from abc_notation import ABCNotator
import bebop
import music

def generate_etude(chords):
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

    abc = ABCNotator()
    for tone in all_tones:
        abc.notate(tone)

    return abc.score

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        msrs = urllib.parse.unquote(self.path.split("=")[1]).split("|")
        leadsheet = []

        for msr in msrs:
            chords = msr.split(",")
            leadsheet.extend(chords)

            if len(chords) == 1:
                leadsheet.append(chords[0])

        self.send_response(200, generate_etude(leadsheet))
        print("sent")

        self.close_connection = True

if __name__ == "__main__":
    chords = (
        "G7","G7","C7","C7","G7","G7","D-","G7",
        "C7","C7","C7","C#-7","G7","G7","B-7","E7",
        "A-7","A-7","D7","D7","G7","E7","A-7","D7"
    )

    with open("output.abc", "w") as f:
        f.write(generate_etude(chords))

    """with http.server.HTTPServer(("", 80), RequestHandler) as httpd:
        print("hosting")
        httpd.serve_forever()"""