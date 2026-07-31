import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from PIL import Image

from processor import process_file

ctk.set_appearance_mode("dark")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ---------------- Colors ----------------

        self.BG = "#1E2C1B"
        self.PANEL = "#202020"
        self.GOLD = "#F19E40"
        self.GOLD_HOVER = "#D98A2B"
        self.WHITE = "#F5F5F5"

        self.title("Reserve Splitter")
        self.geometry("820x650")
        self.resizable(False, False)

        self.configure(fg_color=self.BG)

        self.selected_files = []

        project = Path(__file__).resolve().parent

        # ================= HEADER =================

        logo_path = project / "assets" / "KMI logo.png"

        self.logo = ctk.CTkImage(
            light_image=Image.open(logo_path),
            dark_image=Image.open(logo_path),
            size=(420,124)       # keeps original aspect ratio
        )

        logo = ctk.CTkLabel(
            self,
            image=self.logo,
            text=""
        )

        logo.pack(pady=(20,10))

        title = ctk.CTkLabel(
            self,
            text="Reserve Splitter",
            font=("Segoe UI",30,"bold"),
            text_color=self.WHITE
        )

        title.pack(pady=(0,20))

        # ================= FILE BOX =================

        self.file_box = ctk.CTkTextbox(
            self,
            width=700,
            height=230,
            fg_color=self.PANEL,
            border_width=2,
            border_color=self.GOLD,
            font=("Consolas",13),
            text_color="white"
        )

        self.file_box.pack()

        self.file_box.insert("1.0", "No files selected.")

        # ================= BUTTONS =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(pady=25)

        browse_button = ctk.CTkButton(

            button_frame,

            text="Select Files",

            width=180,
            height=42,

            fg_color=self.GOLD,
            hover_color=self.GOLD_HOVER,

            text_color="black",

            font=("Segoe UI",15,"bold"),

            command=self.select_files

        )

        browse_button.grid(row=0,column=0,padx=10)

        process_button = ctk.CTkButton(

            button_frame,

            text="Process",

            width=180,
            height=42,

            fg_color=self.GOLD,
            hover_color=self.GOLD_HOVER,

            text_color="black",

            font=("Segoe UI",15,"bold"),

            command=self.process_files

        )

        process_button.grid(row=0,column=1,padx=10)

        # ================= STATUS =================

        self.status = ctk.CTkLabel(

            self,

            text="Status: Ready",

            font=("Segoe UI",15),

            text_color=self.GOLD

        )

        self.status.pack(pady=15)

    # =====================================================

    def select_files(self):

        files = filedialog.askopenfilenames(

            title="Select Reserve Files",

            filetypes=[("Excel Files","*.xlsx")]

        )

        self.selected_files = files

        self.file_box.delete("1.0","end")

        if not files:

            self.file_box.insert("1.0","No files selected.")
            return

        for file in files:

            self.file_box.insert(
                "end",
                Path(file).name + "\n"
            )

    # =====================================================

    def process_files(self):

        if not self.selected_files:

            self.status.configure(
                text="Status: No files selected."
            )

            return

        for file in self.selected_files:

            filename = Path(file).name

            self.status.configure(
                text=f"Processing {filename}..."
            )

            self.update()

            process_file(file)

        self.status.configure(
            text="Status: Completed!"
        )


def run():
    app = App()
    app.mainloop()