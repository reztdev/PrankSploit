#!/usr/bin/python
import src.source.use
import src.banner.color
from src.process.MainProcess import Process_Shell
import src.Logging.print_stdout
import src.Logging.global_help
import src.Logging.Author

import bin.interfaces.source.exploit.modules_exploit
from bin.interfaces.source.payloads.modules_payload import (
    Main_Interactive_BlueScreen, Main_Interactive_Caplock, Main_Interactive_CDROM,
    Main_Interactive_ChangeName, Main_Interactive_Crashing,
    Main_Interactive_CreatedFolder, Main_Interactive_DelContents, Main_Interactive_Deleted,
    Main_Interactive_Flooder, Main_Interactive_Handler, Main_Interactive_Kill,
    Main_Interactive_Registry, Main_Interactive_Shutdown, Main_Interactive_Talking,
)
class Interactive_Console(object):
    def __init__(self, process):
        self.command_process = process

    def main_console(self):
        try:
            if "use" in self.command_process:
                try:
                    exploit = self.command_process[4:]
                    if exploit == "exploit/crack/hash":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Cracker() # hash
                    
                    elif exploit == "exploit/scanner/admin_finder":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Finder() # admin scanner

                    elif exploit == "exploit/attack/udp_flood":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Flood() # udp flood

                    elif exploit == "exploit/brute/ftp_brute":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_FTP()

                    elif exploit == "exploit/listener/handler":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_HandlerRemote()

                    elif exploit == "exploit/anonymous/linux":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Linux()

                    elif exploit == "exploit/anonymous/android":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Android()

                    elif exploit == "exploit/dumping/injection":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Injection()

                    elif exploit == "exploit/network/man_the_middle":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_MITM()

                    elif exploit == "exploit/inject/buffer_overflow":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Overflow()

                    elif exploit == "exploit/buffer/long_transport_overflow":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Long_Transporting()

                    elif exploit == "exploit/gather/nmap_scanner":
                        bin.interfaces.source.exploit.modules_exploit.Interactive_Nmap_Scanner()

                    elif exploit == "exploit/scanner/ports":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_PortScanner()

                    elif exploit == "exploit/network/sniffer":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_Sniffer()

                    elif exploit == "exploit/attack/synflood":
                        bin.interfaces.source.exploit.modules_exploit.Main_Interactive_SYN()

                    # payload modules

                    elif exploit == "modules/payload/bluesc":
                        Main_Interactive_BlueScreen()

                    elif exploit == "modules/payload/caplock":
                        Main_Interactive_Caplock()

                    elif exploit == "modules/payload/CDROM":
                        Main_Interactive_CDROM()

                    elif exploit == "modules/payload/change_name":
                        Main_Interactive_ChangeName()

                    elif exploit == "modules/payload/ram_crash":
                        Main_Interactive_Crashing()

                    elif exploit == "modules/payload/create_folder":
                        Main_Interactive_CreatedFolder()

                    elif exploit == "modules/payload/delete_all":
                        Main_Interactive_Deleted()

                    elif exploit == "modules/payload/delete_content":
                        Main_Interactive_DelContents()

                    elif exploit == "modules/payload/kill_process":
                        Main_Interactive_Kill()

                    elif exploit == "modules/payload/delete_reg":
                        Main_Interactive_Registry()

                    elif exploit == "modules/payload/listener_handler":
                        Main_Interactive_Handler()

                    elif exploit == "modules/payload/shutdown_auto":
                        Main_Interactive_Shutdown()

                    elif exploit == "modules/payload/pc_talking":
                        Main_Interactive_Talking()

                    elif exploit == "modules/payload/user_flood":
                        Main_Interactive_Flooder()

                    else:
                        src.Logging.print_stdout.print_error("Not found exploit/payloads modules!! -_-")
                except IndexError:
                    src.Logging.print_stdout.print_error("Usage: use <name expoit> or <name modules>")
                    
            elif self.command_process == "help":
                print(
                    src.Logging.global_help.showGlobalHelp()
                )

            elif self.command_process == "show exploit":
                print(
                    src.Logging.global_help.showExploit()
                )

            elif self.command_process == "show payload":
                print(
                    src.Logging.global_help.show_payload()
                )
                
            elif self.command_process == "version":
                print(
                    src.Logging.Author.show_version()
                )

            elif self.command_process == "exit":
                src.source.use.sys.exit(1)

            else:
                proc = Process_Shell(self.command_process)
                proc.main_process()

        except IOError as error:
            src.Logging.print_stdout.print_error(str(error))

def main_interfaces():
    try:
        while True:
            try:
                cmd = raw_input(
                    "{ln}prsf{ln2} > ".format(
                        ln=src.banner.color.pycolor_style.L, 
                        ln2=src.banner.color.pycolor_style.W
                    )
                )
                run = Interactive_Console(cmd)
                run.main_console()
                if cmd == "exit":
                    break
                    src.source.use.sys.exit(1)
            except KeyboardInterrupt:
                print
                src.Logging.print_stdout.print_error(
                    'Interrupt by user, command "exit" to quit!!'
                )
                main_interfaces()
    except EOFError:
        src.Logging.print_stdout.print_error(
            "Exiting by Interrupt!!"
        )
        src.source.use.sys.exit(0)