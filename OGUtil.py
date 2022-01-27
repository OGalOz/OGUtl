import sys
import json
import logging
import os
from typing import List, Dict

class OGUtil:
    def __init__(self, logger=None):
        if logger is not None:
            self.l = logger
    def ex(self, inp):
        raise Exception(str(inp))
    def load_json(self, fp):
        with open(fp, 'r') as f:
            x = json.loads(f.read())
        return x
    def export_json(self, fp: str, obj, indent: int = 0,
                    dbg: bool = False) -> None:
        with open(fp, 'w') as g:
            if indent == 0:
                g.write(json.dumps(obj))
            else:
                g.write(json.dumps(obj, indent=abs(indent)))
        if dbg:
            print("Wrote out JSON object to " + fp)

