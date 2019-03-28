#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import cap_lock
from src.Logging.print_stdout import print_error, print_process

class Cap_lock_Payload(object):
    def __init__(self, output_files):
        self.code = cap_lock
        self.filename = output_files
        if not self.filename:
            print_error("Please input output name payload!!")
            src.source.use.sys.exit(0)

    def writing_payload(self):
        try:
            print_process("Loaded payload Caplock Error...")
            src.source.use.time.sleep(1)
            with open(self.filename, "w") as output_payload:
                print_process("Generating payload... please wait..")
                src.source.use.time.sleep(2.5)
                output_payload.write(self.code)
                output_payload.close()
            src.source.use.time.sleep(1)
            print_process("Successfully completed")
        except IOError as error:
            print_error(str(error))