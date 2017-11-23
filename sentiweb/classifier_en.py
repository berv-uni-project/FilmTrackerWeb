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

def train(clf, X, y):
    r_state = 100
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=r_state)
    clf.fit(X_train, y_train)
    print ("Accuracy: %s" % clf.score(X_test, y_test))
    print(clf.named_steps['vectorizer'].get_feature_names())
    name = clf.get_params(False)
    joblib.dump(clf, 'model/clf-'+name['memory']+'-'+str(r_state)+'.pkl')

def stemming_tokenizer(sentence):
    stemmer = PorterStemmer()
    sentence = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    newsentence = []
    for word in sentence :
        if word not in stop_words :
            if len(word) >=3:
                newsentence.append(word)

    newsentence = mark_negation(newsentence)
    return newsentence



def createClassifier() :
    file = open("resource/rt-polarity-pos", encoding = "ISO-8859-1")
    sentences = []
    expected = []

    # for line in file:
    #     print(line)

    for line in file :
        line = line.encode('utf-8').decode('utf-8')
        line = line.strip()
        line = re.sub(r'[^\w\s]|[0-9]', ' ', line)
        line = re.sub(' +',' ', line)
        sentences.append(line)
        expected.append(1)


    file.close()

    file = open("resource/rt-polarity-neg", encoding = "ISO-8859-1")

    for line in file :
        line = line.encode('utf-8').decode('utf-8')
        line = line.strip()
        line = re.sub(r'[^\w\s]|[0-9]', ' ', line)
        line = re.sub(' +',' ', line)
        sentences.append(line)
        expected.append(0)

    file.close()

    classifier = LinearSVC()#LogisticRegression(C=1.0, solver='lbfgs', multi_class='multinomial')

    clf = Pipeline(
        [
            ('vectorizer', CountVectorizer(analyzer="word",
                                           ngram_range=(1,2),
                                           tokenizer=stemming_tokenizer,
                                           stop_words=stopwords.words('english')
                                           )),
            ('classifier', classifier)
        ],
        type(classifier).__name__
    )

    train(clf, sentences, expected)


def main() :
    createClassifier()

if __name__ == '__main__':
   main()
