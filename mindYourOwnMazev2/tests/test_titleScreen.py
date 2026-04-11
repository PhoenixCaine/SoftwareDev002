import pytest
from unittest.mock import patch, MagicMock
from mindYourOwnMazeV2.titleScreen import titleScreen

# ---------------------------
# Test for title screen display
# ---------------------------

def test_titleScreen():
    with patch("os.system") as mock_sys, \
         patch("mindYourOwnMazeV2.titleScreen.Figlet") as mock_fig, \
         patch("builtins.print") as mock_print, \
         patch("builtins.input", return_value="") as mock_input:

        fig_instance = MagicMock()
        fig_instance.renderText.return_value = "ASCII"
        mock_fig.return_value = fig_instance

        titleScreen()

        mock_sys.assert_called_once()
        mock_fig.assert_called_once_with(font="ansi_shadow")
        fig_instance.renderText.assert_called_once_with("MAGIC MAZE")
        mock_input.assert_called_once()
        assert mock_print.call_count >= 2