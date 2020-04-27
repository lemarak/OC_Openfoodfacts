# coding: utf-8

"""
Set of tkinter classes for interface display
"""
import tkinter as tk

from common import config as c


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


class MainFrame(tk.Frame):
    """
    Parent class for all frames
    """

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.label = None
        self.label_comment = None

    def clear_frame(self):
        """
        Clean all widgets in the frame
        """
        for widget in self.winfo_children():
            widget.destroy()

    def frame_title(self, title, subtitle):
        """
        Displays a title of the frame
        """
        self.label = tk.Label(
            self,
            font='bold',
            text=title)
        self.label.pack(side=tk.TOP, pady=4)
        self.label = tk.Label(
            self,
            text=subtitle)
        self.label.pack(side=tk.TOP, pady=4)

    def frame_comment(self, text_title):
        """
        Displays a comment in the bottom of the frame
        """
        if self.label_comment:
            self.label_comment.destroy()
        self.label_comment = tk.Label(
            self,
            fg="darkgreen",
            text=text_title)
        self.label_comment.pack(side=tk.BOTTOM, pady=3)


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
