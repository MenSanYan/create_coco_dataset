import json
import numpy as np

def getMaxLength(sentences):
    maxLength = 0
    for sentenceTuple in sentences.iteritems():
        for sentence in sentenceTuple[1]:
            if len(sentence) > maxLength:
                maxLength = len(sentence)
    return maxLength

#def create_dataset(imgVectors, sentences, wordVectors):
#    dataset = []
#    dataLength = []
#    dataName = []
#    zeroVector = getZeroVector(wordVectors)
#    maxLength = getMaxLength(sentences)
#    for imgTuple in imgVectors.iteritems():
#        example = []
#        imgName = imgTuple[0]
#        imgVector = imgTuple[1]
#        for sentence in sentences[imgName]:
#            example.append(imgVector)
#            for word in sentence:
#                example.append(wordVectors[word])
#            dataLength.append(len(example) - 1)
#            dataName.append(imgName)
#            while len(example) - 1 < maxLength:
#                example.append(zeroVector)
#            dataset.append(example)
#            example = []
#    return dataset, dataLength, dataName

def create_dataset(imgVectors, sentences, word2vec, word2idx):
    imgNames=[]
    imgFeatures=[]
    idxSentences=[]
    input_lens=[]
    wordFeatures=[]
    vocabulary=[]

    dataset = {}

    idx2word = {idx:word for word,idx in word2idx.iteritems()}
    for i in range(len(idx2word.keys())):
        wordFeatures.append(word2vec[idx2word[i]])
        vocabulary.append(idx2word[i])

    dataset['vocabulary'] = vocabulary
    dataset['wordFeatures'] = wordFeatures


    maxLength = getMaxLength(sentences)
    for imgTuple in imgVectors.iteritems():

        imgName = imgTuple[0]
        imgVector = imgTuple[1]
        for sentence in sentences[imgName]:
            imgNames.append(imgName)
            imgFeatures.append(imgVector)
            idxSentence = [word2idx[word] for word in sentence]
            input_lens.append(len(idxSentence)-1)

            while len(idxSentence) < maxLength:
                idxSentence.append(word2idx['PAD'])
            idxSentences.append(idxSentence)
    dataset['imgNames'] = imgNames
    dataset['imgFeatures'] = imgFeatures
    dataset['idxSentences'] = idxSentences
    dataset['input_lens'] = input_lens
    return dataset

with open('train_features.json', 'r') as f:
    imgVectors = json.load(f)
#imgVectors = {
#    "01.jpg" : [11,0,11,0,11],
#    "02.jpg" : [22,0,22,0,22]
#}

with open('sentences.json','r') as f:
    sentences = json.load(f)
#sentences = {
#    "01.jpg" : [
#        ['START', 'a', 'dog', 'is', 'running', 'on', 'grassland', 'END'],
#        ['START', 'a', 'child', 'is', 'playing', 'with', 'the', 'puppy','END']
#    ],

#    "02.jpg" : [
#        ['START', 'a', 'ferry', 'sails', 'across', 'the', 'lake', 'END'],
#        ['START', 'a', 'boat', 'floats', 'on', 'a', 'green', 'lake' ,'END']
#    ]

#}

with open('wordVectors.json','r') as f:
    wordVectors = json.load(f)
    word2vec = wordVectors['word2vec']
    word2idx = wordVectors["word2idx"]
#wordVectors = {
#    'START' : [11,11,11,11,11],
#    'END' : [1,1,1,1,1],
#    'a' : [0,0,0,0,1],
#    'dog' : [0,0,0,1,0],
#    'is' : [0,0,0,1,1],
#    'running' : [0,0,1,0,0],
#    'on' : [0,0,1,0,1],
#    'grassland' : [0,0,1,1,0],
#    'child' : [0,0,1,1,1],
#    'playing' : [0,1,0,0,0],
#    'with' : [0,1,0,0,1],
#    'the' : [0,1,0,1,0],
#    'puppy' : [0,1,0,1,1],
#    'ferry' : [0,1,1,0,0],
#    'sails' : [0,1,1,0,1],
#    'across' : [0,1,1,1,0],
#    'lake' : [0,1,1,1,1],
#    'boat' : [1,0,0,0,0],
#    'floats' : [1,0,0,0,1],
#    'green' : [1,0,0,1,0]
#}

print "max length is ", getMaxLength(sentences)

dataset = create_dataset(imgVectors, sentences, word2vec, word2idx)

with open('dataset', 'w') as f:
    json.dump(dataset, f)
#print type(dataset[0][0][0])
#for data, length, name in zip(dataset, dataLength, dataName):
#    print length, name
#    print np.array(data,np.float32).tolist()



#imgFeatures, sentences, input_lens, wordFeatures

