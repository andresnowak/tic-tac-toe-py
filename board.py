#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Wed Feb 12 20:37:27 CST 2020

import sys

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGroupBox, QLabel, QDialog, QLineEdit, QSizePolicy
from PyQt5 import QtCore


class Board(QDialog):
    def __init__(self, width, height, parent=None):
        super(Board, self).__init__(parent)

        self.resize(width, height)
        # Setup the ui for the game
        self.setupUi()

    def setupUi(self):
        # Create layout
        layout = QGridLayout()
        # Create scoreboard and game layout
        scoreboard = QGridLayout()
        game_layout = QGridLayout()
        # Add scoreboard and game to principal layout
        layout.addLayout(scoreboard, 1, 1, 1, 3)
        layout.addLayout(game_layout, 2, 1, 1, 3)
        # Create buttons
        self.__create_buttons(game_layout)
        # Create scoreboard
        self.__create_scoreboard(scoreboard)
        # Set dialog layout
        self.setLayout(layout)

    def __create_buttons(self, layout):
        self.buttons_list = []

        for i in range(3):
            for j in range(3):
                button = QPushButton(" ", self)

                button.setSizePolicy(
                    QSizePolicy.Preferred,
                    QSizePolicy.Expanding)
                # We put the focus policy so that the firs button created
                # Isnt put with a different color than the others
                button.setFocusPolicy(QtCore.Qt.NoFocus)
                button.setStyleSheet("color: %s" % "#000000")

                layout.addWidget(button, i, j)

                self.buttons_list.append(button)

    def __create_scoreboard(self, layout):
        self.player1 = QLabel("player " + u"\u0058" + ": 0")
        self.player2 = QLabel("player " + u"\u20DD" + ": 0")
        self.player1.setStyleSheet("font-size: 15px")
        self.player2.setStyleSheet("font-size: 15px")

        layout.addWidget(self.player1, 1, 1)
        layout.addWidget(self.player2, 1, 3)

    def get_buttons(self):
        return self.buttons_list

    def get_scoreboard(self):
        return self.player1, self.player2


# test the ui
if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication([])
    # Create and show the form
    board = Board(500, 500)
    board.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
