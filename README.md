# FOS-Data-Scraping

This project includes several Python scripts for extracting and parsing data from websites using different modules and libraries. The scripts utilize `requests`, `BeautifulSoup`, and `Selenium` to retrieve information from various sources and save it to text files. 

## Files

The project contains the following files:

1. `extract.py`: This file contains a function called `extract` that utilizes the `requests` module to send a GET HTTP request to a specified URL. The response is then saved as a text file named `extract.txt`.

2. `parse.py`: This file contains a function called `parse` that uses the `requests` module to send a GET HTTP request to 'https://fr.wikipedia.org/wiki/Alger'. It further utilizes the `BeautifulSoup` library to parse the data and extract the population information. The extracted data is saved as a text file named `parse.txt`.

3. `parse_js.py`: This file uses `Selenium` to parse data from 'https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas' website, which requires JavaScript rendering. The script aims to retrieve prices of products from any given category. The prices are saved in a text file named `parse_js.txt`.

4. `scraper.py`: This file serves as the main file and executes the previous Python scripts in the specified order. It acts as the entry point for running the extraction and parsing processes.

## Prerequisites

To run the scripts successfully, ensure that you have the following requirements met:

1. Python 3 installed on your system.
2. Required Python packages/modules: `requests`, `BeautifulSoup`, and `Selenium`.
3. Chrome web browser and the corresponding ChromeDriver (compatible with your browser version) for `Selenium` to work properly.

## Usage

Follow the steps below to run the project:

1. Download the project files and place them in a single directory.

2. Install the required Python packages by running the following command in your command prompt or terminal:

   ```bash
   pip install requests beautifulsoup4 selenium
   ```

3. Ensure you have the ChromeDriver executable downloaded and placed in your system's PATH or in the same directory as the project files. You can download the ChromeDriver from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Open the `scraper.py` file and customize the URL and other parameters according to your needs.

5. Run the `scraper.py` script using the following command:

   ```bash
   python scraper.py
   ```

   This will execute the scripts in the specified order and generate the respective output files.

6. Check the generated output files (`extract.txt`, `parse.txt`, `parse_js.txt`) to view the extracted and parsed data.

## Notes

- The `extract.py` script saves the response content as plain text in the `extract.txt` file. If you need to save the content in a different format, you can modify the script accordingly.

- The `parse.py` script is specifically designed to parse data from the 'https://fr.wikipedia.org/wiki/Alger' page. If you want to parse data from a different page, you can modify the URL and the parsing logic inside the script.

- The `parse_js.py` script requires the ChromeDriver executable to be in your system's PATH or in the same directory as the project files. If you have the ChromeDriver stored in a different location, you need to update the `webdriver.Chrome()` line in the script to provide the correct path.

- Customize the `parse_js.py` script to target the specific data you want to extract from the 'https://www.wo

olworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas' website.

- The `scraper.py` file executes the other Python scripts in the specified order. If you need to modify the execution order or include additional scripts, you can edit the `scraper.py` file accordingly.

- Ensure that you have the necessary permissions to read and write files in the directory where the scripts are located, as the output files will be generated in that directory.
