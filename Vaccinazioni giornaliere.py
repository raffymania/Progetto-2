import csv
daily_vaccinations_per_million = {}
#inserisco un dizionario vuoto da poter in seguito all'iterazione sommare ai miei risultati estratti dal file.csv
with open('C:\\Users\\Utente\Documents\\Raffaele Fiordoro\\vaccinations.csv', mode = 'r') as file:
    leggi = csv.DictReader(file)
    for i in leggi:
        temp = {}
        if i['daily_vaccinations_per_million'] == '':
            i['daily_vaccinations_per_million'] = 0
        else:
            i['daily_vaccinations_per_million'] = int(i['daily_vaccinations_per_million'])
        if daily_vaccinations_per_million.get(i['location'], None) is None:
            daily_vaccinations_per_million[i['location']] = {'total': i['daily_vaccinations_per_million'] }
        else:
            daily_vaccinations_per_million[i['location']]['total'] = daily_vaccinations_per_million[i['location']]['total'] + i['daily_vaccinations_per_million']
print(daily_vaccinations_per_million)
#Ho ottenuto un dizionario avente come chiave il paese e valore il totale dei vaccinati in quel determinato paese
italia_vax = daily_vaccinations_per_million['Italy']['total']
spagna_vax = daily_vaccinations_per_million['Spain']['total']
eu_vax = daily_vaccinations_per_million['Europe']['total']
north_america_vax = daily_vaccinations_per_million['North America']['total']

print('Il numero di vaccinati per milioni di abitanti in Italia è:', italia_vax,'mentre il numero di vaccinati per milioni di abitanti in Spagna è:', spagna_vax)
print('Il numero di vaccinati per milioni di abitanti in Nord America è:', north_america_vax,'mentre il numero di vaccinati per milioni di abitanti in Europa è:', eu_vax)
"""
Ho confrontato Italia e Spagna in quanto la densità di popolazione dei due paesi è molto simile, 
mentre il confronto tra Europa e Nord America è dovuto alla similitudine nel numero del campione e dei dati che erano a disposizione
"""

