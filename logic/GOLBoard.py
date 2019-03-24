import time
import turtle

import numpy as np


class GOLBoard:
    def __init__(self, universe_size, seed, seed_position, n_generations=50, interval=300, CELL_SIZE=10):
        self.universe = np.zeros(universe_size)
        x_start, y_start = seed_position[0], seed_position[1]
        seed_array = np.array(seed)
        x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
        self.universe[x_start:x_end, y_start:y_end] = seed_array
        self.n_generations = n_generations
        self.interval = interval
        self.CELL_SIZE = CELL_SIZE

    def survival(self, x, y, universe):
        num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
        if universe[x, y] and not 2 <= num_neighbours <= 3:
            return 0
        elif num_neighbours == 3:
            return 1
        return universe[x, y]

    def generation(self, universe):
        new_universe = np.copy(universe)
        for i in range(universe.shape[0]):
            for j in range(universe.shape[1]):
                new_universe[i, j] = self.survival(i, j, universe)
        return new_universe

    def animate_life(self):
        for _ in range(self.n_generations):
            self.display()
            self.universe = self.generation(self.universe)
            time.sleep(self.interval/1000)
        turtle.done()

    def draw(self, x, y):
        turtle.penup()
        if self.universe[x, y] == 1:
            turtle.setpos(x * self.CELL_SIZE, y * self.CELL_SIZE)
            turtle.color('black')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(self.CELL_SIZE)
                turtle.left(90)
            turtle.end_fill()

    def display(self):
        turtle.clear()
        for i in range(self.universe.shape[0]):
            for j in range(self.universe.shape[1]):
                self.draw(i, j)
        turtle.update()
