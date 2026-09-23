import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import pymorphy3

m = pymorphy3.MorphAnalyzer()
f = open('текст1.txt', encoding="utf-8")
text = f.read()
sent = sent_tokenize(text)
for s in sent:
    word = word_tokenize(s)
    for i in range(len(word)-1):
        w1 = m.parse(word[i])[0]
        w2 = m.parse(word[i+1])[0]
        if (w1.tag.POS in ("NOUN", "ADJF")
            and w2.tag.POS in ("NOUN", "ADJF")):
            if (w1.tag.number == w2.tag.number
                and w1.tag.case == w2.tag.case):
                if (w1.tag.number == "plur"):
                    print(w1.normal_form, w2.normal_form)
                elif (w1.tag.gender is not None
                      and w1.tag.gender == w2.tag.gender):
                    print(w1.normal_form, w2.normal_form)

f.close()