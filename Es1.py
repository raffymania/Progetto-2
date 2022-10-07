import csv
vaccinated = {}
popolazione_ita = 595800000
popolazione_spa = 478500000

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
#print(vaccinated)
#Ho ottenuto un dizionario avente come chiave il paese e valore il totale dei vaccinati in quel determinato paese
italia_vax = vaccinated['Italy']['total']
ita_vax_pop = italia_vax/popolazione_ita
spagna_vax = vaccinated['Spain']['total']
spa_vax_pop = spagna_vax/popolazione_spa
#print('il nr di vaccinati in italia_vax è:', italia_vax, 'mentre in Spagna è:', spagna_vax )
europa = vaccinated['Europe']['total']
eu_pop = 746500000
nord_ame_pop = 579000000
eu_vax_pop = europa/eu_pop
nord_america = vaccinated['North America']['total']
nord_vax_pop = nord_america/nord_ame_pop
print('il nr di vaccinati in italia è:', italia_vax, 'mentre in Spagna è:', spagna_vax)
print('Il numero dei vaccinati in Europa è complessivamente pari a:', europa, '. Invece il numero dei vaccinati in America del Nord è complessivamente pari a:', nord_america)
print('In percentuale i vaccinati in Italia sono:', ita_vax_pop, '. In percentuale i vaccinati in Spagna sono:', spa_vax_pop)
print('In percentuale i vaccinati in Europa sono:', eu_vax_pop, '. In percentuale i vaccinati in America sono:', nord_vax_pop)