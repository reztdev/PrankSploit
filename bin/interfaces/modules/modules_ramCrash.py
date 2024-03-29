#!/usr/bin/python
import src.source.use
from src.banner.color import pycolor_style
from src.Logging.print_stdout import print_error
from src.process.MainProcess import Process_Shell
from bin.modules.payloads.RAM_crash import RAM_Crashing
import bin.interfaces.MainConsole
from bin.interfaces.source.help_interfaces.modules.help_crash import (
    showHelpMessage, showOptionsMessage
)

filename = ''
class Payloads_RAM_Crashing(object):
    def __init__(self, current):
        self.current_setting = current

    def main_payload(self):
        try:
            global filename
            if self.current_setting == "help":
                print(showHelpMessage())

            elif self.current_setting == "show options":
                print(showOptionsMessage(filename))

            elif self.current_setting == "back":
                bin.interfaces.MainConsole.main_interfaces()

            elif "set OUTPUT" in self.current_setting:
                try:
                    filename = self.current_setting.split()[2]
                    print("OUTPUT => {}".format(filename))
                except IndexError:
                    print_error("Required the output name payload!!")

            elif self.current_setting == "generate":
                if filename != "":
                    ram = RAM_Crashing(filename)
                    ram.writing_payload()
                else:
                    print(showOptionsMessage(filename))

            else:
                proc = Process_Shell(self.current_setting)
                proc.main_process()

        except:
            pass

def Main_Interactive_Crashing():
    try:
        while True:
            cmd = raw_input("{ln}prsf{ln1} payloads({rd}ram_crash{rd1}) > ".format(
                ln=pycolor_style.L, ln1=pycolor_style.W, rd=pycolor_style.R, rd1=pycolor_style.W
            ))
            cd = Payloads_RAM_Crashing(cmd)
            cd.main_payload()
            if cmd == "exit":
                src.source.use.sys.exit()
    except KeyboardInterrupt:
        print_error('Interrupt by user, command "exit" to quit!!')
        Main_Interactive_Crashing()