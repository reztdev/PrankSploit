#!/usr/bin/python
import src.source.use
from bin.modules.encode.encode import BlueScreen
from src.Logging.print_stdout import print_error, print_process

class Blue_Screen_Injection(object):
    def __init__(self, output_files):
        self.code = BlueScreen
        self.filename = output_files
        if not self.filename:
            print_error("Please input output name payload!!")
            src.source.use.sys.exit(0)

    def writing_payload(self):
        try:
            print_process("Loaded payload Shutdown_Auto...")
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