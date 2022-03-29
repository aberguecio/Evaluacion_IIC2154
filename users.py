import re
from collections import Counter

with open('farmers-protest-tweets-2021-03-5.json') as fp:
    users = []
    for line in fp:
        x = re.findall('"user": {"username": [a-zA-Z0-9._%+\-"]*', line)[0]
        users.append(x)
    users = Counter(users).most_common(10)
    print(users)