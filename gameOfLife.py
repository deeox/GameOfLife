from load_config.load_config import load_config
from logic.GOLBoard import GOLBoard
from driver.main import main

if __name__ == "__main__":
    seed, universe_size, num_iter, seed_pos, interval, CELL_SIZE = load_config()

    board = GOLBoard(
        universe_size=(
            int(universe_size[0]),
            int(universe_size[1]),
        ),
        seed=seed,
        seed_position=(
            int(seed_pos[0]),
            int(seed_pos[1]),
        ),
        n_generations=num_iter,
        interval=interval,
        CELL_SIZE=CELL_SIZE
    )

    main(board, CELL_SIZE)

