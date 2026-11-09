
import tkinter as tk

from Views.login_view import LoginView


def main():
    root = tk.Tk()
    LoginView(root)
    root.mainloop()


if __name__ == "__main__":
    main()


"""
The library 'fpdf' is used to create archives PDF
with coding. It is more useful because you do not have
to install another external program to convert a file
to PDF, while .csv and .json is included in Python.

You can add new pages (add_page), set a font for your words(set_font),
and the most important function: save the archive into your system.
There are some disadvantages such as line breaks manually and the limitation
of characters because fpdf only support 'latin-1'.

"""