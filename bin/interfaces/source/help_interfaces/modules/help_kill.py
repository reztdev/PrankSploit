#!/usr/bin/python
from src.Logging.Author import Info_Author_Payloads


def showHelpMessage():
    text = """
Show Help
=========

    Commands               Descriptions
    --------               ------------
    back                   return back to the main
    set OUTPUT <file>      specify filename to output payload
    generate               start write and generate payload
"""
    return text


def showOptionsMessage(filename):
    text = """
Show Options
============

    Info:
    -----
    Author by: {name}:{nick}
    Version: {version}
    Descriptions: {descriptions}

    Payloads: modules/payload/kill_process (Kill Process in Device Manager)

    Values              Description                Current Settings
    ------              -----------                ----------------
    OUTPUT FILE   =>    specify filename payload   {filename}
""".format(
        name=(Info_Author_Payloads()['author']),
        nick=(Info_Author_Payloads()['codename']),
        version=(Info_Author_Payloads()['version']),
        descriptions=(Info_Author_Payloads()['descriptions']),
        filename=filename
    )
    return text
