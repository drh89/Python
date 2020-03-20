import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import re


def get_webpage(url):
    """Henter URL ned som tekst"""
    r = requests.get(url)
    r.raise_for_status()
    return r.text


def find_top_five(html_txt):
    """1. Brug web scraping til at finde top 5 hold i verden"""
    soup = bs4.BeautifulSoup(html_txt, 'html.parser')
    ranking = soup.select(".leftCol aside .rank")

    teams = []
    for target in ranking:
        teams.append(target.text)
    content = "\n".join(teams)
    return content

def team_ranking(url, team):
    """returner teams rank placering og soup object til videre"""
    browser = webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(3)

    # search_field = browser.find_element_by_tag_name('input')
    search_field = browser.find_element_by_name('query')
    search_field.send_keys(team)
    search_field.submit()
    sleep(3)
    link = browser.find_element_by_link_text(team)
    link.click()
    sleep(3)
    
    page_source = browser.page_source
    save_to_file(page_source, "team.txt")
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    ranking = soup.select(".profile-team-stat")[0].text
    return ranking

def find_matches():
    """ved hjælp af regex findes alle de steder teamet der er gemt i team.txt har hhv vundet og tabt"""
    flames_file = open_file("team.txt")
    victory_pattern_obj = re.compile(r'(<div class="team-flex team-1\s">)')
    match_victories = victory_pattern_obj.findall(flames_file)
    lost_pattern_obj = re.compile(r'(<div class="team-flex team-1 lost">)')
    match_lost = lost_pattern_obj.findall(flames_file)
    result = "Vundet: " + str(len(match_victories)) + "\nTabt: " + str(len(match_lost)) + "\n"
    return result
    
def open_file(path):
    """åben fil og returner indhold som tekst"""
    with open(path) as content:
        return "".join(content.readlines())


def save_to_file(content, out_path='./webpage.txt'):
    """gemmer indhold i tekst-fil"""
    c = []
    if type(content) == list:
        for target in content:
            c.append(str(target))
        content = "\n".join(c)
    with open(out_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    """07 Exercise
    Grupper unusual ear
    hltv.org	
    1. Brug web scraping til at finde top 5 hold i verden	
    2. Brug selenium til at finde "Copenhagen Flames" placering på verdensranglisten (Ranking)
    3. Stadig på "Copenhagen Flames" siden.
       Find ved hjælp af regex hvor mange sejre de har under matches"""

    url = "https://www.hltv.org/"
    hltv = get_webpage(url)
    save_to_file(hltv, "hltv.html")       # gemmer til fil for ikke at skulle hente siden, så mange gange under test
    hltv_file = open_file("./hltv.html")
    top5 = find_top_five(hltv_file)
    
    # 1. top 5 hold counterstrike hold i verden
    print("HLTV Top 5 CounterStrike hold:")
    print(top5, "\n\n")

    # 2. "Copenhagen Flames" placering på verdensranglisten
    print("Copenhagen Flames placering på verdensranglisten")
    print(team_ranking(url, "Copenhagen Flames"), "\n\n")

    # 3. Find ved hjælp af regex hvor mange sejre de har under matches
    # foregående side blev gemt i filen team.txt
    print("Copenhagen Flames seneste kampe")
    print(find_matches())
