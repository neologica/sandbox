from imp import find_module

libs = ["matplotlib", "gensim", "nltk", "spacy", "numpy", "sklearn", "scipy", "seaborn", "sqlite3", "statsmodels"]

def checkPythonmod(mod):
    try:
        op = find_module(mod)
        return True
    except ImportError:
        return False

for l in libs:
    if checkPythonmod(l):
        print "Module exists: " + l;
    else:
        print "Not installed: " + l;