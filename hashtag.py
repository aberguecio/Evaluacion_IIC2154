import re
from collections import Counter

def hashtag (json):
    with open(json) as fp:
        h = []
        for line in fp:
            x = re.findall('#[a-zA-Z0-9_]{1,99}', line)
            h = h + x
        h = Counter(h).most_common(10)
    return(h)

#print(hashtag("test.json"))