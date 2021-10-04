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
def home() -> None:
    """ render the remote template, via index.html """

    return render_template("index.html")


@app.route('/option', methods=['POST'])
def option() -> dict:
    """ send response back for keyboard operation """

    c = Config()
    c.init_config("Youtube")

    b = Board(c)

    json = request.get_json()
    res = json['typ']
    print(res)

    if res == "forward":
        b.fast_forward()
        return { "data": 0}

    elif res == "backward":
        b.go_backward()
        return { "data": 0}
    elif res == "next":
        b.get_next_video()
        return { "data": 0}
    elif res == "play" or res == "pause":
        b.pause_play_video()
        return { "data": 0}
    elif res == "prev":
        b.get_previous_video()
        return { "data": 0}
    elif res == "vol_up":
        b.increase_volume(1)
        return { "data": 0}
    elif res == "vol_down":
        b.decrease_volume(1)
        return { "data": 0}
    elif res == "fullscreen":
        b.fullscreen()
        return { "data": 0}
    else:
        return { "data": 1}
        


def main() -> None:
    port = 6565

    # get ip routine which is a little hacky, but should work just fine
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip_ = sock.getsockname()[0]
    sock.close()

    # ensure that we have a port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # See --> qr.py
    init_qr_code(ip_, port)

    # o_image = Image.open("../images/tmp_qr.png")
    # o_image.show()

    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
