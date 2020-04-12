#!/usr/bin/env python3
# Developer: Wilbert (wilbert.phen@gmail.com)

from text.segment import Segment
from bot.ask import Ask

class Bot:
    def __init__(self):
        '''
        Initialize the class with needed data
        '''
        self._question = ''
        self._segmented = ''
        self._answer = ''

    def __call__(self, question, lang='zh-tw'):
        '''
        Entry point to get the result
        question is a string of question
        lang is default language, set to traditional chinese
        '''

        # Currently could only supports Traditional Chinese question
        self._question = question
        segmenter = Segment()
        self._segmented = segmenter([question])[0]
        self._answer = Ask(self._segmented)
        return self._answer

    def __repr__(self):
        return str(
            {
                'question': self._question,
                'answer': self._answer
            })