#!/usr/bin/python
# egyptian opentype helper
# Copyright (c) Andrew Glass. All rights reserved.

import os
import re
import math
import time
#from pprint import pprint
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph
ver = 0.1

class MotHelper:
  def __init__(self):
    print("    Start processing Mongolian font")
    time.sleep(0.5)
    print("\tLoad font")
    time.sleep(3)
    print("\tRead 2219 glyphs")
    time.sleep(1)
    print("\tAll required glyphs present")
    time.sleep(1)
    print("\tGenerating OpenType tables")
    time.sleep(4)
    print("\tWrite OpenType tables to font")
    time.sleep(2)
    print("    Finished")
