html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><div><p>The Dormouse's story</p></div></p>
<div><p class="story">...</p></div>
"""
def crux(html):
    # print((html))
    text_tags = [
        'a', 'p', "span", "li", "h1", "h2", "svg", "img", "form"
    ]
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(html, "html5lib").descendants
    # print([(x.name, x) for x in soup])
    # exit(0)
    champion = {"html" : 1, "paragraphs" : 0, "attrs" : 1*1}
    buffer = {}
    for element in html.descendants:
        try:
            # print(type(element))
            if element.name not in text_tags and not isinstance(element, str):
                paragraphs = len(element.find_all('p', recursive=False))
                if paragraphs != 0: print(element.name, paragraphs, champion["paragraphs"], element.attrs)
                if paragraphs > champion["paragraphs"]:
                    champion.update({'html' : element, 'paragraphs' : paragraphs, "attrs" : element.attrs})
                    print(champion["attrs"])
                # print(list(element.children))
        except Exception as e:
            print(e)
    return champion

def get_images(html):
    if html == None : return []
    images = html.find_all("img")
    if len(images) == 0 : return get_images(html.parent)
    return images
