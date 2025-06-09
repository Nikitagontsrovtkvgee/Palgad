def lisa_inimesi(inimesed, palgad, mitu):
    for _ in range(mitu):
        inimesed.append(input("Sisesta nimi: "))
        palgad.append(int(input("Sisesta palk: ")))

def kustuta_isik(inimesed, palgad):
    while (nimi := input("Sisesta kustutatava isiku nimi (Enter lõpetab): ")):
        while nimi in inimesed:
            i = inimesed.index(nimi)
            inimesed.pop(i)
            palgad.pop(i)
            print(f"{nimi} eemaldatud.")

def suurim_palk(inimesed, palgad):
    max_palk = max(palgad)
    for nimi, palk in zip(inimesed, palgad):
        if palk == max_palk:
            print(f"Suurim palk: {nimi} - {palk}€")

def vaikseim_palk(inimesed, palgad):
    min_palk = min(palgad)
    for nimi, palk in zip(inimesed, palgad):
        if palk == min_palk:
            print(f"Väikseim palk: {nimi} - {palk}€")

def sorteeri_palgad(inimesed, palgad, kasvav=True):
    for nimi, palk in sorted(zip(inimesed, palgad), key=lambda x: x[1], reverse=not kasvav):
        print(f"{nimi}: {palk}€")

def votrdsed_palgad(inimesed, palgad): #Одинаковые зарплаты
    from collections import defaultdict
    d = defaultdict(list)
    for nimi, palk in zip(inimesed, palgad):
        d[palk].append(nimi)
    for palk, nimed in d.items():
        if len(nimed) > 1:
            print(f"{palk}€ saavad: {', '.join(nimed)} (kokku {len(nimed)})")

def otsi_palk_nime_jargi(inimesed, palgad):
    nimi = input("Sisesta otsitav nimi: ").lower()
    for n, p in zip(inimesed, palgad):
        if n.lower() == nimi:
            print(f"{n} saab {p}€")

def suurem_vaiksem_summa(inimesed, palgad):
    valik = input("Kas soovid 'suurem' või 'väiksem' kui summa? ")
    piir = int(input("Sisesta summa: "))
    for nimi, palk in zip(inimesed, palgad):
        if (valik == "suurem" and palk > piir) or (valik == "väiksem" and palk < piir):
            print(f"{nimi} - {palk}€")

def top_inimesed(inimesed, palgad, T=3):
    top = sorted(zip(inimesed, palgad), key=lambda x: x[1])
    print(f"\nTOP {T} vaeseimat:")
    for nimi, palk in top[:T]: print(f"{nimi}: {palk}€")
    print(f"\nTOP {T} rikkamat:")
    for nimi, palk in top[-T:]: print(f"{nimi}: {palk}€")

def keskmine_palk(inimesed, palgad):
    k = sum(palgad) / len(palgad)
    print(f"Keskmine palk: {k:.2f}€")
    for nimi, palk in zip(inimesed, palgad):
        if palk == round(k):
            print(f"{nimi} saab täpselt keskmist palka.")

def tulumaks(inimesed, palgad):
    for nimi, palk in zip(inimesed, palgad):
        print(f"{nimi}: Bruto {palk}€, Neto {palk * 0.8:.2f}€")

def sorteeri_nimed(inimesed, palgad, reverse=False):
    for nimi, palk in sorted(zip(inimesed, palgad), key=lambda x: x[0], reverse=reverse):
        print(f"{nimi}: {palk}€")

def kustuta_alla_keskmise(inimesed, palgad):
    k = sum(palgad) / len(palgad)
    i = 0
    while i < len(palgad):
        if palgad[i] < k:
            print(f"Kustutatud: {inimesed[i]} - {palgad[i]}€")
            inimesed.pop(i)
            palgad.pop(i)
        else:
            i += 1

def puhasta_andmed(inimesed, palgad):
    for i in range(len(inimesed)):
        inimesed[i] = inimesed[i].capitalize()
        palgad[i] = int(palgad[i])

def prognoos_palk(inimesed, palgad, T):
    nimi = input("Sisesta isiku nimi: ")
    for i, n in enumerate(inimesed):
        if n == nimi:
            print(f"{n} palk {T} aasta pärast: {palgad[i] * (1.05 ** T):.2f}€")

def nime_muutmine(inimesed):
    for i in range(2, len(inimesed), 3):
        inimesed[i] = input(f"Sisesta uus nimi isikule {inimesed[i]}: ")

def redigeeri_andmeid(inimesed, palgad):
    nimi = input("Sisesta isiku nimi: ")
    for i, n in enumerate(inimesed):
        if n == nimi:
            v = input("Muuda 'nimi' või 'palk'? ")
            if v == "nimi":
                inimesed[i] = input("Sisesta uus nimi: ")
            elif v == "palk":
                palgad[i] = int(input("Sisesta uus palk: "))

def otsi_tahe_jargi(inimesed, palgad):
    täht = input("Sisesta täht: ").lower()
    for nimi, palk in zip(inimesed, palgad):
        if nimi.lower().startswith(täht):
            print(f"{nimi} - {palk}€")

def naljakas_funktsioon(inimesed, palgad):
    def suhe(nimi, palk): return palk / (len(nimi) + 1)
    max_s = max(suhe(n, p) for n, p in zip(inimesed, palgad))
    for nimi, palk in zip(inimesed, palgad):
        if suhe(nimi, palk) == max_s:
            print(f"'{nimi}' on efektiivseim: {palk}€ nime pikkusega {len(nimi)}.")
