class City:
    def __init__(self, city, name, region, country):

        self.city = city
        self.name = name
        self.region = region
        self.country = country

    def set_data(self, city=None, name=None, region=None, country=None):

        if city is not None:
            self.city = city
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country

    def get_data(self):

        print(
            f"Město: {self.city}\n"
            f"Jméno: {self.name}\n"
            f"Region: {self.region}\n"
            f"Země: {self.country}"
        )


    def get_city(self):
        print(f"Město: {self.city}")

    def set_city(self, city):
        self.city = city

    def get_name(self):
        print(f"Jméno: {self.name}")

    def set_name(self, name):
        self.name = name

    def get_region(self):
        print(f"Region: {self.region}")

    def set_region(self, region):
        self.region = region

    def get_country(self):
        print(f"Země: {self.country}")

    def set_country(self, country):
        self.country = country


brno = City("Brno", "Fakepraha", "SkoroRusko", "CZ")

print(brno)