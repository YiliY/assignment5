from unittest import TestCase
from play import load_advent_dat
import game
from game import Game

class CommandTest(TestCase):
    _do_command_testResult = None
#    def setUp(self):
#        game = Game()
#        load_advent_dat(game)
#        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
#        self.words.remove('suspend')
#
#    def test_intransitive_commands_should_not_throw_exceptions(self):
#        for word in self.words:
#            game = Game()
#            load_advent_dat(game)
#            game.start()
#            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
#            game.do_command([word])
#
#    def test_transitive_commands_should_not_throw_exceptions(self):
#        for word in self.words:
#            game = Game()
#            load_advent_dat(game)
#            game.start()
#            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
#            game.do_command(['enter'])  # so we are next to lamp
#            game.do_command([word, 'lamp'])

    def _do_command_testEval(self, callback_argument):
        self._do_command_testResult = callback_argument
        
        

    def test_do_command(self):

        possitive_answers = ['y','yes']

        testGame = Game()
        load_advent_dat(testGame)
        testGame.start()


        affirmativeAnswers = [ affirmativeAnswer for affirmativeAnswer
                            in game.YESNO_ANSWERS.keys() 
                            if game.YESNO_ANSWERS[affirmativeAnswer] == True]

        
        negativeAnswers = [ negativeAnswer for negativeAnswer
            in game.YESNO_ANSWERS.keys() 
            if game.YESNO_ANSWERS[negativeAnswer] == False]


        otherAnswers = [otherAnswer for otherAnswer 
                        in testGame.vocabulary.keys() 
                        if otherAnswer not in game.YESNO_ANSWERS.keys() ]
        

        for testAnswer in affirmativeAnswers:
            self._do_command_testResult = None
            testGame.yesno_callback = self._do_command_testEval
            testGame._do_command([testAnswer])
            self.assertTrue(self._do_command_testResult)
        
        for testAnswer in negativeAnswers:    
            self._do_command_testResult = None
            testGame.yesno_callback = self._do_command_testEval
            testGame._do_command([testAnswer])
            self.assertFalse(self._do_command_testResult)  

        for testAnswer in otherAnswers: 
            self._do_command_testResult = None               
            testGame.yesno_callback = self._do_command_testEval
            testGame._do_command([testAnswer])
            self.assertIsNone(self._do_command_testResult)  