#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import DeleteAll
from src.Logging.print_stdout import print_error, print_process

class Deleted_All_Payloads(object):
    def __init__(self, output_file):
        self.file_output = output_file
        self.code = DeleteAll
        if not self.file_output:
            print_error("Please input output name payload!!")
            src.source.use.sys.exit(0)

    def writing_payload(self):
        try:
            print_process("Loaded payload Delete_All ...")
            src.source.use.time.sleep(1)
            with open(self.file_output, "w") as output_payload:
                print_process("Generating payload... please wait..")
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