#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Wed Feb 12 20:37:40 CST 2020

import sys

from board import Board
from player import Player
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtTest
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
        self.list_of_players = [self.player1, self.player2]
        self.actual_player = 1
        self.actual_symbol = self.player1.get_player_sign()
        self.actual_stylesheet = self.player1.get_player_stylesheet()
        # Create the Qt Application
        app = QApplication([])
        # Create and show the form, and connect buttons to event
        self.board = Board(WIDTH, HEIGHT)
        # Change scoreboard of the actual player to say it is its turn
        # with a green color
        self.scoreboard = self.board.get_scoreboard()
        self.scoreboard[self.actual_player-1].setStyleSheet(
            "font-size: 15px; color: green")

        self.connect_event_to_buttons()
        self.board.show()
        # Convert list of buttons to matrix
        self.convert_button_list_to_matrix()
        # Run the main Qt loop
        sys.exit(app.exec_())

    def connect_event_to_buttons(self):
        self.button_list = self.board.get_buttons()

        for button in self.button_list:
            button.clicked.connect(self.update_button_text)

    def update_button_text(self):
        button = self.board.sender()

        button.setStyleSheet(self.actual_stylesheet)
        button.setText(self.actual_symbol)
        # To update the change of text in the button
        button.repaint()

        button.setDisabled(True)

        self.turn += 1

        self.check_if_player_has_won()
        self.update_actual_player()
        self.check_for_tie()

    def update_actual_player(self):
        if self.turn == 1:
            self.turn *= -1

            self.actual_player = 2
        elif self.turn == 0:
            self.actual_player = 1

        self.scoreboard[self.actual_player-1].setStyleSheet(
            "font-size: 15px; color: green")
        # To change the text of the other player to black we use the if
        self.scoreboard[1 if self.actual_player-1 == 0 else 0].setStyleSheet(
            "font-size: 15px; color: black")

        for i in range(2):
            # To update the change of text in the scoreboard
            self.scoreboard[i].repaint()

        self.actual_symbol = self.list_of_players[self.actual_player -
                                                  1].get_player_sign()
        self.actual_stylesheet = self.list_of_players[self.actual_player -
                                                      1].get_player_stylesheet()

    def check_if_player_has_won(self):
        buttons_horizontal_bool = self.check_buttons_horizontally()
        buttons_diagonal_bool = self.check_buttons_diagonally()
        buttons_vertical_bool = self.check_buttons_vertically()

        if buttons_horizontal_bool or buttons_diagonal_bool or buttons_vertical_bool:
            self.disable_buttons()

            self.update_scoreboard()
            # QtCore.QTimer.singleShot(2000, lambda:num(i))
            QtTest.QTest.qWait(2000)
            self.next_round()

    def check_for_tie(self):
        state = 0

        for row in self.button_list:
            for button in row:
                if button.isEnabled() == False:
                    state += 1

        if state == 9:
            QtTest.QTest.qWait(2000)
            self.next_round()

    def disable_buttons(self):
        for row in self.button_list:
            for button in row:
                button.setDisabled(True)

    def check_buttons_horizontally(self):
        i = 0

        for row in self.button_list:
            for index, button in enumerate(row):
                if button.text() == row[index-1].text() and button.text() != " " and index != 0:
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
                if button.text() == column[index-1].text() and button.text() != " " and index != 0:
                    i += 1

            if i == 2:
                return True
            else:
                i = 0

        return False

    def check_buttons_diagonally(self):
        if self.button_list[0][0] == self.button_list[1][1] and self.button_list[1][1] == self.button_list[2][2]:
            return True
        elif self.button_list[0][2] == self.button_list[1][1] and self.button_list[1][1] == self.button_list[2][0]:
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

    def update_scoreboard(self):
        self.list_of_players[self.actual_player-1].update_score()

        score_of_actual_player = self.board.get_scoreboard()[
            self.actual_player-1]

        score_of_actual_player.setText(
            score_of_actual_player.text()[0:-1] + str(self.list_of_players[self.actual_player-1].get_score()))

    def next_round(self):
        for row in self.button_list:
            for button in row:
                button.setText(" ")
                button.setDisabled(False)


if __name__ == "__main__":
    game = Game()
