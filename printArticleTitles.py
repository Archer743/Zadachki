import requests
from bs4 import BeautifulSoup

# Just testing BeautifulSoup
if __name__ == "__main__":
    url = "https://www.nytimes.com/"
    r = requests.get(url=url)
    r_html = r.text

    soup = BeautifulSoup(r_html, features="lxml")

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a: 
            print(story_heading.a.text.replace("\n", " ").strip())  # https://www.w3schools.com/python/ref_string_strip.asp
        else: 
            print(story_heading.contents[0].strip())