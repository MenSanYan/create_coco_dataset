import json
with open('/home/yan/PycharmProjects/create_dataset/src/captions_train2014.json', 'r') as f:
    captions = json.load(f)

#print type(captions)
#print len(captions.keys())
#print captions.keys()
#print captions['info']
#print type(captions['images'])
imgId2imgName = {}
print len(captions['images'])
print captions['images'][0]['file_name']
print captions['images'][0]['id']
for i in range(0,len(captions['images'])):
    imgId2imgName[captions['images'][i]['id']] = captions['images'][i]['file_name']

print type(imgId2imgName.keys()[0])
#print imgId2imgName[57870] == 'COCO_train2014_000000057870.jpg'
#print captions['licenses']
#print type(captions['annotations'])
#print len(captions['annotations'])
#image_id
print captions['annotations'][0]['caption']
print captions['annotations'][1]['caption']
print captions['annotations'][2]['caption']
print captions['annotations'][3]['caption']
print captions['annotations'][4]['caption']

sentences = {}
i=1
to_write = ''

for cap in captions['annotations']:

    caption = cap['caption'].replace('.', '').replace(',', '').replace("'", "").replace('"', '')
    caption = caption.replace('&', 'and').replace('(', '').replace(")", "").replace('-', ' ')
    caption = " ".join(caption.split())  # replace multiple spaces
    caption = caption.lower()
    if i % 5000 == 0:
        print i

    caption = 'START ' + caption + ' END'
    caption = caption.split()

    imgName = imgId2imgName[cap['image_id']]
    if not sentences.has_key(imgName):
        sentences[imgName] = []
        sentences[imgName].append(caption)
    else:
        sentences[imgName].append(caption)
    i += 1

with open('imgId2imgName.json', 'w') as f:
    json.dump(imgId2imgName, f)
with open('sentences.json', 'w') as f:
    json.dump(sentences, f)
