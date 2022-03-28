import json
import re
#farmers-protest-tweets-2021-03-5

with open('test.json') as fp:
    user = []
    for line in fp:
        x = re.findall('"user": {"username": [a-zA-Z0-9._%+\-"]*', line)[0]
        print(x)
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