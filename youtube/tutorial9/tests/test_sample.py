from unittest import mock

from youtube.tutorial9.myapp.sample import guess_number


@mock.patch("youtube.tutorial9.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "You won!"
    mock_roll_dice.assert_called_once()