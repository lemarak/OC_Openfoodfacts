# coding: utf-8

import tkinter as tk


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
