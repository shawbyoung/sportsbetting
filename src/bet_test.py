from Bet import *
import unittest

class TestBet(unittest.TestCase):

    def test_equals(self):
        a = Bet('apple','banana',0,0,"")
        b = Bet('banana','apple',0,0,"")
        huh = Bet('bob','',0,0,"")
        print(a.getSides())
        self.assertTrue(a.sameGame(b),str(huh.getSides()) + str(b.getSides()))
        self.assertTrue(b.sameGame(a), b.getSides())
        self.assertTrue(b.sameGame(a), str(huh.getSides()) + str(b.getSides()))
        self.assertFalse(b.sameGame(huh), str(huh.getSides()) + str(b.getSides()))

    
if __name__ == '__main__':
    unittest.main()