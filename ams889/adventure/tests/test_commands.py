from unittest import TestCase
from play import load_advent_dat
from game import Game
import unittest

class CommandTest(TestCase):

    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')

    def test_intransitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command([word])

    def test_transitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command(['enter'])  # so we are next to lamp
            game.do_command([word, 'lamp'])
            
    def test_do_command_valid(self):
        #initializes game
        game = Game()
        load_advent_dat(game)
        game.start()
        #setting up test for do_command
        validWordList = ['y', 'yes', 'n', 'no']
        posWordList = validWordList[:2]#build two word lists, one true and one false
        negWordList =validWordList[2:]
        for words in posWordList:
            game.yesno_callback=self.assertTrue
            game.do_command([words])
        for words in negWordList:
            game.yesno_callback=self.assertFalse
            game.do_command([words])
        invalidWordList = ['kind of', 'perhaps', 'definitely']
        for words in invalidWordList:
            game.yesno_callback=self.assertIsNotNone
            game.do_command([words]) 

if __name__ == '__main__':
   log_file = 'test_output2.txt'
   f = open(log_file, "w")
   runner = unittest.TextTestRunner(f)
   unittest.main(testRunner=runner)
   f.close()