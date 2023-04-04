from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'top rated lectures_Opencode'

sheet.append(['Name', 'URL', 'Label', 'Views', 'Old'])

urls = [
    'https://www.youtube.com/c/Codemycom',
    'https://www.youtube.com/Albert10110',
    'https://www.youtube.com/c/TokyoEdTech',
    'https://www.youtube.com/c/Coreyms',
    'https://www.youtube.com/c/CodingEntrepreneurs/',
   # 'https://www.youtube.com/c/noobtoprofessional',
    'https://www.youtube.com/c/CSDojo'
]
def main():
    driver = webdriver.Chrome()
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        print(url)
    #   waiting for the page to load
        time.sleep(3) 
    #   repeat scrolling 10 times
        for i in range(20):
        #scroll 800 px
            driver.execute_script('window.scrollTo(0,(window.pageYOffset+2000))')
        #waiting for the page to load
            time.sleep(3) 
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('div', id = "items", class_="style-scope ytd-grid-renderer").find_all('div', id = "details", class_="style-scope ytd-grid-video-renderer")

    # titles = soup.findAll('a', id= "video-title")

        for bo in box: 
            name = bo.find('a', id= "video-title").text
            url = 'http://www.youtube.com/' + bo.find('a', id= "video-title")['href']
            label = bo.find('a', id= "video-title")['aria-label']
            views = bo.find('div', id= "metadata-line").find('span', class_="style-scope ytd-grid-video-renderer").text
            old = bo.find('div', id= "metadata-line").find_all('span', class_="style-scope ytd-grid-video-renderer")[-1].text
            sheet.append([name, url, label, views, old])
    
    excel.save('Compendium.xlsx')

main()