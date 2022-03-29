import json
import re

with open('farmers-protest-tweets-2021-03-5.json') as fp:
    tweet = []
    data = []
    for line in fp:
        data.append(json.loads(line))
        x = re.findall("\d*",re.findall('retweetCount": [0-9]*', line)[0])[15]
        if (x != None):
            x = int(x)
            print(x)
            if len(tweet) < 5:
                tweet.append([x,x])
                tweet.sort(key=lambda i:i[1],reverse=True)
            elif tweet[4][1] < x:
                tweet[4] = [x,x]
                tweet.sort(key=lambda i:i[1],reverse=True)
print(tweet)