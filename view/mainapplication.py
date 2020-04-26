# coding: utf-8

"""
Set of tkinter classes for interface display
"""
import tkinter as tk

from common import config as c


class MainApplication(tk.Tk):
    """
    
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

    def display_frame_content(self, content):

        self.status = content

        # categories
        if content == 1:
            self.display_frame(self.frame_categories)
        # favorites
        else:
            self.display_frame(self.frame_favorites)

    def display_frame(self, frame):
        self.hide_frame(self.frame_categories)
        self.hide_frame(self.frame_favorites)
        self.hide_frame(self.frame_products)
        self.show_frame(frame)

    def show_frame(self, frame):
        frame.pack(side=tk.TOP)

    def hide_frame(self, frame):
        frame.pack_forget()


class MainFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.label = None

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def frame_title(self, title):
        self.label = tk.Label(
            self,
            text=title)
        self.label.pack(pady=10)

    def frame_comment(self, text_title):
        self.label = tk.Label(
            self,
            fg="darkgreen",
            text=text_title)
        self.label.pack(side=tk.BOTTOM, pady=3)


class MenuFrame(MainFrame):
    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        """

        """
        self.button1 = tk.Button(
            self.root,
            text="Quel aliment " +
            "souhaitez-vous remplacer ?",
            width=35,
            command=lambda: self.root.display_frame_content(1)
        )
        self.button2 = tk.Button(
            self.root,
            text="Retrouver mes aliments substitués.",
            width=35,
            command=lambda: self.root.display_frame_content(2)
        )
        self.button3 = tk.Button(
            self.root, text="Quitter",
            command=self.master.destroy
        )
        self.button1.pack(padx=5, pady=8)
        self.button2.pack(padx=5, pady=8)
        self.button3.pack(padx=5, pady=8)


class CategoriesFrame(MainFrame):
    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.config(pady="30")

    def display(self, categories):
        self.frame_title("********** Catégories **********")

        number = 1
        for category in categories:
            category_text = "{} - {} ".format(number, category.name)
            label_category = tk.Label(
                self,
                fg="Blue",
                text=category_text)
            label_category.bind(
                '<Button-1>', lambda event,
                id=category.id_category: self.bind_categories(id))
            label_category.pack()
            number += 1
        self.focus_set()

    def bind_categories(self, id_categorie=None):
        self.root.category = id_categorie


class ProductsFrame(MainFrame):
    def __init__(self, root):
        MainFrame.__init__(self, root)
        self.root = root
        self.config(pady="30")

    def refresh_favorites(self, favorites):
        self.clear_frame()

        self.frame_title("********** Favoris **********")

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
        self.clear_frame()
        title = """
               ********** Produits **********
        Cliquer sur un produit pour afficher ses substituts
        """
        self.frame_title(title)

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
        self.clear_frame()
        title = """
                ************* Substituts *************
                Cliquer sur un produit pour enregister
                un substitut dans les favoris
                """
        self.frame_title(title)

        if substitutes:
            number = 1
            for substitute in substitutes:
                substitute_text = substitute.__str__()
                label_substitute = tk.Label(
                    self,
                    fg="Blue",
                    text=substitute_text)
                label_substitute.bind(
                    '<Button-1>', lambda event,
                    arg=substitute: self.bind_product(arg))
                label_substitute.pack()
                number += 1
        else:
            label_product = tk.Label(
                self,
                text="Pas de produits !")
            label_product.pack()

    def bind_product(self, product, is_product=None):
        if is_product:
            self.root.status = 3
        else:
            self.root.status = 4
        self.root.product = product
