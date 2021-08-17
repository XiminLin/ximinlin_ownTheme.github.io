import glob
import json

galleries = glob.glob("source/gallery-images/*")

galleries_json = []
for gallery in galleries:
    photos = glob.glob(gallery + "/*")
    photos = [x.split("/")[-1] for x in photos]

    has_cover = glob.glob(gallery + "/cover*")
    if has_cover:
        cover = glob.glob(gallery + "/cover*")[0]
        cover = cover.split("/")[-1]
    else:
        cover = photos[0]
    

    gallery_json = {
        "name": gallery.split("/")[-1],
        "cover": cover,
        "photos": photos
    }
    galleries_json.append(gallery_json)


with open("source/_data/galleries.json", 'w') as f:
    galleries_json_str = json.dumps(galleries_json)
    f.write(galleries_json_str)

