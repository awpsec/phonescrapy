# phonescrapy

```

 ,--.  _   _   __  _ .--.   .--.  .---.  .---.
`'_\ :[ \ [ \ [  ][ '/'`\ \( (`\]/ /__\/ /'`\]
// | |,\ \/\ \/ /  | \__/ | `'.'.| \__.,| \__.
'-;__/ \__/\__/   | ;.__/ [\__) )'.__.''.___.'
                  [__|

usage: phonescrapy.py [-h] [-d DEPTH] [-v] [-o OUTPUT] domain

Phone Number Scraper Tool

positional arguments:
  domain                The domain to scrape for phone numbers (e.g., tesla.com).

options:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        Maximum depth for crawling subpages (default: 2).
  -v, --verbose         Enable verbose mode.
  -o OUTPUT, --output OUTPUT
                        Output file to save phone numbers (default: phonebook.txt).
```

# usage

python3 phonescrapy.py www.example.com -d 2 -v -o example_phones.txt

# installation

```chmod +x setup.sh```
```./setup.sh```
```source scrapy-env/bin/activate```

done
