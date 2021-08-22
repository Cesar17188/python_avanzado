# union
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
print(my_set3)

# 3,4,5,6,7

# Interseccion

imy_set1 = {3,4,5}
imy_set2 = {5,6,7}

imy_set3 = imy_set1 & imy_set2
print(my_set3)

# Diferencia

dmy_set1 = {3,4,5}
dmy_set2 = {5,6,7}

dmy_set3 = dmy_set1 - dmy_set2
print(dmy_set3)

dmy_set4 = dmy_set2 - dmy_set1
print(dmy_set4)

# Diferecia simetrica
dfmy_set1 = {3,4,5}
dfmy_set2 = {5,6,7}

dfmy_set3 = dfmy_set1 ^ dfmy_set2
print(dfmy_set3)