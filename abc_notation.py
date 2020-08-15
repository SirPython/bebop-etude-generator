class ABCNotator():
    def __init__(self):
        self.note_cnt = 0
        self.msr_cnt = 0
        self.accids = []

    def header(self, key="C", meter="4/4"):
        return f"""X: 1
T: Bebop Etude
C: Bebop Etude Generator
M: {meter}
K: {key}
L: 1/8
"""

    def note(self, note):
        ret = ""

        # If there's an accidental
        if len(note) > 1:
            self.accids.append(note[1])

        # If there's no accidental but the note has appeared before with one
        elif note in self.accids:
            note = f"={note}"

        if self.note_cnt == 8:
            self.note_cnt = 0
            self.accids = []
            self.msr_cnt += 1

            ret += "|"
        elif self.note_cnt == 4:
            ret += " "

        if self.msr_cnt == 4:
            self.msr_cnt = 0

            ret += "\n"

        ret += note
        self.note_cnt += 1

        return ret
