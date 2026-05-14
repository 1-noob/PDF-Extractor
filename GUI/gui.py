import customtkinter as ctk
from tkinter import filedialog
import os



#create the main window
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Extractor")
        self.geometry("510x550")
        self.resizable(False, False)
        
        # Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue") 

        # Path of selected PDF file  
        self.selected_pdf = None
        self.file_name = None

        # Output files
        self.output_pdf = None
        self.output_file_name = None

        self.setup_ui()

    
    def setup_ui(self):

        # Main Container
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(
            fill="both", 
            expand=True,
            padx=30,
            pady=30
        )

        # Header Section
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="PDF Extractor", 
            font=ctk.CTkFont("Arial", size=28, weight="bold")
        )

        self.title_label.grid(
            row=0, 
            column=0,  
            sticky="w"
        )

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="Extract selected pages into a new PDF",
            font=ctk.CTkFont("Arial", size=16)
        )
        self.subtitle_label.grid(
            row=1, 
            column=0,  
            sticky="w",
            pady=(0, 25)
        )


        # PDF Selection Section
        self.pdf_selection_frame = ctk.CTkFrame(self.main_frame)
        self.pdf_selection_frame.grid(
            row=2, 
            column=0, 
            sticky="ew",
            pady=10
        )

        self.pdf_selection_frame.columnconfigure(0, weight=1)

        self.select_pdf_button = ctk.CTkButton(
            self.pdf_selection_frame,
            text="Choose PDF",
            font=ctk.CTkFont("Arial", size=16),
            width=150,
            command=self.select_pdf
        )

        self.select_pdf_button.grid(
            row=0, 
            column=0, 
            padx = 20,
            pady = (20, 10),
            sticky="w"
        )

        # Selected file label
        self.file_label = ctk.CTkLabel(
            self.pdf_selection_frame,
            text="No PDF selected",
            font=ctk.CTkFont("Arial", size=14)
        )

        self.file_label.grid(
            row=1, 
            column=0, 
            padx = 20,
            pady = (0, 20),
            sticky="w"
        )


        # Page Range Section
        self.page_section = ctk.CTkFrame(self.main_frame)
        self.page_section.grid(
            row=3, 
            column=0, 
            sticky="ew",
            pady=10
        )

        self.start_label = ctk.CTkLabel(
            self.page_section,
            text="Start Page:"
        )

        self.start_label.grid(
            row=0, 
            column=0, 
            padx=(20, 10),
            pady= 20,
            sticky="w"
        )

        self.start_entry = ctk.CTkEntry(
            self.page_section,
            width=120
        )

        self.start_entry.grid(
            row=0, 
            column=1, 
            pady= 20,
            sticky="w"
        )

        self.end_label = ctk.CTkLabel(
            self.page_section,
            text="End Page:"
        )

        self.end_label.grid(
            row=0, 
            column=2, 
            padx=(40, 10),
            pady= 20,
            sticky="w"
        )

        self.end_entry = ctk.CTkEntry(
            self.page_section,
            width=120
        )

        self.end_entry.grid(
            row=0, 
            column=3, 
            pady= 20,
            sticky="w"
        )


        # Output file section
        self.output_section = ctk.CTkFrame(self.main_frame)

        self.output_section.grid(
            row=4, 
            column=0, 
            sticky="ew",
            pady=10
        )

        self.choose_output_button = ctk.CTkButton(
            self.output_section,
            text="Choose Output Location",
            font=ctk.CTkFont("Arial", size=16),
            width=200,
            command=self.select_output_location
        )

        self.choose_output_button.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )

        self.output_label = ctk.CTkLabel(
            self.output_section,
            text="No output location selected",
            font=ctk.CTkFont("Arial", size=14)
        )

        self.output_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="w"
        )


        # Extract Button
        self.extract_button = ctk.CTkButton(
            self.main_frame,
            text="Extract Pages",
            font=ctk.CTkFont("Arial", size=16),
            width=150,
            command=self.extract_pages
        )

        self.extract_button.grid(
            row=5,
            column=0,
            sticky="ew",
            pady=(25, 0)
        )


    def select_pdf(self):
        self.selected_pdf = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if self.selected_pdf:
            self.file_name = os.path.basename(self.selected_pdf)
            self.file_label.configure(text=f"Selected: {self.file_name}")
            print(f"Selected PDF: {self.file_name}")

    def extract_pages(self):
        print("Extracting pages...")

    def select_output_location(self):
        self.output_pdf = filedialog.asksaveasfilename(
            title="Save Extracted PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if self.output_pdf:
            self.output_file_name = os.path.basename(self.output_pdf)
            self.output_label.configure(text=f"Output: {self.output_file_name}")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()