import json
with open("wordVectors.json", 'r') as f:
    vectors = json.load(f)

print 'vectors is a ', type(vectors)
length = len(vectors.keys())
print 'vectors has ', length, ' elements:'
print vectors.keys()

print "vectors['word2vec'] is a ", type(vectors['word2vec'])
length = len(vectors['word2vec'].keys())
print "vectors['word2vec'] has ", length, 'elements:'
for i in range(0,length, 5000):
    words=vectors['word2vec'].keys()
    print i+1, '\t', words[i], '\t', len(vectors['word2vec'][words[i]]), '\t', type(vectors['word2vec'][words[i]][0])

print length, '\t', words[length-1], '\t', len(vectors['word2vec'][words[length-1]]), '\t', type(vectors['word2vec'][words[length-1]][0])

print "vectors['word2idx'] is a ", type(vectors['word2idx'])
length = len(vectors['word2idx'].keys())
print "vectors['word2idx'] has ", length, 'elements:'
for i in range(0,length, 5000):
    words = vectors['word2idx'].keys()
    print i + 1, '\t', words[i], '\t', vectors['word2idx'][words[i]]
print length, '\t', words[length-1], '\t', vectors['word2idx'][words[length-1]]

with open("vectors.txt", 'r') as f:
    a = f.read()
elements = a.split()
WORD_NUM = len(elements)/1001

print "vectors['vec'] is a ", type(vectors['vec'])
length = len(vectors['vec'])
for i in range(0, length, 5000):
    vector = [float(x) for x in elements[i * 1001 + 1: (i + 1) * 1001]]
    print vector
    print vectors['vec'][i]
print vectors['vec'][length-1]
