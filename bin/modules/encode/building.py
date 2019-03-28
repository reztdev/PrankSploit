#!/usr/bin/python
import sys
import os

if sys.argv != 2:
    pass
else:
    files = sys.argv[1]
    process = os.system(
        "pyinstaller -F {source_file}".format(
            source_file=files
        )
    )
