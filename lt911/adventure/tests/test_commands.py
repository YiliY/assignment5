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

    def test_yes_no_answers(self):
        '''This is an added test to check valid yes/ no answers for the the Game class'''
        for word in self.words:
            YESNO_RESPONSE = ['y','yes','n','no','what']
            output = open('output2.txt', 'w')
            for ans in YESNO_RESPONSE:
                game = Game()
                load_advent_dat(game)
                game.start()
                if ans[0] == 'y':
                    output_string = ans + " is true \n" 
                    output.write(output_string)
                    game.yesno_callback = self.assertTrue
                    game.do_command([ans])

                elif ans[0] == 'n':
                    output_string = ans + " is false \n" 
                    output.write(output_string)
                    game.yesno_callback = self.assertFalse
                    game.do_command([ans])

                else:
                    output_string = ans + "\n"
                    output.write(output_string)
                    do_command_output = game.do_command([ans])
                    output.write(do_command_output)


if __name__ == '__main__':
    unittest.main()
