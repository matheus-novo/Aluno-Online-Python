import random
from security.pass_verifier import PasswordVerifier

class PasswordGenerator:
    def __init__(self):
        self.pass_verifier = PasswordVerifier()
        return

    def gerar(self, length):
        if length < 4:
            return "Tamanho invalido"
        contador = 0
        while contador < 5000000:
            contador += 1

            lista = [random.randrange(48, 123) for i in range(1, length+1)]
            senha = str(''.join(chr(i) for i in lista))

            if self.pass_verifier.verify(senha):
                return senha

