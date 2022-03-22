# Need wkhtmltopdf to work
# Download ZIP file from http://wkhtmltopdf.org/downloads.html
# Set path to wkhtmltopdf in the configuration and we are all set

import shutil
import pdfkit
import os
import logging


# Configuration
APP = {
    "PDF_PATH" : "C:\\Temp\\PDF\\",
    "LOG_FILE" : "C:\\Temp\\pdf_generation_log.txt",
    "ROOT_URL" : "http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"
}

def main():
    logging.basicConfig(filename=APP["LOG_FILE"], level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s', filemode='w')
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.debug("Starting to generate PDF files")
    create_pdf(APP['ROOT_URL'])

def create_pdf(url):
    logging.debug(f"Url: {url} ")

    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'dpi': 300
    }
    path_wkthmltopdf = 'C:\\Projects\\pypdf\\wkhtmltox\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    try:
        #os.mkdir(APP["PDF_PATH"] )
        file_path = APP["PDF_PATH"] + "filename.pdf"
        logging.debug(f"File path: {file_path}")
        pdfkit.from_url(url, file_path, options=options, configuration=config)
    except:
        logging.error('Creating PDF fil failed.', exc_info=True)
    logging.debug('Creating PDF file complete')


if __name__ == "__main__":
    if os.path.exists(APP["LOG_FILE"]):
        os.remove(APP["LOG_FILE"])

    for filename in os.listdir(APP["PDF_PATH"]):
        filepath = os.path.join(APP["PDF_PATH"], filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)
    main()
