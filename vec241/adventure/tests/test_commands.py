# -*-coding:Utf-8 -*

import sys
sys.path.append("/home/ds-ga-1007/Assignments/assignment5/vec241/adventure")

from unittest import TestCase
import play
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

    def test_do_command(self):
        
        possible_answers = ["y", "n", "yes", "no"]
        wrong_answers = ["wrong", "maybe", "later"]
        
        
        for answer in possible_answers:
            
            game = Game()
            load_advent_dat(game)
                     
            # This will test if argument to callback is True
            game.yesno_callback = self.assertTrue
            
            game.start()
            
            # Run the actual test
            game.do_command([answer])
            
        for answer in wrong_answers:
            
            game = Game()
            load_advent_dat(game)
                     
            # This will test if argument to callback is True
            game.yesno_callback = self.assertFalse
            
            game.start()
            
            # Run the actual test
            game.do_command([answer])
            

