# coding: utf-8

"""
Class inheriting from the mainframe class
for displaying menu
"""


import tkinter as tk

from .mainframe import MainFrame


class MenuFrame(MainFrame):
    """
    Child Class representing the frame menu
    """

    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        """
        Displays all widgets in the frame
        """
        self.button1 = tk.Button(
            self.root,
            text="Quel aliment " +
            "souhaitez-vous remplacer ?",
            width=35,
            command=lambda: self.display_frame_content(1)
        )
        self.button2 = tk.Button(
            self.root,
            text="Retrouver mes aliments substitués.",
            width=35,
            command=lambda: self.display_frame_content(2)
        )
        self.button3 = tk.Button(
            self.root, text="Quitter",
            command=self.master.destroy
        )
        # displays buttons
        self.button1.pack(padx=5, pady=8)
        self.button2.pack(padx=5, pady=8)
        self.button3.pack(padx=5, pady=8)

    def display_frame_content(self, content):
        """
        Displays categories or favorites
        depending on the menu choice.
        Updates the root.status (use in main)
        """
        self.root.status = content

        # categories
        if content == 1:
            self.root.display_frame(self.root.frame_categories)
        # favorites
        else:
            self.root.display_frame(self.root.frame_favorites)
