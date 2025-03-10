import pandas as pd

print(f"nom du module1 est :{__name__}")

print(f"nom du module2 est:  {__name__}")

print("executer dans tous les cas")

if __name__ == '__main__':
    print("le module est exécuté en tant que script principal")

else:

    print("le module est pandas")