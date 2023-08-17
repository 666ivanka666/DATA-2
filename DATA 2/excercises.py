# Use BeautifulSoup library to parse ("web-scrape") retrieved HTML data. Base URL: https://realpython.github.io/fake-jobs/
# HINT: soup = BeautifulSoup(response.content, "html.parser")
# Print first 200 characters of the parsed HTML code.
# HINT: use str(soup)
# Also, print first 200 characters of the HTML code in "prettified" form (formatting and indentation applied).
# HINT: use soup.prettify()

import requests
from bs4 import BeautifulSoup

# Definiraj URL sa kojeg želiš dohvatiti podatke
base_url = "https://realpython.github.io/fake-jobs/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(base_url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Ispiši prvih 200 znakova analiziranog HTML koda
analizirani_html = str(soup)
print("Prvih 200 znakova analiziranog HTML-a:")
print(analizirani_html[:200])

# Uredi HTML kod za bolji prikaz i ispiši prvih 200 znakova
uredjeni_html = soup.prettify()
print("\nPrvih 200 znakova uredjenog HTML-a:")
print(uredjeni_html[:200])


# Parser je komponenta koja se koristi za razumijevanje i obradu strukturiranih dokumenata, kao što su HTML, XML ili JSON. 
# U kontekstu BeautifulSoup biblioteke u Pythonu, parser se koristi za analizu HTML ili XML dokumenata kako bi se izvukle informacije iz njih.

# Kada se radi o analizi HTML-a ili XML-a, parser je odgovoran za razbijanje dokumenta na njegove osnovne elemente 
# (tagove, atributi, sadržaj itd.) kako bi se mogla manipulirati i izvlačiti informacije iz njega. 
# Parser analizira niz znakova koji čini HTML ili XML dokument i stvara strukturu podataka koja omogućava programima da lakše pristupaju i obrađuju podatke.

# U primjeru s BeautifulSoup, kada koristimo BeautifulSoup(response.content, "html.parser"), koristimo parser ("html.parser") 
# kako bi se HTML sadržaj analizirao i pretvorio u strukturu podataka koju Python program može koristiti. Parser omogućava programu da "shvati" strukturu HTML-a, 
# pristupi oznakama, atributima i sadržaju, te izvuče potrebne informacije

#######################
# In the last example, use BeautifulSoup object to retrieve job postings (all elements of class card inside a container of id=ResultsContainer).
# HINT: To get the elements with particular id, use some_element.find(id="card")
# HINT: To get all the elements of a particular class, use some_element.find_all(class_="card")
# HINT: In general, if you need to get particular elements that have a speciffic attribute name and value, you can use some_element.find('elem_name', {"attr": "value"})
# Inside each such element, find first element of class media-content. Inside there should be h2 and h3 elements. Print their text values.
# HINT: If you know that there should be h2 inside your element, you can use element.h2 to reference it. Also, you can use element.h2.text to get the text from the related h2.

import requests
from bs4 import BeautifulSoup

# Definiraj URL sa kojeg želiš dohvatiti podatke
base_url = "https://realpython.github.io/fake-jobs/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(base_url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi kontejner s id-om "ResultsContainer"
results_container = soup.find(id="ResultsContainer")

# Pronađi sve elemente s klasom "card" unutar kontejnera
job_cards = results_container.find_all(class_="card")

# Iteriraj kroz svaki pronađeni oglas za posao
for job_card in job_cards:
    # Pronađi prvi element s klasom "media-content" unutar ovog oglasa
    media_content = job_card.find(class_="media-content")
    
    # Pronađi naslove h2 i h3 unutar "media-content"
    naslov_h2 = media_content.h2.text
    naslov_h3 = media_content.h3.text
    
    # Ispiši tekstualne vrijednosti naslova h2 i h3
    print("Naslov (h2):", naslov_h2)
    print("Podnaslov (h3):", naslov_h3)
    print("-------------------------")


#############################
# Find all the paragraphs in the following URL:
# http://quotes.toscrape.com/
# HINT: To get the specific tags, use some_element.find_all(id="tag_name")
# Print texts of these paragraphs.
# HINT: when reading text values, it is wise to strip the whitespace off the text

import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želiš analizirati
url = "http://quotes.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi sve oznake paragrafa
paragrafi = soup.find_all("p")

# Ispiši tekst svakog paragrafa
for paragraf in paragrafi:
    tekst_paragrafa = paragraf.get_text(strip=True)  # Ukloni početne i završne razmake
    print(tekst_paragrafa)
    print("-------------------------")

##############################
# Draw a random number between 1 and 2719 and parse JSON from URL: https://xkcd.com/{random_num}/info.0.json
# Use img data from that JSON to:
# retrieve data from that address
# create file name using last part of that address
# save retrieved data to the file with the created file name

import random      ### pitati marka dali valja
import requests
import os

# Generiraj slučajan broj između 1 i 2719
random_num = random.randint(1, 2719)

# Definiraj URL za dohvaćanje JSON podataka
json_url = f"https://xkcd.com/{random_num}/info.0.json"

# Pošalji HTTP GET zahtjev na URL bez provere SSL sertifikata
response = requests.get(json_url, verify=False)

# Dohvati JSON podatke
json_data = response.json()

# Dohvati URL slike iz JSON podataka
image_url = json_data["img"]

# Kreiraj ime datoteke iz posljednjeg dijela URL-a slike
file_name = os.path.basename(image_url)

# Pošalji HTTP GET zahtjev na URL slike bez provere SSL sertifikata
image_response = requests.get(image_url, verify=False)

# Spremi dohvaćene podatke u datoteku s kreiranim imenom
with open(file_name, "wb") as file:
    file.write(image_response.content)

print(f"Podaci spremljeni u datoteku: {file_name}")


######################
# Dohvatiš podatke s navedene adrese
# Kreiraš ime datoteke koristeći posljednji dio adrese
# Spremiš dohvaćene podatke u datoteku s kreiranim imenom
# Ovaj kod generira slučajan broj, koristi ga za stvaranje URL-a s 
# JSON podacima za određeni XKCD strip, dohvaća JSON podatke i iz njih izdvaja URL slike. 
# Zatim stvara ime datoteke koristeći posljednji dio URL-a slike i sprema dohvaćene slikovne 
# podatke u datoteku s tim imenom.

# Write a Python program that retrieves and prints the title text from URL http://books.toscrape.com/.

import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želimo analizirati
url = "http://books.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi naslovnu tekst
naslovna_tekst = soup.title.text

# Ispiši naslovnu tekst
print("Naslovna Tekst:", naslovna_tekst)


# Write a Python program that retrieves and prints URLs of images found on URL http://books.toscrape.com/.
import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želimo analizirati
url = "http://books.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi sve slike na stranici
slike = soup.find_all("img")

# Ispisivanje URL-ova slika
for slika in slike:
    url_slike = slika["src"]
    print("URL slike:", url_slike)
#Ovaj kod šalje GET zahtjev na navedeni URL, analizira HTML sadržaj i koristi BeautifulSoup da pronađe sve slike na stranici. Zatim ispisuje URL-ove pronađenih slika.


########################
# Write a Python program that retrieves and prints the book titles found on URL http://books.toscrape.com/.
# Each book is inside its own <article> tag, which has a product_pod class assigned. There is <img> tag inside, with the alt attribute that contains the name of the book.

import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želimo analizirati
url = "http://books.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi sve članke s klasom "product_pod"
clanci_knjiga = soup.find_all("article", class_="product_pod")

# Ispisivanje naslova knjiga
for clanak in clanci_knjiga:
    img_tag = clanak.find("img")
    ime_knjige = img_tag["alt"]
    print("Naslov knjige:", ime_knjige)

# programa koji dohvaća i ispisuje naslove knjiga pronađenih na URL-u "http://books.toscrape.com/". 
# Svaka knjiga je unutar svoje oznake <article> s dodijeljenom klasom "product_pod". Unutar svake takve oznake nalazi se <img> 
# oznaka s atributom "alt" koji sadrži ime knjige


###########################
# Write a Python program that retrieves and prints the book titles and star rating found on URL http://books.toscrape.com/.
# Each book is inside its own <article> tag, which has a product_pod class assigned. There is <img> tag inside, with the alt attribute that contains the name of the book.
# Also, inside the book article there is a paragraph with star-rating class and another class which has the information about rating.
import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želimo analizirati
url = "http://books.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi sve članke s klasom "product_pod"
clanci_knjiga = soup.find_all("article", class_="product_pod")

# Ispisivanje naslova knjiga i ocjena zvijezda
for clanak in clanci_knjiga:
    img_tag = clanak.find("img")
    ime_knjige = img_tag["alt"]
    
    ocjena_tag = clanak.find("p", class_="star-rating")
    ocjena_klasa = ocjena_tag.get("class")[-1]  # Zadnja klasa sadrži informaciju o ocjeni
    ocjena = ocjena_klasa.split("-")[-1]
    
    print("Naslov knjige:", ime_knjige)
    print("Ocjena zvijezda:", ocjena)
    print("-------------------------")

# programa koji dohvaća i ispisuje naslove knjiga i ocjene zvijezda pronađene na URL-u "http://books.toscrape.com/". 
# Svaka knjiga je unutar svoje oznake <article> s dodijeljenom klasom "product_pod". Unutar svake takve oznake nalazi se <img> 
# oznaka s atributom "alt" koji sadrži ime knjige. 
# Također, unutar članka knjige nalazi se odlomak s klasom "star-rating" i drugom klasom koja sadrži informacije o ocjeni:


#######################
# Write a Python program that retrieves and prints the book titles and star rating found on URL http://books.toscrape.com/.
# Each book is inside its own <article> tag, which has a product_pod class assigned. There is <img> tag inside, with the alt attribute that contains the name of the book.
# Also, inside the book article there is a paragraph with star-rating class and another class which has the information about rating.

import requests
from bs4 import BeautifulSoup

# Definiraj URL koji želimo analizirati
url = "http://books.toscrape.com/"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi sve članke s klasom "product_pod"
clanci_knjiga = soup.find_all("article", class_="product_pod")

# Ispisivanje naslova knjiga i ocjena zvijezda
for clanak in clanci_knjiga:
    img_tag = clanak.find("img")
    ime_knjige = img_tag["alt"]
    
    ocjena_tag = clanak.find("p", class_="star-rating")
    ocjena_klasa = ocjena_tag.get("class")[-1]  # Zadnja klasa sadrži informaciju o ocjeni
    ocjena = ocjena_klasa.split("-")[-1]
    
    print("Naslov knjige:", ime_knjige)
    print("Ocjena zvijezda:", ocjena)
    print("-------------------------")


# Ovaj kod šalje GET zahtjev na navedeni URL, analizira HTML sadržaj i koristi BeautifulSoup da pronađe sve članke s 
# klasom "product_pod" koji predstavljaju knjige. Zatim iz svakog članka izdvaja <img> oznaku i iz nje uzima vrijednost atributa "alt" 
# koja sadrži ime knjige. Također, traži odlomak s klasom "star-rating" 
# i iz njega izdvaja zadnju klasu koja sadrži informaciju o ocjeni. Na kraju, ispisuje naslove knjiga i pripadne ocjene.

################
# Parse HTML from URL: https://books.toscrape.com/catalogue/black-dust_976/index.html
# Save the image found on that URL with the original name.

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin  # Importujemo urljoin funkciju za konstruisanje apsolutnih URL-ova

# Definiraj URL za analizu
url = "https://books.toscrape.com/catalogue/black-dust_976/index.html"

# Pošalji HTTP GET zahtjev na URL
response = requests.get(url)

# Analiziraj HTML sadržaj pomoću BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Pronađi oznaku za sliku
img_tag = soup.find("img")

# Dohvati URL slike
image_url = img_tag["src"]

# Konstruiši apsolutni URL za sliku
base_url = "https://books.toscrape.com/catalogue/"
absolute_image_url = urljoin(base_url, image_url)

# Dohvati ime slike iz URL-a
image_name = os.path.basename(absolute_image_url)

# Pošalji HTTP GET zahtjev na apsolutni URL slike
image_response = requests.get(absolute_image_url)

# Spremi sliku s originalnim imenom
with open(image_name, "wb") as image_file:
    image_file.write(image_response.content)
    
print(f"Slika spremljena kao: {image_name}")

# Ovaj kod šalje HTTP GET zahtjev na navedenu URL adresu, 
# analizira HTML sadržaj, pronalazi oznaku <img>, izdvaja URL slike iz atributa "src", izvlači ime slike iz URL-a, 
# šalje još jedan HTTP GET zahtjev na URL slike i sprema sliku s originalnim imenom u trenutačni radni direktorij.





