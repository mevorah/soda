from bs4 import BeautifulSoup
import requests
import random
from imgcat import imgcat
import urllib
import PIL
import sys
from PIL import Image

img_size = 300, 300

def get_concat_h(imgFiles):
    aggregate_width = 0
    largest_height = 0
    imgs = []
    for imgFile in imgFiles:
        img = Image.open(imgFile)
        img = img.resize(img_size)
        imgs.append(img)
        aggregate_width += img.width
        if img.height > largest_height:
            largest_height = img.height
    dst = Image.new('RGB', (aggregate_width, largest_height))
    current_index = 0
    for img in imgs:
        dst.paste(img, (current_index, 0))
        current_index += img.width
    return dst

names = sys.argv[1].split(',')
imgs = []
for name in names:
    url = "https://www.clipart.com/en/search/split?sub1=&orows=3&ocols=10&realign=&q={}&srch=Searc&cid=&date=&pubid=&rows=3".format(name)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_img_urls = map(lambda img_elt: img_elt['src'],  soup.find_all('img'))
    valid_img_urls = filter(lambda url: 'http://images' in url, all_img_urls)
    if len(valid_img_urls) > 0:
        random_int = random.randint(1, len(valid_img_urls)) - 1
        chosen_url = valid_img_urls[random_int]
        local_image_filename = urllib.urlretrieve(chosen_url)[0]
        img = open(local_image_filename)
        imgs.append(img)

if len(imgs) > 0:
    imgcat(get_concat_h(imgs))
else:
    print("No art :(")
