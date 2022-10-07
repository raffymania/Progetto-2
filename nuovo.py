import csv

cases = {}
#inserisco un dizionario vuoto da poter in seguito all'iterazione sommare ai miei risultati estratti dal file.csv
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\coviddataaprire.csv', mode = 'r') as file:
    leggi = csv.DictReader(file)
    for i in leggi:
        temp = {}
        d = i.items()
        print(i)



        #if i['total_cases'] == '':
         #   i['total_cases'] = 0
        #else:
           # i['total_cases'] = float(i['total_cases'])
        #if cases.get(i['location'], None) is None:
         #   cases[i['location']] = {'total': i['total_cases']}
       # else:
          #  cases[i['location']]['total'] = cases[i['location']]['total'] + i['total_cases']
   # print(cases['location'])
#t = {'Algeria', 'Afghanistan'}
#for i in cases:
#    print(t)
        #location = i(['data']['total_vaccinations'])
        #print(location)
        #i['total_vaccinations'] = int(i['total_vaccinations'])
        #print('total_vaccinations')
