#!/usr/bin/env python3
#
#   NOTE: This is the main runtime file
#
#   /title    remote.py
#
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     Main runtime for the mote
#

from typing import Any
from flask import Flask, render_template, request
from qr import init_qr_code, cleanup_tmp_qrcode
from config_opt import Config
from board import Board
from PIL import Image
import socket
import sys

#TODO: write a page-progress handler so that we can redirect to previous videos
app = Flask(__name__)

@app.route("/")
def home() -> str:
    """ render the remote template, via index.html """

    return render_template("index.html")


@app.route('/option', methods=['POST'])
def push_option_request() -> dict:
    """ send response back for keyboard operation """

    c = Config()
    c.init_config("Youtube")
    b = Board(c)
    json: Any = request.get_json()
    res = json['typ']

    return _parse_request(b, res)

def _parse_request(b: Board, res: str) -> dict:
    """ Parse the option request that comes and emit an event """

    if res == "forward": return b.fast_forward()
    elif res == "backward": return b.go_backward()
    elif res == "next": return b.get_next_video()
    elif res in {"play", "pause"}: return b.pause_play_video()
    elif res == "prev": return b.get_previous_video()
    elif res == "vol_up": return b.increase_volume(1)
    elif res == "vol_down": return b.decrease_volume(1)
    elif res == "fullscreen": return b.fullscreen()
    else: return { "data": 1}
        
def main() -> None:
    PORT = 6565

    # get ip routine which is a little hacky, but should work just fine
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect(("8.8.8.8", 80))
        ip_ = sock.getsockname()[0]
        sock.close()

    # See --> qr.py
    init_qr_code(ip_, PORT)

    if "--test" not in sys.argv:
        o_image = Image.open("../images/tmp_qr.png")
        o_image.show()

    app.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()
