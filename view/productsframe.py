# coding: utf-8

"""
Class inheriting from the mainframe class
for displaying products
"""

import tkinter as tk

from .mainframe import MainFrame


class ProductsFrame(MainFrame):
    """
    Child Class to implement the products,
    favorites and substitutes windows
    """

    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.config(pady="30")

    def refresh_favorites(self, favorites):
        """
        refresh the favorites frame
        called in main
        """
        self.clear_frame()

        self.frame_title("********** Favoris **********", "")

        if favorites:
            number = 1
            for favorite in favorites:
                product = favorite.product
                label_favorite = tk.Label(
                    self,
                    text=product.__str__())
                label_favorite.pack()
                number += 1
        else:
            label_favorite = tk.Label(
                self,
                text="Pas de favoris !")
            label_favorite.pack()

    def refresh_products(self, products):
        """
        refresh the products frame
        called in main
        """
        self.clear_frame()

        self.frame_title(
            "********** Produits **********",
            "Cliquer sur un produit pour afficher ses substituts"
        )

        if products:
            number = 1
            for product in products:
                product_text = "{} - {} ({})".format(number,
                                                     product.name,
                                                     product.brands)
                label_product = tk.Label(
                    self,
                    fg="Blue",
                    text=product_text)
                label_product.bind(
                    '<Button-1>', lambda event,
                    arg=product: self.bind_product(arg, True))
                label_product.pack()
                number += 1
        else:
            label_product = tk.Label(
                self,
                text="Pas de produits !")
            label_product.pack()

    def refresh_substitutes(self, substitutes):
        """
        refresh the substitutes frame
        called in main
        """
        self.clear_frame()

        self.frame_title(
            "************* Substituts *************",
            """Cliquer sur un produit pour l'enregister
            dans les favoris"""
        )

        if substitutes:
            number = 1
            for substitute in substitutes:
                substitute_text = substitute.__str__()
                label_substitute = tk.Label(
                    self,
                    fg="Blue",
                    justify=tk.LEFT,
                    text=substitute_text)
                label_substitute.bind(
                    '<Button-1>', lambda event,
                    arg=substitute: self.bind_product(arg))
                label_substitute.pack(padx=2)
                number += 1
        else:
            label_product = tk.Label(
                self,
                text="Pas de produits !")
            label_product.pack()

    def bind_product(self, product, is_product=None):
        """
        update product instance of root
        when event click on the categories frame
        """
        if is_product:
            self.root.status = 3
        else:
            self.root.status = 4
        self.root.product = product
