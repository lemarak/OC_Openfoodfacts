# coding: utf-8

import tkinter as tk

from .mainframe import MainFrame


class CategoriesFrame(MainFrame):
    """
    Child Class to implement the categories window
    """

    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.config(pady="30")

    def display(self, categories):
        """
        Displays widgets in the frame
        """
        self.frame_title(
            "********** Catégories **********",
            "Cliquer sur une catégorie pour afficher ses produits"
        )

        number = 1
        for category in categories:
            category_text = "{} - {} ".format(number, category.name)
            label_category = tk.Label(
                self,
                fg="Blue",
                text=category_text)
            id_category = category.id_category
            label_category.bind(
                '<Button-1>', lambda event,
                id=id_category: self.bind_categories(id))
            label_category.pack()
            number += 1
        self.focus_set()

    def bind_categories(self, id_categorie=None):
        """
        update id_category of root when event click on the categories frame
        """
        self.root.category = id_categorie
