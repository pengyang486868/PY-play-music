from core import SimplePysicWriter, NameNotes
from core import SinglePysicWriter
import numpy as np


def write_simple():
    # music = 68 + np.array([1, 1, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
    music = [NameNotes.DO, NameNotes.DO, NameNotes.SO, NameNotes.SO, NameNotes.LA, NameNotes.LA, NameNotes.SO,
             NameNotes.BLANK,
             NameNotes.FA, NameNotes.FA, NameNotes.MI, NameNotes.MI, NameNotes.RE, NameNotes.RE, NameNotes.DO,
             NameNotes.BLANK]
    writer = SimplePysicWriter()
    writer.write(music, 'star.mid')


def write():
    music = [
        # 1
        [0.5, 5, 0],
        [0.5, 6, 0],
        [0.5, 5, 0],
        [0.5, 4, 0],
        [0.5, 3, 0],
        [0.5, 2, 0],
        [1.5, 1, 0],
        [1.5, 5, -1],
        # 2
        [0.5, 1, 0],
        [0.5, 3, 0],
        [0.5, 1, 1],
        [0.5, 7, 0],
        [0.5, 6, 0],
        [0.5, 3, 0],
        [3, 5, 0],
    ]
    w = SinglePysicWriter(diff=6)
    w.write(music, 'motherland.mid')


if __name__ == '__main__':
    # write_simple()
    write()
