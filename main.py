import argparse
import logging

from engine import *


def get_args():
    parser = argparse.ArgumentParser(description='Inverted Pendulum game')

    # Add arguments
    parser.add_argument(
            '-l', '--learning', help='do learning', required=False, action='store_true')
    parser.add_argument(
            '-a', '--ai-player', help='user ai player for game', required=False, action='store_true')
    parser.add_argument(
            '-e', '--episode-num', type=int, help='number of episodes', required=False, default=1)
    parser.add_argument(
            '-c', '--clean-learning-data', help='backup current learned data and create new one',
            required=False, action='store_true')
    parser.add_argument(
            '-s', '--show-learning-data', help='backup current learned data and create new one',
            required=False, action='store_true')
    parser.add_argument(
            '-g', '--enable-gui', help='backup current learned data and create new one',
            required=False, action='store_true', default=False)

    return parser.parse_args()


def reset_learned_data():
    backup_file_nums = [int(filename[len(config.LEARNED_DATA["backup_prefix"]):])
                        for filename in os.listdir(config.LEARNED_DATA["dir"])
                        if filename.startswith(config.LEARNED_DATA["backup_prefix"])]

    max_backup_num = max(backup_file_nums) if len(backup_file_nums) > 0 else 0
    if os.path.exists(config.LEARNED_DATA["path"]):
        os.rename(config.LEARNED_DATA["path"],
                  os.path.join(config.LEARNED_DATA["dir"],
                               config.LEARNED_DATA["backup_prefix"] + str(max_backup_num + 1)))


if __name__ == "__main__":
    # logger configuration
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    args = get_args()
    if args.clean_learning_data:
        reset_learned_data()

    if args.learning:
        engine = LeaningEngine(episodeNum=args.episode_num, enableGui=args.enable_gui)
    else:
        engine = Engine()

    if args.learning and args.show_learning_data:
        engine.show()
    else:
        engine.run()
