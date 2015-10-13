from unittest import TestCase
from play import load_advent_dat
from game import Game

class CommandTest(TestCase):

    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')

    '''
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
    '''        

    # Assignment 5 - Test cases for checking the YES/NO Answers in the game
    def test_yes_answers(self):
        # Checking the 'yes' response
        test_commands_yes = ['', 'y', 'ye', 'yes', 'x', 'n']
        for test_string in test_commands_yes:
            game = Game()
            load_advent_dat(game)
            game.start()
            
            game.yesno_callback = self.assertTrue
            
            game.do_command([test_string])
            
    def test_no_answers(self):    
        # Checking the 'no' response
        test_commands_no = ['', 'n', 'no', 'p']
        for test_string in test_commands_no:
            game = Game()
            load_advent_dat(game)
            game.start()
            
            game.yesno_callback = self.assertFalse
            
            game.do_command([test_string])
