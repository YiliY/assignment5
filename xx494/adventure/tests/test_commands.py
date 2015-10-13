import unittest
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
    def test_do_command(self):
        with open('test_output2.txt', 'w') as text_file:
            yes_no_options = ["y","yes","no","n"]
            for word in yes_no_options:
                #Game initialization
                game = Game()
                load_advent_dat(game)
                game.start()
                #No response
                if word in ["no", "n"]:
                    game.yesno_callback = self.assertFalse
                    text_file.write("Output for {0}: {1}\n".format(word, False))
                    game.do_command([word]) 
                elif word in ["y", "yes", "yessir", "yes please"]:
                    game.yesno_callback = self.assertTrue
                    text_file.write("Output for {0}: {1}\n".format(word, True))
                    game.do_command([word])
            
            invalidWordList = ['stop', 'maybe', 'actually']
            for words in invalidWordList:
                game.yesno_callback=self.assertIsNotNone
                #gtext_file.write("Output for {0}: {1}\n".format(word, True))
                value=str(game.do_command([words]))
                text_file.write("Output for {0}: {1}\n".format(words,value))
if __name__ =='__main__':  
   unittest.main()