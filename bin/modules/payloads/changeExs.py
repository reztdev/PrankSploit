#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import ChangeExtension
from src.Logging.print_stdout import print_error, print_process

class Change_Name_Extension(object):
    def __init__(self, output):
        self.File_Name = output
        self.code = ChangeExtension
        if not self.File_Name:
            print_error("Please input output name payload!")
            src.source.use.sys.exit(0)

    def writing_payload(self):
        try:
            print_process("Loaded payload Change Extension...")
            src.source.use.time.sleep(2)
            with open(self.File_Name, "w") as payload_output:
                print_process("Generating payload... please wait...")
                src.source.use.time.sleep(1)
                payload_output.write(self.code)
                payload_output.close()
            src.source.use.time.sleep(0.9)
            print_process("Successfully completed")
        except KeyboardInterrupt:
            print_error("Interrupt, Exiting...!!")
            src.source.use.sys.exit(0)
        except IOError as error:
            print_error(str(error))