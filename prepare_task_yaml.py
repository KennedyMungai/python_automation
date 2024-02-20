"""Something something YAML output config"""
import sys

import argparse
import yaml


def main(number, other_number, output):
    """The main function of the script

    Args:
        number (int): Some number
        other_number (int ): Some other number
        output (txt?): A text file output
    """
    result = number * other_number
    print(f'The result is {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('-c', dest='config', type=argparse.FileType(mode='r', bufsize=-1,
                        encoding=None, errors=None), help='output file', default=sys.stdout)

    args = parser.parse_args()

    if args.config:
        config = yaml.load(args.config, Loader=yaml.FullLoader)

    # No need to transform values
    args.n1 = config['ARGUMENTS']['n1']
    args.n2 = config['ARGUMENTS']['n2']

    main(args.n1, args.n2, args.output)
