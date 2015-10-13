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
    
    def test_all_yes_commands(self):
        yes_commands = ['','y','yes','ye','yessss']
        for affirmative_string in yes_commands:
            game = Game()
            load_advent_dat(game)
            game.start()
            # This will test if argument to callback is True
            game._do_command([affirmative_string])  # WOULD YOU LIKE INSTRUCTIONS?
            # Run the actual test
            game.yesno_callbakc = self.assertTrue
            
            
    def test_all_no_commands(self):
        no_commands = ['','n','no','nn','nooooo']
        for negative_string in no_commands:
            game = Game()
            load_advent_dat(game)
            game.start()
            # This will test if argument to callback is True
            game._do_command([negative_string])  # WOULD YOU LIKE INSTRUCTIONS?
            # Run the actual test
            game.yesno_callbakc = self.assertTrue

            
            
    

    def test_transitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command(['enter'])  # so we are next to lamp
            game.do_command([word, 'lamp'])
