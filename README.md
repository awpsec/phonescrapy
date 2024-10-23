# phonescrapy

```
 ,--.  _   _   __  _ .--.   .--.  .---.  .---.
`'_\ :[ \ [ \ [  ][ '/'`\ \( (`\]/ /__\/ /'`\]
// | |,\ \/\ \/ /  | \__/ | `'.'.| \__.,| \__.
'-;__/ \__/\__/   | ;.__/ [\__) )'.__.''.___.'
                  [__|
            ,---.,---.,---.,---.,---.,   .
            `---.|    |    ,---||   ||   |
            `---'`---'`    `---^|---'`---|
                                |    `---'

usage: phonescrapy.py [-h] [-d DEPTH] [-v] [-o OUTPUT] domain

phone number scraping tool

positional arguments:
  domain                the domain to scrape for phone numbers (e.g., example.com).

options:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        maximum depth for crawling subpages (default: 2).
  -v, --verbose         enable verbose mode.
  -o OUTPUT, --output OUTPUT
                        output file to save phone numbers (default: phonebook.txt).
```

# usage

python3 phonescrapy.py www.example.com -d 2 -v -o example_phones.txt

phonescrapy will take a client's tld and click links (depth decides how far it goes with this), identifying any and all phone numbers listed in different destinations on the site.

# installation

```chmod +x setup.sh```
```./setup.sh```
```source scrapy-env/bin/activate```

done
