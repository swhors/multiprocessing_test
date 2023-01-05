import argparse

from app.operate.op_cnt import count_data
from app.operate.op_del import delete_data
from app.operate.op_gen import generate_data
from app.operate.op_test import test_data, test_subcmd
from app.config import current_config
from app.service import init_flask


def parse_int_arg(argument: str):
    try:
        return int(argument)
    except ValueError:
        print(f'Invalid Int Value : {argument}')
        return 0


def pass_str_arg(argument: str):
    return argument


commands = {"gen": [generate_data, ], "del": [delete_data, ], "test": [test_data, test_subcmd], "cnt": [count_data, ]}


def get_argument():
    parser = argparse.ArgumentParser(
        prog='python main',
        description='multiprocess_test')
    parser.add_argument('-c', '--cmd', action="store", dest="cmd", default="gen",
                        help="gen/test/del/cnt", type=str)
    parser.add_argument('-s', '--subcmd', action="store", dest="subcmd", default="None",
                        help="test=[simple/data]", type=str)
    parser.add_argument('-a', '--argument', action="store", dest="argument", default="None",
                        help="\n\t- gen : data count to generate\n\t- cnt : user name to find", type=str)
    return parser.parse_args()


def main():
    args = get_argument()

    init_flask(config=current_config)

    if args.cmd not in commands.keys():
        print(f"Not supported command = {args.cmd}")

    commands[args.cmd][0](commands[args.cmd][1][args.subcmd] if args.subcmd != "None" else [], args.argument)
