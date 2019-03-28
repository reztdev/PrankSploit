#!/usr/bin/python
import src.Logging.Author

def showHelpMesssage():
    text = ("""
Show Help
=========

    Commands               Descriptions
    --------               ------------
    back                   return back to the main
    set LHOST              set specify LHOST/your ip address
    set LPORT              set specify LPORT/port number
    set OUTPUT             set specify filename to output payload
    generate               start write and generate to execute payload
""")
    return text

def showOptionsMessage(ip, port, files):
    opt = ("""
Show Options
============

    Info
    ----
    Author by: {names}:{nick}
    Version: {version}
    Descriptions: {description}
    
    Payloads: modules/payload/listener_handler (Remote Connect Back Shell)
    
    Values            Description                Current Settings
    ------            -----------                ----------------
    LHOST    =>       specify localhost          {ip_address}
    LPORT    =>       specify local port number  {port_number}
    OUTPUT   =>       output the payload         {output}
""".format(
        names=(src.Logging.Author.Info_Author_Payloads()['author']),
        nick=(src.Logging.Author.Info_Author_Payloads()['codename']),
        version=(src.Logging.Author.Info_Author_Payloads()['version']),
        description=(src.Logging.Author.Info_Author_Payloads()['descriptions']),
        ip_address=ip,
        port_number=port,
        output=files
    ))
    return opt