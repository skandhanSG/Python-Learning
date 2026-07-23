import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        # Download webpage
        response = requests.get(url)

        # Raise error if page not found
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # -------------------------
        # Title
        # -------------------------
        print("=" * 40)
        print("Website Title")
        print("=" * 40)

        if soup.title:
            print(soup.title.text.strip())
        else:
            print("No title found.")

        # -------------------------
        # Headings
        # -------------------------
        print("\n" + "=" * 40)
        print("Headings")
        print("=" * 40)

        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        print(headings)

        if headings:
            for heading in headings:
                print(heading.get_text(strip=True))
        else:
            print("No headings found.")

        # -------------------------
        # Links
        # -------------------------
        print("\n" + "=" * 40)
        print("Links")
        print("=" * 40)

        links = soup.find_all("a")

        if links:
            for link in links:
                href = link.get("href")
                if href:
                    print(href)
        else:
            print("No links found.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


url = input("Enter website URL: ")
scrape_website(url)