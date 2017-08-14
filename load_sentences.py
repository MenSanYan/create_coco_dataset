import json
with open('sentences.json','r') as f:
    sentences = json.load(f)

length = len(sentences.keys())
print length
imgNames = sentences.keys()
for i in range(0,length,20000):
    print imgNames[i], ' :'
    for sentence in sentences[imgNames[i]]:
        print ' '.join(sentence)