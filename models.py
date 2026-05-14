class ExtractionResult:

    
    def __init__(self, output_pdf_name: str, number_of_pages: int, message: str):
        self.output_pdf_name = output_pdf_name
        self.number_of_pages = number_of_pages
        self.message = message