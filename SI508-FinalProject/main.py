from advanced_expiry_caching import *
import requests
import json
import twitter
from bs4 import BeautifulSoup as bsoup
import webbrowser
from secrets import *

# put Twitter API key here:
api = twitter.Api(consumer_key="YUMVAhw0d1p2P6kdpqrGFf1EV",
                  consumer_secret="C6MfhVHQl2bV8zWsfFgCiJRwoaeplUnRkdA4drNtcVLrBw79ku",
                  access_token_key="1072600617783312385-8DMcgJ94hNRUGQdlA15oN65L3MH5NW",
                  access_token_secret="O7ydB8MyyvuixEc8gTryJismI6AVUU3ZgGapKiDOMevfz")


CACHE_FNAME = "first_level_cache.json"
primary_cache = Cache(CACHE_FNAME)
base_url = "https://dota2.gamepedia.com/"

def get_specialty_heroes(letter):

    if letter.upper() == "A":
        scrape_url = base_url + "Agility"
    elif letter.upper() == "I":
        scrape_url = base_url + "Intelligence"
    else:
        scrape_url = base_url + "Strength"

    while primary_cache.get(scrape_url) is None:
        data = requests.get(scrape_url)
        html_text = data.text
        primary_cache.set(scrape_url, html_text, 1)

    soup_menu = bsoup(primary_cache.get(scrape_url), features="html.parser")
    hero_list = []
    for b in soup_menu.find_all('b'):
        if (b.a):
            hero_list.append(b.string)
    return hero_list


def get_complexity_heroes(number):
    target_url = "https://dota2.gamepedia.com/Hero_complexity"

    while primary_cache.get(target_url) is None:
        data = requests.get(target_url)
        html_text = data.text
        primary_cache.set(target_url, html_text, 1)

    soup_menu = bsoup(primary_cache.get(target_url), features="html.parser")
    id = 0
    for td in soup_menu.find_all('td', limit=6):
        if id == 1: soup1 = td
        if id == 3: soup2 = td
        if id == 5: soup3 = td
        id += 1

    simple_list = []
    medium_list = []
    complex_list = []

    for a in soup1.find_all('a'):
        simple_list.append(a.get('title'))
    for a in soup2.find_all('a'):
        medium_list.append(a.get('title'))
    for a in soup3.find_all('a'):
        complex_list.append(a.get('title'))
    if number == "1":
        return simple_list
    if number == "2":
        return medium_list
    if number == "3":
        return complex_list
# print(get_complexity_heroes("3"))

class Hero():
    def __init__(self, info_dict):
        self.name = info_dict["name"][0].upper() + info_dict["name"][1:].lower()
        self.lore = info_dict["lore"]
        self.abilitySet = info_dict["ability"]
        self.talents = info_dict['talents']
        self.items = info_dict['items']

    def __str__(self):
        hero_str = "Hero: " + self.name + "\n"
        hero_str += ("Lore: " + self.lore + "\n")
        hero_str += "Abilities: \n"
        for key in self.abilitySet:
            hero_str += (key + " -> " + self.abilitySet[key] + "\n")
        hero_str += "Abilities: \n"
        hero_str += ("Level 10 -> " + self.talents[7] + " or " + self.talents[6] + "\n")
        hero_str += ("Level 15 -> " + self.talents[5] + " or " + self.talents[4] + "\n")
        hero_str += ("Level 20 -> " + self.talents[3] + " or " + self.talents[2] + "\n")
        hero_str += ("Level 25 -> " + self.talents[1] + " or " + self.talents[0] + "\n")
        return hero_str

def get_hero_info(name):
    hero_url = base_url + name.replace(" ", "_")

    info = {}
    info["name"] = name
    while primary_cache.get(hero_url) is None:
        data = requests.get(hero_url)
        html_text = data.text
        primary_cache.set(hero_url, html_text, 1)

    soup = bsoup(primary_cache.get(hero_url), features="html.parser")

    info["lore"] = soup.find(style="display: table-cell; font-style: italic;").text

    ablty_list = []
    ablty_desc = []
    ablty_dict = {}
    for x in soup.find_all('span', id=True, class_=False):
        ablty_list.append(x.get('id').replace('_', ' '))

    for y in soup.find_all(style="vertical-align: top; padding: 3px 5px; border-top: 1px solid black;"):
        ablty_desc.append(y.text)

    for i in range(4):
        ablty_dict[ablty_list[i]] = ablty_desc[i]

    info["ability"] = ablty_dict

    talents = []
    for x in soup.find_all('td', style="width:240px"):
        talents.append(x.text)

    info["talents"] = talents

    item_list = []
    for x in soup.find_all(class_="image-link"):
        content = x.a.get('title')
        if (content.lower() != name.lower() and content not in item_list):
            item_list.append(content)

    info["items"] = item_list

    return Hero(info)

# mirana = Hero(get_hero_info("mirana"))
# print(mirana)

class item():
    def __init__(self, info_dict):
        self.name = info_dict["name"]
        self.cost = info_dict["cost"]
        self.shop = info_dict["buy_place"]
        self.desc = info_dict["desc"]

    def __str__(self):
        return "You can buy {} for {} in {}.\nHere are the tips for using {}: \n {}".format(self.name, self.cost, self.shop, self.name, self.desc)

def get_item_info(item_name):
    item_url = base_url + item_name.replace(" ", "_")
    while primary_cache.get(item_url) is None:
        data = requests.get(item_url)
        html_text = data.text
        primary_cache.set(item_url, html_text, 1)

    info = {}
    info["name"] = item_name
    soup = bsoup(primary_cache.get(item_url), features="html.parser")

    buy = soup.find(style="display:flex; align-items:center; background-color:#B44335; color:white;")
    try:
        info["cost"] = buy.find(style="width:50%; background-color:#DAA520;").text.replace("Cost","")
        info["cost"] = info["cost"].replace(" ", "")
    except:
        info["cost"] = "unknown"

    try: info["buy_place"] = buy.find(style="width:50%;").text.replace("Bought From", "")
    except: info["buy_place"] = "unknown"

    info_para = ""
    for ss in soup.find_all('li', id=False, class_=False):
        if ss.find_all('div') == []:
            if ss.find_all('a') == []:
                info_para += ("* " + ss.text + "\n")

    info["desc"] = info_para
    return item(info)


if FLICKR_KEY == "" or not FLICKR_KEY:
    print(
        "Your flickr key is missing from the file. Enter your flickr key where directed and save the program!")
    exit()

CACHE_FNAME_FLICKR = "Flickr_Cached_Data.json"

try:
    cache_file = open(CACHE_FNAME_FLICKR, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.load(cache_contents)
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_flickr_data(search_string, photo_number = 50):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["tag_mode"] = "all"
    params_diction["tags"] = search_string
    params_diction["per_page"] = photo_number
    params_diction["media"] = "photos"
    params_diction["nojsoncallback"] = 1
    params_diction["format"] = "json"
    params_diction["method"] = "flickr.photos.search"
    unique_ident = params_unique_combination(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        flickr_resp = requests.get(baseurl, params_diction)
        flickr_text = flickr_resp.text
        CACHE_DICTION[unique_ident] = json.loads(flickr_text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME_FLICKR, "w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

def get_photo_data(photo_id):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["tag_mode"] = "all"
    params_diction["media"] = "photos"
    params_diction['photo_id'] = photo_id
    params_diction["nojsoncallback"] = 1
    params_diction["format"] = "json"
    params_diction["method"] = "flickr.photos.getInfo"
    unique_ident = params_unique_combination(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        flickr_resp = requests.get(baseurl, params_diction)
        flickr_text = flickr_resp.text
        CACHE_DICTION[unique_ident] = json.loads(flickr_text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME_FLICKR, "w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

class photo():
    def __init__(self, info_dict):
        self.id = info_dict["id"]
        self.secret = info_dict["secret"]
        self.server = info_dict["server"]
        self.farm = info_dict["farm"]
        self.format = info_dict["originalformat"]
        self.views = info_dict["views"]

    def __lt__(self, other):
        return self.views < other.views

    def __str__(self):
        return self.id + ":" + str(self.views)

    def get_url(self):
        return ("https://farm" + str(self.farm) +".staticflickr.com/" + self.server + "/" + self.id + "_" + self.secret + "." + self.format)


def produce_photo_page(number=5):
    result = get_flickr_data("dota2")
    search_photo_set = result['photos']['photo']
    search_photo_ids = []
    search_photo_dic_list = []
    for item in search_photo_set:
        search_photo_ids.append(item['id'])
        search_photo_dic_list.append(get_photo_data(item['id']))

    photo_list = []
    for each_dic in search_photo_dic_list:
        if (each_dic["photo"]["visibility"]["ispublic"] == 1):
            photo_item = photo(each_dic["photo"])
            photo_list.append(photo_item)
    photo_list.sort()

    GEN_HTML = "flickr_photo_page.html"

    img = ""
    if number <= len(photo_list):
        for i in range(number):
            img += "<img src=\"" + photo_list[i].get_url() + "\" />\n   "
    else:
        for x in photo_list:
            img += "<img src=\"" + x.get_url() + "\" />\n   "


    f = open(GEN_HTML, 'w')
    message = """
    <html>
    <head>
    <style>
    img{height="300"}
    </style>
    </head>
    <body>
    <p class="sheet">Hello, here are the flickr photos for you!</p>
    """
    message += img + "  </body>\n   </html>\n  "

    f.write(message)
    f.close()
    webbrowser.open(GEN_HTML, new=1)

def get_twitter_data(number=5):
    tweets = api.GetSearch(term="dota2", lang="en", count=number, return_json=True)
    json_str = json.dumps(tweets)
    with open('twitter_data.json', 'w') as json_file:
        json_file.write(json_str)
    for x in tweets["statuses"]:
        print(x["text"])

def call_help():
    print("ss <Letter A or I or S> (e.g. ss A - View heroes by specialty: \'A\' for Agility, \'I\' for Intelligence, and \'S\' for Strength.)\n")
    print("cc <Integer 1 to 3> (e.g. cc 1 - View heroes by complexity level: 1 for the simpliest, 3 for the most complex.)\n")
    print("hero <Result_Number> (e.g. show 3 - View the information of the third hero in the recently viewed hero list.)\n")
    print("item (View the recommended items in a web page for the recently viewed hero.)\n")
    print("show <Result_Number> (e.g. show 2 - View the information of the second item in the recently viewed item list.)\n")
    print("photo <(optional)Number> (e.g. photo or photo 4 - An HTML file with DotA2 photos will be generated. If you are not typing number after \'photo\', this web page will contain 5 most viewed photos. You can also input the number of photos you want. Note: please DO NOT input number larger than 50, because it will be too slow to process!)\n")
    print("tweet <(optional)Number> (e.g. tweet or tweet 4 - View tweets about DotA2 at a number of your choice. If you are not typing number after \'tweet\', this web page will contain 5 popular and latest tweets. You can also input the number of tweets you want. Note: please DO NOT input number larger than 50, because I have a limit of API requests!)\n")
    print("help (List all available commands.)\n")
    print("exit (Simply exit this program.)\n")

def check_valid_ss(str):
    if len(str) != 4:
        return False
    if str[2] != " ":
        return False
    if not (str[3].upper() == "A" or str[3].upper() == "I" or str[3].upper() == "S"):
        return False
    return True

def check_valid_cc(str):
    if len(str) != 4:
        return False
    if str[2] != " ":
        return False
    if not (str[3] == "1" or str[3] == "2" or str[3] == "3"):
        return False
    return True

def check_valid_heroandshow(str, list):
    if not (str[:5] == "hero " or str[:5] == "show "):
        return False
    try:
        input_num = int(str[5:])
        if list == []:
            return False
        if input_num <= 0:
            return False
        elif input_num > len(list):
            return False
        else:
            return input_num
    except:
        return False

def check_valid_photoandtweet(str):
    if not (str[:6] == "photo " or str[:6] == "tweet "):
        return False
    try:
        input_num = int(str[6:])
        if input_num <= 0:
            return False
        elif input_num > 50:
            return False
        else:
            return input_num
    except:
        return False


if __name__ == "__main__":
    print("********\nHi! Welcome to Hanqi's DotA 2 Gaming Assistant!")
    print("Simply type the letter order at the beginning of each line to play with it:\n")
    call_help()
    herolist = []
    itemlist = []
    target_hero = None
    input_type = input("Please input a command: \n").lower()
    while (input_type != "exit"):
        if input_type == "help":
            call_help()

        elif input_type[:2].lower() == "ss":
            if check_valid_ss(input_type) == False:
                print("Invalid Input! Please try like \"ss A\"")
            else:
                herolist = get_specialty_heroes(input_type[3])
                total = len(herolist)
                for i in range(total):
                    print(str(i + 1) + ". " + herolist[i])

        elif input_type[:2].lower() == "cc":
            if check_valid_cc(input_type) == False:
                print("Invalid Input! Please try like \"cc 2\"")
            else:
                herolist = get_complexity_heroes(input_type[3])
                total = len(herolist)
                for i in range(total):
                    print(str(i + 1) + ". " + herolist[i])

        elif input_type[:4].lower() == "hero":
            if check_valid_heroandshow(input_type, herolist) == False:
                print("Invalid Input! Have you viewed any hero list?")
            else:
                num = check_valid_heroandshow(input_type, herolist)
                target_hero = get_hero_info(herolist[num - 1])
                print(target_hero)
        elif input_type.lower() == "item":
            if target_hero == None:
                print("Please choose a hero first!")
            else:
                itemlist = target_hero.items
                total = len(itemlist)
                for i in range(total):
                    print(str(i + 1) + ". " + itemlist[i])
        elif input_type[:4].lower() == "show":
            if check_valid_heroandshow(input_type, itemlist) == False:
                print("Invalid Input! Have you viewed any hero?")
            else:
                num = check_valid_heroandshow(input_type, itemlist)
                target_item = get_item_info(itemlist[num - 1])
                print(target_item)
        elif input_type == "photo":
            produce_photo_page()
            print("Please find the HTML file in this directory!")
        elif input_type[:5] == "photo":
            if check_valid_photoandtweet(input_type) == False:
                print("Invalid Input! Please enter a proper number!")
            else:
                search_number = check_valid_photoandtweet(input_type)
                produce_photo_page(search_number)
                print("Please find the HTML file in this directory!")
        elif input_type == "tweet":
            get_twitter_data()
        elif input_type[:5] == "tweet":
            if check_valid_photoandtweet(input_type) == False:
                print("Invalid Input! Please enter a proper number!")
            else:
                search_number = check_valid_photoandtweet(input_type)
                print("Here are what I have found for you: ")
                get_twitter_data(search_number)
        else:
            print("Invalid input! Please type \"help\" to look at the command list!")
        input_type = input("Please input a command: \n").lower()

