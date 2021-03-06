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
    
    def test_yes_no_input_handling(self):
        game = Game()
        load_advent_dat(game)
        
        YESNO_ANSWERS = {'y': True, 'yes': True, 'n': False, 'no': False}
        for input_word in YESNO_ANSWERS.keys():
            build_assert_string = 'assert' + str(YESNO_ANSWERS[input_word])
            game.yesno_callback = getattr(self, build_assert_string)
            game.do_command([input_word])
            
        INVALID_ANSWERS = ['maybe', 'IDK','what would you do?','other!)@#_random_135l_string']
        message_for_invalid_input = 'Please answer the question.'
        expected_output = message_for_invalid_input.upper() + '\n'
        for invalid_input_word in INVALID_ANSWERS:
            game.yesno_callback = getattr(self, 'assertEqual')
            game.do_command([invalid_input_word])
            self.assertEqual(game.output, expected_output)
        