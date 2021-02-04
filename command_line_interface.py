import argparse
from argparse import Namespace
from unique_characters_app import get_unique_characters


def parse() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=argparse.FileType('r'))
    parser.add_argument("--string", type=str)
    return parser.parse_args()


def count_uniq_symbols(parameters: Namespace) -> [int]:
    number_of_uniq_symbols_list = []
    if parameters.file:
        for line in parameters.file:
            number_of_uniq_symbols_list.append(get_unique_characters(line.rstrip()))
    if parameters.string:
        number_of_uniq_symbols_list.append(get_unique_characters(parameters.string))
    return number_of_uniq_symbols_list


def cli() -> [int]:
    parsed_parameters = parse()
    result = count_uniq_symbols(parsed_parameters)
    return result


if __name__ == '__main__':
    print(cli())
