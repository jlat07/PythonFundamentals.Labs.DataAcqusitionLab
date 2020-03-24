import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import file_reader


class FileReaderTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
      def test_multiple_exception_handling_reader(self):
        test_cases = [
            (
                "file_that_does_not_exist.txt",
                "No such file or directory: 'file_that_does_not_exist.txt'"
            ),
            (
                "locked_out_file.txt",
                "Permission denied: 'locked_out_file.txt'"
            )
        ]
        for file_path, message in test_cases:
            with self.subTest(f"{file_path} -> {message}"):
                with self.assertLogs() as cm:
                    file_reader.multiple_exception_handling_reader(file_path)
                    self.assertIn(message, cm.output[0])

    @patch('sys.stdout', new_callable=StringIO)
    def test_base_class_exception_handling_reader(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.base_class_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_tuple_exception_handling_reader(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.tuple_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_better_file_reader_known_exceptions(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.better_file_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    def test_better_file_reader_known_happy_path(self):
        with patch('file_reader.process_file') as cm:
            file_reader.better_file_reader("my_awesome_file.txt")
        cm.assert_called_once()
