from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'top rated movies'

sheet.append(['Name', 'Rank', 'Year', 'Time', 'Bio'])

for i in range(1,8):
    url = f'https://www.imdb.com/list/ls000634294/?sort=list_order,asc&st_dt=&mode=detail&page={i}'

    source = requests.get(url)

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('div', class_= "lister-list").find_all('div', class_="lister-item mode-detail")

    for movie in movies:
        name = movie.find('h3', class_="lister-item-header").a.text
        try:
            rating = movie.find('div', class_="ipl-rating-star small").find('span', class_="ipl-rating-star__rating").text
        except AttributeError:
            rating = 0
        year = movie.find('span', class_="lister-item-year text-muted unbold").text.strip('()')
        time = movie.find('p', class_ = "text-muted text-small").find('span', class_ ="runtime").text
        bio = movie.find('p', class_="").text
        sheet.append([name, rating, year, time, bio])
excel.save('IMDB Movie Ratings.xlsx')