from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag

def penn_to_wn(tag):
    """
    Convert between the PennTreebank tags to simple Wordnet tags
    """
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None


def clean_text(text):
    text = text.replace("<br />", " ")
    text = text.decode("utf-8")

    return text


def swn_polarity(text):
    """
    Return a sentiment polarity: 0 = negative, 1 = positive
    """
    sentiment = 0.0

    raw_sentences = sent_tokenize(text)
    for raw_sentence in raw_sentences:
        tagged_sentence = pos_tag(word_tokenize(raw_sentence))

        for word, tag in tagged_sentence:
            wn_tag = penn_to_wn(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue

            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                continue

            synsets = wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue

            # Take the first sense, the most common
            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())

            sentiment += swn_synset.pos_score() - swn_synset.neg_score()
            tokens_count += 1

    # judgment call ? Default to positive or negative
    if not tokens_count:
        return 0

    # sum greater than 0 => positive sentiment
    if sentiment >= 0:
        return 1

    # negative sentiment
    return 0


# Since we're shuffling, you'll get diffrent results
print swn_polarity(train_X[0]), train_y[0] # 1 1
print swn_polarity(train_X[1]), train_y[1] # 0 0
print swn_polarity(train_X[2]), train_y[2] # 0 1
print swn_polarity(train_X[3]), train_y[3] # 1 1
print swn_polarity(train_X[4]), train_y[4] # 1 1`


def main() :
    file = open("rt-polarity.pos", "w+")
    lemmatizer = WordNetLemmatizer()





if __name__ == '__main__':
   main()
