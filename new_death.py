import csv
import statistics
death_days= {}
#inserisco un dizionario vuoto da poter in seguito all'iterazione sommare ai miei risultati estratti dal file.csv
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\coviddataaprire.csv', mode = 'r') as file:
    leggi = csv.DictReader(file)
    for i in leggi:
        temp = {}
        d = i.items()
        #print(i)
        if i['new_deaths'] == '':
            i['new_deaths'] = 0
        else:
            i['new_deaths'] = float(i['new_deaths'])
        if death_days.get(i['location'], None) is None:
            death_days[i['location']] = {'total': i['new_deaths']}
        else:
            death_days[i['location']]['total'] = death_days[i['location']]['total'] + i['new_deaths']
        print(death_days)




"""
cases = {}
#inserisco un dizionario vuoto da poter in seguito all'iterazione sommare ai miei risultati estratti dal file.csv
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\coviddataaprire.csv', mode = 'r') as file:
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
"""