import unittest
from translator import english_to_french, french_to_english


class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 
        self.assertNotEqual(french_to_english("Bonjour"), "Hola") 
        self.assertEqual(french_to_english(""), "") 

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_to_french("Hello"), "Hola") 
        self.assertEqual(english_to_french(""), "")
        
unittest.main()