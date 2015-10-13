import sys
sys.path.append("/home/ds-ga-1007/Desktop/workspace/assignment5/mch529/adventure")
from unittest import TestCase
from play import load_advent_dat
from game import Game

class CommandTest(TestCase):

    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')

    def test_yesno_list_in_do_commands(self):
	acceptable_yesno_words=["yes","no","y","n","ye"]
	bad_yesno_words = ["nope","noooooo","nooo","!@$%^&*", "hell no", "for sure"]
	
	for word in acceptable_yesno_words:
	    game=Game()
	    load_advent_dat(game)
            game.yesno_callback = self.assertFalse
	    game.start()
	    game.do_command([word])

        for word in bad_yesno_words:
            game=Game()
            load_advent_dat(game)
            game.yesno_callback = self.assertTrue
            game.start()
            game.do_command([word])
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
