#!/usr/bin/python
import src.banner.color

def Info_Author_Payloads():
    info = {
        'author' : 'Mochammad Rizki',
        'codename' : 'ReztDev',
        'version' : '1.0.1',
        'descriptions' : 'Payloads For Exploit and Virus Infected System Operations'
    }
    return info

def show_version():
    print("\n{cyan}\tAbout PrankSploit Toolkit{_cyan}\n\t-------------------------".format(
        cyan=src.banner.color.pycolor_style.C,
        _cyan=src.banner.color.pycolor_style.W
    ))
    print(" {yellow}+{_yellow} Created by: {name} ({red}{code}{_red})".format(
        name=Info_Author_Payloads()['author'],
        red=src.banner.color.pycolor_style.R,
        code=Info_Author_Payloads()['codename'],
        _red=src.banner.color.pycolor_style.W,
	yellow=src.banner.color.pycolor_style.Y,
	_yellow=src.banner.color.pycolor_style.W
    ))
    return (" {yellow}+{_yellow} PrankSploit Framework Version 2.1.1\n".format(yellow=src.banner.color.pycolor_style.Y, _yellow=src.banner.color.pycolor_style.W))

def version(
    author='Mochammad Rizki', 
    codename='ReztDev', 
    version='2.1.1', 
    email='ryzkialvaro07@gmail.com', visit_link='https://github.com/ReztDev/PrankSploit2'):
    _show = ("""
Author and Created by {author}
Codename Author {codename}
Version {version}
Email to Report bugs {email}
Source Code {visit_link}""".format(
        author=author,
        codename=codename,
        version=version,
        email=email,
        visit_link=visit_link
    ))
    return _show
