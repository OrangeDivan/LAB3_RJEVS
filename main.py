import tkinter as tk
from math import sqrt, sin, cos, tan, log, exp

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Научный калькулятор")
        self.root.geometry("400x500")  # Начальный размер окна
        self.root.resizable(True, True)  # Разрешить изменение размеров окна

        # Создание поля для ввода
        self.entry = tk.Entry(self.root, font=("Arial", 20), bd=10, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, pady=10)

        # Добавление кнопок
        buttons = [
            ("C", 1, 0), ("←", 1, 1), ("(", 1, 2), (")", 1, 3), ("%", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("sqrt", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("x^2", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("1/x", 4, 4),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3), ("sin", 5, 4),
            ("cos", 6, 0), ("tan", 6, 1), ("log", 6, 2), ("ln", 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

        # Меню приложения
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Очистить", command=self.clear_entry)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)

    def on_button_click(self, key):
        try:
            if key == "=":
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            elif key == "C":
                self.clear_entry()
            elif key == "←":
                self.entry.delete(len(self.entry.get()) - 1, tk.END)
            elif key == "sqrt":
                self.entry.insert(tk.END, "sqrt(")
            elif key == "x^2":
                self.entry.insert(tk.END, "**2")
            elif key == "1/x":
                self.entry.insert(tk.END, "1/")
            elif key == "sin":
                self.entry.insert(tk.END, "sin(")
            elif key == "cos":
                self.entry.insert(tk.END, "cos(")
            elif key == "tan":
                self.entry.insert(tk.END, "tan(")
            elif key == "log":
                self.entry.insert(tk.END, "log(")
            elif key == "ln":
                self.entry.insert(tk.END, "log(")
            else:
                self.entry.insert(tk.END, key)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Ошибка")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()