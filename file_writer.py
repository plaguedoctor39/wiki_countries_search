from wiki_search import country_search
from iter_hash import do_hash


def writer(countries):
    with open('result.txt', 'w') as f:
        for country in countries:
            f.write(f'{country} - {country_search(country)}\n')

