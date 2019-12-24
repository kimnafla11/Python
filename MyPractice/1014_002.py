r = int(input("원의 반지름 = ",))
def nulbi(r):
    nul = r*r*3.14
    return nul
def dulle(r):
    dul = 2*r*3.14
    return dul
print("원의 넓이 = ",nulbi(r))
print("원의 둘레 = ", dulle(r))