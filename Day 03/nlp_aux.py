import math
import wikipedia
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from nltk.data import find

nltk.download('wordnet')
nltk.download('omw')
nltk.download('stopwords')
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('treebank')


def wiki_bag_of_words(page, n=5, remove_stop_words=False, print_bow=False):
    wikipedia.set_lang("it")
    page = wikipedia.page(page)
    counter = Counter()
    words = page.content.lower().split()
    counter.update(words)
    if remove_stop_words:
        for stopword in stopwords.words("italian"):
            del counter[stopword]

    if print_bow:
        for letter, count in counter.most_common(n):
            print('%s: %7d' % (letter, count))
    return counter


def bow_distance(vec1, vec2):
    a = [vec1, vec2]
    d = set()
    for row in a:
        d = d.union(row.keys())
    dist = 0
    for k in d:
        dist += (vec1[k] - vec2[k]) ** 2
    return math.sqrt(dist)


def _lang_ratios(text):
    lang_ratios = {}  # initialize a dictionary called lang_ratios
    tokens = wordpunct_tokenize(text)  # tokenize text
    words = [word.lower() for word in tokens]  # convert to lower case
    words_set = set(words)

    for language in stopwords.fileids():  # select a language from the list of available languages
        stopwords_set = set(stopwords.words(language))
        common_set = words_set.intersection(stopwords_set)
        lang_ratios[language] = len(common_set)

    return lang_ratios


def detect_language(text):
    ratios = _lang_ratios(text)
    lang = max(ratios,
               key=ratios.get)  # the key option takes a function returns the key having the largest "value" in the iterable
    return lang
