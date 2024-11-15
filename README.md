## ENGLISH BELOW

# Zawartość repozytorium TASK_REKRUTACYJNY

W repozytorium znajdują się pliki:
- main.py - program generujący HTML dla artykułu
- artykul.html - plik wygenerowanego przez program main.py artykułu
- szablon.html - szablon html do wklejenia wygenerowanego artykułu
- podglad.html - gotowy podgląd z wklejonym wygenerowanym artykułem
- style.css - plik stylów dla szablon.html i podglad.html

# Generator HTML dla artykułu

Program main.py pobiera treść artykułu, wysyła ją do API OpenAI w celu przekształcenia na HTML, a następnie zwraca plik z gotowym artykułem w postaci artykul.html

## Wymagania

- Python 3.6 lub nowszy
- Biblioteki: `openai`, `requests`, `beautifulsoup4`

## Instalacja

1. Sklonuj repozytorium: `git clone https://github.com/GABARZABA/TASK_REKRUTACYJNY.git`
2. Zainstaluj wymagane biblioteki: `openai`, `requests`, `beautifulsoup4` 


## Uruchomienie

1. Otwórz plik 'main.py' i w miejsce 'KLUCZ' wstaw własny klucz API, po czym uruchom skrypt.
2. Program pobierze treść artykułu z podanego URL.
3. Wyśle zapytanie do API OpenAI w celu wygenerowania kodu HTML.
4. Utworzy pliki `artykul.html` w bieżącym katalogu.

## Użycie

1. Otwórz plik `szablon.html` w przeglądarce.
2. Skopiuj wygenerowaną treść artykułu w HTML (z pliku `artykul.html`).
3. Wklej treść do sekcji `<body>` w pliku `szablon.html`.
4. Zapisz plik `szablon.html`.
5. Odśwież stronę w przeglądarce, aby zobaczyć podgląd artykułu.

## Uwagi

- Klucz był wcześniej dodany na potrzeby procesu, ale z uwagi na bezpieczeństwo, OpenAi automatycznie wyłączyło klucz. Mam świadomość, że udostępnianie własnego klucza nie jest dobrą praktyką. Z uwagi na to należy wstawić własny klucz API w miejsce 'KLUCZ' w pliku 'main.py'. W normalnych warunkach, kod odnosiłby się do pliku '.env'.



## ENGLISH

# Content of the TASK_REKRUTACYJNY Repository

The repository includes the following files:
- main.py - a program that generates HTML for the article
- artykul.html - the file containing the article generated by main.py
- szablon.html - an HTML template for embedding the generated article
- podglad.html - a complete preview with the embedded generated article
- style.css - a stylesheet file for szablon.html and podglad.html

# HTML Generator for Articles

The main.py program takes the content of an article, sends it to the OpenAI API for conversion to HTML, and then returns a file with the complete article as artykul.html.

## Requirements

- Python 3.6 or higher
- Libraries: `openai`, `requests`, `beautifulsoup4`

## Installation

1. Clone the repository: `git clone https://github.com/GABARZABA/TASK_REKRUTACYJNY.git`
2. Install the required libraries: `openai`, `requests`, `beautifulsoup4`

## Execution

1. Open 'main.py' file and paste you API key in the place of 'KLUCZ', then run the script.
2. The program will fetch the article content from a provided URL.
3. It will send a request to the OpenAI API to generate the HTML code.
4. It will create the `artykul.html` file in the current directory.

## Usage

1. Open the `szablon.html` file in a browser.
2. Copy the generated article content in HTML (from `artykul.html`).
3. Paste the content into the `<body>` section of `szablon.html`.
4. Save the `szablon.html` file.
5. Refresh the page in the browser to see the article preview.

## Notes

- The key was previously added for the purpose of the process, but due to security reasons, OpenAI has automatically disabled the key. I am aware that sharing one's own key is not a good practice. Therefore, a personal API key should be inserted in place of 'KEY' in the 'main.py' file. Under normal circumstances, the code would refer to the '.env' file.
