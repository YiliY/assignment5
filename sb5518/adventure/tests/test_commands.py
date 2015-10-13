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
            
    def test_do_command_yes_no_check(self):
        
        YES_VALID_OPTIONS = ['y', 'yes']
        NO_VALID_OPTIONS = ['n', 'no']
        POSSIBLE_INVALID_OPTIONS = ['ye', 'YES', 'YESE', 'YEAH', 'yese', 'NO', 'maybe', '', '$*^%^&+++']
        
        for possible_answer in YES_VALID_OPTIONS:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertTrue
            game._do_command([possible_answer])
            
        for possible_answer in NO_VALID_OPTIONS:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertFalse
            game._do_command([possible_answer])
            
        for possible_answer in POSSIBLE_INVALID_OPTIONS:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertIsNone
            game._do_command([possible_answer])