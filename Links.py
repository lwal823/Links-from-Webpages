import os
import requests
from bs4 import BeautifulSoup

# Function to fetch links from a webpage
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    
    # Find all anchor tags <a> and extract href attribute
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):  # Filter out only absolute URLs
            links.append(href)
    
    return links

# Function to save links to a single text file
def save_links_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

# Main function
def main():
    url = 'https://onepiece.fandom.com/wiki/One_Piece_Wiki'  # Replace with the desired webpage URL
    links = get_links(url)
    
    file_name = 'all_links.txt'  # File to save all links
    save_links_to_file(links, file_name)
    print(f"{len(links)} links saved to '{file_name}' file.")

if __name__ == "__main__":
    main()
