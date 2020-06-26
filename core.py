import mido


class PysicWriterBase():
    def __init__(self):
        self.notes = []
        self.velocity = []

    def write(self, musicdata, path):
        pass


class SimplePysicWriter(PysicWriterBase):
    def __init__(self):
        super().__init__()

    def write(self, musicdata, path):
        length = len(musicdata)
        self.notes = musicdata
        self.velocity = [60 for i in musicdata]

        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        track.append(mido.MetaMessage('set_tempo', tempo=1500000, time=0))
        track.append(mido.MetaMessage('track_name', name='Piano 1', time=0))
        track.append(mido.Message('program_change', program=1, time=0))

        for note, vel in zip(self.notes, self.velocity):
            track.append(mido.Message('note_on', note=note, velocity=vel, time=150))
        for note, vel in zip(self.notes, self.velocity):
            track.append(mido.Message('note_off', note=note, velocity=vel, time=50))

        mid.save(path)


class SNotes:
    A = 0
    B = 2
    C = 3
    D = 5
    E = 7
    F = 8
    G = 10
    DIFF = 12


class NameNotes:
    DO = 60
    RE = 62
    MI = 64
    FA = 65
    SO = 67
    LA = 69
    TI = 71
    DIFF = 12
    BLANK = 0


def num2note(num: int, stage=0, diff=0):
    if num < 1 or num > 7:
        return NameNotes.BLANK
    base = 0
    if num == 1:
        base = NameNotes.DO
    if num == 2:
        base = NameNotes.RE
    if num == 3:
        base = NameNotes.MI
    if num == 4:
        base = NameNotes.FA
    if num == 5:
        base = NameNotes.SO
    if num == 6:
        base = NameNotes.LA
    if num == 7:
        base = NameNotes.TI
    return base + stage * NameNotes.DIFF + diff
