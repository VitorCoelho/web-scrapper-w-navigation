# web-scrapper-w-navigation
A simple python webscrapping tool with bs4 that navigates to sub pages. It navigates through each company URL and collects specific information, saving it to a CSV file. This can be useful for gathering data for research or analysis purposes.

## Features

- Navigates through each company URL on the URL and extracts relevant information.
- Collects data such as company name, address, city, state, postal code, phone number, email, and website.
- Saves the extracted data to a CSV file for further analysis.

## Prerequisites

- Python 3.x installed on your machine.
- Required Python libraries: requests, beautifulsoup4.

## Installation

1. Clone the repository or download the source code.
2. Install the required Python dependencies by running the following command:

**$ pip install requests beautifulsoup4**

## Usage

1. Open the Python script `anpp-lojas.py` in a text editor.
2. Update the `url_base` variable in the code with the URL of the company page containing the list of companies.
3. Run the Python script by executing the following command:

**$ python anpp-lojas.py**

4. The script will start scraping the company data by navigating through each company URL and saving it to a CSV file named `company_data.csv`.

## Customization

- You can modify the CSV file name and the specific fields being extracted by modifying the code in `anpp-lojas.py`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
