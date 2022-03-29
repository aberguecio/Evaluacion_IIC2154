import re
from collections import Counter

def dias(json):
    with open(json) as fp:
        dias = []
        for line in fp:
            x = (re.findall('"created": "[0-9-]*', line)[0])[12:]
            dias.append(x)
        dias = Counter(dias).most_common(10)
    return(dias)

#print(dias("test.json"))
