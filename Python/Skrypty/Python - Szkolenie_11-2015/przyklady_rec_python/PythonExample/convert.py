f = open('data.csv','r')

# Zlicz wiersze ktorych suma ma wartosc powyzej 50
lin = 0
for line in f.xreadlines():
    # poprawienie formatu poprzez
    #   1. Zamiane "," w kazdym polu na kropke
    #   2. Oddzielenie pol przez ","
    line = line.replace(',','.').replace("'.'", ',')
    # obliczenie sumy danych w wierszu
    print line.split(',')
    lin += 1
print lin
