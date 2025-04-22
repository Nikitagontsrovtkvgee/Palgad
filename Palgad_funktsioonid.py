def lisa_inimesi(inimesed, palgad, mitu):
    for _ in range(mitu):
        nimi = input("Sisesta nimi: ")
        palk = int(input("Sisesta palk: "))
        inimesed.append(nimi)
        palgad.append(palk)

def kustuta_isik(inimesed, palgad):
    nimi = input("Sisesta kustutatava isiku nimi: ")
    while nimi in inimesed:
        indeks = inimesed.index(nimi)
        inimesed.pop(indeks)
        palgad.pop(indeks)
        print(f"{nimi} eemaldatud.")
        nimi = input("Sisesta järgmine või vajuta Enter lõpetamiseks: ")

def suurim_palk(inimesed, palgad):
    max_palk = max(palgad)
    for i, palk in enumerate(palgad):
        if palk == max_palk:
            print(f"Suurim palk: {inimesed[i]} - {palk}€")

def vaikseim_palk(inimesed, palgad):
    min_palk = min(palgad)
    for i, palk in enumerate(palgad):
        if palk == min_palk:
            print(f"Väikseim palk: {inimesed[i]} - {palk}€")

def sorteeri_palgad(inimesed, palgad, kasvav=True):
    kokku = list(zip(inimesed, palgad))
    kokku.sort(key=lambda x: x[1], reverse=not kasvav)
    for nimi, palk in kokku:
        print(f"{nimi}: {palk}€")

def votrdsed_palgad(inimesed, palgad):
    palk_dict = {}
    for nimi, palk in zip(inimesed, palgad):
        palk_dict.setdefault(palk, []).append(nimi)
    for palk, nimed in palk_dict.items():
        if len(nimed) > 1:
            print(f"{palk}€ saavad: {', '.join(nimed)} (kokku {len(nimed)})")

def otsi_palk_nime_jargi(inimesed, palgad):
    nimi = input("Sisesta otsitav nimi: ")
    for i, nimi_ in enumerate(inimesed):
        if nimi_.lower() == nimi.lower():
            print(f"{nimi_} saab {palgad[i]}€")

def suurem_vaiksem_summa(inimesed, palgad):
    valik = input("Kas soovid 'suurem' või 'väiksem' kui summa? ")
    piir = int(input("Sisesta summa: "))
    for nimi, palk in zip(inimesed, palgad):
        if (valik == "suurem" and palk > piir) or (valik == "väiksem" and palk < piir):
            print(f"{nimi} - {palk}€")

def top_inimesed(inimesed, palgad, T=3):
    kokku = list(zip(inimesed, palgad))
    kokku.sort(key=lambda x: x[1])
    print(f"\nTOP {T} vaeseimat:")
    for nimi, palk in kokku[:T]:
        print(f"{nimi}: {palk}€")
    print(f"\nTOP {T} rikkamat:")
    for nimi, palk in kokku[-T:]:
        print(f"{nimi}: {palk}€")

def keskmine_palk(inimesed, palgad):
    keskmine = sum(palgad) / len(palgad)
    print(f"Keskmine palk: {keskmine:.2f}€")
    for i, palk in enumerate(palgad):
        if palk == round(keskmine):
            print(f"{inimesed[i]} saab täpselt keskmist palka.")

def tulumaks(inimesed, palgad):
    for i, palk in enumerate(palgad):
        netto = palk * 0.8  # oletame 20% tulumaks
        print(f"{inimesed[i]}: Bruto {palk}€, Neto {netto:.2f}€")

def sorteeri_nimed(inimesed, palgad, reverse=False):
    kokku = list(zip(inimesed, palgad))
    kokku.sort(key=lambda x: x[0], reverse=reverse)
    for nimi, palk in kokku:
        print(f"{nimi}: {palk}€")

def kustuta_alla_keskmise(inimesed, palgad):
    keskmine = sum(palgad) / len(palgad)
    i = 0
    while i < len(palgad):
        if palgad[i] < keskmine:
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
    for i in range(len(inimesed)):
        if inimesed[i] == nimi:
            tulevikupalk = palgad[i] * ((1.05) ** T)
            print(f"{nimi} palk {T} aasta pärast: {tulevikupalk:.2f}€")

def nime_muutmine(inimesed):
    for i in range(2, len(inimesed), 3):
        uus_nimi = input(f"Sisesta uus nimi isikule {inimesed[i]}: ")
        inimesed[i] = uus_nimi

def redigeeri_andmeid(inimesed, palgad):
    nimi = input("Sisesta isiku nimi: ")
    for i, n in enumerate(inimesed):
        if n == nimi:
            valik = input("Muuda 'nimi' või 'palk'? ")
            if valik == "nimi":
                uus = input("Sisesta uus nimi: ")
                inimesed[i] = uus
            elif valik == "palk":
                uus = int(input("Sisesta uus palk: "))
                palgad[i] = uus

def otsi_tahe_jargi(inimesed, palgad):
    täht = input("Sisesta täht: ").lower()
    for nimi, palk in zip(inimesed, palgad):
        if nimi.lower().startswith(täht):
            print(f"{nimi} - {palk}€")

def naljakas_funktsioon(inimesed, palgad):
    # 19 - Väljastab inimestest ja palkadest kõige naljakama "palk inimese kohta" suhet
    max_suhe = max(palk / (len(nimi) + 1) for nimi, palk in zip(inimesed, palgad))
    for nimi, palk in zip(inimesed, palgad):
        if palk / (len(nimi) + 1) == max_suhe:
            print(f"'{nimi}' on efektiivseim: {palk}€ nime pikkusega {len(nimi)}.")