# hebrew-special-numbers

## Purpose
This project holds data for generating [Hebrew numerals][]. `hebrew-special-numbers` has three goals:

* Platform-independence
* Ease-of-use
* Freedom

## Features
* Compatible with YAML 1.1 and higher.
* [Gershayim][] marks (ט״ו vs טו) are optional.
* Includes style extensions for:
    * `chaipower` - Uses חי instead of יח for 18.
    * `legibility` - Spells out commonly-confused letters for clarity.
    * `fullspell` - Spells out all single-letter numerals.
    * `av`, `sag`, `mah`, `ban` - Contains letter spellings for Kabbalistic applications.
* Free and open-source under the non-restrictive MIT License.

## Background
In making programs that produce [Hebrew numerals][], most numbers follow a set pattern of combining letters in order from largest to smallest until the proper [gematria][] sum is produced. For example, 123:

* ק = 100
* כ = 20
* ג = 3

This yields קכ״ג.

To aid in such regular cases, this project includes a lookup table for generating regular numerals. See `styles/defaults.yml`, the 'numerals' and 'separators' keys.

However, many such letter combinations produce words that are customarily avoided. On one side of the spectrum, since it is forbidden to take the Divine Name in vain, combinations otherwise spelling out Divine Names, like for 15 and 16, are spelled as 9+6 (ט״ו) or 9+7 (ט״ז), rather than as 10+5 and 10+6. On the opposite end of the spectrum, 270 (ע״ר) would normally spell "evil" and 278 (רח״צ) would normally spell "murder." Other examples exist. The solution for such words is to reorder the letters to avoid the undesired word.

Since many such special exceptions exist, this project includes a list mapping the numerical values to the irregular Hebrew numeral spelling. See `styles/defaults.yml`, in the 'specials' key.

In addition, sometimes single-letter numerals are spelled out in full. For such cases, the `legibility`, `fullspell`, `av`, `sag`, `mah` and `ban` styles may be useful.

## Usage

### Setup

1. Download the [latest binary][] and expand it. On a Unix-like command line:
    ```bash
    tar -xf hebrew-special-numbers-*.tar.gz  # produces hebrew-special-numbers/
    ```

2. Use a YAML library to load `hebrew-special-numbers/styles/default.yml` into an associative array. For example, in Python (with the `pyyaml` package installed):
    ```python
    import yaml
    hsn = yaml.load(open('hebrew-special-numbers/styles/default.yml'))
    ```

3. Optional: It is possible to create styles by cascading styles on top of each other. Load in any additional styles and recursively merge them into your associative array. This may require defining a recursive `merge` function.
    ```python
    # using merge() by Andrew Cooke, http://stackoverflow.com/a/7205107
    chaipower = yaml.load(open('hebrew-special-numbers/styles/chaipower.yml'))
    hsn = merge(hsn, chaipower)
    ```

4. Optional: To clarify what order the styles were added, update the 'order' key:
    ```python
    hsn['version']['order'] = ['default', 'chaipower']
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

See also `test/test.py`.

# Change log
* 1.0.0 - first release
* 2.0.0:
    * new styles: legibility, fullspell, av, sag, mah, ban
    * more documentation
    * fix style name for chaipower
    * rename 'version.additions' to 'version.styles'
    * remove redundant 'version.release' field, put under 'version.styles'
    * add optional 'versions.order' list

[latest binary]: https://github.com/chaimleib/hebrew-special-numbers/releases/download/2.0.0/hebrew-special-numbers-2.0.0.tar.gz
[Hebrew numerals]: https://en.wikipedia.org/wiki/Hebrew_numerals
[gematria]: https://en.wikipedia.org/wiki/Gematria
[gershayim]: https://en.wikipedia.org/wiki/Gershayim
