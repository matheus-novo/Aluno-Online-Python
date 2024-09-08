class PasswordVerifier:
    def __init__(self):
        self.invalid_chars = [34, 39, 40, 41, 43, 44, 46, 47, 58, 59, 60, 61, 62, 91, 92, 93, 94, 95, 96]
        self.lower_char = [c for c in range(97, 123)]
        self.upper_char = [c for c in range(65, 91)]
        self.number_char = [c for c in range(48, 58)]
        all_chars = self.upper_char + self.lower_char + self.number_char + self.invalid_chars
        self.especial_char = [c for c in range(33, 123) if c not in all_chars]


    def verify(self, password):
        self.has_lower = False
        self.has_upper = False
        self.has_number = False
        self.has_especial = False

        for caractere in password:
            if ord(caractere) < 33 or ord(caractere) > 122:
                return False
            elif ord(caractere) in self.invalid_chars:
                return False

            if ord(caractere) in self.lower_char:
                self.has_lower = True
            elif ord(caractere) in self.upper_char:
                self.has_upper = True
            elif ord(caractere) in self.number_char:
                self.has_number = True
            elif ord(caractere) in self.especial_char:
                self.has_especial = True

        if self.has_lower and self.has_upper and self.has_number and self.has_especial:
            return True
        return False

