import re
from collections import Counter

#'farmers-protest-tweets-2021-03-5.json'
def users (json):
    with open(json) as fp:
        users = []
        for line in fp:
            x = re.findall('"user": {"username": [a-zA-Z0-9._%+\-"]*', line)[0]
            users.append(x[22:-1])
        users = Counter(users).most_common(10)
    return users

#print(users('farmers-protest-tweets-2021-03-5.json'))