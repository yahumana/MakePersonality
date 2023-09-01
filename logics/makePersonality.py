from names_dataset import NameDataset
from random_username.generate import generate_username
import random, time


class MakePersonality(NameDataset):
    """
        Class for make Personality

        Create pair name and lastname
        Create Date of Birth (dob)
    """

    def __init__(self, country="", gender=""):
        """

        :param country: country code in alpha_2
        """

        super().__init__()

        # Add fields to class
        self.gender = None
        self.country = None
        self.dob = None
        self.name = None
        self.lastname = None
        self.username = None

        self.set_country(country)
        self.set_gender(gender)
        self.gen_username()
        self.gen_name()
        self.gen_dob()

    def gen_personality(self):
        self.gen_username()
        self.gen_name()
        self.gen_dob()

    def get_personality(self):
        return {
            'name': self.name,
            'lastname': self.lastname,
            'dob': self.dob,
            'username': self.username,
            'sex': self.gender,
            'country': self.country,
        }

    def gen_dob(self, start="1/1/1970", end="1/1/2005"):
        """
        Method for create Date of Birth
        :param start:
        :param end:
        :return:
        """
        format = '%d/%m/%Y'

        start = time.mktime(time.strptime(start, format))
        end = time.mktime(time.strptime(end, format))

        ptime = start + random.random() * (end - start)

        self.dob = time.strftime(format, time.localtime(ptime))

    def gen_gender(self):
        if random.randint(0, 1) == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"

    def set_gender(self, gender):
        if gender == "":
            self.gen_gender()
        else:
            self.gender = gender

    def gen_country(self):
        country_codes = self.get_country_codes(alpha_2=True)
        self.country = country_codes[random.randint(0, len(country_codes) - 1)]

    def set_country(self, country):
        if country == "":
            self.gen_country()
        else:
            self.country = country

    def gen_name(self):
        """
        Method for create Personality
        :param country: country code in alpha_2
        :return:
        """
        names = self.get_top_names(n=random.randint(100, 10000), gender=self.gender, country_alpha2=self.country)
        names = names[self.country][self.gender[0]]
        self.name = names[random.randint(0, len(names) - 1)]

        lastnames = self.get_top_names(n=random.randint(100, 10000), use_first_names=False, country_alpha2=self.country)
        lastnames = lastnames[self.country]
        self.lastname = lastnames[random.randint(0, len(lastnames) - 1)]

    def gen_username(self):
        self.username = generate_username(1)[0]


if __name__ == '__main__':
    m = MakePersonality(country='RU')
    print(m.get_personality())
