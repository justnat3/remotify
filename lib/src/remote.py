#
#   NOTE: This is the main runtime file
#
#   /title    remote.py
# 
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     Main runtime for the mote
#

from qr import init_qr_code
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

@app.route("/qr")
def qr(qrcode: str) -> str:
    """ this is to ensure that we have access to original qrcode """
    return ...

@app.route("/info")
def info() -> str:
    return render_template()
    
@app.route("/home") -> None:
    """ render the remote template, via index.html """

    return render_template("../templates/index.html")

def main() -> None:
    ports = [692, 9191, 999, 992]
    port = None

    # get ip routine which is a little hacky, but should work just fine
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip_ = sock.getsockname()[0]
    sock.close()

    # ensure that we have a port 
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # see if the socket we pass in exists on the system already
        if sock.connect_ex(("localhost", port)) == 0:
            print(f"using port: {port}")
            sock.close()

    if port is None:
        sock.close()
        print("could not find port")
        sys.exit(1)

    # See --> qr.py
    init_qr_code(ip_, port)

    o_image = Image.open("tmp_qr.svg")
    o_image.show()

    # FIXME: some runtime loop here

    # See --> qr.py
    cleanup_tmp_qrcode()

if __name__ == "__main__":
    main()
