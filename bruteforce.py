import csv
from itertools import combinations
from tqdm import tqdm
from time import strftime

def read_file(file_csv):
    datas = []
    with open(file_csv) as file:
        reader = csv.DictReader(file, delimiter=",")
        for line in reader:
            value = (line["action"], line["price"], line["profit"])
            datas.append(value)

    return datas


def display_actions(combinaison):
    for combi in combinaison:
        ligne = f"{combi[0]} : {combi[1]}€ - {combi[2]}%"
        print(ligne)


def get_combination(file):
    gain = 0
    for i in tqdm(range(len(file))):
        combinaisons = combinations(file, i + 1)

        for combinaison in combinaisons:
            somme = calcul_investissement(combinaison)
            if somme["euros"] <= 500:
                if somme["pourcentage"] > gain:
                    gain = somme["pourcentage"]
                    investissement = combinaison

    display_actions(investissement)
    print()
    print(f"Bénéfices après 2 ans : +{gain}€")


def calcul_investissement(combinaison):
    somme = 0
    gain = 0
    for combi in combinaison:
        somme += float(combi[1])

        calcul = (float(combi[1]) * float(combi[2])) / 100
        gain += calcul

    return {"euros": somme, "pourcentage": gain}

print()
print(f"Recherche démarrée à {strftime('%H:%M:%S')}")
print()
start = int(strftime('%S'))
filename = read_file("datas2.csv")
get_combination(filename)
end = int(strftime('%S'))
delay = end - start
print()
print(f"Recherche terminée à {strftime('%H:%M:%S')}")
print()
print(f"Temps d'exécution : {delay} secondes")
