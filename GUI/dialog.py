import customtkinter as ctk
from pymupdf import message


class StatusDialog(ctk.CTkToplevel):
    def __init__(self, title, message, is_success=True):
        super().__init__()

        self.title(title)
        self.geometry("350x180")
        self.resizable(False, False)
        self.grab_set()  # makes it modal

        # color choice
        bg_color = "#1f1f1f"
        success_color = "#2ecc71"
        error_color = "#e74c3c"

        self.configure(fg_color=bg_color)

        color = success_color if is_success else error_color

        # Message label
        self.label = ctk.CTkLabel(
            self,
            text=message,
            font=("Arial", 14),
            text_color=color,
            wraplength=300
        )
        self.label.pack(pady=30)

        # OK button
        self.button = ctk.CTkButton(
            self,
            text="OK",
            width=120,
            command=self.destroy,
            fg_color=color,
            hover_color=color
        )
        self.button.pack(pady=10)
    
    def show_success(message):
        StatusDialog("Success", message, is_success=True)


    def show_error(message):
        StatusDialog("Error", message, is_success=False)