import customtkinter as ctk
from tkinter import filedialog

from processor import process_file


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Reserve Splitter")
        self.geometry("600x400")

        self.selected_files = []

        # ---------- Title ----------
        title = ctk.CTkLabel(
            self,
            text="Reserve Splitter",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # ---------- File List ----------
        self.file_box = ctk.CTkTextbox(
            self,
            width=500,
            height=150
        )
        self.file_box.pack(pady=10)

        # ---------- Browse Button ----------
        browse_button = ctk.CTkButton(
            self,
            text="Select Files",
            command=self.select_files
        )
        browse_button.pack(pady=10)

        # ---------- Process Button ----------
        process_button = ctk.CTkButton(
            self,
            text="Process",
            command=self.process_files
        )
        process_button.pack(pady=10)

        # ---------- Status ----------
        self.status = ctk.CTkLabel(
            self,
            text="Status: Ready"
        )
        self.status.pack(pady=20)

    def select_files(self):

        files = filedialog.askopenfilenames(
            title="Select Excel Files",
            filetypes=[("Excel Files", "*.xlsx")]
        )

        self.selected_files = files

        self.file_box.delete("1.0", "end")

        for file in files:
            self.file_box.insert("end", file + "\n")

    def process_files(self):

        if not self.selected_files:
            self.status.configure(text="No files selected.")
            return

        for file in self.selected_files:

            self.status.configure(
                text=f"Processing {file.split('/')[-1]}..."
            )

            self.update()

            process_file(file)

        self.status.configure(text="Done!")


def run():
    app = App()
    app.mainloop()