#!/usr/bin/env python3
# Developer: Wilbert (wilbert.phen@gmail.com)

import os
from ckiptagger import WS, POS, NER

ws = WS(os.path.join(os.path.dirname(__file__), 'data/'))
pos = POS(os.path.join(os.path.dirname(__file__), 'data/'))
ner = NER(os.path.join(os.path.dirname(__file__), 'data/'))

class Segment:
    def __init__(self):
        '''
        Initialize the class with the segmenter object
        '''
        self.ws = ws
        self.pos = pos
        self.ner = ner
        self.__reset_flag__()

    def __call__(self, sentence_list, ws=True, pos=True, ner=True):
        '''
        Entry point to get the result.
        ws is needed to process pos and ner.
        pos is needed to process ner.
        Therefore, the needed parts need to be on when being called
        Output:
            Dictionary with key 'ws', 'pos', 'ner' if corresponding flag is True
        '''
        self.__reset_flag__()
        if ws:
            word_s = self.ws(sentence_list, sentence_segmentation=True, 
            segment_delimiter_set={'?', '？', '!', '！', '。', ',', '，', ';', ':', '、'})
            if pos:
                word_p = self.pos(word_s)
                if ner:
                    word_n = self.ner(word_s, word_p)
            else:
                if ner:
                    raise ValueError('ner flag is True but pos is False when calling Segment class')
        else:
            if pos:
                raise ValueError('pos flag is True but ws is False when calling Segment class')
            if ner:
                raise ValueError('ner flag is True but ws is False when calling Segment class')
        
        results = {}
        if 'word_s' in locals():
            self.ws_flag = True
            results['ws'] = word_s
        if 'word_p' in locals():
            self.pos_flag = True
            results['pos'] = word_p
        if 'word_n' in locals():
            self.ner_flag = True
            results['ner'] = word_n
        return results

    def __repr__(self):
        pass

    def __reset_flag__(self):
        self.ws_flag = False
        self.pos_flag = False
        self.ner_flag = False

