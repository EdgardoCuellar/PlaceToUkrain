import unittest
from unittest.mock import patch
import io
import sys

from exo import exo1, exo2, exo3, exo4, exo5, exo6, exo7, exo8, exo9, exo10, exo11, exo12, exo13, exo14

class TestExos(unittest.TestCase):

    @patch('builtins.input', side_effect=['170', '70'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exo1(self, mock_stdout, mock_input):
        exo1()
        self.assertEqual(mock_stdout.getvalue().strip(), "Votre IMC est de :  0.002418815331010453")

    @patch('builtins.input', side_effect=['abcdef'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exo2(self, mock_stdout, mock_input):
        exo2()
        self.assertEqual(mock_stdout.getvalue().strip(), "abc")

    @patch('builtins.input', side_effect=['abcdef'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exo3(self, mock_stdout, mock_input):
        exo3()
        self.assertEqual(mock_stdout.getvalue().strip(), "def")

    @patch('builtins.input', side_effect=['5', '10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exo4(self, mock_stdout, mock_input):
        exo4()
        self.assertEqual(mock_stdout.getvalue().strip(), "a =  10 b =  5")

    @patch('builtins.input', side_effect=['50'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exo5(self, mock_stdout, mock_input):
        exo5()
        self.assertEqual(mock_stdout.getvalue().strip(), "Pour 50 grammes de sucre, il faut 2.0 cuillères à soupe.")

    # Continue with the rest of the tests for each function

if __name__ == '__main__':
    unittest.main()
