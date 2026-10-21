import gensim
import re

pat = re.compile("(.*)_NOUN")
a = "король_NOUN"
b = "мужчина_NOUN"
word2vec = gensim.models.KeyedVectors.load_word2vec_format("cbow.txt", binary=False)
nouns = [w for w in word2vec.index_to_key if pat.match(w)]
found = []

print("ok")
for c in nouns:
    if c in (a, b):
        continue
    dist = word2vec.most_similar(positive=[a, c], negative=[b], topn=10)
    words = [w for w, _ in dist]
    if a in words or b in words:
        found.append((c, words))
        print( c, " ", [pat.match(w).group(1) for w in words if pat.match(w)])
print("done")