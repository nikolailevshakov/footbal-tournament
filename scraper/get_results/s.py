import os


path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
p = os.path.join(os.getcwd(), "players_preds")

for filename in os.listdir(p):
    predictions = []
    with open(os.path.join(p, filename), 'r') as f:
        s = f.readlines()

s = [el.replace('\n', '') for el in s]
print(s)