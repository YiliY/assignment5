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

    def test_yesno_callback_with_entry_yes_no_invalid(self):
        game = Game()
        load_advent_dat(game)
        game.start()
        
        # to test whether the yesno_callback is True when entry is 'yes' or 'y'
        for yes_entry in ['yes','y']:
            game.yesno_callback = self.assertTrue
            game.do_command([yes_entry])
        
        # to test whether the yesno_callback is False when entry is 'no' or 'n'
        for no_entry in ['no','n']:
            game.yesno_callback = self.assertFalse
            game.do_command([no_entry])

        # to test whether the yesno_callback is None when entry is invalid
        for invalid_entry in ['nossss','yss']:
            game.yesno_callback = self.assertIsNone
            game.do_command([invalid_entry])