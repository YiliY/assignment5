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
            
    # Test that the portion of Game class' do_command() method that evaluates yes and no inputs 
    # is correct.
    def test_do_command_checks_yesno_inputs_correctly(self):
        # Valid yes and no inputs, as specified in the Game class.
        VALID_YES_ANSWERS = ['y', 'yes']
        VALID_NO_ANSWERS = ['n', 'no']
        
        # Test a variety of possible answers that the user may input, including
        # valid yes answers, valid no answers, and invalid answers.
        possible_answers = ['y', 'yes', 'n', 'no', 'typo', 'sure why not', 'okay', '129jio43w2']
        
        for answer in possible_answers:
            # Initialize game
            game = Game()
            load_advent_dat(game)
            game.start()
            
            isinvalidword = False                   # Keeps track of whether the answer is invalid
            
            # The test for a valid yes answer.
            if answer in VALID_YES_ANSWERS:
                game.yesno_callback = self.assertTrue
                print "For the valid input answer '%s', TestCase assertTrue function succeeded." % answer
            # The test for a valid no answer.
            elif answer in VALID_NO_ANSWERS:
                game.yesno_callback = self.assertFalse
                print "For the valid input answer '%s', TestCase assertFalse function succeeded." % answer 
            # Else the answer is invalid.
            else:
                isinvalidword = True
                
            game.do_command([answer])
            
            # The test for an invalid answer.
            if isinvalidword:
                expected_output = 'PLEASE ANSWER THE QUESTION.\n'
                self.assertEqual(game.output, expected_output)
                print "For the invalid input answer '%s', TestCase assertEqual function succeeded." % answer