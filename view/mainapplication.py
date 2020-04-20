# coding: utf-8

import tkinter as tk


class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(
            self,
            text="********** Menu Principal **********")
        self.button1 = tk.Button(self,
                                 text="Quel aliment " +
                                 "souhaitez-vous remplacer ?",
                                 width=35,
                                 command=self.next_menu(1))
        self.button2 = tk.Button(self,
                                 text="Retrouver mes aliments substitués.",
                                 width=35,
                                 command=self.next_menu(2))
        self.button3 = tk.Button(self, text="Quitter", command=self.quit)

        self.label_title.pack(pady=10)
        self.button1.pack(padx=5, pady=8)
        self.button2.pack(padx=5, pady=8)
        self.button3.pack(padx=5, pady=8)

    @classmethod
    def next_menu(cls, arg):
        if arg == 1:
            cls.app = MenuCategories()
        else:
            cls.app = MenuFavorites()


class MenuCategories(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(
            self,
            text="********** Menu catégories **********")

        self.label_title.pack(pady=10)


class MenuFavorites(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(
            self,
            text="********** Menu favoris **********")

        self.label_title.pack(pady=10)


def main():
    app = MainApplication()
    app.title("Openfoodfacts")
    app.mainloop()


if __name__ == "__main__":
    main()
