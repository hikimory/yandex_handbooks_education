import numpy as np


def need_to_work_better(j):
    new_j = j.copy()
    return new_j[(new_j['maths'] == 2) | (new_j['physics'] == 2) | (new_j['computer science'] == 2)]