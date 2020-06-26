from core import SimplePysicWriter, NameNotes
import numpy as np


def write_simple():
    # music = 68 + np.array([1, 1, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
    music = [NameNotes.DO, NameNotes.DO, NameNotes.SO, NameNotes.SO, NameNotes.LA, NameNotes.LA, NameNotes.SO,
             NameNotes.BLANK,
             NameNotes.FA, NameNotes.FA, NameNotes.MI, NameNotes.MI, NameNotes.RE, NameNotes.RE, NameNotes.DO,
             NameNotes.BLANK]
    writer = SimplePysicWriter()
    writer.write(music, 'star.mid')


if __name__ == '__main__':
    write_simple()
