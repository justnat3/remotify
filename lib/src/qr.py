#
#   /title    qr.py
#
#   /author   Nathan reed<nreed@linux.com>
#
#   /desc     QRCODE generation & cleanup code
#

from dataclasses import dataclass
import qrcode
import os

def init_qr_code(ip: str, port: int) -> None:
    """ Create a qr_code containing a destination url for our remote """

    assert isinstance(ip, str), "IP: Not Typeof str"
    assert isinstance(port, int), "port: Not Typeof int"

    img = qrcode.make(f'http://{ip}:{port}')
    img.save("../images/tmp_qr.png")

def cleanup_tmp_qrcode() -> None:
    """ duh cleanup our qr image """

    os.remove("tmp_qr.png")
