pole = ["oheň", "voda", "teplo", "zima", "sníh"] #vytvoření pole s 5 stringovými hodnotami
print(pole)#výpis kodu

pole.append("vítr")#přidání jednoho prvku pomocí append
print(pole)#výpis kodu

pole.remove("voda")#odstranění druhého prvku pomocí remove
print(pole)#výpis kodu

pole[4] = "slunce"#změna páté hodnoty na slunce
print(pole)#výpis kodu

pole.extend(["podzim", "jaro"])#přidání dvou dalších stringových hodnot pomocí extend
print(pole)#výpis kodu

