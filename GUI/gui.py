import customtkinter as ctk



#create the main window
class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("800x450")
        
        # Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")   

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

    def select_pdf(self):
        # Placeholder for PDF selection logic
        print("Select PDF button clicked")




if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()