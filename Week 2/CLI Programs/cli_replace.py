# Adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners

import re
import sys


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # printf "uiuiui cat aiaia bumbum\naiaiai" | python cli_replace.py cat dog
    pattern = sys.argv[1]
    substitution = sys.argv[2]

    for line in sys.stdin:
        sys.stdout.write(re.sub(pattern, substitution, line))