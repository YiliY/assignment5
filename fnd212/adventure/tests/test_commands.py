from unittest import TestCase
from play import load_advent_dat
import game
from game import Game

class CommandTest(TestCase):
    _do_command_testResult = None


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

    def _do_command_testEval(self, callback_argument):
        self._do_command_testResult = callback_argument
        
        

    def setUp_test_do_command(self,testGame):
        self._do_command_testResult = None
        testGame.yesno_callback = self._do_command_testEval
        
    def test_do_command(self):
        # Set up the test case
        testGame = Game()
        load_advent_dat(testGame)
        testGame.start()

        affirmativeAnswers = ['yes','y']
        negativeAnswers = ['no','n']
        #Use as other possible answers all the words in the vocabulary plus
        #some malformed answers.
        otherAnswers = [otherAnswer for otherAnswer 
                        in testGame.vocabulary.keys() 
                        if otherAnswer not in affirmativeAnswers+negativeAnswers ]
        otherAnswers.extend(['asdf','fgjh', ' '])

        for testAnswer in affirmativeAnswers:
            self.setUp_test_do_command(testGame)
            testGame._do_command([testAnswer])
            self.assertTrue(self._do_command_testResult)
        
        for testAnswer in negativeAnswers:    
            self.setUp_test_do_command(testGame)
            testGame._do_command([testAnswer])
            self.assertFalse(self._do_command_testResult)  
        
        for testAnswer in otherAnswers: 
            self.setUp_test_do_command(testGame)
            testGame._do_command([testAnswer])
            self.assertIsNone(self._do_command_testResult)  
        