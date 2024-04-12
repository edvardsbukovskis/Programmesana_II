skaitlu_saraksts = {}
for i in range(0, 5):
    skaitlu_saraksts[i] = []

while True:
    skaitlis = input("Ievadi skaitli: ")
    if skaitlis.isnumeric():
        skaitlis = int(skaitlis)
        skaitlu_saraksts[skaitlis % 5].append(skaitlis)
        print(f"Grupai {skaitlis%5} tiek pievienots {skaitlis}")
        print(skaitlu_saraksts)
    elif skaitlis == "exit":
        break
    else:
        print("Nepareizs skaitlis")
        pass
    

    

    
