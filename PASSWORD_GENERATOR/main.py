from ui import PasswordGeneratorUI
import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.app = PasswordGeneratorUI(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    main_app = Main()
    main_app.run()
