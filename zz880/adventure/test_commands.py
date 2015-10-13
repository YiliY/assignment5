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

    def test_yes_no(self):
        game = Game()
        load_advent_dat(game)
        game.start()
        # test if callback is true when input is 'y' or 'yes'
        game.yesno_callback = self.assertTrue
        game.do_command(['y'])
        game.yesno_callback = self.assertTrue
        game.do_command(['yes'])
        
        # test if callback is false when input is 'n' or 'no'
        game.yesno_callback = self.assertFalse
        game.do_command(['n'])
        game.yesno_callback = self.assertFalse
        game.do_command(['no'])
        
        # test if callback is none when input is invalid words like 'what', 'not sure'
        game.yesno_callback = self.assertIsNone
        game.do_command(['what'])
        game.yesno_callback = self.assertIsNone
        game.do_command(['not sure'])
        
if __name__ == '__main__':
    unittest.main()
