import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from PIL import Image

from processor import process_file

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Reserve Splitter")
        self.geometry("850x720")
        self.resizable(False, False)

        # Colors
        BG = "#123524"          # dark mining green
        PANEL = "#0F2C1F"
        GOLD = "#E6B325"
        GOLD_HOVER = "#C89A16"
        TEXT = "#F4F4F4"

        self.configure(fg_color=BG)

        self.selected_files = []

        project_root = Path(__file__).resolve().parent

        # ---------------- Logo ----------------

        logo_path = project_root / "assets" / "KMI logo.png"

        self.logo = ctk.CTkImage(
            light_image=Image.open(logo_path),
            dark_image=Image.open(logo_path),
            size=(600, 120)
        )

        logo_label = ctk.CTkLabel(
            self,
            image=self.logo,
            text=""
        )
        logo_label.pack(pady=(20,10))

        # ---------------- Title ----------------

        title = ctk.CTkLabel(
            self,
            text="Reserve Splitter",
            text_color=TEXT,
            font=("Segoe UI",34,"bold")
        )

        title.pack(pady=(0,20))

        # ---------------- File Box ----------------

        self.file_box = ctk.CTkTextbox(
            self,
            width=700,
            height=220,
            fg_color=PANEL,
            border_width=2,
            border_color=GOLD,
            font=("Consolas",14)
        )

        self.file_box.pack()

        # ---------------- Buttons ----------------

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(pady=30)

        browse_button = ctk.CTkButton(
            button_frame,
            text="📂  Select Files",
            width=220,
            height=45,
            fg_color=GOLD,
            hover_color=GOLD_HOVER,
            text_color="black",
            font=("Segoe UI",16,"bold"),
            command=self.select_files
        )

        browse_button.pack(pady=10)

        process_button = ctk.CTkButton(
            button_frame,
            text="⚙  Process",
            width=220,
            height=45,
            fg_color=GOLD,
            hover_color=GOLD_HOVER,
            text_color="black",
            font=("Segoe UI",16,"bold"),
            command=self.process_files
        )

        process_button.pack()

        # ---------------- Status ----------------

        self.status = ctk.CTkLabel(
            self,
            text="✔ Status: Ready",
            text_color=GOLD,
            font=("Segoe UI",16)
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