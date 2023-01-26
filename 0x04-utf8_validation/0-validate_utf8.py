#!/usr/bin/python3
""" utf validation module """


def validUTF8(data):
    """checks utf8 validation for data"""
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
