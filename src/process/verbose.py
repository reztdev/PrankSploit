#!/usr/bin/python
import src.source.use
import src.Logging.print_stdout
import src.banner.color
import bin.interfaces.exploit.exploit_cracking

def verbose_mode(words):
    try:
        start_time = src.source.use.time.time()
        for show_verbose in range(len(words)):
            src.source.use.sys.stdout.write(
                    "\r{gr}[+]{gr1} Scan {f} of {s}".format(
                    gr=src.banner.color.pycolor_style.B, 
                    gr1=src.banner.color.pycolor_style.W,
                    f=show_verbose, 
                    s=len(words)
                )
            )
            src.source.use.sys.stdout.flush()
        end_time = src.source.use.time.time()
        print(
                "\r{gr}[+]{gr1} Scan wordlist completed".format(
                gr=src.banner.color.pycolor_style.B, 
                gr1=src.banner.color.pycolor_style.W
            )
        )
        print(
                "{gr}[+]{gr1} Time elapsed: {times} seconds".format(
                gr=src.banner.color.pycolor_style.B, 
                gr1=src.banner.color.pycolor_style.W,
                times=round(end_time-start_time)
            )
        )
    except KeyboardInterrupt:
        print
        src.Logging.print_stdout.print_error("Canceling process...")
        src.source.use.time.sleep(1)
        src.Logging.print_stdout.print_error("Exiting...")
        bin.interfaces.exploit.exploit_cracking.Main_Interactive_Cracker()