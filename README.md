# hebrew-special-numbers

## Purpose
This project is a repository of [Hebrew numeral][Hebrew numerals] respellings, designed for use in other libraries. `hebrew-special-numbers` has three goals:

* Platform-independence
* Ease-of-use
* Freedom

## Features
* Compatible with YAML 1.1 and higher.
* Includes extra additions for people who like חי and כח!
* Free and open-source under MIT.

## Background
In making programs that produce [Hebrew numerals][], most numbers follow a set pattern of combining letters in order from largest to smallest until the proper [gematria][] sum is produced.

However, many such letter combinations produce words that are customarily avoided. On one side of the spectrum, since it is forbidden to take the Divine Name in vain, combinations otherwise spelling out Divine Names, like for 15 and 16, are spelled as 9+6 or 9+7, rather than as 10+5 and 10+6. On the opposite end of the spectrum, 270 would normally spell "evil" and 278 would spell "murder." Other examples exist. The solution for such words is to reorder the letters to avoid the undesired word.

## Usage

### Setup

1. Clone the repo. On the command line:
    ```bash
    git clone https://github.com/chaimleib/hebrew-special-numbers.git
    ```

2. Use a YAML library to load `hebrew-special-numbers/styles/default.yml` into an associative array. For example, in Python (with the `pyyaml` package installed):
    ```python
    import yaml
    hsn = yaml.load(open('hebrew-special-numbers/styles/default.yml'))
    ```

3. Optional: Load in any additional styles and recursively merge them into your associative array. This may require defining a recursive `merge` function.
    ```python
    # using merge() by Andrew Cooke, http://stackoverflow.com/a/7205107
    hsn = merge(hsn, yaml.load(open('hebrew-special-numbers/styles/chaipower.yml')))
    ```

### Generating numerals
Basic sample code for values less than 1000, in Python:

```python
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
```


[Hebrew numerals]: https://en.wikipedia.org/wiki/Hebrew_numerals
[gematria]: https://en.wikipedia.org/wiki/Gematria
