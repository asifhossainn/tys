import PyPDF3
import PyPDF2
import os
import tabula   # tabula is a open source library that effectively extracts table from the PDF files. It can aslo extract tables in the images of PDF files!!
import pandas as pd

PDF_PATH = 'pdf'
EXTRACTED_PATH = 'csv_approch2'

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = []
        for page in range(reader.numPages):
            text.append([reader.getPage(page).extract_text()])
    return text

def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

def save_text_in_each_page(text, main_folder_path):
    subfolder_path = os.path.join(main_folder_path, "text")
    if not os.path.exists(subfolder_path):
        os.mkdir(subfolder_path)

    for i,page in enumerate(text):
        with open(os.path.join(subfolder_path,f"page_{i}.txt"), 'w', encoding='utf-8') as f:
            f.write(page[0])

def save_tables_in_pdf(tables, main_folder_path):
    subfolder_path = os.path.join(main_folder_path, "tables")
    if not os.path.exists(subfolder_path):
        os.mkdir(subfolder_path)

    # Iterating through all the tables we extracted from the PDF
    cleaned_tables = []
    for table in tables:
        # Dropping columns and rows that are completely null
        table = table.dropna(axis=0, how='all').dropna(axis=1, how='all')
        table = table.reset_index(drop=True)
        cleaned_tables.append(table)

    for idx, table in enumerate(cleaned_tables):
        table.to_csv(os.path.join(subfolder_path,f"table_{idx}.csv"), index=False)

if __name__ == "__main__":
    for filename in os.listdir(PDF_PATH):
        if filename.endswith('.pdf'):
            input_path = os.path.join(PDF_PATH, filename)
            text = extract_text_from_pdf(input_path)
            tables = extract_tables_from_pdf(input_path)

            folder_name = os.path.splitext(filename)[0]
            main_folder_path = os.path.join(EXTRACTED_PATH, folder_name)
            
            # creating a separate folder for all the PDF we have with the same name
            if not os.path.exists(main_folder_path):
                os.mkdir(main_folder_path)

            save_text_in_each_page(text, main_folder_path)
            save_tables_in_pdf(tables, main_folder_path)