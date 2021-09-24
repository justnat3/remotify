from mtpyes import Error, Exit
import sys

def error() -> Error:
    sys.exit(56)

def report_error() -> Exit:
    error("")

