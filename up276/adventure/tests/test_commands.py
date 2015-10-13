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
            
    def test_do_command_method_for_yesno_answers(self):
        
            game = Game()                          # Instance creation for the Game() class   
            load_advent_dat(game)
            game.start()
            game.yesno_callback = self.assertTrue  # This will test if argument to callback is True
            game.do_command(['y'])                 # 'y' is passed to 'do_command' method - To test the 'y' case 
            game.yesno_callback = self.assertTrue  # This will test if argument to callback is True
            game.do_command(['yes'])               # 'yes' is passed to 'do_command' method - To test the 'yes' case
            game.yesno_callback = self.assertFalse # This will test if argument to callback is False
            game.do_command(['n'])                 # 'n' is passed to 'do_command' method - To test the 'n' case
            game.yesno_callback = self.assertFalse # This will test if argument to callback is False
            game.do_command(['no'])                # 'no' is passed to 'do_command' method - To test the 'no' case
