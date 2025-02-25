temps = int(input("Vazy frr, envoie un blase de secondes là : "))

jrs = temps // 86400
reste = temps % 86400  

hrs = reste // 3600
reste = reste % 3600  

minos = reste // 60
secs = reste % 60

print(f"{jrs} jrs, {hrs} hrs, {minos} minos, {secs} secs, la street validé frr")