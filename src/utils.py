"""Demo functions for three type of heavy prediction tasks"""

import time
import numpy as np


def predict_io_bounded(area):
    """Emulate io delay"""
    time.sleep(1)
    avg_price = 200_000                 # RUB / m2
    return int(area * avg_price)


