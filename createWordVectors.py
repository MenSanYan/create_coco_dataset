import json
from collections import OrderedDict

with open("vectors.txt", 'r') as f:
    a = f.read()
# 0*1001~(0+1)*1001
# 1*1001~(1+1)*1001
# 2*1001~(2+1)*1001
# ...
# 24022*1001~(24022+1)*1001
elements = a.split()
WORD_NUM = len(elements)/1001
wordVectors = {}
wordVectors['word2vec'] = OrderedDict()
wordVectors['vec'] = []
wordVectors['word2idx'] = OrderedDict()
for start in range(WORD_NUM):
    vector = [float(x) for x in elements[start * 1001 + 1: (start + 1) * 1001]]
    wordVectors['word2vec'][elements[start*1001]] = vector
    wordVectors['vec'].append(vector)
    wordVectors['word2idx'][elements[start*1001]] = start
with open("wordVectors.json", 'w') as f:
    json.dump(wordVectors, f)


