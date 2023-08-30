from Aluno import Aluno
from ValidadorAluno import ValidadorAluno
# Exemplo de uso
aluno1 = Aluno("12345670", "Fernando")
aluno2 = Aluno("7654321", "Samanta")

if ValidadorAluno.validar_RA(aluno1.ra) and ValidadorAluno.validar_nome(aluno1.nome):
    print(f"Aluno 1: RA {aluno1.ra} - Nome {aluno1.nome} é válido.")
else:
    print(f"Aluno 1: RA {aluno1.ra} - Nome {aluno1.nome} é inválido.")

if ValidadorAluno.validar_RA(aluno2.ra) and ValidadorAluno.validar_nome(aluno2.nome):
    print(f"Aluno 2: RA {aluno2.ra} - Nome {aluno2.nome} é válido.")
else:
    print(f"Aluno 2: RA {aluno2.ra} - Nome {aluno2.nome} é inválido.")