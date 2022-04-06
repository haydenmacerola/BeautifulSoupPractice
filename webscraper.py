import requests
from bs4 import BeautifulSoup

def main():

    try: 
      url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
    
      webpage = requests.get(url)
      webpage.raise_for_status()
      print (f'Scraping..... {url}')

    except Exception as e:
        print(e)  
    soup = BeautifulSoup(webpage.content, 'html.parser')
    tdata = soup.find('tbody', attrs={'class': 'lister-list'}).find_all('tr')
    
    titles = []
    ratings = []
    for data in tdata:
        
        movie_name = data.find('td', attrs={'class' :'titleColumn'}).a
        titles.append(movie_name.get_text())

        mov_rating = data.find('td', attrs={'class': 'ratingColumn imdbRating'}).strong.get_text()
        ratings.append(mov_rating)
       
        ##print(titles)
        ##print(ratings)

    imdb_dict = {}

    for title in titles:
        for rating in ratings:
          imdb_dict[title] = rating
    
    print(imdb_dict)
if __name__ == '__main__':
    main()



