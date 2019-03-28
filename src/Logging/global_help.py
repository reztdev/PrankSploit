#!/usr/bin/python
def showGlobalHelp():
    text_help = ("""
Show Help
=========

    Options                  Descriptions
    -------                  ------------
    ?                        show help message
    back                     return back to the main
    banner                   display the banner of prank toolkit
    cd                       switch the another folder 
    clear                    clear the screen
    del                      delete file or folder
    delall                   delete all file in current directory
    exit                     quit of prank toolkit
    exec=[command]           interactive with command shell
    listdir                  show directory and file you
    use [exploit/payload]    using a exploit or modules payload of prank toolkit
    show exploit             show help message and menu of modules exploit
    show payload             show help message and menu of modules payload
    version                  show version pranksploit
""")
    return text_help

def showExploit():
    exploit = ("""
Exploit Modules:
================

    Names                            Rank        Descriptions
    -----                            ----        ------------
    exploit/crack/hash               normal      Cracking password hash (support for md5,sha1,sha224,sha256,sha384,sha512)
    exploit/scanner/admin_finder     normal      Scanner website to search admin login page
    exploit/attack/udp_flood         good        DDOS Flooding with packet UDP
    exploit/brute/ftp_brute          great       Brute Forcing FTP on target (default port 21)
    exploit/listener/handler         excellent   Remote Code Execution for control target
    exploit/anonymous/linux          normal      Change Mac Address your interfaces for Linux OS
    exploit/anonymous/android        normal      Change Mac Address your interfaces for Android System
    exploit/network/man_the_middle   good        Packet Sniffing with Man In The Middle Attack
    exploit/dumping/injection        good        Injection and Dumping username and password on site vulnerable
    exploit/inject/buffer_overflow   great       Injection with Buffer Overflow Attack
    exploit/gather/nmap_scanner      good        Scanning port on nmap
    exploit/scanner/ports            normal      Scanning Port on target
    exploit/network/sniffer          goood       Simple Packet Sniffing on Local Area Network
    exploit/attack/synflood          good        Flooding packet SYN Attack
""")
    return exploit

def show_payload():
    payload = ("""
Payload Modules:
================

    Names                             Rank         Descriptions
    -----                             ----         ------------
    modules/payload/bluesc            great        payload crashing BSOD on monitor
    modules/payload/caplock           good         Error button <Caplock> keyboard
    modules/payload/CDROM             good         Error device CD-ROM (is funny :D)
    modules/payload/change_name       normal       Replace extension filename
    modules/payload/ram_crash         great        Crashing Random Access Memory
    modules/payload/create_folder     normal       Flooding to make a folder with random names
    modules/payload/delete_all        great        Delete All file on locate disk (example: D:\)
    modules/payload/delete_content    good         Delete All content (images, audio, video, etc)
    modules/payload/kill_process      good         Killing process program on running background jobs
    modules/payload/delete_reg        excellent    Delete Registry files
    modules/payload/listener_handler  great        Remote Connect back Shell
    modules/payload/shutdown_auto     normal       Shutting down automatic
    modules/payload/pc_talking        bad          Computer talking (Jarvis :D is Funny!!)
    modules/payload/user_flood        good         Flooder to make a user account
""")
    return payload