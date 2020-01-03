from main import *
import unittest

class TestHeroSearch(unittest.TestCase):

    def hero_is_in_list(self, hero_name, hero_list):
        for s in hero_list:
            if hero_name == s:
                return True
        return False

    def get_hero_from_list(self, hero_name, hero_list):
        for s in hero_list:
            if hero_name == s:
                return get_hero_info(hero_name)
        return None

    def setUp(self):
        self.agility_hero_list = get_specialty_heroes('A')
        self.third_level_hero_list = get_complexity_heroes('3')
        self.mirana = self.get_hero_from_list('Mirana', self.agility_hero_list)
        self.storm_spirit = self.get_hero_from_list('Storm Spirit', self.third_level_hero_list)

    def test_basic_search(self):
        self.assertEqual(len(self.agility_hero_list), 37)
        self.assertEqual(len(self.third_level_hero_list), 13)

        self.assertTrue(self.hero_is_in_list('Mirana', self.agility_hero_list))
        self.assertTrue(self.hero_is_in_list('Storm Spirit', self.third_level_hero_list))

        self.assertTrue(self.hero_is_in_list('Luna', self.agility_hero_list))
        self.assertTrue(self.hero_is_in_list('Io', self.third_level_hero_list))

        self.assertFalse(self.hero_is_in_list('Abaddon', self.agility_hero_list))
        self.assertFalse(self.hero_is_in_list('Abaddon', self.third_level_hero_list))

    def test_lore(self):

        self.assertEqual(self.mirana.lore, 'Born to a royal family, a blood princess next in line for the Solar Throne, Mirana willingly surrendered any claim to mundane land or titles when she dedicated herself completely to the service of Selemene, Goddess of the Moon. Known ever since as Princess of the Moon, Mirana prowls the sacred Nightsilver Woods searching for any who would dare poach the sacred luminous lotus from the silvery pools of the Goddess\'s preserve. Riding on her enormous feline familiar, she is poised, proud and fearless, attuned to the phases of the moon and the wheeling of the greater constellations. Her bow, tipped with sharp shards of lunar ore, draws on the moon\'s power to charge its arrows of light.')
        self.assertEqual(self.storm_spirit.lore, 'Storm Spirit is literally a force of nature--the wild power of wind and weather, bottled in human form. And a boisterous, jovial, irrepressible form it is! As jolly as a favorite uncle, he injects every scene with crackling energy. But it was not always thus, and there was tragedy in his creation. Generations ago, in the plains beyond the Wailing Mountains, a good people lay starving in drought and famine. A simple elementalist, Thunderkeg by name, used a forbidden spell to summon the spirit of the storm, asking for rain. Enraged at this mortal’s presumption, the Storm Celestial known as Raijin lay waste to the land, scouring it bare with winds and flood. Thunderkeg was no match for the Celestial--at least until he cast a suicidal spell that forged their fates into one: he captured the Celestial in the cage of his own body. Trapped together, Thunderkeg\'s boundless good humor fused with Raijin\'s crazed energy, creating the jovial Raijin Thunderkeg, a Celestial who walks the world in physical form.')

    def test_ability(self):
        self.assertIn("Sacred Arrow", self.mirana.abilitySet)
        self.assertIn("Ball Lightning", self.storm_spirit.abilitySet)

    def test_talents(self):
        self.assertIn("+12% Spell Amplification", self.mirana.talents)
        self.assertIn("+0.5s  Electric Vortex", self.storm_spirit.talents)

    def test_items(self):
        self.assertIn("Magic Wand", self.mirana.items)
        self.assertIn("Eul\'s Scepter of Divinity", self.mirana.items)
        self.assertIn("Dagon",self.storm_spirit.items)

        self.assertEqual(len(self.mirana.items), 35)
        self.assertEqual(len(self.storm_spirit.items), 27)

class TestItemSearch(unittest.TestCase):

    def setUp(self):
        self.desolator = get_item_info("Desolator")
        self.ghost_scepter = get_item_info("Ghost Scepter")

    def test_item_cost(self):
        self.assertEqual(self.desolator.cost, "3500")
        self.assertEqual(self.ghost_scepter.cost, "1500")

    def test_item_shop(self):
        self.assertEqual(self.desolator.shop, "Artifacts")
        self.assertEqual(self.ghost_scepter.shop, "Arcane")

    def test_item_tips(self):
        self.assertIn("The attacks first apply the debuff, then their own damage.", self.desolator.desc)
        self.assertIn("Use Ghost Scepter after baiting an enemy carry to attack you, causing them to waste time switching between targets.", self.ghost_scepter.desc)

class TestPageProducing(unittest.TestCase):
    def test_url_generate(self):
        infodict = {'id': '44166170370', 'secret': '420ae07d67', 'server': '4804', 'farm': 5, 'dateuploaded': '1542788990', 'isfavorite': 0, 'license': '0', 'safety_level': '0', 'rotation': 0, 'originalsecret': 'e8555c8477', 'originalformat': 'jpg', 'owner': {'nsid': '58073045@N06', 'username': 'tarasvb', 'realname': 'Taras V. B.', 'location': 'Voronezh, Russia', 'iconserver': '0', 'iconfarm': 0, 'path_alias': 'tarasvb'}, 'title': {'_content': 'Anti-Mage cosplay'}, 'description': {'_content': 'Anti-Mage (Dota 2), Alex Wolf \n(<a href="https://instagram.com/alexwolf_cosplay" rel="noreferrer nofollow">instagram.com/alexwolf_cosplay</a>)\nat Comic Con Russia 2018'}, 'visibility': {'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, 'dates': {'posted': '1542788990', 'taken': '2018-10-06 15:23:49', 'takengranularity': '0', 'takenunknown': '0', 'lastupdate': '1542789556'}, 'views': '119', 'editability': {'cancomment': 0, 'canaddmeta': 0}, 'publiceditability': {'cancomment': 1, 'canaddmeta': 0}, 'usage': {'candownload': 1, 'canblog': 0, 'canprint': 0, 'canshare': 1}, 'comments': {'_content': '0'}, 'notes': {'note': []}, 'people': {'haspeople': 0}, 'tags': {'tag': [{'id': '58027723-44166170370-18838021', 'author': '58073045@N06', 'authorname': 'tarasvb', 'raw': 'antimage', '_content': 'antimage', 'machine_tag': 0}, {'id': '58027723-44166170370-4659', 'author': '58073045@N06', 'authorname': 'tarasvb', 'raw': 'cosplay', '_content': 'cosplay', 'machine_tag': 0}, {'id': '58027723-44166170370-61969385', 'author': '58073045@N06', 'authorname': 'tarasvb', 'raw': 'dota2', '_content': 'dota2', 'machine_tag': 0}]}, 'urls': {'url': [{'type': 'photopage', '_content': 'https://www.flickr.com/photos/tarasvb/44166170370/'}]}, 'media': 'photo'}
        self.aphoto = photo(infodict)
        self.assertEqual(self.aphoto.get_url(), "https://farm5.staticflickr.com/4804/44166170370_420ae07d67.jpg")

    def test_show_produce_page(self):
        try:
            produce_photo_page()
            produce_photo_page(6)
        except:
            self.fail()

if __name__ == '__main__':
    unittest.main()
