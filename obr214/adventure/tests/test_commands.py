import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from unittest import TestCase
from game import Game
from play import load_advent_dat

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

    def test_valid_yes_commands_should_return_true(self):
        valid_yes_words = ['yes', 'y']
        for word in valid_yes_words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertTrue
            game.do_command([word])

    def test_valid_no_commands_should_return_false(self):
        valid_no_words = ['no', 'n']
        for word in valid_no_words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertFalse
            game.do_command([word])

    def test_invalid_commands_should_not_throw_exceptions(self):
        invalid_words = ['maybe', 'perhaps', 'dunno']
        for word in invalid_words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertIsNone
            game.do_command([word])



