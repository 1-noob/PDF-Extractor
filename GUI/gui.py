import customtkinter as ctk
from tkinter import filedialog



#create the main window
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("800x450")
        
        # Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue") 

        # Path of selected PDF file  
        self.selected_pdf = None

        self.setup_ui()

    
    def setup_ui(self):

        self.title_label = ctk.CTkLabel(
            self,
            text="PDF Extractor", 
            font=ctk.CTkFont("Arial", size=28, weight="bold")
        )

        self.title_label.pack(pady=40)


        # Select PDF Button
        self.select_pdf_button = ctk.CTkButton(
            self,
            text="Select PDF",
            font=ctk.CTkFont("Arial", size=16),
            command=self.select_pdf
        )
        self.select_pdf_button.pack(pady=20)


        # Selected file label
        self.file_label = ctk.CTkLabel(
            self,
            text="No PDF selected",
            font=ctk.CTkFont("Arial", size=14)
        )
        self.file_label.pack(pady=10)



    def select_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if file_path:
            self.selected_pdf = file_path
            self.file_label.configure(text=f"Selected: {file_path}")
            print(f"Selected PDF: {file_path}")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()