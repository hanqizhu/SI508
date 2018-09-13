import unittest
import sys
from SI508_assignment1 import *

class Problem1(unittest.TestCase):
    def test_numchars(self):
        self.assertEqual(num_chars, 348, "Testing the value of num_chars")
    def test_numwords(self):
        self.assertEqual(num_words,57, "Testing the value of num_words")

class Problem2(unittest.TestCase):
    def test_third_elem(self):
        self.assertEqual(third_elem, 25)
    def test_elem_sixth(self):
        self.assertEqual(elem_sixth, 12)
    def test_num_lst_len(self):
        self.assertEqual(num_lst_len,7)
    def test_fifth_type(self):
        self.assertEqual(fifth_type, type(3.0))
    def test_another_type_var(self):
        self.assertEqual(another_type, type("hi"))

class Problem3(unittest.TestCase):
    def test_func_var(self):
        self.assertEqual(func_var, greeting)
    def test_new_digit(self):
        self.assertIsInstance(new_digit, int)
        self.assertTrue(new_digit<10 and new_digit > -1)
    def test_digit_func(self):
        self.assertEqual(digit_func, random_digit)

class Problem4(unittest.TestCase):
    def setUp(self):
        self.f = open('out.txt')
        self.fstr = self.f.read()
    def test_output_p4(self):
        self.assertTrue("""5\n13\n11\n12\n3\n12\n11\n6""" in self.fstr)
    def tearDown(self):
        self.f.close()

class Problem5(unittest.TestCase):
    def test_some_of_list(self):
        self.assertEqual(some_of_list,[4, 6.0, 7.5])

class Problem6(unittest.TestCase):
    def setUp(self):
        self.f = open('out.txt')
        self.fstr = self.f.read()
    def test_output_p6(self):
        self.assertTrue("hello\ngoodbye\nwonderful\nI love Python" in self.fstr)
    def tearDown(self):
        self.f.close()

class Problem7(unittest.TestCase):
    def setUp(self):
        self.f = open('out.txt')
        self.fstr = self.f.read()
    def test_output_p7(self):
        self.assertTrue("hello\nhello!\nhello!!\nhello!!!\nhello!!!!" in self.fstr)
    def tearDown(self):
        self.f.close()

class Problem8(unittest.TestCase):
    def test_exclam_str(self):
        self.assertEqual(exclam_string, "h!i! !e!v!e!r!y!o!n!e!")

class Problem9(unittest.TestCase):
    def setUp(self):
        self.f = open('out.txt')
        self.fstr = self.f.read()
    def test_output_p9(self):
        self.assertTrue("you are awesome" in self.fstr)
    def tearDown(self):
        self.f.close()

class Problem10(unittest.TestCase):
    def test_nums_diction(self):
        res_sample = {"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0}
        self.assertEqual(sorted(nums.items()), sorted(res_sample.items()))

class Problem11(unittest.TestCase):
    def test_acc_num(self):
        self.assertEqual(acc_num, 3, "Testing value of acc_num")

class Problem12(unittest.TestCase):
    def test_subtract_3(self):
        self.assertEqual(subtract_three(3),0)
        self.assertEqual(subtract_three(10),7)
        self.assertEqual(subtract_three(0),-3)
        self.assertEqual(subtract_three(100),97)
        self.assertEqual(subtract_three(-4),-7)

class Problem13(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(add_greeting("SI 506"), None)
        self.assertEqual(add_greeting(""), None)
        self.assertEqual(add_greeting("hey there"), None)

# NOTE: Problem 13 function also results in print output, which will be generated when those run!

class Problem14(unittest.TestCase):
    def test_five_dollar(self):
        self.assertEqual(five_dollar, ['apples','pears', 'lemons'])
    def test_cheap_things(self):
        self.assertEqual(cheap_things, ['paper','thread'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
