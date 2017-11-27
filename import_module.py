# Testing out importing modules
#
# NOTES:
#
# importing gensim: warnings.warn("detected Windows; aliasing chunkize to chunkize_serial")
# scikit-learn is sklearn
# sqlite is sqlite3

try:
    import matplotlib
except ImportError, e:
    print "Error importing matplotlib!"

try:
    import gensim
except ImportError, e:
    print "Error importing gensim!"

try:
    import nltk
except ImportError, e:
    print "Error importing nltk!"

try:
    import spacy
except ImportError, e:
    print "Error importing spacy!"

try:
    import numpy
except ImportError, e:
    print "Error importing numpy!"


try:
    import sklearn #scikit-learn
except ImportError, e:
    print "Error importing scikit-learn!"

try:
    import scipy
except ImportError, e:
    print "Error importing scipy!"

try:
    import seaborn
except ImportError, e:
    print "Error importing seaborn!"

try:
    import sqlite3
except ImportError, e:
    print "Error importing sqlite3!"

try:
    import statsmodels
except ImportError, e:
    print "Error importing statsmodels!"

