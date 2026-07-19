# FUNKCIJE ZA MANIPULACIJU SLIKA

import numpy
from numpy.typing import NDArray


def bw_transform(frame, granica: int = 200):
    # pronaci velicinu frejma tj velicinu te numpy matrice
    # ch - channels
    w, h, ch = frame.shape
    bw_frame = numpy.zeros((w, h, ch), dtype=numpy.uint8)

    odabir = (
        (frame[:, :, 0] > granica)
        & (frame[:, :, 1] > granica)
        & (frame[:, :, 2] > granica)
    )
    bw_frame[odabir] = [255, 255, 255]
    bw_frame[~odabir] = [0, 0, 0]

    return bw_frame
