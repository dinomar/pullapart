import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def getSource(url):
    """get website page source code"""
    #add url normalization?
    res = requests.get(url)
    data = res.text
    return data.lower()

def getLinks(soup, domain):
    """get all links from source"""
    links = []
    for link in soup.find_all('a'):
        temp = link.get('href')
        if not temp:
            continue
        if temp[0] == "/":
            temp = domain + temp
        elif temp[0] != "h":
            continue

        if temp not in links:
            links.append(temp)
    return links

def getImages(soup, domain):
    """get all images in source"""
    images = []
    for img in soup.find_all('img'):
        temp = img.get('src')
        if not temp:
            continue
        if temp[0] == "/":
            temp = domain + temp

        if temp not in images:
            images.append(temp)
    return images

def getCSS(soup, domain):
    """get all css links in source"""
    csslinks = []
    for link in soup.find_all('link'):
        temp = link.get('href')
        if not temp or ".css" not in temp:
            continue
        if temp[0] == "/":
            temp = domain + temp

        if temp not in csslinks:
            csslinks.append(temp)
    return csslinks

def getScripts(soup, domain):
    """get all scripts in source"""
    scripts = []
    for script in soup.find_all('script'):
        temp = script.get('src')
        if not temp:
            continue
        if temp[0] == "/":
            temp = domain + temp

        if temp not in scripts:
            scripts.append(temp)
    return scripts


#ajaxMarkers = ["$.ajax(", "$.get(", "$.getJSON(", "$.getScript(", "$.post("]

#def getAjax(source):
#    """get ajax request from source"""
#    ajax = []
#    for marker in ajaxMarkers:
#        pos = source.find(marker)
#        if pos < 0:
#            continue
#
#        tmpSource = source[pos:]
#        pos = tmpSource.find(")")
#
#        tmp = tmpSource[:pos + 1]
#        tmp = " ".join(tmp.split())
#        ajax.append(tmp)
#    return ajax

def getInfo(url):
    """get webpage info"""

    # get url domain
    udomain = urlparse(url)
    domain = udomain.scheme + "://" + udomain.netloc

    # get page
    source = getSource(url);
    soup = BeautifulSoup(source, "html.parser")

    # get elements
    links = getLinks(soup, domain)
    images = getImages(soup, domain)
    css = getCSS(soup, domain)
    scripts = getScripts(soup, domain)

    #ajax = []
    # get main pages ajax | index.html
    #ajax = ajax + getAjax(source)

    #get ajax in all scripts
    #for script in scripts:
    #    tmplist = []
    #    scrSource = getSource(script)
    #    tmplist = getAjax(scrSource)
    #    ajax = ajax + tmplist

    #info dict
    info = {
        "links": links,
        "images": images,
        "css": css,
        "scripts": scripts
    }
    return info