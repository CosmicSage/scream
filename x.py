#!/usr/bin/env python3.6
from flask import Flask, jsonify, request
import requests, re, json
from bs4 import BeautifulSoup
# app = Flask(__name__)
# app.config["DEBUG"] = True
# app.config["FLASK_ENV"] = "production"
# CORS_HEADERS = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin' : '*'}
# @app.route("/")
# def welcome():
#     return "<h1>Brando</h1>"
startpage_cookie = dict(preferences="lang_homepageEEEs/default/en/N1Nresults_countEEE0N1Nlanguage_uiEEEenglishN1Ndisable_open_in_new_windowEEE0N1Nwt_unitEEEcelsiusN1NlanguageEEEenglishN1NsslEEE1N1Ndisable_family_filterEEE1N1Nnum_of_resultsEEE10N1NsuggestionsEEE1N1Ngeo_mapEEE1N1N")
startpage_headers =  {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-length": "80",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": '1',
    "origin": "https://www.startpage.com",
    "referer": "https://www.startpage.com/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": '1',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
x = input("Search:")
startpage_data = {
    "query": x,
    "cat": "web",
    "cmd": "process_search",
    "language": "english",
    "engine0": "v1all",
    "pg": '0',
    "abp": "-1"
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "Host" : "www.google.com",
    "dnt": '1',
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "document",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": '1',
    "x-client-data": "CKC1yQEIlrbJAQimtskBCMS2yQEIqZ3KAQjLrsoBCL2wygEIj7LKAQiXtcoBCO21ygEIjrrKARirpMo"
}
webResults = []

# Requests To Google
# r = requests.get(f"https://www.google.com/search?q={x}", headers=headers)
# print(r.status_code)

# Requests To startpage
r = requests.post("https://www.startpage.com/do/search", headers=startpage_headers, data=startpage_data, cookies=startpage_cookie)
print(r.status_code)
with open("./html/amber.html", 'r') as target:
    soup = BeautifulSoup(r.text, "html5lib").find(class_="w-gl--default")
    h3 = '' if soup.h3 == None else soup.h3.string
    h2 = '' if soup.h2 == None else soup.h2.string
    # URLs
    if "Web Results" in (h2, h3) : webResults.append(soup.find_all(class_='w-gl__result'))
urls = [item.a.get("href") for sublist in webResults for item in sublist]
print(urls)
# if __name__ == '__main__':
#     app.run("0.0.0.0", port=5000)
