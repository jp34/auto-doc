from collect.person.Person import Person
import os

dataTitles = ["Last Name", "First Name", "Address", "Apt", "City", "State", "Zip Code", "Home Number", "Mobile Number", "Email", "DOB"]

state_searches = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

apt_types = ['Apt', 'apt', 'pt', 'Suite', 'suite', 'uite', 'Unit', 'unit', '#']

class Collector:

    # Collector is passed a page object
    def __init__(self, input_path, file_range):
        self._input_path = input_path
        self._file_range = file_range

        self._path_1 = None
        self._path_2 = None
        self._path_3 = None

        self.__data_1 = None
        self.__data_2 = None
        self.__data_3 = None


    def collect(self):
        all_pops = []

        # Do for every file in range
        for i in range(self._file_range[0], self._file_range[1]):

            print('\n')
            print('[Info] Collection began on file:', i)
            print('\n')

            # Prepare paths
            file_name_1 = str(i) + '-1.txt'
            self._path_1 = self._input_path + file_name_1
            self._path_2 = self._input_path + str(i) + '-2.txt'
            self._path_3 = self._input_path + str(i) + '-3.txt'

            # Check if file exists
            if os.path.exists(self._path_1):
                # Open and assign data to instance variable

                file_1 = open(self._path_1, 'r')
                self.__data_1 = file_1.read()
                file_1.close()

                file_2 = open(self._path_2, 'r')
                self.__data_2 = file_2.read()
                file_2.close()

                file_3 = open(self._path_3, 'r')
                self.__data_3 = file_3.read()
                file_3.close()

                # Extract data
                pops = self.extract()

                for pop in pops:
                    all_pops.append(pop)

            else:
                continue

        return all_pops


    def extract(self):
        pops = []

        pop_data = [None, None, None, None, None, None, None, None, None, None, None]

        last_names, first_names, addresses, apts, cities, states, zip_codes, emails = self.first_page()
        home_numbers, mobile_numbers = self.second_page()
        birthdays = self.third_page()

        print(last_names)
        print(first_names)
        print(addresses)
        print(apts)
        print(cities)
        print(states)
        print(zip_codes)
        print(home_numbers)
        print(mobile_numbers)
        print(emails)
        print(birthdays)

        for index in range(len(last_names)):
            pop_data[0] = last_names[index]
            pop_data[1] = first_names[index]
            pop_data[2] = addresses[index]
            pop_data[3] = apts[index]
            pop_data[4] = cities[index]
            pop_data[5] = states[index]
            pop_data[6] = zip_codes[index]
            pop_data[7] = home_numbers[index]
            pop_data[8] = mobile_numbers[index]
            pop_data[9] = emails[index]
            pop_data[10] = birthdays[index]

            person = Person(pop_data)
            pops.append(person)

        for pop in pops:
            if not pop.check_adult():
                del pop

        return pops

    # Methods to organize data collection by page

    def first_page(self):
        # First, last, address, city, state, zip, email
        print('[Info] Started parse: Page one')
        last_names, first_names, name_indexes = self.find_names()
        addresses, inmates_found = self.find_addresses(name_indexes)
        apts = self.find_apt(name_indexes)
        cities, states, zips = self.find_location(inmates_found)
        emails = self.find_email(inmates_found)
        print('[Info] Finished parse: Page one')
        return last_names, first_names, addresses, apts, cities, states, zips, emails


    def second_page(self):
        # Home number, mobile number
        print('[Info] Started parse: Page two')
        numbers = self.find_numbers()
        print('[Info] Finished parse: Page two')
        return numbers


    def third_page(self):
        # Birthday, Gender
        print('[Info] Started parse: Page three')
        birthday = self.find_birthday()
        print('[Info] Finished parse: Page three')
        return birthday

    # Page 1 search methods

    def find_names(self):
        # Search first page for names
        data = self.__data_1.split('\n')
        last_name = []
        first_name = []
        indexes = []

        for line in data:
            split = line.split(' ')
            if len(split) >= 2 and len(split[0]) > 2:
                if split[0][-1] == ',':
                    if len(split[-1]) < 5 or len(split[-2]) > 2:
                        last_name.append(split[0][:-1])
                        split.pop(0)
                        first_name.append(" ".join(split))
                        indexes.append(data.index(line))

        return last_name, first_name, indexes


    def find_addresses(self, indexes):
        # Search first page for address
        data = self.__data_1.split('\n')
        addresses = []
        inmates_found = []
        for i in indexes:
            if len(data[i + 1]) > 5:
                addresses.append(data[i + 1])
            else:
                addresses.append(data[i + 2])

        return addresses, inmates_found


    def find_apt(self, indexes):
        # Search first page for apt
        data = self.__data_1.split('\n')
        apt = []
        for i in indexes:
            for search in apt_types:
                if search in data[i + 2]:
                    apt.append(data[i + 2])
                    break
                elif search in data[i + 3]:
                    apt.append(data[i + 3])
                    break
                elif search in data[i + 4]:
                    apt.append(data[i + 4])
                    break
                else:
                    apt.append(None)
                    break

        return apt

    def find_location(self, inmates):
        # Search first page for city, state, zip
        data = self.__data_1.split('\n')
        city = []
        state = []
        zip_codes = []

        index = 0
        for line in data:

            if len(inmates) > 0:
                for i in inmates:
                    if len(city) == i:
                        city.append('Inmate')
                        state.append('Inmate')
                        zip_codes.append('Inmate')
                        inmates.pop(inmates.index(i))
                        break

            for search in state_searches:
                split = line.split(' ')
                if search in split:
                    if split[-2] == search:
                        zip_codes.append(split[-1])
                        split.pop()

                        state.append(search)
                        split.pop()

                        city.append(" ".join(split)[:-1])
                        index += 1

        return city, state, zip_codes


    def find_email(self, inmates):
        # Search first page for emails
        data = self.__data_1.split('\n')
        emails = []
        email_search = ['E-Mail', 'Mail', 'mail', '@']

        for line in data:

            if len(inmates) > 0:
                for i in inmates:
                    if len(emails) == i:
                        emails.append('Inmate')
                        inmates.pop(inmates.index(i))
                        break

            for search in email_search:
                if search in line:
                    split = line.split(' ')
                    if len(split) == 1:
                        emails.append(None)
                        break
                    elif len(split) == 2:
                        emails.append(split[1])
                        break
                    else:
                        if len(split[-1]) > 6:
                            emails.append(split[-1])
                            break
                        else:
                            emails.append(None)
                            break

        return emails

    # Page 2 search methods

    def find_numbers(self):
        data = self.__data_2.split('\n')

        home_number = []
        mobile_number = []

        for line in data:

            split = line.split(' ')
            if len(split[-1]) >= 12:
                if split[-1][-5] == '-':
                    if 'H' in line:
                        home_number.append(split[-1])
                    elif '4) ' in line:
                        home_number.append(split[-1])
                    elif '1) ' in line:
                        home_number.append(split[-1])
                    elif 'W' in line:
                        continue
                    elif 'O' in line:
                        continue
                    else:
                        mobile_number.append(split[-1])

            if len(home_number) != len(mobile_number):
                if len(home_number) > len(mobile_number) + 1:
                    mobile_number.append(None)
                elif len(mobile_number) > len(home_number) + 1:
                    home_number.append(None)

        while True:
            if len(home_number) != len(mobile_number):
                if len(home_number) > len(mobile_number):
                    mobile_number.append(None)
                elif len(mobile_number) > len(home_number):
                    home_number.append(None)
            else:
                break

        return home_number, mobile_number

    # Page 3 search methods

    def find_birthday(self):
        # Searching third page for birthday
        data = self.__data_3.split('\n')

        birthday = []
        patient_count = 0

        index = 0
        for line in data:

            if index > 3:
                if len(birthday) < 1:
                    birthday.append(None)
                    continue

            if '/' in line:
                split = line.split(' ')
                if len(split[-1]) == 10:
                    birthday.append(split[-1])
                    continue

            if 'Patient' or 'atient' in line:
                patient_count += 1
                continue

            index += 1

            if len(birthday) != patient_count:
                if len(birthday) < patient_count + 1:
                    birthday.append(None)

        return birthday
