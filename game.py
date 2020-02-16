#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Wed Feb 12 20:37:40 CST 2020

import sys

from board import Board
from player import Player
from PyQt5.QtWidgets import QApplication
from numpy import transpose


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
        # Convert list of buttons to matrix
        self.convert_button_list_to_matrix()
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
            # print(self.check_buttons_horizontally())
            # print(self.check_buttons_vertically())
            print(self.check_buttons_diagonally())

    def check_buttons_horizontally(self):
        i = 0

        for row in self.button_list:
            for index, button in enumerate(row):
                if button.text() == row[index-1].text() and button.text() != "" and index != 0:
                    i += 1

            if i == 2:
                return True
            else:
                i = 0

        return False

    def check_buttons_vertically(self):
        i = 0

        transpose_matrix = transpose(self.button_list)
        for column in transpose_matrix:
            for index, button in enumerate(column):
                if button.text() == column[index-1].text() and button.text() != "" and index != 0:
                    i += 1

            if i == 2:
                return True
            else:
                i = 0

        return False

    def check_buttons_diagonally(self):
        i_diagonal_1 = 0
        i_diagonal_2 = 0

        index1 = 0
        index2 = 2
        previous_button_text = ""

        for row in self.button_list:
            if row[index1].text() == previous_button_text and row[index1].text() != "":
                i_diagonal_1 += 1

            previous_button_text = row[index1].text()

            index1 += 1

        for row in self.button_list:
            if row[index2].text() == previous_button_text and row[index2].text() != "":
                i_diagonal_2 += 1

            previous_button_text = row[index2].text()

            index2 -= 1

        if i_diagonal_1 == 2 or i_diagonal_2 == 2:
            return True
        else:
            return False

    def convert_button_list_to_matrix(self):
        matrix = []
        lista = []

        for index, button in enumerate(self.button_list):
            lista.append(button)
            if (index + 1) % 3 == 0:
                matrix.append(lista)
                lista = []

        self.button_list = matrix


if __name__ == "__main__":
    game = Game()
