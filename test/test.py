# The MIT License (MIT)
#
# Copyright (c) 2015 Chaim-Leib Halbert <chaim.leib.halbert@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

this_dir = os.path.dirname(os.path.realpath(__file__))
hsn = yaml.load(open(os.path.realpath('styles/default.yml')))

import yaml

def hebrew_numeral(val, gershayim=True):
    # 1. Lookup in specials
    if val in hsn['specials']:
        retval = hsn['specials'][val]
        return add_gershayim(retval) if gershayim else retval

    # 2. Generate numeral normally
    parts = []
    rest = str(val)
    while rest:
        digit = int(rest[0])
        rest = rest[1:]
        if digit == 0: continue
        power = 10 ** len(rest)
        parts.append(hsn['numerals'][power * digit])
    retval = ''.join(parts)
    # 3. Add gershayim
    return add_gershayim(retval) if gershayim else retval

def add_gershayim(s):
    if len(s) == 1:
        s += hsn['separators']['geresh']
    else:
        s = ''.join([
            s[:-1],
            hsn['separators']['gershayim'],
            s[-1:]
        ])
    return s

# Note: on some terminals, the output may appear left-to-right. Even though the
# ordering of the characters is logically correct, the terminal simply does not
# support right-to-left display, because it is not fully Unicode-compliant.
# If written to a file, such as a .txt plain-text document, or to HTML, etc.,
# the strings should display in the correct sequence, since most text editors
# and web browsers are fully Unicode-compliant and can handle RTL
# (right-to-left) text correctly.
print(hebrew_numeral(1))
print(hebrew_numeral(14))
print(hebrew_numeral(15))
print(hebrew_numeral(114))
print(hebrew_numeral(115))
