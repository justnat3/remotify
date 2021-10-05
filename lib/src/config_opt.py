#
#   /title    config_opt.py
# 
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     configuration management for pymote
#

from dataclasses import dataclass, field
from yaml import safe_load, YAMLError 
from shutil import copyfile
from pathlib import Path
import sys
import os

class File: ...

COPY_OF_CONFIG = os.path.abspath("./players.cfg")
# WINDOWS_CONFIG_LOCATION = os.path.abspath("../../config/")
# LINUX_CONFIG_LOCATION = "/etc/remotify/"

# if sys.platform == "win32":
#     fd = WINDOWS_CONFIG_LOCATION

# elif sys.platform == "linux1" or sys.platform == "linux2":
#     fd = LINUX_CONFIG_LOCATION

# else:
#     print("Unsupported Operating system")
#     sys.exit(65)


@dataclass
class Config:
    player: str = field(init=False)
    play: str = field(init=False)
    pause: str = field(init=False)
    next_: str = field(init=False)
    prev_: str = field(init=False)
    vol_up: str = field(init=False)
    vol_down: str = field(init=False)
    fullscreen: str = field(init=False)
    forward: str = field(init=False)
    backward: str = field(init=False)

    def init_config(self, _class: str) -> None:
        """ load in the player config """
        # global fd
        # full_fd = fd+os.path.sep+"players.cfg"

        # if not os.path.exists(fd):
        #     try:
        #         # create parent config directory
        #         pth = Path(fd)
        #         pth.mkdir(parents=True, exist_ok=True)

        #         # create players.cfg at CONFIG_PATH
        #         fd = fd+os.path.sep+"players.cfg"
        #         Path(fd).touch()

        #     except Exception as err:
        #         print(err)
        #         print(f"unable to copy file: 'players.cfg'  to {fd}" )
        #         sys.exit(5)


        # assert isinstance(fd, str), f"fd is not a string: {type(fd)}"
        assert isinstance(_class, str), f"_class is not a string {type(_class)}"

        with open(COPY_OF_CONFIG, 'r') as fd_:
            # if len(fd_.read()) == 0:
                # TODO: i should just read it in the project
                # open and read the copy of our config file
                # config = open(COPY_OF_CONFIG, 'r')
                # content = config.read()
                # config.close()

                # write the config file
                # try:
                #     fd_.writelines(content)
                # except Exception as err:
                #     print(err)
                #     sys.exit(54)

            try:
                
                self._extracted_from_init_config_42(fd_, _class)
            except YAMLError:
                print("unable to load config file")
                sys.exit(65)

            except KeyError as err:
                print(f"Key->{err} in class_->{_class} does not exist")

    # TODO Rename this here and in `init_config`
    def _extracted_from_init_config_42(self, fd_, _class):
        contents = fd_.read()
        # load in the yaml file and apply the config settings
        content: dict = safe_load(contents)
        self.player = _class
        self.play = content[_class]['play']
        self.pause = content[_class]['pause']
        self.next_ = content[_class]['next']
        self.prev_ = content[_class]['prev']
        self.vol_up = content[_class]['vol_up']
        self.vol_down = content[_class]['vol_down']
        self.fullscreen = content[_class]['fullscreen']
        self.forward = content[_class]['forward']
        self.backward = content[_class]['backward']
            

