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
    
    def test_only_allow_valid_responses_to_yesno_questions(self):
        game = Game()
        # Test valid yes/no responses
        valid_yes_responses = ['y', 'yes']
        valid_no_responses = ['n', 'no']
        
        # Test each yes response
        for response in valid_yes_responses:
            # Yes responses should correspond to true
            game.yesno_callback = self.assertTrue
            game.do_command([response])
        
        # Test each no response
        for response in valid_no_responses:
            # No responses should correspond to false
            game.yesno_callback = self.assertFalse
            game.do_command([response])
        
        # Test invalid yes/no responses
        invalid_responses = ['ye', 'yeah', 'Y', 'Yes', 'No', 'nope', 'nah']
        # Create a callback that always raises an exception
        # That way, if do_command recognizes the response as valid,
        # and thus calls the callback, the test will fail
        def raise_exception_callback(yes):
            raise ValueError
        
        for response in invalid_responses:
            game.yesno_callback = raise_exception_callback
            try:
                game.do_command([response])
            except ValueError:
                raise ValueError("'{}' should not be a valid yes/no response".format(response))
        
