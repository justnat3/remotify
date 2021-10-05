import sys
from shutil import which
from dataclasses import dataclass, field
from config_opt import Config
from board import Board
import webbrowser as wb

@dataclass
class Browser:
    url: str
    config: Config
    opn: bool = field(init=False)


    def __post_init__(self):
        self.opn = False
        assert isinstance(self.url, str), f"url is not a string -> {type(self.url)} {self.url}"
        

    def open_media(self) -> dict:
        """ open a piece of media from a url """ 

        # if there already a window, we will try to clean it up
        if self.opn:
            self.close_media()

        # open browser window
        wb.open(self.url)
        self.opn = True

        return { "data": 0 } 
    

    def close_media(self) -> bool:
        """ returns closed as bool(true) """

        if self.opn:
            assert self.config is not None

            b = Board(self.config)
            b.close_window()

            # we have no way of know if it was closed
            self.opn = False

        # return true if the window was closed
        return self.opn is False