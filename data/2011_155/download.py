from parallel_sync import wget
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import re
import requests
import faster_than_requests as fr
import urllib.request

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("a", href = re.compile("\.IMG$")), "Extracting images"):
        img_url = img.attrs.get("href")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls
def extract(url):
    # get all images
    imgs = get_all_images(url)
    return imgs

def main3(imgs):
    wget.download('.',imgs)

imgs = extract("https://pdsimage2.wr.usgs.gov/archive/mess-e_v_h-mdis-2-edr-rawdata-v1.0/MSGRMDS_1001/DATA/2011_155/")

main3(imgs)
