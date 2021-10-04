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

        if self._config.player is None:
            print("could not find player in config")
            sys.exit(65)


    def increase_volume(self, amount: int) -> dict:

        assert isinstance(amount, int), f"amount is not a int: {type(amount)}"

        cnt = 0
        if self._config.vol_up is None:
            print("decrease volume is not avaliable")
            return { "data": 1 }
            

        while amount != cnt:
            # press the volume up key and increment the counter
            keyboard.press_and_release(self._config.vol_up)
            cnt += 1

        return { "data": 0 }


    def decrease_volume(self, amount: int) -> dict:

        assert isinstance(amount, int), f"amount is not a int: {type(amount)}"

        cnt = 0
        if self._config.vol_down is None:
            print("decrease volume is not avaliable")
            return { "data": 1 }

        while amount != cnt:
            # press the volume up key and increment the counter
            keyboard.press_and_release(self._config.vol_down)
            cnt += 1

        return { "data": 0 }

    def get_next_video(self) -> dict:
        """ Shift+N ensures the next video will play for youtube. """
        if self._config.next_ is not None:
            keyboard.press_and_release(self._config.next_)
            return { "data": 0 }
        else:
            print("next is not avaliable")
            return { "data": 1 }

    def get_previous_video(self) -> dict:
        if self._config.prev_ is not None:
            keyboard.press_and_release(self._config.prev_)
            return { "data": 0 }
        else:
            print("prev video is not avaliable")
            return { "data": 1 }

    def pause_play_video(self) -> dict:
        if self._config.play is not None:
            keyboard.press_and_release(self._config.play)
            return { "data": 0 }
        else:
            print("play_pause is not avaliable")
            return { "data": 1 }

    def fullscreen(self) -> dict:
        if self._config.fullscreen is not None:
            keyboard.press_and_release(self._config.fullscreen)
            return { "data": 0 }
        else:
            print("fullscreen is not avaliable")
            return { "data": 1 }

    def fast_forward(self) -> dict:
        if self._config.forward is not None:
            keyboard.press_and_release(self._config.forward)
            return { "data": 0 }
        else:
            print("forward is not avaliable")
            return { "data": 1 }

    def go_backward(self) -> dict:
        if self._config.backward is not None:
            keyboard.press_and_release(self._config.forward)
            return { "data": 0 }
        else:
            print("forward is not avaliable")
            return { "data": 1 }
