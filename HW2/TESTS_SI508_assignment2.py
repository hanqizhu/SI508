import unittest
import sys
import SI508_assignment2
from SI508_assignment2 import *

# NOTE: Problem 0 graded based on comments describing understanding of ord and chr functions.

class Problem1(unittest.TestCase):
    # return type bool
    def test_return_type(self):
        self.assertIsInstance(check_valid_input("h"), bool, "Testing return type is boolean")
    # length 0 - False
    def test_empty_string(self):
        self.assertEqual(check_valid_input(""),False,"Testing check_valid_input returns False for empty string")
    # length 1 - True
    def test_correct_length(self):
        self.assertEqual(check_valid_input("a"), True, "Testing check_valid_input returns True for input with length of one")
    # length 2 - False
    def test_longer_length(self):
        self.assertEqual(check_valid_input("UM"), False, "Testing check_valid_input returns False for input with length of two")

class Problem2(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(SystemExit):
            crypt_char("",2) # Testing that function exits if input string not valid
    def test_not_valid_input(self):
        with self.assertRaises(SystemExit):
            crypt_char("um",3) # Testing that function exits if input string not valid
    def test_return_type(self):
        self.assertTrue(type(crypt_char("a",6)) is str, "Testing return type is a string")
    # return type string - input digit, assertEqual
    def test_digit_input(self):
        self.assertEqual(crypt_char("3",3), "3", "Testing digit imput returns a string digit")
    # return type string - input space, assertEqual
    def test_space_input(self):
        self.assertEqual(crypt_char(" ",1), " ", "Testing space input returns a string space")
    # check A,3 - Dy
    def test_A_3(self):
        self.assertEqual(crypt_char("a",3), "D", "Testing with input (a,3) returns D")
    # check Z,2 - B
    def test_Z_2(self):
        self.assertEqual(crypt_char("z",2), "B", "Testing with input (z,2) returns B")

class Problem3(unittest.TestCase):
    # check return type string
    def test_return_type(self):
        self.assertIsInstance(encrypt_message("hello, world!",3),str, "Testing return type of encrypt_message is a string")
    # check default False
    def test_default_false(self):
        self.assertEqual(encrypt_message("hello, world!",3), "KHOOR, ZRUOG!", "Testing length of returned string same length as original string")
    # check "hello, world" - decrypt=True
    def test_decrypt_true(self):
        self.assertEqual(encrypt_message("KHOOR, ZRUOG!",3,decrypt=True), "HELLO, WORLD!", "Testing decryption when decrypt=True")

class Problem4(unittest.TestCase):
    # return type
    def test_return_type(self):
        self.assertIsInstance(brute_force_caesar("KHOOR, ... ZRUOG! DQG VL 506!"), list, "Testing return type of brute_force_caesar is a list")
    # return type length - 26
    def test_return_length(self):
        self.assertEqual(len(brute_force_caesar("Hello, world!")), 26, "Testing brute_force_caesar returns a list of length 26")
    # return type of list items - strings
    def test_return_type_items(self):
        self.assertIsInstance(brute_force_caesar("KHOOR, ... ZRUOG! DQG VL 506!")[0],str, "Testing type of return list items is string")

class Problem5(unittest.TestCase):
    def setUp(self):
        self.f = open('out.txt')
        self.fstr = self.f.read()
    def test_output(self):
        ## Testing the display_decryptions line in the HW.
        self.assertIn("Message possibilities are as follows:\n- BUUBDL BU PODF\n- ATTACK AT ONCE\n- ZSSZBJ ZS NMBD\n- YRRYAI YR MLAC",self.fstr,"Testing that the correct display_decryptions output occurs in one case")
        self.assertEqual(self.fstr.strip().rstrip()[-1],"L","Testing the last visible letter of the output of the second example invocation to display_decryptions")
    def tearDown(self):
        self.f.close()
    # Note that you should ensure that


class Problem6(unittest.TestCase):
    # return type list
    def test_return_type(self):
        self.assertTrue(type(small_list([1,4,6,8,2])) is list, "Testing return type of small_list is a list")
    # return list item types - integers
    def test_return_type(self):
        self.assertTrue(type(small_list([6,3,7,3])[0]) is int, "Testing return type list items is type integer")
    # test empty list return type
    def test_empty_list(self):
        self.assertEqual(small_list([]), [], "Testing small_list returns an empty list for an empty list as imput")
    # check all greater than 5 - (6, 7, 13, 10)
    def test_all_greater(self):
        self.assertEqual(small_list([6,7,13,10]), [6,7,13,10], "Testing small_list with values all greater than 5")
    # check none greater than 5 - (1, 2, 4, 0)
    def test_none_greater(self):
        self.assertEqual(small_list([1,3,4,2]), [], "Testing small_list returns an empty list if all values are smaller than 5")
    # check only one greater than 5
    def test_only_one(self):
        self.assertEqual(small_list([6,4,3,0]), [6], "Testing only one value greater than 5")

class Problem7(unittest.TestCase):
    # check default return list length 4
    def test_default_length(self):
        self.assertEqual(small_list_amount([5,6,7,4,10,3,8]), [6,7,10,8], "Testing the default return length is 4")
    # check return list same length of lst_limit
    def test_return_length(self):
        self.assertEqual(small_list_amount([3,5,7,8,9,2,4,10,12],3), [7,8,9], "Testing return list is same length as lst_limit")
    # check none above 5 - returns empty list
    def test_none_greater(self):
        self.assertEqual(small_list_amount([2,3,1,1,2,4],2), [], "Testing small_list_amount returns an empty list if all values smaller than 5")
    # lst_limit = 0
    def test_lst_limit_0(self):
        self.assertEqual(small_list_amount([6,8,2,4,1],0), [], "Testing small_list_amount returns an empty list if lst_limit is 0")
    # lst_limit longer than length of list, return list long as og list
    def test_long_lst_limit(self):
        self.assertEqual(small_list_amount([8,7,9,10,6,7],8), [8,7,9,10,6,7], "Testing if lst_limit is longer than original list")


if __name__ == "__main__":
    unittest.main(verbosity=2)
