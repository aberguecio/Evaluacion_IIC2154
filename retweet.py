import json
import re

def retweet (jsons):
    with open(jsons) as fp:
        tweet = []
        for line in fp:
            x = re.findall("\d*",re.findall('retweetCount": [0-9]*', line)[0])[15]
            if (x != None):
                x = int(x)
                if len(tweet) < 10:
                    id = (re.findall('id": [0-9]*', line)[0])[5:]
                    tweet.append([id,x])
                    tweet.sort(key=lambda i:i[1],reverse=True)
                elif tweet[9][1] < x:
                    id = (re.findall('id": [0-9]*', line)[0])[5:]
                    tweet[9] = [id,x]
                    tweet.sort(key=lambda i:i[1],reverse=True)
    return(tweet)

#print(retweet('farmers-protest-tweets-2021-03-5.json'))