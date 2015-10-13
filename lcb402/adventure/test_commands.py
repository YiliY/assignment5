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


# start of lcb402 work
    def test_yes_no_do_command(self):
	for word in self.words:
	    game = Game()
	    load_advent_dat(game)
	    game.start()
	    # This will test if argument to callback is True
	    try:
	    	game.yesno_callback = self.assertTrue
	    	# Run the actual test
            	game.do_command(['y'])
	    	# Repeat for other cases ...
	    	game.yesno_callback = self.assertTrue
           	game.do_command(['yes'])
	    	game.yesno_callback = self.assertFalse
	    	game.do_command(['n'])
	    	game.yesno_callback = self.assertFalse
	    	game.do_command(['no'])
	    except ValueError:
		file=open("test_output1.txt","w")
		file.write("Error in Yes/No entry\n")
