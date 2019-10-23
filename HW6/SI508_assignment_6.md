# SI 508 - Assignment 6 Hanqi Zhu

### This assignment takes a somewhat different format

**You should:**

* Download this file to a directory
* Create a Git repo inside that directory
* Make any changes necessary to files (e.g. adding answers to questions in this `SI508_assignment_6.md`)
* Add changes to git as necessary and make commits throughout the process (and look up markdown formatting if necessary)
* Create a private GitHub repository on your account called `SI508_HW6`, and make it a remote of the git repo for this assignment
* Add the instructors as collaborators to the repository so we can view it to grade ([see instructions](linktba.com))
* Make sure you've pushed all your edits to your new `SI508_HW6` GitHub repository
* Submit the GitHub repository to Gradescope -- assignment **HW6** (see the HW 6 assignment on Canvas)

* **Note** that any commits made and pushed to your repo after the deadline do *not* count for your grade (and you should not commit to the repository post-deadline pre-grading unless you are submitting the assignment late)

## Answering questions instructions

- Below, in *this* `.md` file, there are bolded questions, largely based on the documentation at this URL: `https://www.crummy.com/software/BeautifulSoup/bs4/doc/`, which is your reading for Thursday.

* You should check out the documentation, the questions, maybe some google searches!, and perhaps try out some example code yourself, in order to be able to write answers to the questions -- which will be graded by humans.

- You will get points for thoughtful, correct answers to each question. (Note that class meetings may be helpful for many, but likely not ALL, of these questions -- use a combination of all the info/input you have available this week, plus the internet! Note also that not all questions have *one* correct answer! There are many possible options!) Answers need not be long -- questions just need to be answered. If the answer is one word, one word is fine! No answer should be longer than a few sentences.

- Please put your answer to each question below the question, with a blank line separating your answer text from any other text. Keep the questions bolded, and do *not* make your answers bold (for easy reading by graders).

---
---

# Questions to Answer


* **What is HTML? Describe in 1 or 2 brief sentences. (It's OK to quote something else if you want, but make sure you cite anything/anyone you quote from, and make sure you understand anyone else's words you use!)**

    * **Answer: HTML is the abbreviation of Hyper Text Markup Language. It helps people build web pages using the blocks that are based on HTML tags.**

* **Why might you find an `id=` in an HTML tag? (Describe in 1 sentence.)**

    * **Answer: Because sometimes people may want the piece with this `id=`  to act as an HTML element with unique attributes or styles that others will not share with.**

* **Why might you find a `class=` in an HTML tag? (Describe in 1 sentence.)**

    * **Answer: Because sometimes people may want some pieces to act as HTML elements with certain same attributes or styles, and with `class=`  they don't need to repeat the code to define the attributes or styles for each piece**

* **What is "scraping data from websites" in a program? (It is OK to quote a source or another person, but you should cite anything/anyone else you quote here, and you should make sure you understand what you quote.)**

    * **Answer: "Web scraping (also termed web data extraction, screen scraping, or web harvesting) is a web technique of extracting data from the web, and turning unstructured data on the web  into structured data that can stored to your local computer or a database."
[Cited: https://www.bigdatanews.datasciencecentral.com/profiles/blogs/top-30-free-web-scraping-software]**


* **What is happening in this line of code: `soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')` ? Describe VERY briefly. Or simply answer the following question: What type is the value of `soup` after that line executes?**

    * **Answer: This line of code transfers an HTML tag `<b class="boldest">Extremely bold</b>` to a BeautifulSoup object, and assigns it to `soup`.**


* **In the following code, what's any one thing that the values of `soup` and `tag_one` have in common? (note: "They're both values in Python code" is too general.)**

        ```py
        soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
        tag = soup.b
        ```

    * **Answer: Their string content are the same, and the both have this tag '<b class="boldest">Extremely bold</b>'**

* **What kind of information can you find in a `BeautifulSoup Tag`'s `.attrs` attribute? e.g. if you ran the following code, what is 1 thing you might find out? (There are many possibilities, you need only answer one. But it will be useful to think about what `.attrs` is here, and whether or not you understand the following code!)**

        ```py
        sp = BeautifulSoup("<html><h1>Title Here</h1><a href="http://www.google.com">Link to Google...</a></html>")
        print(sp.a.attrs)
        print(sp.a.attrs.keys())
        ```

    * **Answer: the results printed out are:
        `{'href': 'http://www.google.com'}`
        `dict_keys(['href'])`
        so the <a> tag of the BeautifulSoup sp here is its link information.**
        **The `.attrs` attribute the additional info that is included in the open tag. The information is stored in a dictionary. And the .attrs.keys() returns the list of keys of the dictionary, which are just the types of attributes that are included in the tag.**
        **Here <a> is only with the link, so the keys list only has `href` in it.**


* **How are the `BeautifulSoup` methods `.find` and `.find_all` different? What does each one return? Briefly, why might you use `.find_all` instead of `.find`? (HINT: Check out the *Searching the Tree* section of the documentation...)**

    * **Answer: 1. `.find` only returns one result, while `.find_all` returns a list of results.**
    **2.  `.find_all` can also use the parameter `limit` to control the number of results, while `.find` cannot.**
    **3. If the search does not find anything,  `.find` returns None, while `.find_all` returns an empty list.**


* **Is using the `BeautifulSoup` library the only way to do scraping in a Python program? If so, why is it the only way? If not, what other module options could you investigate for scraping using a Python program (list just 1 or 2)?**

    * **Answer: It is not the only way. There are 5 libraries related to Python web scraping: Requests, Beautiful Soup 4, lxml, Selenium, and Scrapy.**

	* ** *Consider:* Why might you want to use `BeautifulSoup` instead of another option, even if others exist? Why might you *not* want to use `BeautifulSoup`?**
    
    * **"Beautiful Soup (BS4) is a parsing library that can use different parsers. A parser is simply a program that can extract data from HTML and XML documents.
    Beautiful Soup’s default parser comes from Python’s standard library. It’s flexible and forgiving, but a little slow. The good news is that you can swap out its parser with a faster one if you need the speed.
    One advantage of BS4 is its ability to automatically detect encodings. This allows it to gracefully handle HTML documents with special characters.
    In addition, BS4 can help you navigate a parsed document and find what you need. This makes it quick and painless to build common applications."** 
    **[Cited: https://elitedatascience.com/python-web-scraping-libraries]**


* **Why is some form of caching important to perform when scraping data from web pages?**
    * **Answer:“Caching is the act of keeping data in storage to allow retrieval without having to request the data from the original source, if that data will not change frequently.
        A typical caching scenario is having a cached copy of a web page.  That page doesn't change every five minutes, so caching it locally on your computer saves time and bandwidth for you to re-display it if you hit reload in your browser.
        Cache is generally much faster than loading from disk or having a server generate a page from scratch.”**
            **[Cited: https://www.quora.com/What-is-caching-and-why-is-it-important]**
        **So, generally it saves time. Also, if you want to work on one page for a long time, if you load the page time after time in a short period of time, you may be suspected as attacking this page.**

* **Why would you scrape data rather than using an API to get data? What's an example of a situation in which you would want or need to use scraping techniques, specifically?**
    * **Answer: By scraping, we can directly use HTML to get data;**
    **Any content that can be viewed on a webpage can be scraped;**
    **There's less rate limiting.**
    **Problems of using API:
        **It does not update in real-time.**
        **Also:
        "With APIs, you often have to register to get a key and then send along that key with every request. But with simple HTTP requests, you’re basically anonymous besides your IP address and cookies, which can be easily spoofed."**
        **[Cited: https://blog.hartleybrody.com/web-scraping/]**
        **For example, some small websites that we want to get information from are not completed enough that they don't have APIs, in this case, we need scraping.**
