#!/usr/bin/python
import src.source.use
import src.banner.color
import src.Logging.print_stdout
import src.Logging.global_help
from src.banner.color import (
    banner, banner_italic
)

# Color
RED = src.banner.color.pycolor_style.R
WHITE = src.banner.color.pycolor_style.W
YELLOW = src.banner.color.pycolor_style.Y
GREEN = src.banner.color.pycolor_style.G
BLUE = src.banner.color.pycolor_style.B
CYAN = src.banner.color.pycolor_style.C
PURPLE = src.banner.color.pycolor_style.P

class Process_Shell(object):
    def __init__(self, values):
        self.process_cmd = values

    def main_process(self):
        try:
            if self.process_cmd == "clear" or "cls" == self.process_cmd:
                if src.source.use.os.name == "nt":
                    src.source.use.os.system("cls")
                else:
                    src.source.use.os.system("clear")

            elif self.process_cmd == "?":
                print(
                    src.Logging.global_help.showGlobalHelp()
                )

            elif self.process_cmd.startswith("cd"):
                try:
                    path_file = self.process_cmd[3:]
                    src.source.use.os.chdir(path_file)
                except IndexError:
                    src.Logging.print_stdout.print_error(
                        "Usage: cd [path]"
                    )
                except src.source.use.os.error:
                    src.Logging.print_stdout.print_error(
                        "No such file or directory!!"
                    )

            elif self.process_cmd == "listdir":
                try:
                    print(
                        "\n{C}Location{W}: {Y}{address}{W1}".format(
                            C=CYAN,
                            W=WHITE,
                            Y=YELLOW,
                            W1=WHITE,
                            address=src.source.use.os.getcwd()
                        )
                    )
                    if len(src.source.use.os.listdir(src.source.use.os.getcwd())) == 0:
                        print(
                            "\n0 Folder.\n0 Files."
                        )
                    print
                    for filename in src.source.use.os.listdir(src.source.use.os.getcwd()):
                        if src.source.use.os.path.isfile(filename):
                            print(
                                "{color1}Files{color2} => {name} | Size: {size} Bytes".format(
                                    color1=YELLOW,
                                    color2=WHITE,
                                    name=filename,
                                    size=round(
                                        src.source.use.os.path.getsize(filename)
                                    )
                                )
                            )

                        elif src.source.use.os.path.isdir(filename):
                            print(
                                "{color1}Folder{color2} => {name} | Size: {size} Bytes".format(
                                    color1=GREEN,
                                    color2=WHITE,
                                    name=filename,
                                    size=round(
                                        src.source.use.os.path.getsize(filename)
                                    )
                                )
                            )

                        else:
                            print(
                                "{color1}Unknown{color2} => {name} | Size: {size} Bytes".format(
                                    color1=RED,
                                    color2=WHITE,
                                    name=filename,
                                    size=round(
                                        src.source.use.os.path.getsize(filename)
                                    )
                                )
                            )
                    print
                except src.source.use.os.error as error_show:
                    src.Logging.print_stdout.print_error(
                        "Error Code: [{code}] Message: {message}".format(
                            code=str(error_show[0]),
                            message=error_show[1]
                        )
                    )

            elif self.process_cmd == "banner":
                style = [banner_italic, banner]
                out = src.source.use.random.choice(style)
                print(out())
                print(src.banner.color.word_banner())

            elif self.process_cmd.startswith("mkdir"):
                try:
                    name_folder = self.process_cmd[6:]
                    src.source.use.os.mkdir(name_folder)
                    src.Logging.print_stdout.print_process(
                        "Created folder => {name} success".format(
                            name=name_folder
                        )
                    )
                except IndexError:
                    src.Logging.print_stdout.print_error(
                        "Usage: mkdir [name new folder]"
                    )
                except src.source.use.os.error as error_created:
                    src.Logging.print_stdout.print_error(
                        "Error Code: [{code}] Message: {message}".format(
                            code=str(error_created[0]),
                            message=error_created[1]
                        )
                    )

            elif self.process_cmd == "delall":
                for file_target in src.source.use.os.listdir(src.source.use.os.getcwd()):
                    if src.source.use.os.path.isfile(file_target):
                        src.source.use.os.remove(file_target)
                        src.Logging.print_stdout.print_process(
                            "Deleted file => {name} success".format(
                                name=file_target
                            )
                        )
                    else:
                        src.Logging.print_stdout.print_error(
                            "Deleted folder => {name} failed (folder not support)".format(
                                name=file_target
                            )
                        )

            elif self.process_cmd.startswith('del'):
                try:
                    filename = self.process_cmd[4:]
                    if src.source.use.os.path.isfile(filename):
                        try:
                            src.source.use.os.remove(filename)
                            src.Logging.print_stdout.print_process(
                                "Deleted file => {name} success".format(
                                    name=filename
                                )
                            )
                        except src.source.use.os.error as delete_files:
                            src.Logging.print_stdout.print_error(
                                "Error Code: [{code}] Message: {message}".format(
                                    code=str(delete_files[0]),
                                    message=delete_files[1]
                                )
                            )

                    elif src.source.use.os.path.isdir(filename):
                        try:
                            src.source.use.os.rmdir(filename)
                            src.Logging.print_stdout.print_process(
                                "Deleted folder => {name} success".format(
                                    name=filename
                                )
                            )
                        except src.source.use.os.error as error_delete_folder:
                            src.Logging.print_stdout.print_error(
                                "Error Code: [{code}] Message: {message}".format(
                                    code=str(error_delete_folder[0]),
                                    message=error_delete_folder[1]
                                )
                            )

                    else:
                        src.Logging.print_stdout.print_error(
                            "Invalid filename. No such file or directory!!"
                        )

                except IndexError:
                    src.Logging.print_stdout.print_error(
                        "Usage: del [file/folder]"
                    )

            else:
                if self.process_cmd.startswith('exec'):
                    try:
                        src.source.use.os.system(self.process_cmd.split("=")[1])
                    except IndexError:
                        src.Logging.print_stdout.print_error(
                            "Usage: exec=[command]"
                        )
                else:
                    src.Logging.print_stdout.print_error(
                        "Sorry, Unknown command: {values}".format(
                            values=self.process_cmd
                        )
                    )

        except IOError as error:
            src.Logging.print_stdout.print_error(
                "Error Code: [{code}] Message: {message}".format(
                    code=str(error[0]),
                    message=error[1]
                ) 
            )
