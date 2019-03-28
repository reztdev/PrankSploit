#!/usr/bin/python
import src.source.use
from src.Logging.print_stdout import print_error
from src.banner.color import pycolor_style
from src.process.MainProcess import Process_Shell
import bin.interfaces.MainConsole
from bin.modules.encode.encode import listener
from bin.modules.payloads.Listener_Handler import Listener_Handler_Payloads
from bin.modules.payloads.Listener_Handler import payloads_generator
from bin.interfaces.source.help_interfaces.modules.help_handler import (
    showHelpMesssage, showOptionsMessage
)

lhost = ''
lport = ''
filename = ''
class Payload_Handler_Interfaces(object):
    def __init__(self, commands):
        self.values = commands

    def main_payload(self):
        global filename, lhost, lport
        try:
            if self.values == "help":
                print(showHelpMesssage())

            elif self.values == "show options":
                print(showOptionsMessage(lhost, lport, filename))

            elif self.values == "back":
                bin.interfaces.MainConsole.main_interfaces()

            elif "set LHOST" in self.values:
                try:
                    lhost = self.values.split()[2]
                    print("LHOST => {}".format(lhost))
                except IndexError:
                    print_error("Required the lhost!!")

            elif "set LPORT" in self.values:
                try:
                    lport = int(self.values.split()[2])
                    print("LPORT => {}".format(lport))
                except IndexError:
                    print_error("Required the lport!!")

            elif "set OUTPUT" in self.values:
                try:
                    filename = self.values.split()[2]
                    print("OUTPUT => {}".format(filename))
                except IndexError:
                    print_error("Required the output name payload!!")

            elif self.values == "print":
                output = listener(lhost, lport)
                payloads_generator(output)


            elif self.values == "generate":
                if filename != "" and lhost != "" and lport != "":
                    try:
                        lst = Listener_Handler_Payloads(lhost, lport, filename)
                        lst.writing_payload()
                    except IOError as ioe:
                        print_error(str(ioe))
                else:
                    print(showOptionsMessage(lhost, lport, filename))

            else:
                proc = Process_Shell(self.values)
                proc.main_process()

        except:
            pass

def Main_Interactive_Handler():
    try:
        while True:
            cmd = raw_input("{ln}prsf{ln1} payload({rd}listener_handler{rd1}) > ".format(
                ln=pycolor_style.L, ln1=pycolor_style.W, rd=pycolor_style.R, rd1=pycolor_style.W
            ))
            rat = Payload_Handler_Interfaces(cmd)
            rat.main_payload()
            if cmd == "exit":
                src.source.use.sys.exit(1)
    except KeyboardInterrupt:
        print_error('Interrupt by user, command "exit" to quit!!')
        Main_Interactive_Handler()