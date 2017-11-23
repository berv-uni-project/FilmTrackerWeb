from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.sentiment.util import mark_negation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.base import TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import re
import nltk
from sklearn.model_selection import train_test_split
from .dataProcessor import DataProcessor
import os


class TweetAnalyzer:
    def __init__(self):
        self.TWEET_ROOT = os.path.dirname(os.path.abspath(__file__)) 
        self.MODEL_ROOT = os.path.join(self.TWEET_ROOT, 'model')
        self.threshold = 0.6
     
    def predictTweets(tweets, clf):
        return clf.predict(tweets)

    def stemming_tokenizer(sentence):
        stemmer = PorterStemmer()
        sentence = word_tokenize(sentence)
        stop_words = set(stopwords.words('english'))
        newsentence = []
        for word in sentence:
            if word not in stop_words:
                if len(word) >= 3:
                    newsentence.append(word)

        newsentence = mark_negation(newsentence)
        return newsentence

    def predictProbaTweets(tweets, clf):
        if "predict_proba" in dir(clf):
            return clf.predict_proba(tweets)
        else:
            raise Exception('Error use Logistic Regression classifier')

    def labelTweets(self, tweets, proba):
        newtweetsPos = []
        countPos = 0
        newtweetsNeg = []
        countNeg = 0
        newtweetsUnknown = []
        countUnknown = 0
        for i in range(0, len(tweets)):
            newtweets = tweets[i]
            label = 0
            if proba[i][0] >= self.threshold:
                label = 1
            else:
                if proba[i][1] >= self.threshold:
                    label = 2
            if label == 0:
                newtweetsUnknown.append(newtweets)
                countUnknown += 1
            elif label == 1:
                newtweetsPos.append(newtweets)
                countPos += 1
            else:
                newtweetsNeg.append(newtweets)
                countNeg += 1

        return {
            'text': {
                'pos': newtweetsPos, 'neg': newtweetsNeg, 'unknown': newtweetsUnknown
            },
            'count': {
                'pos': countPos, 'neg': countNeg, 'unknown': countUnknown
            }
        }

    def analyzeTweet(self, id, query):
        document = self.MODEL_ROOT + 'clf-LogisticRegression-100.pkl'
        clf = joblib.load(document)

        tweets_ori = DataProcessor.requestDataFromAPI('en', query, 100)
        tweets = tweets_ori['tweet']
        for i in range(0, len(tweets)):
            tweets[i] = DataProcessor.cleanTotalTweet(tweets[i], query)

        proba = [""] * len(tweets)
        proba = predictProbaTweets(tweets, clf)

        dataTweets = labelTweets(tweets_ori['tweet'], proba)
        message = {}
        message['id'] = id
        message['query'] = query
        message['hasil'] = dataTweets

        return message

