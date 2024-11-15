import openai
import requests
import os

openai.api_key = "KLUCZ"

if openai.api_key is None:
    print("Brak klucza API!")
else:
    print("Klucz API załadowany poprawnie!")

url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"
response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
    article_content = response.text
else:
    raise Exception("Nie udało się pobrać treści artykułu.")

prompt = f"""
Przekształć poniższy artykuł w strukturę HTML, zachowując odpowiednie klasy CSS i struktury elementów, ale bez tagów <html>, <head> i <body>. Znajdź najlepsze miejsca na grafiki i wstaw tam placeholder <img src="image_placeholder.jpg" alt="prompt do grafiki">. Używaj klas CSS takich jak 'content', 'section', 'header', 'paragraph', 'image', aby umożliwić łatwą integrację z szablonem strony. Zadbaj o estetyczne formatowanie tekstu oraz logiczne podziały na nagłówki, akapity i sekcje.

Artykuł:
{article_content}
"""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=3000,
    temperature=0.7
)

html_content = response.choices[0].message.content.strip()

with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Zapisano wygenerowany plik artykul.html")
