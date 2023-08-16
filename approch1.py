import os
import csv
from pdfminer.high_level import extract_text
# pdf minor recognize the pattern of the PDF individually. As we have differnt formats in the stack I started experimenting with pdfminer

PDF_PATH = 'pdf'  # path to our sample PDFs

def extract_from_pdf(absolute_path):
    """
    extract all the text from our sample PDFs
    """
    return extract_text(absolute_path)

def save_to_csv(data, CSV_PATH):
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        for line in data.split('\n'): # based on the newline we are saving them as a row in our spreadsheet
            writer.writerow([line])

def main():
    for filename in os.listdir(PDF_PATH):
        if filename.endswith('.pdf'):
            absolute_path = os.path.join(PDF_PATH, filename)
            extracted_data = extract_from_pdf(absolute_path)
            csv_name = f"{filename[:-4]}.csv"
            CSV_PATH = os.path.join('csv_approch1', csv_name)
            save_to_csv(extracted_data, CSV_PATH)
            print(f"Saved extracted data from {filename} to {csv_name}")

if __name__ == "__main__":
    main()
