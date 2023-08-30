class ValidadorAluno:
    @staticmethod
    def validar_RA(ra):
        return ra.isnumeric() and len(ra) == 7

    @staticmethod
    def validar_nome(nome):
        return len(nome) > 0
