from World import World

import pandas as pd
import numpy as np

import os
import progressbar


class Generator:

    def __init__(self, world_size=(50, 50), steps=10000):
        self.world_size = world_size
        self.steps = steps
        self.__new_world()

    def __new_world(self):
        self.world = World(self.world_size)

    @staticmethod
    def __flush(processed):
        print("\n-----\nFlushing...")

        columns = ["start", "end", "start_living", "num_living_end", "steps"]
        try:
            df = pd.read_csv("./data/games.csv", index_col=False)
        except Exception as e:
            df = pd.DataFrame(columns=columns)

        ls = [int(x[x.rindex("_") + 1:]) for x in os.listdir("./data/") if "game" in x]
        if len(ls) > 0:
            ls.sort()
            highest_game_num = ls[-1]
        else:
            highest_game_num = 0

        for i in range(len(processed)):
            game = processed[i]
            start, end, start_living, num_living_end, steps = game

            dirpath = "./data/game_" + str(i + 1 + highest_game_num) + "/"

            try:
                os.makedirs(dirpath)
            except Exception as e:
                print(e)

            np.save(dirpath + "start.npy", start)
            np.save(dirpath + "end.npy", start)

            new_row = [dirpath + "start.npy", dirpath + "end.npy", start_living, num_living_end, steps]

            row_df = pd.DataFrame({key: val for key, val in zip(columns, new_row)}, index=[0])
            df = df.append(row_df, ignore_index=True, sort=False)

        df.to_csv("./data/games.csv", index=False)

        print("Successful flush\n-----")

    def run_games(self, n):
        """
        :param n: number of games to run
        :return: list of tuples containing start condition, end condition, # of alive at start, whether any are alive
                 at the end, # of alive at end, # of steps processed
        """
        output = []

        bar = progressbar.ProgressBar(max_value=n)
        bar.start()

        for i in range(n):
            bar.update(i)

            self.__new_world()

            start = self.world.data.copy()
            start_living = self.world.num_alive()

            stp = self.steps

            for j in range(self.steps):
                self.world.engine.next_state()
                if self.world.num_alive() == 0:
                    stp = j + 1
                    break
            end = self.world.data.copy()
            num_living_end = self.world.num_alive()

            output.append((start, end, start_living, num_living_end, stp))

            if i % 25 == 0 and i >= 25:
                self.__flush(output)
                output = []
        bar.finish()

        self.__flush(output)

        return output


gen = Generator()

n_games = int(input("How many games? "))

gen.run_games(n_games)
