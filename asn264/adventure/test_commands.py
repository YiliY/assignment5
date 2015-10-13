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

#If input not in dict, then yesno_callback is None
    def test_do_commands(self):
        game = Game()
        load_advent_dat(game)
        game.start()

        #Test how 'y' answer is handled
        game.yesno_callback = self.assertTrue
        game.do_command(['y'])

        #Test how 'yes' answer is handled
        game.yesno_callback = self.assertTrue
        game.do_command(['yes'])

        #Test how 'n' answer is handled
        game.yesno_callback = self.assertFalse
        game.do_command(['n'])

        #Test how 'no' answer is handled
        game.yesno_callback = self.assertFalse
        game.do_command(['no'])
    
        #Test how an answer not in YESNO_ANSWERS dictionary like 'xyz' is handled
        game.yesno_callback = self.assertIsNone
        game.do_command(['xyz'])
        
