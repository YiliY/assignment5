from unittest import TestCase
from play import load_advent_dat
from game import Game

class CommandTest(TestCase):
        
    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')
        self.answers_yes = ('y','yes','Y','Yes','yEs','yeS','YEs','YeS','yES','YES','ye','Ye','yE','YE')
        self.answers_no = ('n','no','N','No','nO','NO')
        self.answers_whether_invalid = ('>',':','$','@!~?',' ')
                
        

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
            
    # Test added based on question 1 of assignment5        
    def test_do_command_is_correct_for_valid_or_invalid_user_yesno_answers(self):
        
        for answer1 in self.answers_yes:
            game = Game()
            load_advent_dat(game)
            game.start()
            # This will test if argument to callback is True
            game.yesno_callback = self.assertTrue      
            # Run the actual test
            game.do_command(answer1)
           
        for answer2 in self.answers_no:
            game = Game()
            load_advent_dat(game)
            game.start()
            # This will test if argument to callback is False
            game.yesno_callback = self.assertFalse     
            # Run the actual test
            game.do_command(answer2)
           
        for answer3 in self.answers_whether_invalid:
            game = Game()
            load_advent_dat(game)
            game.start()
            # This will test if argument to callback is None
            game.yesno_callback = self.assertIsNone 
            # Run the actual test
            game.do_command(answer3)  