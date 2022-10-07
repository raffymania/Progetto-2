import csv
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
#ho ettunuto una sequenza di dizionari dove per ogni paese mi associa il numero di morti complessivo
eu_pop = 746500000
nord_ame_pop = 579000000
ita_pop = 595800000
spa_pop = 478500000
italia_death = death_days['Italy']['total']
spagna_death = death_days['Spain']['total']
percentuale_morti_ita = italia_death/ita_pop
percentuale_morti_spa = spagna_death/spa_pop
#print('il nr di morti complessivo in Italia è:', italia_death, 'mentre in Spagna è:', spagna_death )
europa = death_days['Europe']['total']
nord_america = death_days['North America']['total']
percentuale_death_eu = europa/eu_pop
percentuale_death_n_amer = nord_america/nord_ame_pop
print('la percentuale di morti COVID in Italia è del:', percentuale_morti_ita*100, 'mentre in Spagna è del:', percentuale_morti_spa*100)
print('La percentuale di morti in Europa è del:', percentuale_death_eu*100, 'La percentuale dei morti in America del Nord è del:', percentuale_death_n_amer*100)


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