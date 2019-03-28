#!/usr/bin/python
import src.banner.color
import src.source.use

def print_process(message):
    text = "{color1}[+]{color2} {msg}".format(color1=src.banner.color.pycolor_style.B,
                                              color2=src.banner.color.pycolor_style.W, msg=message)
    print(str(text))

def print_error(message):
    try:
        text = "{color1}[!]{color2} {msg}".format(color1=src.banner.color.pycolor_style.R,
                                              color2=src.banner.color.pycolor_style.W, msg=message)
        print(str(text))
    except KeyboardInterrupt as msg:
        print(str("Error Message: {}".format(
            str(msg)
        )))

def print_warning(message):
    text = "{color1}[-]{color2} {msg}".format(color1=src.banner.color.pycolor_style.Y,
                                              color2=src.banner.color.pycolor_style.W, msg=message)
    print(str(text))

    
def slowprint(text):
    try:
        for text in text + "\n":
            src.source.use.sys.stdout.write(text)
            src.source.use.sys.stdout.flush()
            src.source.use.time.sleep(3.0 / 90)
    except KeyboardInterrupt:
        print
        print_error("User Interrupt...!! Aborted.")
        src.source.use.sys.exit(0)