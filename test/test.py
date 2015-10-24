import yaml
import os

this_dir = os.path.dirname(os.path.realpath(__file__))
hsn = yaml.load(open(os.path.realpath('styles/default.yml')))

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


print(hebrew_numeral(1))
print(hebrew_numeral(14))
print(hebrew_numeral(15))
print(hebrew_numeral(114))
print(hebrew_numeral(115))
