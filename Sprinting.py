from __future__ import division
from random import randint
import random
from decimal import Decimal
import copy
#import time
import math
import locale
import numpy as np













#locale.setlocale(locale.LC_ALL, 'en_US')

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    WHITE = '\033[37m'
    BROWN = '\033[33m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'




First_Names = ["Adam", "Taoufik", "David", "Jimmy", "Usain", "Tyson", "Yohan", "Justin", "Donovan", "Wayde", "Asafa", "Ben", "Charles", "Bob", "Jim", "Andre", "Kirani", "Yousef", "LaShawn", "Ramil"]
Last_Names = ["Makhloufi", "Berian", "Rudisha", "Bolt", "Gay", "Blake", "Gatlin", "Lewis", "Bailey", "Powell", "Johnson", "Greene", "James", "Merritt", "Ahmed Masrahi", "Guliyev"]

First_Names_A = ["Aska", "Xie", "Su", "Jin Wei", "Ryota", "Kim", "Kenji", "Kei", "Teng", "Suguru", "Cheng", "Takayuki", "Park", "Li", "Shota", "Nobuya"]
Last_Names_A = ["Cambridge", "Zhenye", "Bingtian", "Yamagata", "Kuk-young", "Fujimitsu", "Takase", "Osako", "Wenjun", "Wen", "Shiwei", "Kishimoto", "Bong-go", "Chil-sung"]

First_Names_B = ["Taoufik", "Usain", "Yohan", "Asafa", "Andre", "Kirani", "Yousef", "Ramil", "Ogho-Oghene", "Abdullah", "Adama", "Asbel", "El Hassan"]
Last_Names_B = ["Makhloufi", "Berian", "Rudisha", "Bolt", "Bailey", "Powell", "Ahmed Masrahi", "Egwero", "Akbar Mohammed", "Jammeh", "Kipketer", "Cheruiyot Rotich", "Kiprop", "Fraser-Pryce", "El-Abbassi", "Al-Garni"]


First_Names_C = ["Boris","David", "Adam", "Carl", "Jimmy", "Riste", "Lukas", "Julius", "Serhiy", "Andreas", "Marcin", "Alex"]
Last_Names_C = ["Kszczot", "Hayes", "Hines", "Pandev", "Jakubczyk", "Reus", "Smelyk", "Bube", "Lewandowski", "Zyabkina", "Safronova", "Radzivil"]

First_Names_D = ["Christophe", "Boris", "David", "Adam", "Carl", "Jimmy", "Wayde", "Matteo", "James", "Filippo", "Alex", "Pierre-Ambroise"]
Last_Names_D = ["Lemaitre", "Vicaut", "van Niekerk", "Hayes", "Hines", "Galvan", "Ellington", "Tortu", "Wilson", "Bosse"]

First_Names_E = ["Adam", "David", "Jimmy", "Tyson", "Justin", "Donovan", "Ben", "Charles", "Bob", "Jim", "Andre", "LaShawn", "Brendan", "Matthew"]
Last_Names_E = ["Berian", "Gay", "Blake", "Gatlin", "Lewis", "Bailey", "Powell", "Johnson", "Greene", "James", "Merritt", "Rodney", "Centrowitz"]


Jamaica = {'Name': "Jamaica", "Color": color.YELLOW, 'Sprinters': 70, 'Runners': 10, 'Endurance': 5, 'Spots': 4, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
USA = {'Name': "United States", "Color": color.BLUE, 'Sprinters': 30, 'Runners': 60, 'Endurance': 40, 'Spots': 4, 'First Names': First_Names_E, 'Last Names': Last_Names_E}
South_Africa = {'Name': "South Africa", "Color": color.GREEN, 'Sprinters': 20, 'Runners': 30, 'Endurance': 20, 'Spots': 4, 'First Names': First_Names_D, 'Last Names': Last_Names_D}
Canada = {'Name': "Canada", "Color": color.RED, 'Sprinters': 20, 'Runners': 15, 'Endurance': 15, 'Spots': 3, 'First Names': First_Names_E, 'Last Names': Last_Names_E}
France = {'Name': "France", "Color": color.CYAN, 'Sprinters': 20, 'Runners': 20, 'Endurance': 20, 'Spots': 4, 'First Names': First_Names_D, 'Last Names': Last_Names_D}
Trinidad_and_Tobago = {'Name': "Trinidad and Tobago", "Color": color.RED, 'Sprinters': 30, 'Runners': 15, 'Endurance': 5, 'Spots': 4, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Grenada = {'Name': "Grenada", "Color": color.GREEN, 'Sprinters': 10, 'Runners': 30, 'Endurance': 15, 'Spots': 3, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
China = {'Name': "China", "Color": color.RED, 'Sprinters': 30, 'Runners': 15, 'Endurance': 10, 'Spots': 4, 'First Names': First_Names_A, 'Last Names': Last_Names_A}
Costa_Rica = {'Name': "Costa Rica", "Color": color.DARKCYAN, 'Sprinters': 15, 'Runners': 5, 'Endurance': 5, 'Spots': 3, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Germany = {'Name': "Germany", "Color": color.BOLD, 'Sprinters': 5, 'Runners': 12, 'Endurance': 15, 'Spots': 3, 'First Names': First_Names_C, 'Last Names': Last_Names_C}
Dominica = {'Name': "Dominica", "Color": color.PURPLE, 'Sprinters': 4, 'Runners': 2, 'Endurance': 2, 'Spots': 1, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Japan = {'Name': "Japan", "Color": color.RED, 'Sprinters': 20, 'Runners': 10, 'Endurance': 10, 'Spots': 3, 'First Names': First_Names_A, 'Last Names': Last_Names_A}
New_Zealand = {'Name': "New Zealand", "Color": color.BOLD, 'Sprinters': 4, 'Runners': 3, 'Endurance': 3, 'Spots': 1, 'First Names': First_Names_D, 'Last Names': Last_Names_D}
Kenya = {'Name': "Kenya", "Color": color.GREEN, 'Sprinters': 4, 'Runners': 15, 'Endurance': 60, 'Spots': 3, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Botswana = {'Name': "Botswana", "Color": color.CYAN, 'Sprinters': 5, 'Runners': 12, 'Endurance': 5, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Algeria = {'Name': "Algeria", "Color": color.BROWN, 'Sprinters': 4, 'Runners': 10, 'Endurance': 30, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
United_Kingdom = {'Name': "United Kingdom", "Color": color.BLUE, 'Sprinters': 20, 'Runners': 20, 'Endurance': 15, 'Spots': 4, 'First Names': First_Names_D, 'Last Names': Last_Names_D}
Bahrain = {'Name': "Bahrain", "Color": color.RED, 'Sprinters': 10, 'Runners': 2, 'Endurance': 2, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Poland = {'Name': "Poland", "Color": color.WHITE, 'Sprinters': 4, 'Runners': 6, 'Endurance': 15, 'Spots': 2, 'First Names': First_Names_D, 'Last Names': Last_Names_D}
Sri_Lanka = {'Name': "Sri Lanka", "Color": color.BROWN, 'Sprinters': 4, 'Runners': 2, 'Endurance': 2, 'Spots': 1, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Djibouti = {'Name': "Djibouti", "Color": color.DARKCYAN, 'Sprinters': 10, 'Runners': 5, 'Endurance': 5, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Ethiopia = {'Name': "Ethiopia", "Color": color.YELLOW, 'Sprinters': 4, 'Runners': 5, 'Endurance': 30, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Bahamas = {'Name': "Bahamas", "Color": color.CYAN, 'Sprinters': 6, 'Runners': 15, 'Endurance': 4, 'Spots': 2, 'First Names': First_Names_B, 'Last Names': Last_Names_B}
Barbados = {'Name': "Barbados", "Color": color.BLUE, 'Sprinters': 4, 'Runners': 4, 'Endurance': 3, 'Spots': 1, 'First Names': First_Names_B, 'Last Names': Last_Names_B}


Countries = [Jamaica, USA, South_Africa, Canada, France, Trinidad_and_Tobago, Grenada, China, Costa_Rica, Germany, Dominica, Japan, New_Zealand, Kenya, Botswana, Algeria, United_Kingdom, Bahrain, Poland, Sri_Lanka, Djibouti, Ethiopia, Bahamas, Barbados]
Usain_Bolt = {'Seed': "0", 'Name': "Usain Bolt", 'Termination': 80, 'Deceleration': 0.972, 'Acceleration': 3.9, 'Speed': 12.4,'Country': "Jamaica", 'Color': color.YELLOW}
Andre_DeGrasse = {'Seed': "0", 'Name': "Andre DeGrasse", 'Termination': 60, 'Deceleration': 0.972,'Acceleration': 4.1, 'Speed': 12.3,'Country': "Canada", 'Color': color.RED}
LaShawn_Merritt = {'Seed': "0", 'Name': "LaShawn Merritt", 'Termination': 80, 'Deceleration': 0.983, 'Acceleration': 3.1, 'Speed': 11.6,'Country': "United States", 'Color': color.BLUE}
Christophe_LeMaitre = {'Seed': "0", 'Name': "Christophe Lemaitre", 'Termination': 70, 'Deceleration': 0.974, 'Acceleration': 3.6, 'Speed': 11.9,'Country': "France", 'Color': color.CYAN}
Wayde_Niekerk = {'Seed': "0", 'Name': "Wayde Van Niekerk", 'Termination': 90, 'Deceleration': 0.991, 'Acceleration': 3.5, 'Speed': 10.8,'Country': "South Africa", 'Color': color.GREEN}
Kirani_James = {'Seed': "0", 'Name': "Kirani James", 'Termination': 75, 'Deceleration': 0.987, 'Acceleration': 3.1, 'Speed': 11.1,'Country': "Grenada", 'Color': color.GREEN}
Machel_Cedinio = {'Seed': "0", 'Name': "Machel Cedinio", 'Termination': 80, 'Deceleration': 0.989, 'Acceleration': 2.7, 'Speed': 10.7,'Country': "Trinidad and Tobago", 'Color': color.RED}
Justin_Gatlin = {'Seed': "0", 'Name': "Justin Gatlin", 'Termination': 70, 'Deceleration': 0.974, 'Acceleration': 3.5, 'Speed': 12.2, 'Country': "United States", 'Color': color.BLUE}
Yohan_Blake = {'Seed': "0", 'Name': "Yohan Blake", 'Termination': 65, 'Deceleration': 0.972, 'Acceleration': 3.8, 'Speed': 12.4,'Country': "Jamaica", 'Color': color.YELLOW}
Nickel_Ashmeade = {'Seed': "0", 'Name': "Nickel Ashmeade", 'Termination': 70, 'Deceleration': 0.975, 'Acceleration': 3.4, 'Speed': 12.1,'Country': "Jamaica", 'Color': color.YELLOW}
Jimmy_Vicault = {'Seed': "0", 'Name': "Jimmy Vicault", 'Termination': 70, 'Deceleration': 0.975, 'Acceleration': 3.5, 'Speed': 12.1,'Country': "France", 'Color': color.CYAN}
Trayvon_Bromell = {'Seed': "0", 'Name': "Trayvon Bromell", 'Termination': 60, 'Deceleration': 0.973, 'Acceleration': 3.7, 'Speed': 12.3, 'Country': "United States", 'Color': color.BLUE}

spots = 0
n = 0
while n < len(Countries):
    spots += Countries[n]['Spots']
    n += 1
#print(spots

lst = [Usain_Bolt, Justin_Gatlin, Jimmy_Vicault, Kirani_James, Trayvon_Bromell, Yohan_Blake, Nickel_Ashmeade, Machel_Cedinio, Christophe_LeMaitre, Wayde_Niekerk, Andre_DeGrasse, LaShawn_Merritt]



def sprinter(country):
    name = country['First Names'][randint(0, len(country['First Names']) - 1)]
    surname = country['Last Names'][randint(0, len(country['Last Names']) - 1)] # + " - Sprinter"
    if randint(0,100) < 5:
        surname += " Jr"
    acceleration = int(np.random.normal(375, 8)) / 100
    deceleration = int(np.random.normal(9715, 2)) / 10000
    termination = int(np.random.normal(65, 3))
    speed = int(np.random.normal(115, 3)) / 10
    sprinter = {'Seed': "0", 'Name': str(name) + " " + str(surname), 'Termination': termination, 'Deceleration': deceleration, 'Acceleration': acceleration, 'Speed': speed, 'Country': country['Name'], 'Color': country['Color']}
    return sprinter


def runner(country):
    name = country['First Names'][randint(0, len(country['First Names']) - 1)]
    surname = country['Last Names'][randint(0, len(country['Last Names']) - 1)] # + " - Runner"
    if randint(0,100) < 5:
        surname += " Jr"
    acceleration = int(np.random.normal(340, 8)) / 100
    deceleration = int(np.random.normal(9880, 2)) / 10000
    termination = int(np.random.normal(70, 3))
    speed = int(np.random.normal(106, 2)) / 10
    runner = {'Seed': "0", 'Name': str(name) + " " + str(surname), 'Termination': termination, 'Deceleration': deceleration,
                'Acceleration': acceleration, 'Speed': speed, 'Country': country['Name'], 'Color': country['Color']}
    return runner


def endurance(country):
    name = country['First Names'][randint(0, len(country['First Names']) - 1)]
    surname = country['Last Names'][randint(0, len(country['Last Names']) - 1)] # + " - Long Distance"
    if randint(0,100) < 5:
        surname += " Jr"
    acceleration = int(np.random.normal(260, 8)) / 100
    deceleration = int(np.random.normal(9955, 2)) / 10000
    termination = int(np.random.normal(75, 3))
    speed = int(np.random.normal(88, 2)) / 10
    runner = {'Seed': "0", 'Name': str(name) + " " + str(surname), 'Termination': termination,
              'Deceleration': deceleration,
              'Acceleration': acceleration, 'Speed': speed, 'Country': country['Name'], 'Color': country['Color']}
    return runner


def roundup(n):
    return (n + 9) // 10 * 10


def timed(acceleration, speed, deceleration, termination, distance):
    a = acceleration
    u = speed
    v = u
    v_prev = u
    decel = deceleration
    term = termination
    t_1 = u / a
    d_1 = (1/2) * a * t_1 ** 2
    t_2 = (term - d_1) / u
    t = t_1 + t_2
    d = term
    time = 1000
    if d_1 > distance:
        t = (2 * distance / a) ** (1/2)
    elif d > distance:
        dif = d - distance
        t = t - dif / u
    else:
        if math.ceil(t) < time:
            y = math.ceil(t) - t
            t = math.ceil(t)
        else:
            y = time - t
            t = time
        while d <= distance:
            v_prev = copy.copy(v)
            v = u * decel ** y
            add = (v + v_prev) / 2
            if y < 1:
                add *= y + 1
            d += add
            t += 1
            y += 1
        dif = d - distance
        t -= dif / ((v + v_prev) / 2)
    return t


def distance_calculator(acceleration, speed, deceleration, termination, time):
    a = acceleration
    u = speed
    v = u
    v_prev = u
    decel = deceleration
    term = termination
    t_1 = u / a
    d_1 = (1/2) * a * t_1 ** 2
    t_2 = (term - d_1) / u
    t = t_1 + t_2
    d = term
    if t_1 > time:
        d = (1/2) * a * time ** 2
    elif t > time:
        dif = t - time
        d = d - u * dif
    else:
        if math.ceil(t) < time:
            y = math.ceil(t) - t
            t = math.ceil(t)
        else:
            y = time - t
            t = time
        while t <= time:
            v_prev = copy.copy(v)
            v = u * decel ** y
            add = (v + v_prev) / 2
            if y < 1:
                add *= y + 1
            d += add
            t += 1
            y += 1
        dif = t - time
        d -= dif * ((v + v_prev) / 2)
    return d


#
# #def timed_race(sprinter, distance):
#     a = sprinter['Acceleration'] + randint(-50,50) / 100
#     u = sprinter['Speed'] + randint(-20,20) / 100
#     decel = sprinter['Deceleration'] + randint(-10, 10) / 1000
#     term = sprinter['Termination'] + randint(-5,5)
#     d_max = u ** 2 / (2 * a)
#     d = 0
#     while d < distance:
#         d += 10
#         dif = d - d_max
#         if dif < 0:
#             dif = 0
#             s = d
#         else:
#             dif = d - d_max
#             s = d_max
#         if d > term:
#             v = u * decel
#         else:
#             v = u
#         t = (2 * s / a) ** (1 / 2) + (2 * dif) / (u + v)
#         u = v
#         print(sprinter['Name'] + " hit " + str(d) + "m in " + str(t) + " seconds."

# t_max = u / a
                # t_term = timed(a, u, de, term, term)
                # dif = t - t_max
                # if dif < 0:
                #     dif = 0
                #     s = t
                # else:
                #     dif = t - t_max
                #     s = t_max
                # if t > t_term:
                #     x = copy.copy(dist[n])
                #     v = u * de ** (t - t_term)
                #     d = ind[n] + (x + v) / 2
                #     dist[n] = v
                #     ind[n] = d
                # else:
                #     d = (1/2) * a * s ** 2 + dif * u
                # print(timed(a, u, de, term, d)
                # print(distance_calculator(a, u, de, term, t)


def silent_heat(sprinters, distance):
    times = []
    places = []
    intimes = []
    As = []
    Vs = []
    DEs = []
    TEs = []
    dist = []
    ind = []
    place = 1
    n = 0
    while n < len(sprinters):
        times.append(1000)
        intimes.append(0)
        places.append(0)
        a = sprinters[n]['Acceleration'] + np.random.normal(0, 5) / 100
        v = sprinters[n]['Speed'] + np.random.normal(0, 10) / 100
        de = sprinters[n]['Deceleration'] + np.random.normal(0, 2) / 10000
        term = sprinters[n]['Termination'] + np.random.normal(0, 2)
        As.append(a)
        Vs.append(v)
        DEs.append(de)
        TEs.append(term)
        dist.append(v)
        ind.append(0)
        n += 1
    t = 0
    r = 0
    while r != len(sprinters):
        t += int(str(distance)[0])
        n = 0
        while n < len(sprinters):
            if times[n] == 1000:
                a = As[n]
                u = Vs[n]
                de = DEs[n]
                term = TEs[n]
                d = distance_calculator(a, u, de, term, t)
                if d > distance:
                    ot = copy.copy(t)
                    t = timed(a, u, de, term, distance)
                    times[n] = t
                    r += 1
                    place += 1
                    t = ot
                else:
                    intimes[n] = d
            n += 1
        timesc = copy.copy(times)
        n = 1
        while n < place:
            tim = min(timesc)
            pos = timesc.index(tim)
            places[n - 1] = pos
            timesc[pos] = 1000
            n += 1
        n = 0
        spot = place
        while n < len(sprinters) - place + 1:
            d = max(intimes)
            pos = intimes.index(d)
            intimes[pos] = 0
            spot += 1
            n += 1
    return [times, places]


def sprinterlist(number, country):
    lst = []
    n = 0
    while n < number:
        lst.append(sprinter(country))
        n += 1
    return lst


def runnerlist(number, country):
    lst = []
    n = 0
    while n < number:
        lst.append(runner(country))
        n += 1
    return lst


def endlist(number, country):
    lst = []
    n = 0
    while n < number:
        lst.append(endurance(country))
        n += 1
    return lst


def race(sprinters, distance):
    times = []
    places = []
    intimes = []
    As = []
    Vs = []
    DEs = []
    TEs = []
    dist = []
    ind = []
    place = 1
    n = 0
    while n < len(sprinters):
        times.append(1000)
        intimes.append(0)
        places.append(0)
        a = sprinters[n]['Acceleration'] + np.random.normal(0, 5) / 100
        v = sprinters[n]['Speed'] + np.random.normal(0, 10) / 100
        de = sprinters[n]['Deceleration'] + np.random.normal(0, 2) / 10000
        term = sprinters[n]['Termination'] + np.random.normal(0, 2)
        As.append(a)
        Vs.append(v)
        DEs.append(de)
        TEs.append(term)
        dist.append(v)
        ind.append(0)
        n += 1
    t = 0
    r = 0
    while r != len(sprinters):
        t += int(str(distance)[0])
        y = input("GO!")
        n = 0
        while n < len(sprinters):
            if times[n] == 1000:
                a = As[n]
                u = Vs[n]
                de = DEs[n]
                term = TEs[n]
                d = distance_calculator(a, u, de, term, t)
                if d > distance:
                    ot = copy.copy(t)
                    t = timed(a, u, de, term, distance)
                    times[n] = t
                    r += 1
                    place += 1
                    t = ot
                else:
                    intimes[n] = d
            n += 1
        timesc = copy.copy(times)
        n = 1
        while n < place:
            tim = min(timesc)
            pos = timesc.index(tim)
            places[n - 1] = pos
            print(sprinters[pos]['Color'] + str(n) + ". " + sprinters[pos]['Name'] + " (#" + sprinters[pos]['Seed'] + ") hit " + str(distance) + "m in " + str(round(tim, 2)) + " seconds." + color.END)
            timesc[pos] = 1000
            n += 1
        n = 0
        spot = place
        while n < len(sprinters) - place + 1:
            d = max(intimes)
            pos = intimes.index(d)
            print(sprinters[pos]['Color'] + str(spot) + ". " + sprinters[pos]['Name'] + " (#" + sprinters[pos]['Seed'] + ") hit " + str(round(d, 2)) + "m in " + str(t) + " seconds." + color.END)
            intimes[pos] = 0
            spot += 1
            n += 1
        print()
    return [times, places]


def relay(sprinters, distance):
    d_list = []
    t_list = []
    leg = []
    places = []
    place = 1
    leg_list = []
    dist = []
    As = []
    Vs = []
    DEs = []
    Ts = []
    tim_list = []
    n = 0
    while n < len(sprinters):
        d_list.append(0)
        places.append(0)
        leg.append(sprinters[n][0])
        As.append(0)
        Vs.append(0)
        DEs.append(0)
        Ts.append(0)
        leg_list.append(1)
        t_list.append(0)
        dist.append(0)
        tim_list.append(0)
        As[n] = leg[n]['Acceleration'] + np.random.normal(0, 5) / 100
        Vs[n] = leg[n]['Speed'] + np.random.normal(0, 10) / 100
        DEs[n] = leg[n]['Deceleration'] + np.random.normal(0, 2) / 1000
        Ts[n] = leg[n]['Termination'] + np.random.normal(0, 2)
        n += 1
    r = 0
    t = 0
    while r != len(sprinters):
        if distance == 1600:
            t += 8
        else:
            t += int(str(distance)[0])
        y = input("GO!")
        n = 0
        while n < len(sprinters):
            if dist[n] != 1:
                a = As[n]
                v = Vs[n]
                de = DEs[n]
                term = Ts[n]
                d = distance_calculator(a, v, de, term, t - t_list[n])
                tim_list[n] = t_list[n] + timed(a, v, de, term, d)
                total_d = d_list[n] + d
                dist[n] = total_d
                if total_d > distance:
                    t_list[n] += timed(a, v, de, term, distance / 4)
                    tim_list[n] = t_list[n]
                    dist[n] = 1
                    place += 1
                    r += 1
                elif d > distance / 4:
                    t_list[n] += timed(a, v, de, term, distance / 4)
                    tim_list[n] = t_list[n]
                    leg[n] = sprinters[n][leg_list[n]]
                    leg_list[n] += 1
                    As[n] = leg[n]['Acceleration'] + np.random.normal(0, 10) / 100
                    Vs[n] = leg[n]['Speed'] + np.random.normal(0, 20) / 100
                    DEs[n] = leg[n]['Deceleration'] + np.random.normal(0, 0.5) / 1000
                    Ts[n] = leg[n]['Termination'] + np.random.normal(0, 3)
                    d_list[n] += distance / 4
                    dist[n] = d_list[n] + distance_calculator(a, v, de, term, t - t_list[n])
            n += 1
        times = copy.copy(tim_list)
        n = 1
        while n < place:
            tim = min(times)
            pos = times.index(tim)
            places[n - 1] = pos
            print(leg[pos]['Color'] + str(n) + ". " + leg[pos]['Country'] + " (#" + leg[pos]['Seed'] + ") hit " + str(distance) + "m in " + str(round(tim, 2)) + " seconds." + color.END)
            times[pos] = 1000
            n += 1
        n = 0
        spot = place
        while n < len(sprinters) - place + 1:
            d = max(dist)
            pos = dist.index(d)
            print(leg[pos]['Color'] + str(spot) + ". " + leg[pos]['Name'] + " (" + leg[pos]['Country'] + ") hit " + str(round(d, 2)) + "m in " + str(t) + " seconds." + color.END)
            dist[pos] = 0
            spot += 1
            n += 1
        print()
    return [t_list, places]


def heat_intro(sprinters, times):
    print()
    n = 0
    while n < len(sprinters):
        print(sprinters[n]['Color'] + sprinters[n]['Name'] + " (" + sprinters[n]['Country'] + ")" + " (" + str(round(times[n], 2)) + "s)" + color.END)
        n += 1
    print()


def relay_intro(sprinters, times):
    print()
    n = 0
    while n < len(sprinters):
        print(sprinters[n][0]['Color'] + sprinters[n][0]['Country'] + " (" + str(round(times[n], 2)) + "s)" + color.END)
        n += 1
    print()


def team_intro(sprinters, times, team_time):
    print()
    n = 0
    while n < len(sprinters):
        print(sprinters[n]['Color'] + sprinters[n]['Name'] + " (" + str(round(times[n], 2)) + "s)" + color.END)
        n += 1
    print(sprinters[n - 1]['Color'] + "TEAM TIME: " + str(round(team_time, 2)) + color.END)
    print()


def olympic_trials(sprinters, runners, endurance, country, distance):
        relay_team = []
        relay_times = []
        n = 0
        while n < len(sprinters):
            sprinters[n]['Country'] = country['Name']
            sprinters[n]['Color'] = country['Color']
            n += 1
        n = 0
        while n < len(runners):
            runners[n]['Country'] = country['Name']
            runners[n]['Color'] = country['Color']
            n += 1
        if distance == 100:
            competitors = sprinters
        elif distance == 200:
            competitors = sprinters + runners
        elif distance == 400:
            competitors = runners + endurance
        else:
            competitors = endurance
        # print("Welcome to the Olympic Trials for " + country['Name']
        heats = []
        qualified = []
        qualified_times = []
        eliminated = []
        n = 0
        while n < country['Spots']:
            qualified.append(0)
            qualified_times.append(1000 + n)
            n += 1
        n = 0
        while n < 4:
            relay_team.append(0)
            relay_times.append(1000 + n)
            n += 1
        n = 0
        while n < len(competitors) / 8:
            heats.append([])
            u = 0
            while u < 8 and len(eliminated) != len(competitors):
                comp = randint(0, len(competitors) - 1)
                while comp in eliminated and len(eliminated) != len(competitors):
                    comp = randint(0, len(competitors) - 1)
                eliminated.append(comp)
                heats[n].append(competitors[comp])
                u += 1
            n += 1
        z = 0
        while z < 3:
            n = 0
            while n < len(heats):
                # print
                # print("Welcome to Heat " + str(n + 1) + " of the " + str(distance) + "m trials"
                # print
                result = silent_heat(heats[n], distance)
                u = 0
                while u < len(heats[n]):
                    bottom = max(qualified_times)
                    lowest = qualified_times.index(bottom)
                    if result[0][result[1][u]] < bottom and heats[n][result[1][u]] not in qualified:
                        qualified[lowest] = heats[n][result[1][u]]
                        qualified_times[lowest] = result[0][result[1][u]]
                    elif result[0][result[1][u]] < bottom:
                        pos = qualified.index(heats[n][result[1][u]])
                        qualified_times[pos] = result[0][result[1][u]]
                    bottom = max(relay_times)
                    lowest = relay_times.index(bottom)
                    if result[0][result[1][u]] < bottom and heats[n][result[1][u]] not in relay_team:
                        relay_team[lowest] = heats[n][result[1][u]]
                        relay_times[lowest] = result[0][result[1][u]]
                    elif result[0][result[1][u]] < bottom:
                        pos = relay_team.index(heats[n][result[1][u]])
                        relay_times[pos] = result[0][result[1][u]]
                    u += 1
                # print("QUALIFYING TIMES"
                # print
                # u = 0
                # while u < len(qualified):
                #     if qualified[u] != 0:
                #         print(qualified[u]['Color'] + qualified[u]['Name'] + " - " + str(round(qualified_times[u], 2)) + "s" + color.END
                #     u += 1
                # print
                n += 1
            z += 1
        team_time = sum(relay_times)
        return [qualified, qualified_times, relay_team, relay_times, team_time]


def relay_olympics(sprinters, distance):
    print()
    print("OLYMPIC " + str(distance) + "m Relay")
    heats = []
    eliminated = []
    eliminated_times = []
    qualified = []
    qualifed_times = []
    n = 0
    while n < 2:
        heats.append([])
        u = 0
        while u < 8:
            comp = randint(0, 15)
            while comp in eliminated:
                comp = randint(0, 15)
            eliminated.append(comp)
            heats[n].append(sprinters[comp])
            u += 1
        n += 1
    eliminated = []
    n = 0
    while n < 2:
        print("Welcome to Heat " + str(n + 1) + " of the " + str(distance) + "m Relay")
        print()
        result = relay(heats[n], distance)
        qualified.append(heats[n][result[1][0]])
        qualified.append(heats[n][result[1][1]])
        qualified.append(heats[n][result[1][2]])
        qualifed_times.append(result[0][result[1][0]])
        qualifed_times.append(result[0][result[1][1]])
        qualifed_times.append(result[0][result[1][2]])
        u = 3
        while u < 8:
            eliminated.append(heats[n][result[1][u]])
            eliminated_times.append(result[0][result[1][u]])
            u += 1
        print("QUALIFYING TIMES")
        print()
        u = 0
        while u < len(qualified):
            print(qualified[u][0]['Color'] + qualified[u][0]['Country'] + " - " + str(round(qualifed_times[u], 2)) + "s" + color.END)
            u += 1
        print()
        n += 1
    n = 0
    while n < 2:
        t = min(eliminated_times)
        pos = eliminated_times.index(t)
        qualified.append(eliminated[pos])
        qualifed_times.append(t)
        eliminated_times[pos] = 1000
        n += 1
    u = 0
    while u < len(qualified):
        print(qualified[u][0]['Color'] + qualified[u][0]['Country'] + " - " + str(round(qualifed_times[u], 2)) + "s" + color.END)
        u += 1
    print()
    print("Welcome to the " + str(distance) + "m Final")
    relay_intro(qualified, qualifed_times)
    result = relay(qualified, distance)
    print(qualified[result[1][0]][0]['Color'] + qualified[result[1][0]][0]['Country'] +  " has won olympic gold." + color.END)
    print(qualified[result[1][1]][0]['Color'] + qualified[result[1][1]][0]['Country'] + " has won olympic silver." + color.END)
    print(qualified[result[1][2]][0]['Color'] + qualified[result[1][2]][0]['Country'] + " has won olympic bronze." + color.END)


def olympics(sprinters, distance):
    print()
    print("OLYMPIC " + str(distance) + "m")
    heats = []
    eliminated = []
    qualified = []
    qualifed_times = []
    eliminated_times = []
    n = 0
    while n < 8:
        heats.append([])
        u = 0
        while u < 8:
            comp = randint(0, 63)
            while comp in eliminated:
                comp = randint(0, 63)
            eliminated.append(comp)
            heats[n].append(sprinters[comp])
            u += 1
        n += 1
    eliminated = []
    n = 0
    while n < 8:
        print("Welcome to Heat " + str(n + 1) + " of the " + str(distance) + "m")
        print()
        result = race(heats[n], distance)
        qualified += [heats[n][result[1][0]], heats[n][result[1][1]]]
        qualifed_times += [result[0][result[1][0]], result[0][result[1][1]]]
        u = 2
        while u < 8:
            eliminated += [heats[n][result[1][u]]]
            eliminated_times += [result[0][result[1][u]]]
            u += 1
        print("QUALIFYING TIMES")
        print()
        u = 0
        while u < len(qualified):
            print(qualified[u]['Color'] + qualified[u]['Name']+ " (" + qualified[u]['Country'] + ")" + " - " + str(round(qualifed_times[u], 2)) + "s" + color.END)
            u += 1
        print()
        n += 1
    n = 0
    while n < 8:
        t = min(eliminated_times)
        pos = eliminated_times.index(t)
        qualified += [eliminated[pos]]
        qualifed_times += [t]
        eliminated_times[pos] = 1000
        n += 1
    u = 0
    while u < len(qualified):
        print(qualified[u]['Color'] + qualified[u]['Name']+ " (" + qualified[u]['Country'] + ")" + " - " + str(round(qualifed_times[u], 2)) + "s" + color.END)
        u += 1
    print()
    eliminated_times = []
    eliminated = []
    elim = []
    semifinal_1 = []
    semifinal_2 = []
    semifinal_3 = []
    semitimes = [[],[],[]]
    u = 0
    while u < 8:
        comp = randint(0, 23)
        while comp in elim:
            comp = randint(0, 23)
        elim.append(comp)
        semifinal_1.append(qualified[comp])
        semitimes[0].append(qualifed_times[comp])
        u += 1
    u = 0
    while u < 8:
        comp = randint(0, 23)
        while comp in elim:
            comp = randint(0, 23)
        elim.append(comp)
        semifinal_2.append(qualified[comp])
        semitimes[1].append(qualifed_times[comp])
        u += 1
    u = 0
    while u < 8:
        comp = randint(0, 23)
        while comp in elim:
            comp = randint(0, 23)
        elim.append(comp)
        semifinal_3.append(qualified[comp])
        semitimes[2].append(qualifed_times[comp])
        u += 1
    qualified = []
    qualifed_times = []
    print("Welcome to the 1st " + str(distance) + "m Semifinal")
    heat_intro(semifinal_1, semitimes[0])
    result = race(semifinal_1, distance)
    qualified += [semifinal_1[result[1][0]], semifinal_1[result[1][1]]]
    qualifed_times += [result[0][result[1][0]], result[0][result[1][1]]]
    u = 2
    while u < 8:
        eliminated += [semifinal_1[result[1][u]]]
        eliminated_times += [result[0][result[1][u]]]
        u += 1
    print("Welcome to the 2nd " + str(distance) + "m Semifinal")
    heat_intro(semifinal_2, semitimes[1])
    result = race(semifinal_2, distance)
    qualified += [semifinal_2[result[1][0]], semifinal_2[result[1][1]]]
    qualifed_times += [result[0][result[1][0]], result[0][result[1][1]]]
    u = 2
    while u < 8:
        eliminated += [semifinal_2[result[1][u]]]
        eliminated_times += [result[0][result[1][u]]]
        u += 1
    print("Welcome to the 3rd " + str(distance) + "m Semifinal")
    heat_intro(semifinal_3, semitimes[2])
    result = race(semifinal_3, distance)
    qualified += [semifinal_3[result[1][0]], semifinal_3[result[1][1]]]
    qualifed_times += [result[0][result[1][0]], result[0][result[1][1]]]
    u = 2
    while u < 8:
        eliminated += [semifinal_3[result[1][u]]]
        eliminated_times += [result[0][result[1][u]]]
        u += 1
    n = 0
    while n < 2:
        t = min(eliminated_times)
        pos = eliminated_times.index(t)
        qualified += [eliminated[pos]]
        qualifed_times += [t]
        eliminated_times[pos] = 1000
        n += 1
    print()
    print("Welcome to the " + str(distance) + "m Final")
    heat_intro(qualified, qualifed_times)
    result = race(qualified, distance)
    print(qualified[result[1][0]]['Color'] + qualified[result[1][0]]['Name'] + " (" + qualified[result[1][0]]['Country'] + ") has won olympic gold." + color.END)
    print(qualified[result[1][1]]['Color'] + qualified[result[1][1]]['Name'] + " (" + qualified[result[1][1]]['Country'] + ") has won olympic silver." + color.END)
    print(qualified[result[1][2]]['Color'] + qualified[result[1][2]]['Name'] + " (" + qualified[result[1][2]]['Country'] + ") has won olympic bronze." + color.END)


def preview(qualifiers, times, distance):
    t = copy.copy(times)
    print()
    print("Olympic " + str(distance) + "m Preview")
    print()
    n = 0
    while n < len(qualifiers):
        top = min(t)
        spot = t.index(top)
        qualifiers[spot]['Seed'] = str(n + 1)
        if n < 10:
            print(qualifiers[spot]['Color'] + str(n+1) + ". " + qualifiers[spot]['Name'] + " (" + qualifiers[spot]['Country'] + ") - "+ str(round(top, 2)) + "s" + color.END)
        t[spot] = 1000
        n += 1
    print()


def relay_preview(qualifiers, times, distance):
    t = copy.copy(times)
    print()
    print("Olympic " + str(distance) + "m Relay Preview")
    print()
    n = 0
    while n < len(qualifiers):
        top = min(t)
        spot = t.index(top)
        qualifiers[spot][0]['Seed'] = str(n + 1)
        qualifiers[spot][1]['Seed'] = str(n + 1)
        qualifiers[spot][2]['Seed'] = str(n + 1)
        qualifiers[spot][3]['Seed'] = str(n + 1)
        if n < 16:
            print(qualifiers[spot][0]['Color'] + str(n + 1) + ". " + qualifiers[spot][0]['Country'] + " - " + str(round(top, 2)) + "s" + color.END)
        t[spot] = 1000
        n += 1
    print()


def season():
    one = []
    two = []
    four = []
    eight = []
    one_times = []
    two_times = []
    four_times = []
    eight_times = []
    team_times_one = []
    team_times_four = []
    four_by_one = []
    four_by_four = []
    n = 0
    while n < len(Countries):
        print("Welcome to the Olympic Trials for " + Countries[n]['Name'])
        sprinters = sprinterlist(Countries[n]['Sprinters'], Countries[n])
        runners = runnerlist(Countries[n]['Runners'], Countries[n])
        endurance = endlist(Countries[n]['Endurance'], Countries[n])
        # if Countries[n] == Jamaica:
        #     sprinters.append(Usain_Bolt)
        #     sprinters.append(Nickel_Ashmeade)
        #     sprinters.append(Yohan_Blake)
        # if Countries[n] == USA:
        #     runners.append(LaShawn_Merritt)
        #     sprinters.append(Trayvon_Bromell)
        #     sprinters.append(Justin_Gatlin)
        # if Countries[n] == France:
        #     sprinters.append(Jimmy_Vicault)
        #     sprinters.append(Christophe_LeMaitre)
        # if Countries[n] == South_Africa:
        #     runners.append(Wayde_Niekerk)
        # if Countries[n] == Canada:
        #     sprinters.append(Andre_DeGrasse)
        # if Countries[n] == Grenada:
        #     runners.append(Kirani_James)
        # if Countries[n] == Trinidad_and_Tobago:
        #     runners.append(Machel_Cedinio)
        a = olympic_trials(sprinters, runners, endurance, Countries[n], 100)
        b = olympic_trials(sprinters, runners, endurance, Countries[n], 200)
        c = olympic_trials(sprinters, runners, endurance, Countries[n], 400)
        d = olympic_trials(sprinters, runners, endurance, Countries[n], 800)
        print()
        print(color.BOLD + "Qualifying for the 100m" + color.END)
        heat_intro(a[0], a[1])
        print(color.BOLD + "4 x 100m Relay Team" + color.END)
        team_intro(a[2], a[3], a[4])
        team_times_one.append(a[4])
        four_by_one.append(a[2])
        print(color.BOLD + "Qualifying for the 200m" + color.END)
        heat_intro(b[0], b[1])
        print(color.BOLD + "Qualifying for the 400m" + color.END)
        heat_intro(c[0], c[1])
        print(color.BOLD + "4 x 400m Relay Team" + color.END)
        team_intro(c[2], c[3], c[4])
        team_times_four.append(c[4])
        four_by_four.append(c[2])
        print(color.BOLD + "Qualifying for the 800m" + color.END)
        heat_intro(d[0], d[1])
        one += a[0]
        two += b[0]
        four += c[0]
        eight += d[0]
        one_times += a[1]
        two_times += b[1]
        four_times += c[1]
        eight_times += d[1]
        n += 1
    times = copy.copy(team_times_one)
    times2 = copy.copy(team_times_four)
    fourone_times = []
    fourone = []
    fourfour_times = []
    fourfour = []
    n = 0
    while n < 16:
        bottom = min(times)
        lowest = times.index(bottom)
        fourone_times.append(team_times_one[lowest])
        fourone.append(four_by_one[lowest])
        times[lowest] = 5000
        bottom = min(times2)
        lowest = times2.index(bottom)
        fourfour_times.append(team_times_four[lowest])
        fourfour.append(four_by_four[lowest])
        times2[lowest] = 5000
        n += 1
    relay_preview(fourone, fourone_times, 400)
    relay_preview(fourfour, fourfour_times, 1600)
    preview(one, one_times, 100)
    preview(two, two_times, 200)
    preview(four, four_times, 400)
    preview(eight, eight_times, 800)
    olympics(eight, 800)
    preview(four, four_times, 400)
    olympics(four, 400)
    preview(two, two_times, 200)
    olympics(two, 200)
    preview(one, one_times, 100)
    olympics(one, 100)
    relay_preview(fourone, fourone_times, 400)
    relay_olympics(fourone, 400)
    relay_preview(fourfour, fourfour_times, 1600)
    relay_olympics(fourfour, 1600)


#race([Usain_Bolt, Andre_DeGrasse, Trayvon_Bromell, Jimmy_Vicault, Justin_Gatlin, LaShawn_Merritt, Christophe_LeMaitre, Nickel_Ashmeade], 100)

#print(timed(3.3, 9.4, 0.994, 90, 800)



season()




#
# lst = sprinterlist(64)
# lst[0] = Usain_Bolt
# lst[1] = Andre_DeGrasse
# lst[2] = L
# aShawn_Merritt
# lst[3] = Christophe_LeMaitre
# lst[4] = Wayde_Niekerk
# lst[5] = Machel_Cedinio
# lst[6] = Kirani_James
# lst[7] = Justin_Gatlin
# lst[8] = Yohan_Blake
# lst[9] = Nickel_Ashmeade
# lst[10] = Jimmy_Vicault
# lst[11] = Trayvon_Bromell
# #olympics(lst, 100)
#
# olympic_trials(sprinterlist(20), runnerlist(20), Jamaica, 100)
#
# #timed_race(Usain_Bolt, 400)

