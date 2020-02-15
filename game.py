#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Wed Feb 12 20:37:40 CST 2020

import sys

from board import Board
from player import Player
from PyQt5.QtWidgets import QApplication


class Game:
    def __init__(self):
        # Define height and width
        WIDTH = 500
        HEIGHT = 500
        # Create players
        self.player1 = Player(u"\u0058", "color: %s; font-size: %s;" % (
            "#ff0000", "80px"))
        self.player2 = Player(u"\u20DD", "color: %s; font-size: %s;" % (
            "#000000", "80px"))

        self.turn = 0
        # Prepare the variable to be used to update the buttons with the symbol # of the actual player and the actual stylesheet
        self.actual_symbol = self.player1.get_player_sign()
        self.actual_stylesheet = self.player1.get_player_stylesheet()
        # Create the Qt Application
        app = QApplication([])
        # Create and show the form, and connect buttons to event
        self.board = Board(WIDTH, HEIGHT)

        self.connect_event_to_buttons()
        self.board.show()
        # Run the main Qt loop
        sys.exit(app.exec_())

    def connect_event_to_buttons(self):
        self.button_list = self.board.get_buttons()

        for button in self.button_list:
            button.clicked.connect(self.update_button_text(button))

    def update_button_text(self, button):
        # We made like this because lambda didnt give th efunction the correct
        # button it always gave it the last button, and why does having two
        # functions work, i dont know
        def button_text():
            button.setStyleSheet(self.actual_stylesheet)
            button.setText(self.actual_symbol)
            button.animateClick(1)
            button.setDisabled(True)

            self.turn += 1
            self.check_if_player_has_won()
            self.update_actual_player()

        return button_text

    def update_actual_player(self):
        if self.turn == 2:
            self.turn *= -1

            self.actual_symbol = self.player2.get_player_sign()
            self.actual_stylesheet = self.player2.get_player_stylesheet()
        if self.turn == 0:
            self.actual_symbol = self.player1.get_player_sign()
            self.actual_stylesheet = self.player1.get_player_stylesheet()

    def check_if_player_has_won(self):
        if self.turn == 2 or self.turn == 0:
            print(self.check_buttons_horizontally())

    def check_buttons_horizontally(self):
        i = 0

        for index, button in enumerate(self.button_list):
            if (index) % 3 != 0:
                if button.text() == self.button_list[index-1].text() and button.text() != "":
                    i += 1

            if (index + 1) % 3 == 0:
                if i == 2:
                    return True
                else:
                    i = 0

                buttons_to_check = []

        return False

    def check_buttons_vertically(self):
        for button in self.button_list:
            pass

    def check_buttons_diagonally(self):
        pass

    def check_if_all_buttons_are_equal(self, list_of_buttons):
        i = 0
        for index, button in enumerate(list_of_buttons):
            if button.text() == list_of_buttons[index-1].text():
                i += 1
                print(button.text())

        if i == 2:
            return True
        else:
            return False


if __name__ == "__main__":
    game = Game()
