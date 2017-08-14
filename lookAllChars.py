import json
with open('/home/yan/PycharmProjects/create_dataset/src/captions_train2014.json', 'r') as f:
    captions = json.load(f)

charSet = set()
print charSet
for caption in captions['annotations']:
    for character in caption['caption']:
        charSet.add(character)
print charSet
# u'(', u',', u'@', u'\\', u'`', u'#', u"'", u'+', u'/', u';', u'?', u'[', u'_', u'\n', u'"', u'&', u'*', u'.',
# u':', u'>', u'!', u')', u'-',  u'=', u']',

charList = [str(char) for char in charSet]
print charList
removedChars = [char for  char in charList if not(char >= '0' and char <= '9' and char >= 'a' and char <= 'z' and char >= 'A' and char <= 'Z')]
print removedChars