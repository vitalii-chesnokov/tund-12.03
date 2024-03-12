from MinuOmaMoodul import*

n=input("Sisestage oma nimi: ")
kus_vas={}

küsimused, vastus=loe_ankeet("Ankeet.txt")
print(küsimused)
input(vastus)
for i in range(len(küsimused)):
    print(f"{i+1}.küsimus on: "+küsimused[1]+", vastus on: "+vastus[i])
