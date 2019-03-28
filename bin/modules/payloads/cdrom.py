#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import CD_ROM
from src.Logging.print_stdout import print_error, print_process

class CD_ROM_Payloads(object):
    def __init__(self, outputFiles):
        self.code = CD_ROM
        self.Filename = outputFiles
        if not self.Filename:
            print_error("Please input output name payload!")
            src.source.use.sys.exit(0)

    def writing_payload(self):
        try:
            print_process("Loaded payload CD_ROM...")
            src.source.use.time.sleep(2)
            with open(self.Filename, "w") as payload_output:
                print_process("Generating payload... please wait..")
                src.source.use.time.sleep(1.6)
                payload_output.write(self.code)
                payload_output.close()
            src.source.use.time.sleep(0.9)
            print_process("Successfully completed")
        except KeyboardInterrupt:
            print_error("Interrupt, Exiting...!!")
            src.source.use.sys.exit()
        except IOError as error:
            print_error(str(error))