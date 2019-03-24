import json
import argparse


def load_config():
    parser = argparse.ArgumentParser(
        description="GameofLife. Defauls: 50 iterations, 'infinite' seed. Settings in config"
    )
    parser.add_argument(
        "-seed", type=str, default="infinite", help="initial seed, see config for list"
    )
    args = parser.parse_args()

    config_file = open('config.json', 'r')
    config = json.load(config_file)

    seeds = config['seed']
    seed = seeds[args.seed]
    universe_size = config['universe_size'].split(",")
    num_iter = config['num_iter']
    seed_pos = config['seed_pos'].split(",")
    interval = config['interval']
    cell_size = config['cell_size']

    return seed, universe_size, num_iter, seed_pos, interval, cell_size