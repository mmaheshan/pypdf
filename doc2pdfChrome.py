# chromredriver.exe will need to be updated to the installed
# Chrome version on pc for this code to work
# This code produces a small file compared to QT WebKit

import json, base64
# example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def send_devtools(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')


def get_pdf_from_html(driver, url, print_options={}, output_file_path="example.pdf"):
    driver.get(url)

    calculated_print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
    }
    calculated_print_options.update(print_options)
    result = send_devtools(driver, "Page.printToPDF", calculated_print_options)
    data = base64.b64decode(result['data'])
    with open(output_file_path, "wb") as f:
        f.write(data)


url = "https://en.wikipedia.org/wiki/Illinois_Central_College"
webdriver_options = Options()
webdriver_options.add_argument("--no-sandbox")
webdriver_options.add_argument('--headless')
webdriver_options.add_argument('--disable-gpu')
driver = webdriver.Chrome("C:\\Projects\\pypdf\\chromedriver\\chromedriver.exe", options=webdriver_options)
get_pdf_from_html(driver, url)
driver.quit()