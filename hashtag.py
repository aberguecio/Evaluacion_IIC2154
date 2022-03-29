import re
from collections import Counter

with open('test.json') as fp:
    h = []
    for line in fp:
        x = re.findall('#[a-zA-Z0-9_]{1,99}', line)
        h = h + x
    h = Counter(h).most_common(10)
    print(h)