#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Wed Feb 12 20:37:56 CST 2020


class Player:
    def __init__(self, player_sign, stylesheet):
        self.player_sign = player_sign
        self.player_stylesheet = stylesheet
        self.player_score = 0

    def update_score(self):
        self.player_score += 1

    def get_player_sign(self):
        return self.player_sign

    def get_player_stylesheet(self):
        return self.player_stylesheet
