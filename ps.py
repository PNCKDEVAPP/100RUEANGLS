# -*- coding: utf-8 -*-
import json
import markdown
import re
import glob
# with open("ew.json", "r", encoding='utf-8') as read_file:
#     PSData = json.load(read_file)

# title = PSData['data']["title"]["rendered"]
# content = PSData['data']["content"]["rendered"]

# addNo = content.replace('alt=""', 'alt="'+title+'" rel="nofollow noopener"')
# tem_img = re.findall(r"(https?.+?(jpe?g|gif|png))",addNo)

# print(tem_img)D:\WEBSITE-HUGO\100RUEANG\getD\data\xn--12c1c0afratb1edf7x.com\0a7842a924fe4894ce309bb58c3cfc514c162d1e4bbbf9b59840aaec1f67225a.json
for file_name in glob.iglob('getD/data/javhubpremium.com/**/*.json', recursive=True):
  print(file_name)
  #with open('no.txt', 'w') as file:
   # file.write(file_name)

#tem_h =+ "--- \
        # title: " + title + " \
        # excerpt:" + title + " \
        # date: '2019-03-10' \
        # thumb_image: images/12_thumb.jpg \
        # image: images/12.jpg \
        # layout: post \
        # --- \
        # <h2>" + title + "</h2> \
        # "

#D:\WEBSITE-HUGO\happy-onion-seo-hugo\content\blog\100warp  "(https?.+?\.(jpe?g|gif|png))"



#html = markdown.markdown(tem_h)
#print(tem_h)
#markdown.markdownFromFile(input=html, output='./content/blog/100warp/'+title+'.html')