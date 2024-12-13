import requests
import re

def get_movies(search_term):
    url = f'https://catflix.su/?s={search_term}'
    response = requests.get(url)
    pattern = r'https://catflix\.su/movies/(?!movies/)[^"]+'
    matches = re.findall(pattern, response.text)
    return matches

def get_turbovid_url(url):
    response = requests.get(url)
    pattern = r'https://turbovid\.eu/embed/[^"]+'
    matches = re.findall(pattern, response.text)
    return matches

search_term = input("Enter your search term: ")
matches = get_movies(search_term)

if matches:
    print("Found the following movie URLs:")
    for i, match in enumerate(matches, start=1):
        title = match.replace("https://catflix.su/movies/", "").replace("/", "").replace("-", " ")
        title = title.title()
        print(f"{i}. {title}")
    choice = input("Enter the number of the movie you want to watch: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(matches):
            url = matches[choice - 1]
            turbovid_urls = get_turbovid_url(url)
            if turbovid_urls:
                print("Found the following TurboVid URLs:")
                for turbovid_url in turbovid_urls:
                    print(turbovid_url)
            else:
                print("No TurboVid URLs found")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice")
else:
    print("No movie URLs found")

