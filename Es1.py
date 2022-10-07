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
            i['total_vaccinations'] = float(i['total_vaccinations'])
        if vaccinated.get(i['location'], None) is None:
            vaccinated[i['location']] = {'total': i['total_vaccinations'] }
        else:
            vaccinated[i['location']]['total'] = vaccinated[i['location']]['total'] + i['total_vaccinations']
#print(vaccinated)
#Ho ottenuto un dizionario avente come chiave il paese e valore il totale dei vaccinati in quel determinato paese
italia_vax = vaccinated['Italy']['total']
spagna_vax = vaccinated['Spain']['total']
eu_vax = vaccinated['Europe']['total']
usa_vax = vaccinated['North America']['total']
#print('il nr di vaccinati in italia_vax è:', italia_vax, 'mentre in Spagna è:', spagna_vax )
rapp_ita_vax =italia_vax/eu_vax*100
rapp_spa_vax =spagna_vax/eu_vax*100

print('il nr di vaccinati in italia è:', italia_vax, 'mentre in Spagna è:', spagna_vax)
print('Il numero dei vaccinati in Europa è complessivamente pari a:', eu_vax, '. Invece il numero dei vaccinati in America del Nord è complessivamente pari a:', usa_vax)
print('In percentuale i vaccinati in Italia sono:', rapp_ita_vax, '. In percentuale i vaccinati in Spagna sono:', rapp_spa_vax)