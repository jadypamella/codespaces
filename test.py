import unittest

def friends_in_trouble(j_angry, s_angry):
    if (j_angry == True) and (s_angry == True):
        return True
    else: 
        return False
        
print(friends_in_trouble(5, 10))


class TestFriendsInTrouble(unittest.TestCase):
    def test_both_angry(self):
        self.assertTrue(friends_in_trouble(True, True))
    
    def test_one_angry(self):
        self.assertFalse(friends_in_trouble(True, False))
        self.assertFalse(friends_in_trouble(False, True))
    
    def test_neither_angry(self):
        self.assertFalse(friends_in_trouble(False, False))
        
if __name__ == '__main__':
    unittest.main()