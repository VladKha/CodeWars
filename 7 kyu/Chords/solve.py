notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def chords(root):
    n = notes + notes
    i = n.index(root)
    return [[n[i], n[i + 4], n[i + 7]], [n[i], n[i + 3], n[i + 7]]]
