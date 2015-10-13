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

    def test_do_command_pass(self):
	    game = Game()
 	    load_advent_dat(game)
	    game.start()
            # This will test if argument to callback is True
            game.yesno_callback = self.assertTrue
 	    # Run the test for the answer 'y'
  	    game.do_command(['y'])
            
            game.yesno_callback = self.assertTrue
            # Run the test for the answer 'yes'
            game.do_command(['yes'])
	
            # This will test if argument to callback is False
            game.yesno_callback = self.assertFalse
            # Run the test for the answer 'n'
            game.do_command(['n'])

            game.yesno_callback = self.assertFalse
            # Run the test for the answer 'no'
            game.do_command(['no'])

            # Run the test for the invalid input, for example 'yyes' 
            game.yesno_callback = self.assertIsNone
            game.do_command(['yyes'])
 
            # Run the test for the invalid input, for example 'nno'
            game.yesno_callback = self.assertIsNone
            game.do_command(['nno'])

if __name__ == '__main__':
    unittest.main()
