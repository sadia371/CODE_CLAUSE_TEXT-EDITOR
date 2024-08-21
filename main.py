import tkinter as tk
from tkinter import filedialog, messagebox, font
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Text Editor")
        self.root.geometry("900x600")

        # Fonts and colors
        self.text_font = font.Font(family="Helvetica", size=14)
        self.text_bg = "#1e1e1e"
        self.text_fg = "#ffffff"
        self.cursor_color = "#ffcc00"
        self.select_bg = "#666666"
        self.status_bg = "#333333"
        self.status_fg = "#ffffff"

        # Create a text widget with custom styling
        self.text_area = tk.Text(self.root, undo=True, font=self.text_font, bg=self.text_bg, fg=self.text_fg,
                                 insertbackground=self.cursor_color, selectbackground=self.select_bg, wrap="word")
        self.text_area.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor, accelerator="Ctrl+Q")

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"), accelerator="Ctrl+Y")

        # Status bar
        self.status_bar = tk.Label(self.root, text="Line 1, Column 1", anchor="e", bg=self.status_bg, fg=self.status_fg)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind events
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-s>", lambda event: self.save_as_file())
        self.root.bind("<Control-q>", lambda event: self.exit_editor())

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - Modern Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"{os.path.basename(file_path)} - Modern Text Editor")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{os.path.basename(file_path)} - Modern Text Editor")

    def save_as_file(self):
        self.save_file()

    def exit_editor(self):
        self.root.quit()

    def update_status(self, event=None):
        line, column = self.text_area.index(tk.INSERT).split(".")
        self.status_bar.config(text=f"Line {line}, Column {column}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
