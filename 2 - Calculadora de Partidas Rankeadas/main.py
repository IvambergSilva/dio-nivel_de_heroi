vitorias = int(input("Numero de vitorias: \n"))
derrotas = int(input("Numero de derrotas: \n"))
nivel = ""

def ranker(vitorias, derrotas):
    saldo = vitorias - derrotas
    return saldo
    
saldoVitorias = ranker(vitorias, derrotas)

if saldoVitorias < 10:
    nivel = "Ferro"
elif 11 <= saldoVitorias <= 20:
    nivel = "Bronze"
elif 21 <= saldoVitorias <= 50:
    nivel = "Prata"
elif 51 <= saldoVitorias <= 80:
    nivel = "Ouro"
elif 81 <= saldoVitorias <= 90:
    nivel = "Diamante"
elif 91 <= saldoVitorias <= 100:
    nivel = "Lendario"
else:
    nivel = "Imortal"

print(f"O Heroi tem de saldo de {saldoVitorias} esta no nivel de {nivel}")
