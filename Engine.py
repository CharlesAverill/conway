import numpy as np


class Engine(object):
    def __init__(self, world, dtype=np.int8):
        self._world = world
        self.shape = world.shape
        self.neighbor = np.zeros(world.shape, dtype=dtype)
        self._neighbor_id = self._make_neighbor_indices()

    @staticmethod
    def _make_neighbor_indices():
        # create a list of 2D indices that represents the neighbors of each
        # cell such that list[i] and list[7-i] represents the neighbor at
        # opposite directions. The neighbors are at North, NE, E, SE, S, SW,
        # W, NE directions.
        d = [slice(None), slice(1, None), slice(0, -1)]
        d2 = [
            (0, 1), (1, 1), (1, 0), (1, -1)
        ]
        out = [None for x in range(8)]
        for i, idx in enumerate(d2):
            x, y = idx
            out[i] = [d[x], d[y]]
            out[7 - i] = [d[-x], d[-y]]
        return out

    def _count_neighbors(self):
        self.neighbor[:, :] = 0  # reset neighbors
        # count #neighbors of each cell.
        w = self._world.data
        n_id = self._neighbor_id
        n = self.neighbor
        for idx in range(8):
            n[tuple(n_id[idx])] += w[tuple(n_id[7 - idx])]

    def _update_world(self):
        w = self._world.data
        n = self.neighbor

        w &= (n == 2)
        w |= (n == 3)

    def next_state(self):
        self._count_neighbors()
        self._update_world()
