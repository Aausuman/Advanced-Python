#
# Assignment 6
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : March 7, 2020

from nltk.corpus import gutenberg as g
from nltk.stem.porter import *

def analyze(book_name):
    # This function analyzes the 'book_name' file and prints out its characteristics using nltk package

    # Extracting characters, words and sentences respectively below
    characters = g.raw(book_name)
    words = g.words(book_name)
    sentences = g.sents(book_name)

    max_length_word = words[0]
    max_length_sentence = sentences[0]
    max_length_sentence_word_count = len(max_length_sentence)
    vocabulary = list()
    stem_families = dict()
    stemmer = PorterStemmer()

    for word in words:
        # Checking for the longest word
        if len(word) > len(max_length_word):
            max_length_word = word
        stemmed_word = stemmer.stem(word)
        # Creating a vocabulary of stemmed words and a dictionary for stem families
        if stemmed_word not in vocabulary and stemmed_word.isalpha():
            vocabulary.append(stemmed_word)
            stem_families[stemmed_word] = list()
            stem_families[stemmed_word].append(word.lower())
        elif stemmed_word in vocabulary and word.lower() not in stem_families[stemmed_word]:
            stem_families[stemmed_word].append(word.lower())

    for sentence in sentences:
        # Checking for the longest sentence
        if len(sentence) > len(max_length_sentence):
            max_length_sentence = sentence
            max_length_sentence_word_count = len(max_length_sentence)
    # Converting that largest sentence from a list of words to a cumulative string sentence
    max_length_sentence_string = " "
    max_length_sentence_string = max_length_sentence_string.join(max_length_sentence)

    max_stem_family = list(list(stem_families.items())[0])
    for key, value in stem_families.items():
        # Checking for the largest stem family
        if len(value) > len(max_stem_family[1]):
            max_stem_family[0] = key
            max_stem_family[1] = list(value)

    # Printing the characteristics as requested
    print("Analysis of '%s'" % book_name)
    print("# chars =", len(characters))
    print("# words =", len(words))
    print("# sentences =", len(sentences))
    print("Longest word = '%s'" % max_length_word)
    print("Longest sentence = '%s' (%d words)" % (max_length_sentence_string, max_length_sentence_word_count))
    print("Vocab size =", len(vocabulary))
    print("Largest stem family '%s' : {" % max_stem_family[0], end=" ")
    for i in range(len(max_stem_family[1])):
        if i != 0:
            print(",", end=" ")
        print("'%s'" % max_stem_family[1][i], end=" ")
    print("}")
