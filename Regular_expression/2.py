#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import re

line = "##@&das2_321_**AFKJ#V"
searchObj = re.search('[a-zA-Z0-9]', line).span()

print searchObj
