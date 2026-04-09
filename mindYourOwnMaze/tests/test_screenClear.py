import pytest
from unittest.mock import patch
from screenClear import clearScreen

def test_clearScreen_calls_correct_os_command():
    with patch("os.system") as mock_system, patch("os.name", "nt"):
        clearScreen()
        mock_system.assert_called_once_with("cls")

def test_clearScreen_calls_correct_os_command_unix():
    with patch("os.system") as mock_system, patch("os.name", "posix"):
        clearScreen()
        mock_system.assert_called_once_with("clear")