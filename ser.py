
import requests
import base64,re,os,json
from contextlib import closing
from datetime import date, datetime, timedelta
from wordpress_xmlrpc import WordPressPage
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost ,EditPost
from wordpress_xmlrpc.methods.media import UploadFile
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc import Client, WordPressPost , WordPressComment
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts  ,comments
import markdown
import urllib.request
import mimetypes
import json
import datetime

now = datetime.datetime.now() #get current time

def jsonData():
    with open("./img.json", "r") as read_file:
        print("Converting JSON encoded data into Python dictionary")
        developer = json.load(read_file)
        #packDATA = []
        for key, value in developer.items():
            
            packIMG = []
            #print(key, ":", value)
            title = value["title"].replace('[','').replace(']','').replace('(','').replace(')','')
            prev_url = value["prev_url"]
            img_pack = value["img_pack"]
            for img_url in img_pack:
                packIMG.append("!(100RUEANG"+title+")["+"https://asiansister.com/"+img_url["photo_url"]+" 100เรื่อง"+title+"]") 
            datad = {
                key:[{
                    "title":title,
                    "prev_url":prev_url,
                    "pack": packIMG
                }]
            }
            
            mdcontent = './content/english/blog/asian/'+title+'.md' #add .md at the end
            with open(mdcontent, 'w') as f:
                f.write('---')
                f.write('\n')
                f.write('date: "'+now.strftime("%Y-%m-%d")+'"')
                f.write('\n')
                f.write('draft: false')
                f.write('\n')
                f.write('title: "'+title+'"')
                f.write('\n')
                f.write('subtitle: "100เรื่องพาดู'+title+' น้องเอเชีย"') #update with affiliate code later
                f.write('\n')
                f.write('excerpt: "'+title+' โดย 100เรื่อง"')
                f.write('\n')
                f.write(f'image: "'+prev_url+'"')
                f.write('\n')
                f.write('image_alt: "100เรื่อง'+title+'"')
                # f.write('\n')
                # f.write('layout: postAV') #list
                f.write('\n')
                f.write('---')
                f.write('\n')
                f.write(title +' ASIAN')
                for ii in packIMG:
                    f.write(ii)
                f.write('\n')
                f.close()
            #packDATA.append(datad)

        

        #with open('file_IMG.json', 'w') as f:
            #json.dump(packDATA, f)
        #return json.dumps(packDATA, indent=4, sort_keys=True)
        

print(jsonData())

def mainPost():
    wp_url = "https://ufatop1.net//xmlrpc.php"
    wp_username = "admin"
    wp_password = "nook@kissmepress"
    wp = Client(wp_url, wp_username, wp_password)

    # datauser
 
    
    for dpost in jsonData()[0]:


        #haeder = post_title
        print(dpost.pack)

    #print(wp)
    
    # def Images(haeder,urlIMG):
    #     tilt = re.sub(r'\W+', '', haeder)
    #     url = urlIMG
    #     image_name = str(tilt) + '.jpg'
    #     image_location = './web/static/tmp/' + image_name
    #     urllib.request.urlretrieve( url , image_location) # download the image
    #     image = image_location
    #     imageType = mimetypes.guess_type(str(image))[0]
    #     img_data = {
    #         'name': image_name,
    #         'type': imageType,  
    #     }
    #     with open(image, 'rb') as img:
    #         img_data['bits'] = xmlrpc_client.Binary(img.read())

    #     img_response = wp.call(media.UploadFile(img_data))   
    #     attachment_id = img_response['id']
    #     return attachment_id

    # ImgPPost = Images(haeder,urlIMG)  
    # html = markdown.markdown(post_content)
    # print("markdown html")
    # #post and activate new post
    
    # post = WordPressPost()
    # post.title = haeder
    # post.content = html
    # post.post_status = 'publish'
    # #image_id = resp['id']
    # post.thumbnail = ImgPPost
    # #post.Large = ImgPPost
    # #post.excerpt = post_excerpt
    # #post.terms_names = {
    # #'post_tag': [post_tag1,post_tag2],
    # #'category': ['บทความ', 'ยอดนิยม']
    # #}
    # wp.call(NewPost(post))
    # #print(wp.call(NewPost(post)))
#mainPost()