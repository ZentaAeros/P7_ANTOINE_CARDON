import csv
from tqdm import tqdm
from time import strftime

MAX_INVEST = 500

def read_file(file_csv):
    datas = []
    with open(file_csv) as file:
        reader = csv.DictReader(file, delimiter=",")
        for line in reader:
            actions = (line["action"], float(line["price"]), float(line["profit"]))
            datas.append(actions)
    
    return datas

def get_best_combo(datas):
    price = 0
    profit = 0
    for action in datas:
        if price + action[1] < MAX_INVEST and action[1] > 0:
            print(f"{action[0]} : {action[1]}€ - {action[2]}%")
            price += action[1]
            win = action[1] * action[2] / 100
            profit += win
    print(f"+ {profit} €")

print(f"Recherche démarrée à {strftime('%H:%M:%S')}")
start = int(strftime('%S'))
actions = read_file('dataset2.csv')
sorted_actions = sorted(actions, key=lambda action: action[2], reverse=True)
get_best_combo(sorted_actions)
end = int(strftime('%S'))
delay = end - start

print(f"Temps d'exécution : {delay} secondes")
print(f"Recherche terminée à {strftime('%H:%M:%S')}")
