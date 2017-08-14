import json
with open('/home/yanzehang/PycharmProjects/create_corpus/src/captions_train2014.json', 'r') as f:
    captions = json.load(f)

#print type(captions)
#print len(captions.keys())
print captions.keys()
#print captions['info']
#print type(captions['images'])
#print len(captions['images'])
print captions['images'][0]
#print captions['licenses']
#print type(captions['annotations'])
#print len(captions['annotations'])
print captions['annotations'][0]['caption']
print captions['annotations'][1]['caption']
print captions['annotations'][2]['caption']
print captions['annotations'][3]['caption']
print captions['annotations'][4]['caption']
i=1
to_write = ''
to_pad = []
for _ in range(20):
    to_pad.append('PAD')

for cap in captions['annotations'][:]:

    caption = cap['caption'].replace('.', '').replace(',', '').replace("'", "").replace('"', '')
    caption = caption.replace('&', 'and').replace('(', '').replace(")", "").replace('-', ' ')
    caption = " ".join(caption.split())  # replace multiple spaces
    caption = caption.lower()
    print i
    to_write += 'START ' + caption + ' END'
    to_write += ' ' + ' '.join(to_pad) + ' '
    i += 1

with open('text8', 'w') as f:
    f.write(to_write)




