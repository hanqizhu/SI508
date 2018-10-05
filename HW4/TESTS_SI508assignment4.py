from SI508_assignment4 import *
import unittest

class Problem1(unittest.TestCase):
    def setUp(self):
        self.f = open("post_data.csv")
        self.lines = self.f.readlines()
        self.f.close()
    def test_headers(self):
        self.assertTrue("CREATED_TIME,COMMENT_TEXT,NAME_OF_POSTER,NUM_LIKES,NUM_WORDS" in self.lines[0])
    ## TEST FOR AUTOGRADER - NOT FOR RUNNING IN ASSIGNMENT - DO NOT UNCOMMENT
    # def test_file(self):
    #     self.assertEqual(open("SOLN_post_data.csv").read(),open("post_data.csv").read())
    def test_line(self):
        self.assertTrue("The river has been frozen so long that we decided to test whether" in self.lines[1])

class Problem2(unittest.TestCase):
    def setUp(self):
        self.f = open("scores_names.json")
    def test_scores_diction(self):
        self.assertEqual(sorted({'Student 3457': ['78', '89', '92', '81'], 'Student 6894': ['94', '36', '87', '92'], 'Student 8732': ['65', '78', '78', '97'], 'Student 9510': ['93', '93', '72', '72'], 'Student 1010': ['34', '48', '51', '65'], 'Student 0986': ['73', '89', '89', '81']}.items()),sorted(scores_diction.items()),"Testing if scores_diction contains the correct data")
    def test_file_exists(self):
        self.assertTrue(self.f.read())
    def tearDown(self):
        self.f.close()

class Problem3(unittest.TestCase):
    def test_jm_lst(self):
        # self.assertEqual(sorted(jm_lst),['BaBopBye Ya', "Can't Live Without Your Love", 'Cold War', 'Come Alive (War of the Roses)', 'Crazy, Classic, Life', 'Dance Apocalyptic', 'Dance or Die (feat. Saul Williams)', 'Dirty Computer (feat. Brian Wilson)', 'Django Jane', 'Don’t Judge Me', 'Dorothy Dandridge Eyes (feat. Esperanza Spalding)', 'Electric Lady (feat. Solange)', 'Ghetto Woman', 'Givin Em What They Love (feat. Prince)', 'Good Morning Midnight (Interlude)', 'Hidden Figures', 'I Got The Juice (feat. Pharrell Williams)', 'I Like That', "It's Code", 'Jane’s Dream', 'Locked Inside', 'Look Into My Eyes', 'Make Me Feel', 'Moonlight', 'Neon Gumbo', 'Neon Valley Street', 'Neon Valley Street', 'Oh, Maker', 'Our Favorite Fugitive (Interlude)', 'PrimeTime (feat. Miguel)', 'Pynk (feat. Grimes)', 'Q.U.E.E.N. (feat. Erykah Badu)', 'Sally Ride', "Say You'll Go", 'Screwed (feat. Zoë Kravitz)', 'So Afraid', 'Stevie’s Dream', 'Suite III Overture', 'Suite IV: Electric Overture', 'Suite V: Electric Overture', 'Take A Byte', 'The Chrome Shoppe (Interlude)', 'This Is for My Girls', 'Tightrope (feat. Big Boi)', 'Victory', 'We Are Young (feat. Janelle Monáe)', "We Were Rock n' Roll", 'What An Experience', 'What Is Love', 'Yoga'])
        self.assertEqual(type(jm_lst[0]), type(""))
        self.assertEqual(type(jm_lst), type([]))
        self.assertTrue(len(jm_lst) > 1)
        #self.assertTrue("feat. Pharrell Williams" in "".join(jm_lst))
    def test_beatles_lst(self):
        # self.assertEqual(sorted(beatles_lst),['A Day In the Life', 'Abbey Road (Documentary)', 'All You Need Is Love', 'Back In the U.S.S.R.', 'Because', 'Birthday', 'Blackbird', 'Carry That Weight', 'Come Together', 'Dear Prudence', "Don't Let Me Down", 'Eleanor Rigby', 'Golden Slumbers', 'Hello, Goodbye', 'Help!', 'Helter Skelter', 'Her Majesty', 'Here Comes the Sun', 'Hey Jude', 'I Am the Walrus', 'I Saw Her Standing There', "I Want You (She's So Heavy)", 'I Will', 'In My Life', 'Let It Be', 'Let It Be', 'Lucy In the Sky With Diamonds', "Maxwell's Silver Hammer", 'Mean Mr. Mustard', 'Norwegian Wood (This Bird Has Flown)', 'Ob-La-Di, Ob-La-Da', "Octopus's Garden", 'Oh! Darling', 'Penny Lane', 'Polythene Pam', 'Revolution', 'Rocky Raccoon', "Sgt. Pepper's Lonely Hearts Club Band", 'She Came In Through the Bathroom Window', "She's Leaving Home", 'Something', 'Strawberry Fields Forever', 'Sun King', 'The End', 'Twist and Shout', "When I'm Sixty-Four", 'While My Guitar Gently Weeps', 'With a Little Help From My Friends', 'Yesterday', 'You Never Give Me Your Money'])
        self.assertEqual(type(beatles_lst[0]),type(""))
        self.assertEqual(type(beatles_lst), type([]))
        self.assertTrue(len(beatles_lst) > 1)
        #self.assertTrue("Yesterday" in beatles_lst)
        #self.assertTrue("Abbey Road (Documentary)" in beatles_lst)

if __name__  == "__main__":
    unittest.main(verbosity=2)
