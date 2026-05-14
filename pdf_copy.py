from pypdf import PdfReader, PdfWriter
from exceptions import PdfExtractorError
from models import ExtractionResult




def extract_pages(input_pdf, output_pdf, start_page, end_page):
    # Load original PDF 
    reader = PdfReader(input_pdf)
    # Create a PDF writer object to create a new PDF
    writer = PdfWriter()

    # Validate page numbers
    if start_page < 1 or end_page > len(reader.pages) or start_page > end_page:
        raise PdfExtractorError("Invalid page range specified.")
    
    # Copy pages
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])
    
    # Save the new PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

    return ExtractionResult(
        output_pdf_name=output_pdf, 
        number_of_pages=end_page - start_page + 1, 
        message="Pages extracted successfully."
    )
    


if __name__ == "__main__":

    # testing it
    input_pdf = r"C:\Users\Shiv\Downloads\the-age-of-confucian-rule-the-song-transformation-of-china-9780674244344-0674244346.pdf"

    output_pdf = r"C:\Users\Shiv\dev\PDF-Extractor\new_pdf.pdf"

    try:
        result = extract_pages(input_pdf, output_pdf, 11, 18)
        print(result.message)
    
    except PdfExtractorError as e:
        print(f"Error: {e}")