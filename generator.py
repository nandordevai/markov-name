# D&D Markov chain name generator
# based on https://github.com/gzomer/startup-name-gen

import random


def build_chain(data, n):
    chain = {
        '_start': {},
        '_names': set(data)
    }
    [add_word(word + '.', chain, n) for word in data]
    return chain


def add_word(word, chain, n):
    for i in range(0, len(word) - n):
        tuple = word[i:i + n]
        next = word[i + 1:i + n + 1]
        chain.setdefault(tuple, {})
        entry = chain[tuple]
        if i == 0:
            chain['_start'][tuple] = chain['_start'].get(tuple, 0) + 1
        entry[next] = entry.get(next, 0) + 1


def generate(chain):
    tuple = random.choice(list(chain['_start'].keys()))
    result = [tuple]

    while True:
        tuple = random.choice(list(chain[tuple].keys()))
        last = tuple[-1]
        if last == '.':
            break
        else:
            result.append(last)

    generated = ''.join(result)
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)


elf = ['Adran', 'Adrie', 'Aelar', 'Althaea', 'Amakiir', 'Amastacia', 'Anastrianna', 'Andraste', 'Antinua', 'Ara', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian', 'Bethrynna', 'Birel', 'Bryn', 'Caelynn', 'Carrie', 'Del', 'Drusilia', 'Enialis', 'Enna', 'Erdan', 'Erevan', 'Eryn', 'Faen', 'Felosial', 'Galanodel', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Holimion', 'Ielenia', 'Ilphelkiir', 'Immeral', 'Innil', 'Ivellios', 'Jelenneth', 'Keyleth', 'Lael',
       'Laucian', 'Leshanna', 'Lia', 'Liadon', 'Meliamne', 'Mella', 'Meriele', 'Mialee', 'Mindartis', 'Naeris', 'Naill', 'Naivara', 'Nallo', 'Paelias', 'Peren', 'Phann', 'Quarion', 'Quelenna', 'Quillathe', 'Rael', 'Riardon', 'Rinn', 'Rolen', 'Sai', 'Sariel', 'Shanairra', 'Shava', 'Siannodel', 'Silaqui', 'Soveliss', 'Syllin', 'Thamior', 'Tharivol', 'Theirastra', 'Theren', 'Thia', 'Thia', 'Vadania', 'Valanthe', 'Vall', 'Varis', 'Xanaphia', 'Xiloscient']

dwarf = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik', 'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin', 'Thorin', 'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit', 'Vonda', 'Amber', 'Artin',
         'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 'Liftrasa', 'Mardred', 'Riswynn', 'Sann', 'Torbera', 'Torgga', 'Vistra', 'Balderk', 'Dankil', 'Gorunn', 'Holderhek', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart']

halfling = ['Alton', 'Ander', 'Andry', 'Bree', 'Cade', 'Callie', 'Cora', 'Corrin', 'Eldon', 'Errich', 'Euphemia', 'Finnan', 'Garret', 'Jillian', 'Kithri', 'Lavinia', 'Lidda',
            'Linda', 'Lyle', 'Merla', 'Merrie', 'Milo', 'Nedda', 'Osborn', 'Paela', 'Perrin', 'Portia', 'Reed', 'Roscoe', 'Seraphina', 'Shaena', 'Trym', 'Vani', 'Verna' 'Wellby']

human = ['Agosto', 'Alethra', 'Amafrey', 'Amblecrown', 'Ander', 'Ankhalab', 'Anskuld', 'Anton', 'Aoth', 'Arizima', 'Arveene', 'Astoria', 'Balama', 'Bareris', 'Bersk', 'Betha', 'Blath', 'Bor', 'Borivik', 'Bran', 'Brightwood', 'Buckman', 'Calabra', 'Cefrey', 'Chathi', 'Chergoba', 'Chernin', 'Darvin', 'Diero', 'Domine', 'Dona', 'Dorn', 'Dotsk', 'Dundragon', 'Dyernina', 'Ehput-Ki', 'Esvele', 'Evendur', 'Evenwood', 'Faila', 'Faurgar', 'Fezim', 'Fode', 'Frath', 'Fyevarra', 'Geth', 'Glar', 'Gorstag', 'Greycastle', 'Grigor', 'Grim', 'Hahpet', 'Helder', 'Helm', 'Hornraven', 'Hulmarra', 'Igan', 'Iltazyara', 'Immith', 'Imzel', 'Ivor', 'Jalana', 'Jandar', 'Jhessail', 'Kanithar', 'Kara', 'Katernin', 'Kerri', 'Kethoth', 'Kethra', 'Kosef', 'Kulenov', 'Lackman', 'Lander',
         'Luisa', 'Lureene', 'Luth', 'Madislak', 'Malark', 'Malcer', 'Mara', 'Mara', 'Marcon', 'Marivaldi', 'Marsk', 'Marta', 'Miri', 'Mival', 'Morn', 'Mumed', 'Murithi', 'Murnyethara', 'Natali', 'Nathandem', 'Navarra', 'Nemetsk', 'Nephis', 'Nulara', 'Olga', 'Olma', 'Orel', 'Palone', 'Pavel', 'Pieron', 'Pisacar', 'Quara', 'Ralmevik', 'Ramas', 'Ramonda', 'Randal', 'Rimardo', 'Romero', 'Rowan', 'Salazar', 'Sefris', 'Selise', 'Sepret', 'Sergor', 'Shandri', 'Shaumar', 'Shemov', 'Shevarra', 'Silifrey', 'So-Kehur', 'Star', 'Starag', 'Stayanoga', 'Stedd', 'Stormwind', 'Tallstag', 'Taman', 'Tammith', 'Tana', 'Tessele', 'Thazar-De', 'Thola', 'Ulmokina', 'Umara', 'Umbero', 'Urhur', 'Urth', 'Uuthrakt', 'Vladislak', 'Vonda', 'Westra', 'Windrivver', 'Yuldra', 'Zolis', 'Zora']

dragonborn = ['Akra', 'Arjhan', 'Balasar', 'Bharash', 'Biri', 'Clethtinthiallor', 'Daar', 'Daardendrian', 'Delmirev', 'Donaar', 'Drachedandion', 'Farideh', 'Fenkenkabradon', 'Ghesh', 'Harann', 'Havilar', 'Heskan', 'Jheri', 'Kava', 'Kepeshkmolik', 'Kerrhylon', 'Kimbatuul', 'Korinn', 'Kriv', 'Linxakasendalor',
              'Medrash', 'Mehen', 'Mishann', 'Myastan', 'Nadarr', 'Nala', 'Nemmonis', 'Norixius', 'Ophinshtalajiir', 'Pandjed', 'Patrin', 'Perra', 'Prexijandilin', 'Raiann', 'Rhogar', 'Shamash', 'Shedinn', 'Shestendeliath', 'Sora', 'Surina', 'Tarhun', 'Thava', 'Torinn', 'Turnuroth', 'Uadjit', 'Verthisathurgiesh', 'Yarjeri']

gnome = ['Alston', 'Alvyn', 'Beren', 'Bimpnottin', 'Boddynock', 'Breena', 'Broce', 'Burgell', 'Caramip', 'Carlin', 'Daergel', 'Dimble', 'Donella', 'Duvamil', 'Eldon', 'Ella', 'Ellyjobell', 'Ellywick', 'Erky', 'Folkor', 'Fonkin', 'Frug', 'Garrick', 'Gerbo', 'Gimble', 'Glim', 'Jebeddo',
         'Kellen', 'Lilli', 'Loopmottin', 'Lorilla', 'Mardnab', 'Murnig', 'Nackle', 'Namfoodle', 'Ningel', 'Nissa', 'Nyx', 'Oda', 'Orla', 'Orryn', 'Raulnor', 'Roondar', 'Roywyn', 'Scheppen', 'Seebo', 'Shami', 'Sindri', 'Tana', 'Timbers', 'Turen', 'Warryn', 'Waywocket', 'Wrenn', 'Zanna', 'Zook']

orc = ['Baggi', 'Dench', 'Emen', 'Engong', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Kansif', 'Keth', 'Krusk',
       'Mhurren', 'Myev', 'Neega', 'Ovak', 'Ownka', 'Ront', 'Shautha', 'Shump', 'Sutha', 'Thokk', 'Vola', 'Volen', 'Yevelda']

tiefling = ['Akmenos', 'Akta', 'Amnon', 'Anakis', 'Barakas', 'Bryseis', 'Criella', 'Damaia', 'Damakos', 'Ea', 'Ekemon', 'Iados', 'Kairon',
            'Kallista', 'Lerissa', 'Leucis', 'Makaria', 'Melech', 'Mordai', 'Morthos', 'Nemeia', 'Orianna', 'Pelaios', 'Phelaia', 'Rieta', 'Skamos', 'Therai']

for i in range(10):
    print(generate(build_chain(tiefling, 2)))
