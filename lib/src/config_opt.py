#
#   /title    config_opt.py
# 
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     configuration management for pymote
#

from dataclasses import dataclass, field

class File: ...

@dataclass
class Config:
    player: str = field(init=False, default=None)
    play: str = field(init=False, default=None)
    pause: str = field(init=False, default=None)
    next_: str = field(init=False, default=None)
    prev_: str = field(init=False, default=None)
    vol_up: str = field(init=False, default=None)
    vol_down: str = field(init=False, default=None)
    fullscreen: str = field(init=False, default=None)

    def init_config(fd: File, _class: str) -> File:
        """ load in the player config """

        assert isinstance(fd, str), f"fd is not a string: {type(fd)}"
        assert isinstance(_class, str), f"_class is not a string {type(_class)}"

        with open(fd, 'r') as fd_:
            try:
                # load in the yaml file and apply the config settings
                content: dict = yaml.safe_load(fd_)
                self.player: str = content[_class]
                self.play = content[_class].play
                self.pause = content[_class].pause
                self.next_ = content[_class].next_
                self.prev_ = content[_class].prev_
                self.vol_up = content[_class].vol_up
                self.vol_down = content[_class].vol_down
                self.fullscreen = content[_class].fullscreen

            except yaml.YAMLError:
                print("unable to load config file")
                sys.exit(65)

