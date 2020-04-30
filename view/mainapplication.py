# coding: utf-8

"""
Set of tkinter classes for interface display
"""
import tkinter as tk

from common import config as c

from .categoriesframe import CategoriesFrame
from .productsframe import ProductsFrame
from .menuframe import MenuFrame


class MainApplication(tk.Tk):
    """
    Class interface tkinter
    Attributes: the different frames
    """

    def __init__(self):
        tk.Tk.__init__(self)
        # self.geometry("600x800+300+300")
        self.title(c.TITLE_APP)
        self.frame_categories = CategoriesFrame(self)
        self.frame_favorites = ProductsFrame(self)
        self.frame_products = ProductsFrame(self)
        self.frame_menu = MenuFrame(self)
        self.frame_menu.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.status = 0
        self.category = None
        self.product = None

    def display_frame(self, frame):
        """
        Displays the frame passed in parameter
        and hides the others
        """
        self.hide_frame(self.frame_categories)
        self.hide_frame(self.frame_favorites)
        self.hide_frame(self.frame_products)
        self.show_frame(frame)

    def show_frame(self, frame):
        """
        Display a frame
        """
        frame.pack(side=tk.TOP)

    def hide_frame(self, frame):
        """
        Hide a frame
        """
        frame.pack_forget()
