import requests
from bs4 import BeautifulSoup
import time

urls = [
    "https://www.123roulement.com/rubrique/roulement-bille"
]

for i in range(273):
    urls.append("https://www.123roulement.com/rubrique/roulement-bille?page="+i.__str__())

for url in urls:
    print("***********************************************************************")
    print(url.__str__())
    print("***********************************************************************")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    divs = soup.find_all("div", {"class": "card-product"})
    # Boucler sur chaque div
    for div in divs:
        # Extraire le texte contenu dans la div
        div_image = div.find('img', {"class":"card-img-top"})
        div_image2 = div.find('div', {"class":"d-flex"}).get_text()
        div_image2 = div_image2.replace("\n", ";")
        div_image2 = div_image2.replace("										", "")
        div_image2 = div_image2.replace("									", "")
        div_image2 = div_image2.replace("									", "")
        div_image2 = div_image2.replace("								", "")
        img_src = div_image['src']
        div_text = div.find('h6').get_text()
        if div_text != None:
            div_text = div_text.replace("\n", ";")
            print(div_text, div_image2, img_src)
    time.sleep(1)