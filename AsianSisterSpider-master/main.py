import requests
from bs4 import BeautifulSoup
import os
from fetch import Fetch
from tinydb import TinyDB, Query, where
import log

domain = "https://asiansister.com/"
video_page_start = 1
video_page_to = 10
pic_page_start = 1
pic_page_to = 1

proxies = {
    'http': '127.0.0.1:10809',
    'https': '127.0.0.1:10809'
}
proxies = None

Q = Query()
db_url = TinyDB("db.json")
table_video_url = db_url.table("video")
table_pic_url = db_url.table("pic")
fetch = Fetch(proxy=proxies)

if not os.path.exists("static/photo"):
    os.mkdir("static/photo")

if not os.path.exists("static/video"):
    os.mkdir("static/video")


def get_video_art_list():
    repeat_count = 0
    for p in range(video_page_start, video_page_to):
        log.log_info("หน้าวิดีโอ %d" % p)
        video_url = domain + "video.php?page=%d" % p
        res = requests.get(video_url, proxies=proxies)
        if res.status_code == 404:
            log.log_success("404 ดึงรายชื่อหน้าวิดีโอแล้ว")
            return
        res = res.text
        data = BeautifulSoup(res, "html.parser")
        box = data.select(".itemBox_video")
        for b in box:
            # print(b)
            page_url = b.select("a")[0].attrs['href']
            title = b.select(".titleName_video")[0].string
            title = title.replace("\n", "")
            title = title.replace("\t", "")
            prev_url = b.attrs['data']
            item = {
                "page_url": page_url,
                "title": title,
                "prev_url": prev_url,
                "flag": 0
            }
            if table_video_url.get(where('page_url') == page_url):
                log.log_info("ทำซ้ำ" + page_url)
                repeat_count += 1
                if repeat_count > 10:
                    log.log_success("จำนวนการทำซ้ำถึงบรรทัด และมีการรวบรวมข้อมูลรายการหน้าวิดีโอ")
                    return
            else:
                print(item)
                table_video_url.insert(item)
    log.log_success("การรวบรวมข้อมูลรายการหน้าวิดีโอเสร็จสมบูรณ์")


def get_pic_art_list():
    repeat_count = 0
    for p in range(pic_page_start, pic_page_to):
        log.log_info("หน้ารูปภาพ %d" % p)
        pic_url = domain + "_page%d" % p
        res = requests.get(pic_url, proxies=proxies)
        if res.status_code == 404:
            log.log_success("404 รายการหน้ารูปภาพถูกดึงออกมาแล้ว")
            return
        res = res.text
        data = BeautifulSoup(res, "html.parser")
        box = data.select(".itemBox")
        for b in box:
            page_url = b.select("a")[0].attrs['href']
            title = b.select(".titleName")[0].string
            if title is None:
                title = "no titile - " + page_url
            title = title.replace("\n", "")
            title = title.replace("\t", "")
            prev_url = b.select(".lazyload")[0].attrs['data-src']
            item = {
                "page_url": page_url,
                "title": title,
                "prev_url": prev_url,
                "flag": 0
            }
            if table_pic_url.get(where('page_url') == page_url):
                log.log_info("ทำซ้ำ" + page_url)
                repeat_count += 1
                if repeat_count > 10:
                    log.log_success("จำนวนการทำซ้ำถึงบรรทัด และรายการถูกตระเวน")
                    return
            else:
                print(item)
                table_pic_url.insert(item)
    log.log_success("เรียกรายชื่อหน้ารูปภาพแล้ว")


def get_video_meta(page_url=None, prev_url=None):
    if page_url is None:
        item = table_video_url.get(where("flag") == 0)
        if item is None:
            return None
        page_url = item['page_url']
        prev_url = domain + item['prev_url']
        print(item)

    res = requests.get(domain + page_url, proxies=proxies).text
    data = BeautifulSoup(res, "html.parser")
    video_url = data.select("source")[0].attrs['src']
    try:
        fetch.download_large_file(video_url, "static/video/" + page_url + ".mp4")
        fetch.download_large_file(prev_url, "static/video/" + page_url + ".jpg")
    except Exception as e:
        log.log_error(str(e))
        # raise e
    table_video_url.update({"flag": 1, "video_url": video_url}, where("page_url") == page_url)
    return video_url


def get_pic_meta(page_url=None):
    if page_url is None:
        item = table_pic_url.get(where("flag") == 0)
        if item is None:
            return None
        page_url = item['page_url']
        print(item)

    res = requests.get(domain + page_url, proxies=proxies).text
    data = BeautifulSoup(res, "html.parser")
    imgs = data.select(".showMiniImage")
    img_pack = []  # 图包
    for img in imgs:
        if not os.path.exists("static/photo/" + page_url):
            os.mkdir("static/photo/" + page_url)
        
        if 'data-src' in img.attrs:
            pass
        else:
            img = img.select(".showMiniImage img")
            if len(img) == 1:
                img = img[0]
            else:
                continue
        prev_url = img.attrs['data-src']
        if 'dataurl' in img.attrs:
            photo_url = img.attrs['dataurl'][5:]
        elif 'dataUrl' in img.attrs:
            photo_url = img.attrs['dataUrl'][5:]
        else:
            continue
        # 下载VIP图片
        if 'vipppimages' in photo_url:
            photo_url = prev_url.replace("_t.", ".")
            suffix = prev_url.split(".")[-1]
            photo_url = photo_url.split(".")[0] + "." + suffix
        img_pack.append({
            "photo_url": photo_url,
            "prev_url": prev_url,
            "flag": 0
        })

        try:
            fetch.download_file(domain + photo_url, "static/photo/" + page_url + "/" + photo_url.split("/")[-1])
            fetch.download_file(domain + prev_url, "static/photo/" + page_url + "/" + prev_url.split("/")[-1])
        except Exception as e:
            log.log_error(str(e))
            # raise e

    table_pic_url.update({"flag": 1, "img_pack": img_pack}, where("page_url") == page_url)
    return img_pack


def batch_get_video():
    # table_video_url.update({"flag": 0})
    while True:
        if get_video_meta() is None:
            print("finished")
            break


def batch_get_pic():
    # table_pic_url.update({"flag": 0})
    while True:
        if get_pic_meta() is None:
            print("finished")
            break



#get_video_art_list()

#get_pic_art_list()

#batch_get_pic()

batch_get_video()
