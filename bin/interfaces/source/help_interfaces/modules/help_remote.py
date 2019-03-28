#!/usr/bin/python
from src.Logging.Author import Info_Author_Payloads


def showHelpMessage():
    text = """
Show Help
=========

    Commands               Descriptions
    --------               ------------
    back                   return back to the main
    set LHOST <host>       specify local ip address (ex: 192.168.0.125)
    set LPORT <port>       specify local port number 
    set OUTPUT <file>      specify filename to output payload
    generate               start write and generate payload
"""
    return text


def showOptionsMessage(ip, port, filename):
    text = """
Show Options
============

    Info:
    -----
    Author by: {name}:{nick}
    Version: {version}
    Descriptions: {descriptions}

    Payloads: modules/payload/listener_handler (Remote Listener Handler)

    Values              Description                 Current Settings
    ------              -----------                 ----------------
    LHOST         =>    specify local host address  {ip}
    LPORT         =>    specify port local number   {port}
    OUTPUT FILE   =>    specify filename payload    {filename}
""".format(
        name=(Info_Author_Payloads()['author']),
        nick=(Info_Author_Payloads()['codename']),
        version=(Info_Author_Payloads()['version']),
        descriptions=(Info_Author_Payloads()['descriptions']),
        ip=ip,
        port=port,
        filename=filename
    )
    return text
