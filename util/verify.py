class Verify:
    def validate_aluno(self, aluno):
        if 'nome' not in aluno.keys():
            print(aluno.keys())
            return 400
        return 200

