import json
import os


galleries_raw = open("source/_data/galleries_raw.txt", "r")

galleries_json = []
gallery_json = {"photos":[]}
empty = True

while True:
    line = galleries_raw.readline()
    if not line:
        break
    line = line.strip()
    if len(line) == 0:
        continue
    if line.startswith("http"):
        gallery_json['photos'].append(line)
        empty = False
    elif line.startswith("date"):
        gallery_json['date'] = line.replace("date:","").strip()
    else:
        if empty:
            gallery_json['name'] = line
        else:
            gallery_json['cover'] = gallery_json['photos'][0]
            galleries_json.append(gallery_json)
            gallery_json = {"name": line, "cover": "", "photos":[]}
            empty = True

if not empty:
    gallery_json['cover'] = gallery_json['photos'][0]
    galleries_json.append(gallery_json)

galleries_raw.close()


for gallery_json in galleries_json:
    gallery_name = gallery_json['name']
    gallery_pathname = gallery_name.replace(" ", "_")
    gallery_dir = "source/galleries/" + gallery_pathname
    os.makedirs(gallery_dir, exist_ok=True)
    with open(gallery_dir + "/index.md", 'w') as f:
        f.write("""---
title: %s
layout: "gallery"
---
""" % gallery_json['name'])


with open("source/_data/galleries.json", 'w') as f:
    galleries_json_str = json.dumps(galleries_json, ensure_ascii=False)
    f.write(galleries_json_str)



# galleries_json = []
# for gallery in galleries:
#     photos = glob.glob(gallery + "/*")
#     photos = [x.split("/")[-1] for x in photos]

#     has_cover = glob.glob(gallery + "/cover*")
#     if has_cover:
#         cover = glob.glob(gallery + "/cover*")[0]
#         cover = cover.split("/")[-1]
#     else:
#         cover = photos[0]
    

#     gallery_json = {
#         "name": gallery.split("/")[-1],
#         "cover": cover,
#         "photos": photos
#     }
#     galleries_json.append(gallery_json)


# with open("source/_data/galleries.json", 'w') as f:
#     galleries_json_str = json.dumps(galleries_json)
#     f.write(galleries_json_str)

