# Name: Hanqi Zhu
# SI 508 - Final Project

My project targets at helpping people who play DotA2, especially who are newly interested in it and want to learn how to play it, to better understand this game.

You will be able to do the following things:

1. View heroes they want by 3 specialties. The 3 specialties are: Strength, Agility, and Intelligence.

2. View heroes by 3 levels of Complexity. 1 for the simplest and 3 for the most complex.

3. Choose a hero to understand the abilities, lore, talents tree, and the recommended items to buy during a game.

4. Choose an item to view buying information and some tips of using them.

5. Generate a page of some photos from [Flickr](https://www.flickr.com/) about DotA2, photo number depending on your choice, but not exceeding 50.

6. View some popular and new tweets about DotA2 from [Twitter](https://twitter.com/), tweet number depending on your choice, but not exceeding 50.

The instructions on how to complete them will be listed in the following parts, follow me!

## Preparations

### Installing

Modules used in this project:

```
   twitter
   requests
   json
   BeautifulSoup
   webbrowser
```

As json and webbrowser don't need installing, if you don't have requests and bs4, install them:

```
   pip install requests
   pip install bs4
```

__IMPORTANT!!__ Please note that the twitter module might not be installed in your computer, and there are several twitter modules that will contradict to each other. To make sure you don't confuse them, please try uninstalling the other one first. The code is like this:
```
    pip uninstall twitter
    pip install python-twitter
```

Make sure you finish these steps before running my code!

### Files

There are some file folders here, but you will not use them: I just uploaded them because I use PyCharm.

You can clone and download the whole repository to your computer.

Or, simply downloading these files:

[advanced_expiry_caching.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/advanced_expiry_caching.py),
[main.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/main.py),
[project_Test.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/project_Test.py),
and [secrets.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/secrets.py) to a clear directory is fine enough to run my program.


### API keys

1. You will need a Flickr API key, which was used in the first project of SI508.

    If you haven't got one, [here](https://www.flickr.com/services/api/misc.api_keys.html) is the link to get one, it not complex.

    And then fill them in the line in [secrets.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/secrets.py).

2. You will need the RESTful API key from Twitter.

    If you don't have one, you can apply for it from [Twitter Developer Page](https://developer.twitter.com/en.html).

    __However, I highly recommend that you use mine!__

    The reason is, it will ask you to enter a lot of text to apply for it, and the application needs time(maybe half day to several days) to be reviewed and approved by Twitter.

    __IMPORTANT!!__ I will send a .txt file including the Twitter API keys and TOKEN to the instructional team(si508f18instructors@umich.edu)!

    __IMPORTANT!! Please don't paste Twitter API and TOKEN keys in [secrets.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/secrets.py)!!__

    I put these lines on the head of the [main file](https://github.com/hanqizhu/SI508-FinalProject/blob/master/main.py).

    This is because of some unknown reason: I happened to find I can work in using PyCharm if I put the keys in the [secrets.py](https://github.com/hanqizhu/SI508-FinalProject/blob/master/secrets.py), but cannot work if I use terminal.

    So to make sure it works, please first get my keys and paste them on the head of my main file.

### Expected outputs

You are expected to see 2 kinds of output result:

1. You will be able to see all the text outputs through the terminal window, if you use terminal to run the python file.

    If you are using other python editors, you can see the text output in the console window, too.

    Tweets are also going to be shown in text output.

    You can see the sample output screen shots in [this folder](https://github.com/hanqizhu/SI508-FinalProject/tree/master/sample_output_screenshots)

2. If you input the command about getting photos, you will also find an HTML file in the folder where you put all the files in.

    If you open the HTML file, you will see a web page like [this sample page](https://hanqizhu.github.io/SI508/flickr_photo_page)

## Run this program

### Get started with the project

After downloading my files, put them into a clear file folder, as I mentioned before.

Open your terminal, cd to this file folder, (or use your own editor) and type

```
   python main.py
```

Then you can run it.

You will see the initialized interface:

```
********
Hi! Welcome to Hanqi's DotA 2 Gaming Assistant!
Simply type the letter order at the beginning of each line to play with it:

ss <Letter A or I or S> (e.g. ss A - View heroes by specialty: 'A' for Agility, 'I' for Intelligence, and 'S' for Strength.)

cc <Integer 1 to 3> (e.g. cc 1 - View heroes by complexity level: 1 for the simpliest, 3 for the most complex.)

hero <Result_Number> (e.g. show 3 - View the information of the third hero in the recently viewed hero list.)

item (View the recommended items in a web page for the recently viewed hero.)

show <Result_Number> (e.g. show 2 - View the information of the second item in the recently viewed item list.)

photo <(optional)Number> (e.g. photo or photo 4 - An HTML file with DotA2 photos will be generated. If you are not typing number after 'photo', this web page will contain 5 most viewed photos. You can also input the number of photos you want. Note: please DO NOT input number larger than 50, because it will be too slow to process!)

tweet <(optional)Number> (e.g. tweet or tweet 4 - View tweets about DotA2 at a number of your choice. If you are not typing number after 'tweet', this web page will contain 5 popular and latest tweets. You can also input the number of tweets you want. Note: please DO NOT input number larger than 50, because I have a limit of API requests!)

help (List all available commands.)

exit (Simply exit this program.)

Please input a command:
```

### A correct example of entering commands

As you see these commands with examples and instructions, you can enter a command like:

```
ss A
```

You will get a list of names of heroes with agility speacialty like:

```
1. Anti-Mage
2. Arc Warden
3. Bloodseeker
4. Bounty Hunter
5. Broodmother
6. Clinkz
7. Drow Ranger
8. Ember Spirit
9. Faceless Void
10. Gyrocopter
11. Juggernaut
12. Lone Druid
13. Luna
...
```


You can also input like:

```
cc 3
```

You will be able to see a list of names of heroes that are rated the 3rd level complexity:
```
1. Arc Warden
2. Brewmaster
3. Chen
4. Earth Spirit
5. Invoker
6. Io
7. Lone Druid
8. Meepo
9. Morphling
10. Oracle
11. Rubick
12. Storm Spirit
13. Visage
```


Then let's assume you want to go into details of the hero name "Io". As its serial number here is "6", then you can type:

```
hero 6
```

You will be able to see the detailed information of Io:

```
Hero: Io
Lore: Io is everywhere, and in all things.  Denounced by enemies as the great unmaker, worshiped by scholars as the twinkling of a divine eye, this strange Wisp of life-force occupies all planes at once, the merest fraction of its being crossing into physical existence at any one moment.
Like the great twin riders Dark and Light, and yet another ancient traveler whose true history is lost to the ages, Io the Wisp is a Fundamental of the universe, a force older than time, a wanderer from realms far beyond mortal understanding. Io is nothing less than the sum of all attractive and repulsive forces within the material field, a sentient manifestation of the charge that bind existence together. It is only in the controlled warping of these electrical waylines that Io's presence can be experienced on the physical plane. A benevolent, cooperative force, Io bonds its strange magnetism to others so that the power of allies might be enhanced.  Its motives inscrutable, its strength unimaginable, Io moves through the physical plane, the perfect expression of the mysteries of the universe.
Abilities:
Tether -> Tethers Io to an allied unit, granting bonus movement speed to both. When Io restores health or mana, tethered units target gains a larger portion of that amount. The tether breaks when the allied unit moves too far away, or Io cancels the tether.
Break Tether -> Break the link to the tethered unit.
Spirits -> Summon five particle spirits that dance in a circle around Io. If a particle collides with an enemy hero, it explodes, damaging and slowing all enemy units in an area around it. Creeps take minor damage from touching a particle spirit, but do not cause them to explode. When its duration ends, any remaining Spirits explode.
Spirits Movement -> Calls the spirits in and out.
Abilities:
Level 10 -> +20% XP Gain or +45 Damage
Level 15 -> +75  Spirits Hero Damage or  Tether Grants  Scepter Bonus
Level 20 -> +150 Gold/Min or +16 Health Regen
Level 25 -> -60s  Relocate Cooldown or Attack  Tethered Ally's Target
```

This output includes the main information about Io, except the recommended items. If you want to know the items suitable for Io, simply type:

```
item
```

Then you will be able to view a list of recommended items for Io like:
```
1. Lifestealer
2. Slark
3. Disruptor
4. Mekansm
5. Arcane Boots
6. Aghanim's Scepter
7. Tango
8. Healing Salve
9. Clarity
10. Enchanted Mango
11. Gauntlets of Strength
12. Bottle
13. Urn of Shadows
...
```

Of course, only knowing the name may not be enough for you. Let's say, now you're interested in the item "Bottle", and you may want to know how much it is, where in the game can you buy it, and some tips of using it. As you see the serial number of it is 12, then you type:
```
show 12
```

You will see like:
```
You can buy Bottle for 650 in Consumables.
Here are the tips for using Bottle:
 * The Bottle does not disappear upon using up all charges.
* Has no effect when used while having no charges left, only the cooldown gets triggered.
* Successive casts on the same target do not stack, but refresh the duration instead.
* When casting without the Control key, it always casts on self in one click. When holding the Control key, a target has to be selected.
* If the target is more than 600 range away, the caster moves to the target until it is within 350 range before casting.
If a cast order is given on a target which is within 600 range already, the caster does not need to move closer and casts it right away.
* If a cast order is given on a target which is within 600 range already, the caster does not need to move closer and casts it right away.
* The owner does not have to face the target to give it a Bottle charge.
...
```
Note: some items are only formed by recipe, thus have no price or buying places, I have set those values to "unknown".


If you forget what the commands are like. So you type:
```
help
```

Then the instructions of giving commands just show again:

```
ss <Letter A or I or S> (e.g. ss A - View heroes by specialty: 'A' for Agility, 'I' for Intelligence, and 'S' for Strength.)

cc <Integer 1 to 3> (e.g. cc 1 - View heroes by complexity level: 1 for the simpliest, 3 for the most complex.)

hero <Result_Number> (e.g. show 3 - View the information of the third hero in the recently viewed hero list.)

item (View the recommended items in a web page for the recently viewed hero.)

show <Result_Number> (e.g. show 2 - View the information of the second item in the recently viewed item list.)

photo <(optional)Number> (e.g. photo or photo 4 - An HTML file with DotA2 photos will be generated. If you are not typing number after 'photo', this web page will contain 5 most viewed photos. You can also input the number of photos you want. Note: please DO NOT input number larger than 50, because it will be too slow to process!)

tweet <(optional)Number> (e.g. tweet or tweet 4 - View tweets about DotA2 at a number of your choice. If you are not typing number after 'tweet', this web page will contain 5 popular and latest tweets. You can also input the number of tweets you want. Note: please DO NOT input number larger than 50, because I have a limit of API requests!)

help (List all available commands.)

exit (Simply exit this program.)

Please input a command:
```


Then you know what you can input to this program again. You can type like
```
photo
```
or
```
photo 6
```
to generate a web page of photos about DotA2, sourced from [Flickr](https://www.flickr.com/).

You can decide how many photos you want, but please do not enter over 50, which will make the processing speed very slow.

I set all negative number and the number over 50 as invalid input.

After running this command, you will be able to see a text output:

```
Please find the HTML file in this directory!
```

It indicates that you can find an HTML file in the folder. Simply open the webpage, and you can see the pictures.



You can also view tweets about DotA2 from [Twitter](https://twitter.com/) by typing:

```
tweet
```
or
```
tweet 6
```

It will show like:
```
🔥Fast Giveaway:
🤝Tag The Best Friend &amp; Like
🚀Follow us
⏰Wait for 8 Hours!
🎉The winner of the last giveaway:… https://t.co/HSt7UCDvgg
The 7.20e Gameplay Update has been released https://t.co/2CNGZJr8yb
🇬🇧🎈 We need your help to choose the official #ESLOne Birmingham 2019 event shirt! Is Brewmaster your spirit animal?… https://t.co/RE0OrYbtI2
RT @redditdota2: I wish.. https://t.co/KuntDXhbjo #dota2 https://t.co/Nye4YEd2ni
RT @redditdota2: I wish.. https://t.co/KuntDXhbjo #dota2 https://t.co/Nye4YEd2ni
```

Still, you can decide how many tweets you want, but again, __please do not enter over 50__.
This is not because the process is slow, but I do have a limit of getting API requests from Twitter. To make it safe, I have set number over 50 as an invalid input.


Finally, simply type:

```
exit
```
This program ends here!

### Invalid Inputs

I have written codes for almost all kinds of invalid inputs I could think of.

Don't worry about entering wrong input.

## Test file

### Run the test file
Simply cd to the file folder that you store all the files in to run this command:

```
python project_Test.py
```
to test my project.

### What does this file do?

This file has 3 test suites subclasses, with 10 test cases in them:
```
class TestHeroSearch(unittest.TestCase)
```
This one tests scraping hero data from [Dota 2 Wiki](https://dota2.gamepedia.com/Dota_2_Wiki​)


```
class TestItemSearch(unittest.TestCase)
```
This one tests scraping item data from [Dota 2 Wiki](https://dota2.gamepedia.com/Dota_2_Wiki​)


```
class TestPageProducing(unittest.TestCase)
```
This one tests using REST APIs to get pictures from [Flickr](https://www.flickr.com/). I cannot test the pictures, but I can test if the url source of images are successfully generated, and if the HTML file is successfully produced.

I don't test function about tweets, because tweets are going to be updated soon, there's not a good way to test this. Actually, as the tweets results displays, it means the command is right.

## Checklist of project requirements
In this section, I will try to discuss all the requirements in the [final project description](https://paper.dropbox.com/doc/SI-508-Final-Project-Proposal--ATeeg4lYdnZ92ESQhqt32TjgAg-cflJKwQwD6IWpMUmwhfqQ#:uid=761319411194702196784771&h2=To-Submit:-Final-Project) in the order as the instructor listed.

### Requirements for submission
* Repository contains every file necessary to run the project. [100 points]

* Project code must run. [200 points]

* Repository must contain a README.md (Of course it does) [300 points]

* Project relies on Python programming/program(s). [100 points]

### Project technical requirements - Base Requirements
1. At least two data sources used in total [400 points]

   At least one data source must be from accessing the internet  [100 points]
    * Explanation: I used REST APIs of [Flickr](https://www.flickr.com/), REST APIs of [Twitter](https://twitter.com/) and scraped data from a web page [Dota 2 Wiki](https://dota2.gamepedia.com/Dota_2_Wiki​)

2. Caching must be implemented and/or used for any data sourced from the internet, scraping or API(s) [200 points]

3. Process data from each source [300 points]

4. Import and use functionality from at least one Python module that is not json, random, or requests [150 points]
    * Explanation: I also used twitter module, BeautifulSoup module, and webbrowser module.

5. A test suite file containing at least 2 unittest.TestSuite subclasses and at least 10 test methods (beginning with test) which are non-trivial tests [400 points]
    * Explanation: I have 3 nittest.TestSuite subclasses in my test file, and there are 10 test methods in them.

6. Running the project should produce a product that is the result of processing data  [100 points — more points specific to the implementation]
    * Explanation: I have text outputs that are processed from data, and an HTML file generated using the Flickr APIs.

7. Define at least 2 classes and create and use instance(s) of each of them [600 points]
    * Explanation: I have 3 classes named Hero, Item, and Photo. They are involved in the project, and are very important. I use quite different methods of them, including defining the comparison of classes.

8. Include in your repository an example of your output. [100 points]
    * Explanation: The example is linked at the beginning parts of the Readme file, and I also explain the details about how to interact with the project in the Readme file.

9. Errors handling. [100 points]
    * Explanation: I thought I did it well. You can try to input some error lines to see what happens.

10. At Least Two Second Level Requirements[total 450 points]
    * Scraping data that comes in HTML or XML form using BeautifulSoup

    * Accessing a REST API or a new endpoint of a REST API that we have not included in any course (lecture or section) meeting or assignment
        * I used Twitter REST API.
        * I also used Flickr API, which is used also in the first project. I digged more data about URLs of images this time.

11. At Least One Third Level Requirements [total 400 points]
    * An interactive project or game that accepts user input and generates useful results that vary based on user input.

    * A piece of computational art as a result of writing code using data sources.
        * Explanation: I have an HTML and CSS that displays a photo set about DotA2

## Code source
I did this project on my own, without referring to any others' source code.

But I did learn something about using Twitter APIs from [this website](https://code.tutsplus.com/articles/how-to-use-restful-web-apis-in-python--cms-29493)

Some contents of my SI 508 Project 1 and SI508 Project 2 are also used.



