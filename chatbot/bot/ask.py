#!/usr/bin/env python3
# Developer: Wilbert (wilbert.phen@gmail.com)

from label.similarity import score
from db.query import _queryCourseData

class Ask:
    def __init__(self):
        '''
        Initialize the class with needed data
        '''
        self._answer_list = [] # Implemented later

    def __call__(self, question):
        '''
        Input argument is segmented question
        Return string of answer to the caller
        '''
        scores_list = [score(question, answer_candidate) for answer_candidate in self._answer_list]
        topcandidate = self._matchAnswerCandidate(scores_list)
        requirements = self._checkAnswerRequirements(topcandidate)
        answer = self._fillAnswerCandidate(topcandidate, requirements)
        return answer

    def _matchAnswerCandidate(self, scores_list):
        '''
        Input is similarity scores with answer list
        Return the template for answer
        '''
        topcandidate_index = scores_list.index(max(scores_list))
        topcandidate = self._answer_list[topcandidate_index]
        return topcandidate

    def _checkAnswerRequirements(self, ans_candidate):
        '''
        Input is template for the top answer candidate
        Return the information needed to fill the answer
        '''
        pass

    def _fillAnswerCandidate(self, ans_candidate, requirements):
        '''
        Input is template for the top answer candidate and requirements to fill the blank
        This function will match the the appropriate action with the requirements
        # Currently could only match into CourseDataQuery
        Return the answer after processing
        '''
        _queryCourseData(ans_candidate, requirements)
        # Fill in the blank action
