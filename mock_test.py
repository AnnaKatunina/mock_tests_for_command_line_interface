from command_line_interface import cli, count_uniq_symbols
import unittest
from unittest import mock
import argparse


class ParserTest(unittest.TestCase):

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(file=['aaabbbc'], string=None))
    def test_parsing_file(self, mock_args):
        result = cli()
        self.assertEqual(result, [1])

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(file=['aaaafrttyuu', 'abbbc', 'dftdftop'], string=None))
    def test_parsing_file_3_lines(self, mock_args):
        result = cli()
        self.assertEqual(result, [3, 2, 2])

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(string='abc', file=None))
    def test_parsing_string(self, mock_args):
        result = cli()
        self.assertEqual(result, [3])

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(file=['abc'], string='a'))
    def test_parsing_file_and_string(self, mock_args):
        result = cli()
        self.assertEqual(result, [3, 1])

    def test_count_uniq_symbols(self):
        parameters = argparse.Namespace(file=['abc'], string='a')
        result = count_uniq_symbols(parameters=parameters)
        self.assertEqual(result, [3, 1])


if __name__ == '__main__':
    unittest.main()
