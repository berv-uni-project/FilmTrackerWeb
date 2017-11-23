import requests
import json
import preprocessor as p
import re
import csv

class DataProcessor:

    url_train = "http://twitter-crawler-data.herokuapp.com/api/traindata"
    p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.RESERVED, p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.MENTION, p.OPT.HASHTAG)

    def requestDataFromAPI(lang, query, count) :
        params = dict(lang=lang, query=query, count=count)
        req = requests.post(url_train, data=params)
        jsonData = json.loads(req.text)

        return jsonData

    def deleteDuplicate(arrayTweet):
        newArrayTweet = []
        for tweet in arrayTweet:
            if tweet not in newArrayTweet:
                newArrayTweet.append(tweet)

        return newArrayTweet

    def generateTrainData(lang, query, count) :
        file = open(lang+"_"+query+".csv", "w+")
        jsonData = requestDataFromAPI(lang, query, count)
        tweets = deleteDuplicate(jsonData['tweet'])
        for i in range(0, len(tweets)):
            tweets[i] = p.clean(tweets[i])
            print(str(i)+"-"+lang+"-"+query+" =>"+tweets[i])
            file.write(tweets[i]+"\n")
            pass

    def getTweets(lang, query, count) :
        jsonData = requestDataFromAPI(lang, query, count)
        tweets = jsonData['tweet']
        for i in range(0, len(tweets)):
            # print(tweets[i])
            tweets[i] = cleanTotalTweet(tweets[i], query)
        return tweets

    def cleanTotalTweet(tweet, query) :
        tweet = p.clean(tweet)
        tweet = tweet.lower()
        tweet = re.sub(r'[^\w\s]|[0-9]', ' ', tweet)
        tweet = re.sub(' +',' ', tweet)
        if len(tweet) >= 2:
            while tweet[0] == ' ':
                tweet = tweet[1:]
                if len(tweet) < 2 :
                    break;
        return tweet




    def main() :
        # generateTrainData("id", "#marlina", 100)
        # generateTrainData("en", "#marlina", 100)
        # generateTrainData("id", "#jigsaw", 100)
        # generateTrainData("en", "#jigsaw", 100)
        # file = open("IndoDataset.csv", "w+")
        # with open('IDpositif.csv', newline='') as csvfile:
        #     reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
        #     for row in reader:
        #         tweet = cleanTotalTweet(row[0], '#marlina')
        #         data = tweet+"\t"+str(row[1])+"\n";
        #         file.write(data)
        getTweets('en', '#nekomonogatari', 100)

