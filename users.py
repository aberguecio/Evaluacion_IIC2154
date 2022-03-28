import json
import re
from collections import Counter
#farmers-protest-tweets-2021-03-5

with open('farmers-protest-tweets-2021-03-5.json') as fp:
    users = []
    for line in fp:
        x = re.findall('"user": {"username": [a-zA-Z0-9._%+\-"]*', line)[0]
        users.append(x)
    users = Counter(users).most_common(10)
    print(users)

    """  if (x != None):
            x = int(x)
            print(x)
            if len(tweet) < 5:
                tweet.append([json.loads(line),x])
                tweet.sort(key=lambda i:i[1],reverse=True)
            elif tweet[4][1] < x:
                tweet[4] = [json.loads(line),x]
                tweet.sort(key=lambda i:i[1],reverse=True)
print(tweet) """