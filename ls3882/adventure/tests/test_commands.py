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
    
    def test_valid_and_invalid_yes_no_answers(self):
        game = Game();
        load_advent_dat(game)
        game.start()
              
        #Test all valid 'yes' answers
        #'y'
        game.yesno_callback = self.assertTrue
        game.do_command(['y'])
        #'yes'
        game.yesno_callback = self.assertTrue
        game.do_command(['yes'])
        
        #Test all valid 'no' answers
        #'n'
        game.yesno_callback = self.assertFalse
        game.do_command(['n'])
        #'no'
        game.yesno_callback = self.assertFalse
        game.do_command(['no'])
        
        #Test other invalid answers
        #random word 'ny'
        game.yesno_callback = self.assertIsNotNone
        game.do_command(['ny'])
        #random word 'idk'
        game.yesno_callback = self.assertIsNotNone
        game.do_command(['idk'])

