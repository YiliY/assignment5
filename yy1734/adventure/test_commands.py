import unittest
from unittest import TestCase
from play import load_advent_dat
from game import Game

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
            
# Assignment 5 - 1
    def test_do_commands(sefl):
        game = Game()
        load_advent_dat(game)
        game.start()
        
        game.yesno_callback = self.assertTrue
        game.do_command(['y'])
        
        game.yesno_callback = self.assertTrue
        game.do_command(['n'])
        
        game.yesno_callback = self.assertTrue
        game.do_command(['yes'])
        
        game.yesno_callback = self.assertTrue
        game.do_command(['no'])
        
        game.yesno_callback = self.assertTrue
        game.do_command(['abc'])
        
if __name__ == '__main__':
    unittest.main()