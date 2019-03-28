#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import PC_Talk
from src.Logging.print_stdout import print_process, print_error

class PC_Talking(object):
    def __init__(self, output_file):
        self.code = PC_Talk
        self.filename = output_file
        if not self.filename:
            print_error("Please input output name payload!!")
            src.source.use.sys.exit(1)

    def writing_payload(self):
        try:
            print_process("Loaded payload PC_Talk...")
            src.source.use.time.sleep(2)
            with open(self.filename, "w") as output_payload:
                print_process("Generating payload... please wait...")
                src.source.use.time.sleep(1)
                output_payload.write(self.code)
                output_payload.close()
            src.source.use.time.sleep(0.9)
            print_process("Successfully completed")
        except KeyboardInterrupt:
            print_error("Interrupt user, Exiting...")
            src.source.use.sys.exit(0)
        except IOError as error:
            print_error(str(error))