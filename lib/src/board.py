#
#   /title    board.py
# 
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     instructions to control the player in the browser
#

from dataclasses import dataclass
from config_opt import Config
import keyboard
import sys

@dataclass
class Board:
    _config: Config

    def __post_init__(self):
        self._config = Config("./players.cfg")

        if self._config.player is None:
            print("could not find player in config")
            sys.exit(65)


    def increase_volume(self, amount: int) -> None:

        assert isinstance(amount, int), f"amount is not a int: {type(amount)}"

        cnt = 0
        if self._config.playis is not None:
            pass
        else:
            print("decrease volume is not avaliable")
            return

        while len(amount) != cnt:
            # press the volume up key and increment the counter
            keyboard.press_and_release(self._config.vol_up)
            cnt += 1


    def decrease_volume(self, amount: int) -> None:

        assert isinstance(amount, int), f"amount is not a int: {type(amount)}"

        cnt = 0
        if self._config.playis is not None:
            pass
        else:
            print("decrease volume is not avaliable")
            return

        while len(amount) != cnt:
            # press the volume up key and increment the counter
            keyboard.press_and_release(self._config.vol_down)
            cnt += 1

    def get_next_video(self) -> None:
        """ Shift+N ensures the next video will play for youtube. """
        if self._config.playis is not None:
            keyboard.press_and_release(self._config.next_)
        else:
            print("next is not avaliable")

    def get_previous_video(self) -> None:
        if self._config.playis is not None:
            keyboard.press_and_release(self._config.prev_)
        else:
            print("prev video is not avaliable")

    def pause_play_video(self) -> None:
        if self._config.playis is not None:
            keyboard.press_and_release(self._config.play)
        else:
            print("play_pause is not avaliable")

    def fullscreen(self) -> None:
        if self._config.fullscreen is not None:
            keyboard.press_and_release(self._config.fullscreen)
        else:
            print("fullscreen is not avaliable")

