from unittest import TestCase
from play import load_advent_dat
from game import Game
import unittest
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
            
    def test_check_do_command(self):
        game =Game()
        game.yesno_callback=self.assertTrue         
        game._do_command(['y'])
        game.yesno_callback=self.assertTrue
        game._do_command(['yes'])
        game.yesno_callback=self.assertTrue
        game._do_command(['no'])
        game.yesno_callback=self.assertTrue
        game._do_command(['n'])
        
if __name__ == '__main__':
    unittest.main()   
