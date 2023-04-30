# Scraper
In this project, I have developed a web scraping application using Python and Django. This application allows users to scrape specific HTML elements in URL addresses entered by users.

### Installation
To run this project, Python and pip must be installed.

* Clone this repository: ```git clone https://github.com/shaumne/webscraper```
* Create a virtual environment: ```python3 -m venv myenv```
* Activate the virtual environment: ```source myenv/bin/activate```
* Install required packages: ```pip install -r requirements.txt```
* Run the Django project: ```python manage.py runserver```

### Usage
- To access the application, go to http://localhost:8000 in your browser.
- On the home page, there are three input boxes.
- Enter the URL address of the site you want to scrape in the "Enter URL" box.
- Enter the name of the HTML element you want to scrape in the "Enter HTML element name" box (e.g. div, h1, span, etc.).
- Enter the class of the HTML element you want to scrape in the "Enter the element class" box.
- Click the "Scrape" button.
- The results will be displayed on the same page in a table.

### Examples
Below is an example of a website scraped using the application.

| Site Name | HTML Element | Element Class | Value |
| --- | --- | --- | --- |
| YouTube | div | style-scope ytd-channel-name | YouTube |
| Google | div | header | Google |
| GitHub | h1 | lh-condensed | Where the world builds software |

###Contributing
To contribute to this project, please submit a pull request.