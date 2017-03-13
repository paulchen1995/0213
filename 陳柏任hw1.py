from nltk.corpus import stopwords
from nltk import word_tokenize
from collections import Counter


stopwords = set(stopwords.words('english'))

import string
a = string.punctuation
for symbol in a:
    stopwords.add(symbol)
    stopwords.add("``")
    stopwords.add("'s")
    stopwords.add("--")
    stopwords.add("''")
    stopwords.add("'ve")
    stopwords.add("'re")
    stopwords.add("n't")
    stopwords.update(a)

lines = [line.strip() for line in open('building_global_community.txt')]
b =  str(lines)
b = b.lower()
b = word_tokenize(b)


b = [w for w in b if w not in stopwords]
counter = Counter(b)
counter = counter.most_common()

for word, times in counter:
    print ('{0}:{1}'.format(word,times))





