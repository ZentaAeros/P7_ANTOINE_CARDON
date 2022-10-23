import csv
from itertools import combinations

def read_file(document):
    datas = []
    with open(document) as file:
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
    for i in range(len(file)):
        combinaisons = combinations(file, i+1)

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

    return {"euros":somme, "pourcentage":gain}

filename = read_file('datas.csv')
get_combination(filename)