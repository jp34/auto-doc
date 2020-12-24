class Person:

    def __init__(self, data):
        self._last = data[0]
        self._first = data[1]
        self._address = data[2]
        self._apt = data[3]
        self._city = data[4]
        self._state = data[5]
        self._zip_code = data[6]
        self._home = data[7]
        self._mobile = data[8]
        self._email = data[9]
        self._dob = data[10]

    def check_adult(self):
        if self._dob is not None:
            birth_year = self._dob[-4:]
            current_age = 2020 - int(birth_year)
            if current_age >= 18:
                return True
            else:
                return False
        else:
            return True

    def get_print_info(self):
        # Format info and return data

        # Format email
        if self._email == "None":
            email = ""
        elif self._email == "_":
            email = ""
        else:
            email = self._email

        # Format address
        if str(self._apt) == "None":
            full_address = self._address
        else:
            full_address = self._address + " " + self._apt

        phone_misc = ['(', '.', "'"]

        # Format home number
        if self._home is not None:
            new_home = ''
            for char in self._home:
                if char == '(':
                    continue
                elif char == "'":
                    continue
                elif char == '.':
                    continue
                elif char == ')':
                    new_home += '-'
                else:
                    new_home += char
            self._home = new_home

        # Format mobile number
        if self._mobile is not None:
            new_mobile = ''
            for char in self._mobile:
                if char == '(':
                    continue
                elif char == "'":
                    continue
                elif char == '.':
                    continue
                elif char == ')':
                    new_mobile += '-'
                else:
                    new_mobile += char

            self._mobile = new_mobile

        # Format birthday
        if self._dob is not None:
            new_dob = ''
            for char in self._dob:
                if char == '/':
                    new_dob += '-'
                else:
                    new_dob += char
            self._dob = new_dob

        return self._last, self._first, full_address, self._city, self._state, self._zip_code, self._home, self._mobile, email, self._dob

    def __repr__(self):
        return f"{self._last}, {self._first}:" \
               f"{self._address}, {self._apt}, {self._city}, {self._state} {self._zip_code}; {self._dob};" \
               f"Home: {self._home} Mobile: {self._mobile} EMail: {self._email}"
