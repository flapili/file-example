# coding: utf-8
import sys
import json
import subprocess
from typing import List

import typer


def main(files: List[typer.FileBinaryRead]):
    for file in files:
        p = subprocess.run(
            ["file", "-", "--mime-type", "-b"], input=file.read(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if p.stderr:
            print(p.stderr.decode("ascii"), file=sys.stderr, flush=True)
            exit(1)

        print(json.dumps({"path": file.name, "mime-type": p.stdout.decode("ascii").strip()}), flush=True)


if __name__ == "__main__":
    typer.run(main)
