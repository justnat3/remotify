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

from qr import init_qr_code, cleanup_tmp_qrcode
from PIL import Image
from flask import Flask, render_template
import socket
import board
import sys

#TODO: write a page-progress handler so that we can redirect to previous videos
app = Flask(__name__)

@app.route("/health")
def app_health() -> str:
    return "<h1>I am Healthy!</h1>"

@app.route("/dialog")
def app_dialog() -> str:
    return render_template("dialog.html")

@app.route("/qr")
def qr(qrcode: str) -> str:
    """ this is to ensure that we have access to original qrcode """
    return ...

@app.route("/info")
def info() -> str:
    return render_template()

@app.route("/")
def home() -> None:
    """ render the remote template, via index.html """

    return render_template("index.html")

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

    o_image = Image.open("../images/tmp_qr.png")
    o_image.show()
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
