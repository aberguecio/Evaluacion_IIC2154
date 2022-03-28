import json
import re


#farmers-protest-tweets-2021-03-5

with open('test.json') as fp:
    tweet = []
    data = []
    for line in fp:
        data.append(json.loads(line))
        x = re.findall("\d*",re.findall('retweetCount": [0-9]*', line)[0])[15]
        if (x != None):
            x = int(x)
            print(x)
            if len(tweet) < 10:
                tweet.append([x,x])
                tweet.sort(key=lambda i:i[1],reverse=True)
            elif tweet[9][1] < x:
                tweet[9] = [x,x]
                tweet.sort(key=lambda i:i[1],reverse=True)
print(tweet)

"""             t=4
            while t >= 0:
                if tweet[t][1] < x:
                    t -= 1
                    if t == -1:
                        tweet[0] = [x,x]
                        print(tweet)
                else :
                    if t<4:
                        tweet[t+1] = [x,x]
                    break """


