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
tot_death = 193408
italia_death = death_days['Italy']['total']
spagna_death = death_days['Spain']['total']
eu_pop_death = death_days['Europe']['total']
nord_ame_pop = death_days['North America']['total']

rapp_ita_death =italia_death/eu_pop_death*100
rapp_spa_death =spagna_death/eu_pop_death*100
rapp_usa = nord_ame_pop/tot_death
rapp_eu = eu_pop_death/tot_death
#print(rapp_ita_death, rapp_spa_death, rapp_usa, rapp_eu)
print('la percentuale di morti COVID in Italia è del:', rapp_ita_death, 'mentre in Spagna è del:', rapp_spa_death)
print('La percentuale di morti in Europa è del:', rapp_eu, 'La percentuale dei morti in America del Nord è del:', rapp_usa)
