#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import UserFlooder
from src.Logging.print_stdout import print_error, print_process

class User_Flooding(object):
    def __init__(self, output_file):
        self.code = UserFlooder
        self.filename = output_file
        if not self.filename:
            print_error("Please input output name payload!!")
            src.source.use.sys.exit(1)

    def writing_payload(self):
        try:
            print_process("Loaded payload UserFlooder...")
            src.source.use.time.sleep(2)
            with open(self.filename, "w") as output_payload:
                print_process("Generating payload... please wait...")
                src.source.use.time.sleep(1)
                output_payload.write(self.code)
                output_payload.close()
            src.source.use.time.sleep(0.9)
            print_process("Successfully completed")
        except KeyboardInterrupt:
            print_process("Interrupt user, Exiting...")
            src.source.use.sys.exit(0)
        except IOError as error:
            print(str(error))