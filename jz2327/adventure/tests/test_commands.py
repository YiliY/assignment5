import unittest
from unittest import TestCase
from play import load_advent_dat
from game import Game
import sys

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

    def test_do_command_yesno_callback_y(self):
        # Test _do_command when command is y, the yesno_callback is True.
        game = Game()
        load_advent_dat(game)
        game.start()
        # This will test if argument to callback is True.
        game.yesno_callback = self.assertTrue
        # Run the actual test
        game.do_command(['y'])

    def test_do_command_yesno_callback_yes(self):
        # Test _do_command when command is yes, the yesno_callback is True.
        game = Game()
        load_advent_dat(game)
        game.start()
        # This will test if argument to callback is True.
        game.yesno_callback = self.assertTrue
        # Run the actual test
        game.do_command(['yes'])

    def test_do_command_yesno_callback_n(self):
        # Test _do_command when command is n, the yesno_callback is False.
        game = Game()
        load_advent_dat(game)
        game.start()
        # This will test if argument to callback is False.
        game.yesno_callback = self.assertFalse
        # Run the actual test
        game.do_command(['n'])
 
    def test_do_command_yesno_callback_no(self):
        # Test _do_command when command is no, the yesno_callback is False.
        game = Game()
        load_advent_dat(game)
        game.start()
        # This will test if argument to callback is False.
        game.yesno_callback = self.assertFalse
        # Run the actual test
        game.do_command(['no'])

    def test_do_command_yesno_callback_invalid_words(self):
        # Test _do_command when command is invalid words, the yesno_callback is None.
        game = Game()
        load_advent_dat(game)
        game.start()
        # This will test if argument to callback is None.
        self.assertTrue(game.yesno_callback, None)
        # Run the actual test
        game.do_command(['invalidwords'])

def output_to_file(out=sys.stderr, verbosity=2):
    # output test result to a file
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out,verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testresult2.txt','w') as f:
        output_to_file(f)
