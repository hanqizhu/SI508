## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

#######################
#                     #
# Tests of Class Card #
#                     #
#######################

class Problem1(unittest.TestCase):
    def test_default_value(self):
        card1 = Card()
        self.assertEqual(card1.__str__(), "2 of Diamonds", "Testing the default value of default Card.")

    def test_first_card_value(self):
        card2 = Card(3, 1)
        self.assertEqual(card2.__str__(), "Ace of Spades", "Testing the first value of Card given in description.")

    def test_second_card_value(self):
        card3 = Card(1, 3)
        self.assertEqual(card3.__str__(), "3 of Clubs", "Testing the second value of Card given in description.")

    def test_my_value(self):
        card4 = Card(2, 12)
        self.assertEqual(card4.__str__(), "Queen of Hearts", "Testing my value of Card.")

#######################
#                     #
# Tests of Class Deck #
#                     #
#######################
test_player1 = Deck()
test_player2 = Deck()

class Problem2(unittest.TestCase):
    # number of original deck of cards
    def test_original_number(self):
        self.assertEqual(len(test_player1.cards), 52, "Testing whether the number of card in an original deck is 52.")

    # number of the lines of the string method
    def test_lines(self):
        self.assertEqual(test_player1.__str__().count('of'), 52, "Testing whether the number the string method of a original deck is 52.")

    # first value in the given descriptions
    def test_first_deck_value(self):
        self.assertIn("Ace of Diamonds", test_player1.__str__(),"Testing if the first value of card given in the description in this deck.")

    def test_second_deck_value(self):
        self.assertIn("Two of Diamonds", test_player1.__str__(),"Testing if the second value of card given in the description in this deck.")

class Problem3(unittest.TestCase):
    def test_shuffle(self):
        test_player1.shuffle()
        self.assertNotEqual(test_player1.__str__(), test_player2.__str__(), "Test if shuffle works.")


class Problem4(unittest.TestCase):
    def test_pop_normal(self):
        test_player3 = Deck()
        test_player3.pop_card()
        self.assertEqual(len(test_player3.cards), 51, "Test if pop works.")

    def test_pop_empty(self):
        test_player3 = Deck()
        test_player3.deal_hand(53)
        self.assertFalse(test_player3.pop_card())

    def test_replace_card_exist(self):
        test_player3 = Deck()
        test_player3.shuffle()
        pop_item1 = test_player3.pop_card()
        pop_item2 = test_player3.pop_card()
        test_player3.replace_card(pop_item1)
        self.assertEqual(len(test_player3.cards), 51, "Test if replace works if the card is not in.")

    def test_replace_card_notexist(self):
        test_player3 = Deck()
        test_player3.shuffle()
        pop_item1 = test_player3.pop_card()
        test_player1.replace_card(pop_item1)
        self.assertEqual(len(test_player2.cards), 52, "Test if replace works if the card is already in.")

class Problem5(unittest.TestCase):
    def test_deal_hand_normal(self):
        hand = test_player2.deal_hand(5)
        self.assertEqual(len(hand), 5, "Test if deal_hand works for normal situation.")
        self.assertEqual(len(test_player2.cards), 47, "Test if deal_hand works for normal situation.")

    def test_deal_hand_oversize(self):
        test_player2.deal_hand(6)
        test_player2.deal_hand(48)
        self.assertEqual(len(test_player2.cards), 0 ,"Test if deal_hand works for larger hand size than number in cards in deck")

class Problem6(unittest.TestCase):
    def test_sort_full(self):
        test_player1.shuffle()
        test_player1.sort_cards()
        self.assertEqual(test_player1.__str__(), test_player2.__str__(), "Test if sort_card works.")

    def test_sort_card(self):
        test_player1.deal_hand(6)
        test_player2.deal_hand(6)
        test_player1.shuffle()
        test_player1.sort_cards()
        self.assertEqual(test_player1.__str__(), test_player2.__str__(), "Test if sort_card works.")

##########################
#                        #
# Tests of play_war_game #
#                        #
##########################
class Problem7(unittest.TestCase):
    def test_play_war_game(self):
        game_result = play_war_game(True)
        if game_result[1] > game_result[2]:
            self.assertEqual(game_result[0], "Player1", "Test play_war_game")
        elif game_result[1] < game_result[2]:
            self.assertEqual(game_result[0], "Player2", "Test play_war_game")
        else:
            self.assertEqual(game_result[0], "Tie", "Test play_war_game")


if __name__ == "__main__":
    unittest.main(verbosity=2)

