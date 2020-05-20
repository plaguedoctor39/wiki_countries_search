class Countries:
    countries_list = []

    def __init__(self, json_):
        for country in json_:
            self.countries_list.append(country['name']['common'])

    def __iter__(self):
        return iter(self.countries_list)

    def __next__(self):
        try:
            next_country = next(self.countries_list)
        except StopIteration:
            raise StopIteration
        return next_country
