import numpy as np
from Engine import Engine

import random as rd


class World(object):
    def __init__(self, shape, random=True, dtype=np.int8):
        if random:
            temp = [0] * shape[0] * shape[1]
            while 1 not in temp:
                for i in range(len(temp)):
                    temp[i] = rd.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            self.data = np.array(temp)
            self.data = np.reshape(self.data, shape)
        else:
            self.data = np.zeros(shape, dtype=dtype)
        self.shape = self.data.shape
        self.dtype = dtype
        self._engine = Engine(self)

        self.step = 0

    def num_alive(self):
        return self.data.copy().flatten().tolist().count(1)

    def __str__(self):
        return self.data.__str__()

    @property
    def engine(self):
        return self._engine
