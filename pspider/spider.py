#!/bin/python3
import requests
import multiprocessing
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the user agent that pretends to be an iPhone
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"

# Define a set to store the visited URLs
visited = set()

# Define a function that crawls a given URL and returns a list of links found on the page
def crawl(url):
    # Check if the URL is already visited
    if url in visited:
        return []
    # Add the URL to the visited set
    visited.add(url)
    # Print the URL
    # Create a list to store the links
    links = []
    # Try to fetch the page content using requests
    try:
        # Set the user agent header
        headers = {"User-Agent": user_agent}
        # Get the response object
        response = requests.get(url, headers=headers)
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            print(f"Crawled {url}")
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            # Find all the <a> tags that have an href attribute
            for a in soup.find_all("a", href=True):
                # Get the value of the href attribute
                href = a["href"]
                # Convert the relative URL to an absolute one using urljoin
                link = urljoin(url, href)
                # Append the link to the list
                links.append(link)
    # Handle any exceptions
    except Exception as e:
        # Print the exception
        print(f"Error: {e}")
    # Return the list of links
    return links

# Define the starting URL
start_url = "https://moz.com/top500"

# Create a multiprocessing pool with 100 processes
pool = multiprocessing.Pool(100)

# Use the pool to crawl the starting URL and get the links
links = pool.map(crawl, [start_url])

# Use the pool to crawl the links recursively until no more links are found
while links:
    # Flatten the list of lists into a single list
    links = [link for sublist in links for link in sublist]
    # Use the pool to crawl the links and get the new links
    links = pool.map(crawl, links)

# Close the pool
pool.close()
