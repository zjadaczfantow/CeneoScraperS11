import requests
from bs4 import BeautifulSoup
import re
import json
# get component(opinion, selector, None, True)
# get component(opinion, selector, list=True)
def get_component(opinion, selector, attribute=None, list=False):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        return opinion.select(selector).pop(0)[attribute].strip()   
    except IndexError:
        component = None

all_opinions = []
page = 1
#product_id="91715703"
product_id=input("Enter product ID: ")
single_opinion = {
    "opinion_id": [],
    "author": ["span.user-post__author-name"],
    "recommendation": recommendation,
    "stars": stars,
    "content": content,
    "pros": pros,
    "cons": cons,
    "verfied": verfied,
    "post_date": post_date,
    "purchase_date": purchase_date,
    "usefulness": usefulness,
    "uselessness": uselessness
}
while True:
    print(page)
    respons = requests.get(f"https://www.ceneo.pl/{product_id}/opinie-{page}", allow_redirects=False)
    if respons.status_code==200:
        page_dom = BeautifulSoup(respons.text, 'html.parser')
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            opinion_id = opinion["data-entry-id"]
            author = get_component(opinion, "span.user-post__author-name")
            recommendation = get_component(opinion, "span.user-post__author-recomendation > em")

            stars = get_component(opinion, "span.user-post__score-count")
            stars = float(stars.split("/")[0].replace(",","."))

            content = opinion.select("div.user-post__text").pop(0).get_text().strip()
            content = re.sub("\\s"," ",content)
            pros = opinion.select("div.review-feature__col:has(> div[class$=\"positives\"]) > div.review-feature__item")
            pros = [item.get_text().strip() for item in pros]
            cons = opinion.select("div.review-feature__col:has(> div[class$=\"negatives\"]) > div.review-feature__item")
            cons = [item.get_text().strip() for item in cons]
            try:
                verfied = bool(opinion.select("div.review-pz").pop(0).get_text().strip())
            except IndexError:
                verfied = False
            post_date = opinion.select(
                "span.user-post__published > time:nth-child(1)").pop(0)["datetime"].strip()
            try:
                purchase_date = opinion.select(
                "span.user-post__published > time:nth-child(2)").pop(0)["datetime"].strip()
            except IndexError:
                purchase_date = None
            usefulness = int(opinion.select("span[id^='votes-yes']").pop(0).get_text().strip())
            uselessness = int(opinion.select("span[id^='votes-no']").pop(0).get_text().strip())


            all_opinions.append(single_opinion)
        page += 1
    else: break

with open(f"./opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, ensure_ascii=False, indent=4)

print(json.dumps(all_opinions, ensure_ascii=False, indent=4))