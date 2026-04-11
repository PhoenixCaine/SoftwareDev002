import pytest
from unittest.mock import patch, MagicMock
from titleScreen import titleScreen

def test_titleScreen():
    # Mock os.system so it doesn't actually clear the screen
    with patch("os.system") as mock_system, \
         patch("titleScreen.Figlet") as mock_figlet, \
         patch("builtins.print") as mock_print, \
         patch("builtins.input", return_value="") as mock_input:

        # Mock the Figlet instance and its renderText method
        mock_fig_instance = MagicMock()
        mock_fig_instance.renderText.return_value = "ASCII_TITLE"
        mock_figlet.return_value = mock_fig_instance

        # Run the function
        titleScreen()

        # Assert screen clear was called
        mock_system.assert_called_once()

        # Assert Figlet was created with the correct font
        mock_figlet.assert_called_once_with(font="ansi_shadow")

        # Assert ASCII art was rendered
        mock_fig_instance.renderText.assert_called_once_with("MAGIC MAZE")

        # Assert print was called at least twice (ASCII + subtitle)
        assert mock_print.call_count >= 2

        # Assert input was called once
        mock_input.assert_called_once()
        