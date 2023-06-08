# Personal Project: YouTube and IMDb Data Scraping

Welcome to my personal project repository! This repository contains two separate projects that involve data scraping from YouTube and IMDb using different techniques and libraries. The projects are organized into subfolders named "Youtube-selenium" and "imdb-bs4", respectively.

## YouTube Selenium Project

The "Youtube-selenium" subfolder contains a code example that demonstrates how to extract information about top-rated lectures from multiple YouTube channels. The code utilizes the powerful Selenium library, which allows for browser automation, along with the BeautifulSoup library for parsing HTML content.

### Running the YouTube Selenium Project

1. Make sure you have the necessary libraries installed:
   - Selenium: a powerful library for automating web browsers.
   - BeautifulSoup: a library for parsing HTML and XML content.
   - Openpyxl: a library for working with Excel files.

2. Ensure you have the Chrome WebDriver installed and set the appropriate path in the code. The WebDriver is essential for controlling the Chrome browser programmatically.

3. Update the `urls` list in the code with the YouTube channel URLs you want to scrape. You can add or remove URLs as per your requirements.

4. Execute the `main()` function in the code.

The code will visit the specified YouTube channels and scrape various details about their top-rated lectures. It utilizes Selenium to navigate to the videos page of each channel, scroll down to load more videos, and then uses BeautifulSoup to extract relevant information such as video names, URLs, labels, views, and ages. The extracted data will be saved in an Excel file named "Compendium.xlsx" for further analysis.

Feel free to explore the code, make modifications, and adapt it to suit your specific needs. This project can serve as a starting point for your YouTube data scraping endeavors.

## IMDb Beautiful Soup Project

The "imdb-bs4" subfolder contains a code example that focuses on scraping movie ratings from IMDb. The code utilizes the BeautifulSoup library, along with the requests library for fetching HTML content.

### Running the IMDb Beautiful Soup Project

1. Make sure you have the following libraries installed:
   - BeautifulSoup: a library for parsing HTML and XML content.
   - Requests: a library for making HTTP requests.

2. Execute the code provided in the "imdb-bs4" subfolder.

The code will access IMDb's movie ratings list and extract various details about each movie, including the movie name, rating, release year, running time, and a brief description. The extracted data will be saved in an Excel file named "IMDB Movie Ratings.xlsx" for further analysis or visualization.

Feel free to explore the code, make modifications, and customize it according to your specific requirements. This project serves as a foundation for scraping movie ratings from IMDb and provides a valuable starting point for your personal projects.

Enjoy experimenting with these projects, and feel free to enhance them further based on your personal interests and requirements.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/dem0nsl4yer/Scrapers/).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
