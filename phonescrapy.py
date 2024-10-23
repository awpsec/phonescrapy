#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys
import argparse
from colorama import Fore, Style

banner = """
 ,--.  _   _   __  _ .--.   .--.  .---.  .---.
`'_\ :[ \ [ \ [  ][ '/'`\ \( (`\]/ /__\\/ /'`\\]
// | |,\ \/\ \/ /  | \__/ | `'.'.| \__.,| \__.
\'-;__/ \__/\__/   | ;.__/ [\__) )'.__.''.___.'
                  [__|     
            ,---.,---.,---.,---.,---.,   .
            `---.|    |    ,---||   ||   |
            `---'`---'`    `---^|---'`---|
                                |    `---'
"""
print(Fore.GREEN + banner + Style.RESET_ALL)

def vprint(verbose, message):
    if verbose:
        print(message)

def is_html(response):
    content_type = response.headers.get("Content-Type", "").lower()
    return "text/html" in content_type

def scrape_phone_numbers(domain, verbose=False):
    try:
        vprint(verbose, f"Fetching content from {domain}...")

        response = requests.get(domain, timeout=10)
        response.raise_for_status()

        if not is_html(response):
            vprint(verbose, f"Skipping non-HTML content on {domain}")
            return set()

        if response.encoding is None:
            response.encoding = "utf-8"

        vprint(verbose, "Successfully fetched content. Parsing HTML...")

        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract phone numbers
        vprint(verbose, "Extracting phone numbers...")
        text = soup.get_text()
        phone_number_pattern = re.compile(r'\(?\b[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b')
        phone_numbers = phone_number_pattern.findall(text)
        unique_phone_numbers = set(phone_numbers)

        if unique_phone_numbers:
            vprint(verbose, f"Phone numbers found on {domain}:")
            for number in unique_phone_numbers:
                vprint(verbose, number)
        else:
            vprint(verbose, f"No phone numbers found on {domain}.")

        return unique_phone_numbers

    except requests.RequestException as e:
        print(f"Error fetching {domain}: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)

def get_internal_links(domain, soup, base_url):
    links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        url = urljoin(base_url, href)
        parsed_url = urlparse(url)

        if parsed_url.netloc == domain:
            links.add(url)
    
    return links

def crawl_domain(domain, output_file="phonebook.txt", max_depth=2, verbose=False):
    base_url = f"https://{domain}"
    visited = set()
    to_visit = {base_url}
    all_phone_numbers = set()

    try:
        for depth in range(max_depth):
            vprint(verbose, f"Depth {depth + 1}/{max_depth}:")
            next_pages = set()

            for page in to_visit:
                if page in visited:
                    continue

                vprint(verbose, f"Visiting {page}...")
                try:
                    response = requests.get(page, timeout=10)
                    response.raise_for_status()

                    if not is_html(response):
                        vprint(verbose, f"Skipping non-HTML content on {page}")
                        continue

                    soup = BeautifulSoup(response.text, 'html.parser')

                    phone_numbers = scrape_phone_numbers(page, verbose)
                    all_phone_numbers.update(phone_numbers)

                    new_links = get_internal_links(domain, soup, page)
                    next_pages.update(new_links)

                    visited.add(page)

                except requests.RequestException as e:
                    vprint(verbose, f"Error visiting {page}: {e}")
                    continue

            to_visit = next_pages - visited

            if not to_visit:
                break

    except KeyboardInterrupt:
        print("\nOperation manually aborted. Saving progress...")
    finally:
        with open(output_file, "w") as f:
            sorted_phone_numbers = sorted(all_phone_numbers)
            if sorted_phone_numbers:
                print(f"\nPhone numbers found across {len(visited)} pages:")
                for number in sorted_phone_numbers:
                    f.write(number + "\n")
                    print(number)
                print(f"\nPhone numbers saved to {output_file}.")
            else:
                print("No phone numbers found across visited pages.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="phone number scraping tool")
    parser.add_argument("domain", help="the domain to scrape for phone numbers (e.g., example.com).")
    parser.add_argument("-d", "--depth", type=int, default=2, help="maximum depth for crawling subpages (default: 2).")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose mode.")
    parser.add_argument("-o", "--output", type=str, default="phonebook.txt", help="output file to save phone numbers (default: phonebook.txt).")
    args = parser.parse_args()

    crawl_domain(args.domain, output_file=args.output, max_depth=args.depth, verbose=args.verbose)
