import csv

vaccinated = {}
#inserisco un dizionario vuoto da poter in seguito all'iterazione sommare ai miei risultati estratti dal file.csv
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\vaccinations.csv', mode = 'r') as file:
    leggi = csv.DictReader(file)
    for i in leggi:
        temp = {}
        #print(i)
        if i['total_vaccinations'] == '':
            i['total_vaccinations'] = 0
        else:
            i['total_vaccinations'] = int(i['total_vaccinations'])
        if vaccinated.get(i['location'], None) is None:
            vaccinated[i['location']] = {'total': i['total_vaccinations'] }
        else:
            vaccinated[i['location']]['total'] = vaccinated[i['location']]['total'] + i['total_vaccinations']
print(vaccinated)

#print(vaccinated['Afghanistan']['total'])

"""
vaccinated_day = {}
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\vaccinations.csv', mode = 'r') as file:
    leggi = csv.DictReader(file)
    for i in leggi:
        temp = {}
        vaccinated_day[i['location']] = {'n_giornaliero': i['total_vaccinations']}
        print(vaccinated_day)
        
        #for v in vaccinated_day[i['location']]:
            #remp = {}
       # if vaccinated_day.get(i['location'], None) is None:
           # vaccinated_day[v['Albania']] = {'total': v['n_giornaliero']}
       # else:
         #   vaccinated_day[v['Albania']]['total'] = vaccinated_day[v['Albania']]['total'] + v['n_giornaliero']
       # v['Albania'] =
        #print(vaccinated_day)
        #for t in vaccinated_day:
            #temp ={}
            #t[Albania] = int(t[albani])
           # print(t['Albania'])
"""


#print(vaccinated.get('Africa'),None)

#Ho ottenuto un dizionario avente come chiave 'locatione', cioè il paese di appartenenza dei vaccinati, e come valore un dizionario avente il totale dei vaccinati



