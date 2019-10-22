from __future__ import division
from random import randint
import random
from decimal import Decimal
import copy
import time
import math
import locale
import numpy as np

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
    NONE = '\033[22m'
    END = '\033[0m'

British = []
US = []
Masters = []

from bisect import bisect_left

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))


def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

First_Names = ["Christophe", "David", "Adam", "Carl", "Jimmy", "Wayde", "Matteo", "James", "Filippo", "Alex", "Pierre-Ambroise","Boris","David", "Adam", "Carl", "Jimmy", "Riste", "Lukas", "Julius", "Serhiy", "Andreas", "Marcin", "Alex","Aska", "Xie", "Su", "Jin Wei", "Ryota", "Kim", "Kenji", "Kei", "Teng", "Suguru", "Cheng", "Takayuki", "Park", "Li", "Shota", "Nobuya","Tiger", "Phil","Rory","Rickie","Dustin","Jeremy","David","Harold","Gordon","Iain","Neil","Winston","George","Clive", "Neville","Tim","Nick","Nigel","Norman","Vince","Ed","Andy","Boris","Gerry","Alex","Philip","Jacob","John","Sadiq","Liam","Chris","Tom","Tony","Hilary","Clement","Benjamin","William"]
Last_Names = ["Lemaitre", "Vicaut", "van Niekerk", "Hayes", "Hines", "Galvan", "Ellington", "Tortu", "Wilson", "Bosse","Kszczot", "Hayes", "Hines", "Pandev", "Jakubczyk", "Reus", "Smelyk", "Bube", "Lewandowski", "Zyabkina", "Safronova", "Radzivil","Cambridge", "Zhenye", "Bingtian", "Yamagata", "Kuk-young", "Fujimitsu", "Takase", "Osako", "Wenjun", "Wen", "Shiwei", "Kishimoto", "Bong-go", "Chil-sung","Woods","Mickelson", "Fowler", "Johnson","Corbyn","Gladstone", "Wilson", "Gove","Hague","Kinnock","Foote", "Duncan Smith","Brown","Macmillan", "Lloyd George","Cameron","Chamberlain","Osborne","Lewis","May","Farron","Clegg","Farage","Lamb","Rudd","Cable","Miliband","Davey","Balls","Cooper","Burnham","Johnson","Dodds","Adams","Sturgeon","Salmond","Davis","Hammond","Rees-Mogg","Abbott","McDonell","Khan","Patel","Hunt","Truss","Fox","Grayling","Clarke","Livingston","Leadsom","Watson","Benn","Disraeli","Blair","Thornberry","Major","Thatcher","Attlee","Long-Bailey","Rayner","Eagle"]

def create_hole(par, difficulty):
    hole = {}
    l = randint(0,7 - difficulty)
    r = randint(0,7 - difficulty)
    if l == 0:
        hole['Left'] = 'water'
    else:
        hole['Left'] = 'woods'
    if r == 0:
        hole['Right'] = 'water'
    else:
        hole['Right'] = 'woods'
    if par == 3:
        hole['Length'] = np.random.normal(280 + difficulty * 5, 20)
    elif par == 4:
        hole['Length'] = np.random.normal(415 + difficulty * 10, 25)
    else:
        hole['Length'] = np.random.normal(605 + difficulty * 15, 30)
    hole['Location'] = [np.random.normal(0,3 + difficulty / 2),hole['Length'] + np.random.normal(0,3 + difficulty / 2)]
    hole['Green Width'] = np.random.normal(35 - difficulty * 2,5)
    hole['Fairway'] = np.random.normal(75 + difficulty * 3,15)
    hole['Par'] = par
    hole['Fairway Widths'] = []
    bunker1 = [np.random.normal(-5,3),np.random.normal(hole['Length'] - 30,8)]
    hole['Bunker'] = [bunker1,[bunker1[0] + np.random.normal(8 + difficulty, 3),bunker1[1] + np.random.normal(8 + difficulty,3)]]
    len = 0
    while len < hole['Length'] - hole['Green Width']:
        hole['Fairway Widths'].append(np.random.normal(32 - difficulty,5))
        len += 100
    return hole


def location1(coordinates,hole):
    if hole['Bunker'][0][0] < coordinates[0] < hole['Bunker'][1][0] and hole['Bunker'][0][1] < coordinates[1] < hole['Bunker'][1][1]:
        loc = 'Sand'
    elif hole['Length'] - hole['Green Width'] > coordinates[1] > hole['Fairway']:
        width = hole['Fairway Widths'][int(coordinates[1] / 100) - 1]
        if abs(coordinates[0]) < width:
            loc = 'Fairway'
        elif abs(coordinates[0]) < width * 2:
            loc = 'Rough'
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
    elif hole['Length'] + hole['Green Width'] > coordinates[1] > hole['Length'] - hole['Green Width']:
        width = hole['Green Width']
        if abs(coordinates[0]) < hole['Green Width']:
            loc = 'Green'
        elif abs(coordinates[0]) < width * 2:
            loc = 'Rough'
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
    elif coordinates[1] < hole['Fairway']:
        width = hole['Fairway Widths'][0]
        if abs(coordinates[0]) < width * 2:
            loc = 'Rough'
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
    elif coordinates[1] > hole['Length'] + hole['Green Width']:
        width = hole['Green Width']
        if abs(coordinates[0]) < width * 2 and abs(coordinates[1] - hole['Length']) < width * 2:
            loc = 'Rough'
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
    return loc


def location(coordinates,hole):
    dist = str(round(distance(coordinates, hole), 1)) + " yards from the hole."
    if hole['Bunker'][0][0] < coordinates[0] < hole['Bunker'][1][0] and hole['Bunker'][0][1] < coordinates[1] < hole['Bunker'][1][1]:
        loc = 'Sand'
        print("The ball is in the bunker, " + dist)
    elif hole['Length'] - hole['Green Width'] > coordinates[1] > hole['Fairway']:
        width = hole['Fairway Widths'][int(coordinates[1] / 100) - 1]
        if abs(coordinates[0]) < width:
            loc = 'Fairway'
            print("The ball is on the fairway, " + dist)
        elif abs(coordinates[0]) < width * 2:
            loc = 'Rough'
            print("The ball is in the rough, " + dist)
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
            print("The ball is in the " + loc + ", " + dist)
    elif hole['Length'] + hole['Green Width'] > coordinates[1] > hole['Length'] - hole['Green Width']:
        width = hole['Green Width']
        if abs(coordinates[0]) < hole['Green Width']:
            loc = 'Green'
            print("The ball is on the green, " + dist)
        elif abs(coordinates[0]) < width * 2:
            loc = 'Rough'
            print("The ball is in the rough, " + dist)
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
            print("The ball is in the " + loc + ", " + dist)
    elif coordinates[1] < hole['Fairway']:
        width = hole['Fairway Widths'][0]
        if abs(coordinates[0]) < width * 2:
            loc = 'Rough'
            print("The ball is in the rough, " + dist)
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
            print("The ball is in the " + loc + ", " + dist)
    elif coordinates[1] > hole['Length'] + hole['Green Width']:
        width = hole['Green Width']
        if abs(coordinates[0]) < width * 2 and abs(coordinates[1] - hole['Length']) < width * 2:
            loc = 'Rough'
            print("The ball is in the rough, " + dist)
        else:
            if coordinates[0] < 0:
                loc = hole['Left']
            else:
                loc = hole['Right']
            print("The ball is in the " + loc + ", " + dist)
    return loc


def create_golfer():
    golfer = {}
    golfer['Age'] = randint(25,70)
    name = First_Names[randint(0, len(First_Names) - 1)]
    surname = Last_Names[randint(0, len(Last_Names) - 1)]
    golfer['Name'] = str(name) + " " + str(surname)
    golfer['Driving Range'] = np.random.normal(260,10)
    golfer['Driving Accuracy'] = np.random.normal(20,4) / 100
    golfer['Putting Accuracy'] = np.random.normal(7,0.8) / 100
    golfer['Irons Accuracy'] = []
    golfer['Irons Range'] = []
    golfer['Money'] = 0
    n = 0
    while n < 6:
        golfer['Irons Accuracy'].append(np.random.normal(17 - n/2, 1.5) / 100)
        golfer['Irons Range'].append(np.random.normal(230 - 15*n, 10))
        n += 1
    golfer['Wedge Range'] = np.random.normal(90,7)
    golfer['Wedge Accuracy'] = np.random.normal(10,1) / 100
    return golfer


def distance(coordinates,hole):
    d = (abs(coordinates[0] - hole['Location'][0]) ** 2 + abs(coordinates[1] - hole['Location'][1]) ** 2) ** (1/2)
    return d


def drive(golfer, hole,watch):
    coordinates = [0,0]
    if coordinates[0] > hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] < hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] > hole['Location'][0] and coordinates[1] > hole['Location'][1]:
        a = 3.14 + math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    else:
        a =  - 3.14 - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    if distance(coordinates,hole) < golfer['Driving Range']:
        accuracy = distance(coordinates,hole) / golfer['Driving Range'] * golfer['Driving Accuracy']
        length = distance(coordinates,hole)
    else:
        accuracy = golfer['Driving Accuracy']
        length = golfer['Driving Range']
    angle = np.random.normal(a, accuracy)
    dist = np.random.normal(length, accuracy * 20)
    x = dist * math.sin(abs(angle))
    if angle < 0:
        x = -x
    y = dist * math.cos(abs(angle))
    coordinate = [x,y]
    if distance([x, y], hole) < 0.2:
        if watch == "Y":
            print(golfer['Name'] + " makes a hole in one.")
        coordinate = hole['Location']
    return coordinate


def putt(golfer, hole, coordinates,watch):
    d = distance(coordinates,hole)
    length = distance(coordinates,hole)
    length *= np.random.normal(110,5) / 100
    accuracy = golfer['Putting Accuracy']
    if coordinates[0] > hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] < hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] > hole['Location'][0] and coordinates[1] > hole['Location'][1]:
        a = 3.14 + math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    else:
        a =  - 3.14 - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    # vec = [hole['Location'][0] - coordinates[0], hole['Location'][1] - coordinates[1]]
    # a = angle(vec, [0, 1])
    ang = np.random.normal(a, accuracy)
    dist = np.random.normal(length, accuracy * 10)
    z = d * math.sin(ang) + coordinates[0]
    w = d * math.cos(ang)
    w += coordinates[1]
    if dist > d and distance([z,w],hole) < 0.4:
        if watch == "Y":
            print(golfer['Name'] + " makes the putt.")
        coordinate = hole['Location']
    else:
        x = dist * math.sin(ang)
        x = coordinates[0] + x
        y = dist * math.cos(ang) + coordinates[1]
        coordinate = [x, y]
        if distance([x, y],hole) < 0.6:
            if watch == "Y":
                print(golfer['Name'] + " makes the putt.")
            coordinate = hole['Location']
    return coordinate


def iron_shot(golfer,hole,coordinates,watch):
    d = distance(coordinates,hole)
    c = golfer['Irons Range'].index(takeClosest(d,golfer['Irons Range']))
    power = golfer['Irons Range'][c]
    acc = golfer['Irons Accuracy'][c]
    l = location1(coordinates, hole)
    if l == 'woods':
        acc += 0.4
        power /= 1.3
    elif l == 'Rough':
        acc += 0.1
        power /= 1.1
    if watch == "Y":
        print(golfer['Name'] + " has elected to use a " + str(4 + c) + " iron.")
    if d < power:
        accuracy = d / power * acc
        length = d
    else:
        accuracy = acc
        length = power
    if coordinates[0] > hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] < hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] > hole['Location'][0] and coordinates[1] > hole['Location'][1]:
        a = 3.14 + math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    else:
        a =  - 3.14 - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    # vec = [hole['Location'][0] - coordinates[0], hole['Location'][1] - coordinates[1]]
    # a = angle(vec,[0,1])
    ang = np.random.normal(a, accuracy)
    dist = np.random.normal(length, accuracy * 20)
    x = dist * math.sin(ang)
    x = coordinates[0] + x
    y = dist * math.cos(ang) + coordinates[1]
    coordinate = [x, y]
    if distance([x, y], hole) < 0.2:
        if watch == "Y":
            print(golfer['Name'] + " makes the shot.")
        coordinate = hole['Location']
    return coordinate


def wedge_shot(golfer,hole,coordinates,watch):
    d = distance(coordinates, hole)
    if watch == "Y":
        print(golfer['Name'] + " has elected to use a wedge.")
    acc = golfer['Wedge Accuracy']
    power = golfer['Wedge Range']
    l = location1(coordinates, hole)
    if l == 'woods':
        acc += 0.2
        power /= 1.2
    elif l == 'Sand':
        acc += 0.4
        power /= 1.5
    if d < power:
        accuracy = d / power * acc
        length = d
    else:
        accuracy = acc
        length = power
    if coordinates[0] > hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] < hole['Location'][0] and coordinates[1] < hole['Location'][1]:
        a = math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    elif coordinates[0] > hole['Location'][0] and coordinates[1] > hole['Location'][1]:
        a = 3.14 + math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    else:
        a =  - 3.14 - math.atan(abs(coordinates[0] - hole['Location'][0]) / abs(coordinates[1] - hole['Location'][1]))
    # vec = [hole['Location'][0] - coordinates[0], hole['Location'][1] - coordinates[1]]
    # a = angle(vec,[0,1])
    ang = np.random.normal(a, accuracy)
    dist = np.random.normal(length, accuracy * 20)
    x = dist * math.sin(ang)
    x = coordinates[0] + x
    y = dist * math.cos(ang) + coordinates[1]
    coordinate = [x, y]
    if distance([x, y], hole) < 0.2:
        if watch == "Y":
            print(golfer['Name'] + " makes the shot.")
        coordinate = hole['Location']
    return coordinate


def result(par,shots,golfer,number):
    if par - shots == 3:
        print(golfer['Name'] + " got an albatross on hole " + str(number) + "!!!")
    elif par - shots == 2:
        print(golfer['Name'] + " got an eagle on hole " + str(number) + "!!")
    elif par - shots == 1:
        print(golfer['Name'] + " got a birdie on hole " + str(number) + "!")
    elif par - shots == 0:
        print(golfer['Name'] + " got par on hole " + str(number) + ".")
    elif par - shots == -1:
        print(golfer['Name'] + " got a bogey on hole " + str(number) + ".")
    elif par - shots == -2:
        print(golfer['Name'] + " got a double bogey on hole " + str(number) + ".")
    elif par - shots == -3:
        print(golfer['Name'] + " got a triple bogey on hole " + str(number) + ".")
    elif par - shots == -4:
        print(golfer['Name'] + " got a quadruple bogey on hole " + str(number) + ".")
    elif par - shots == -5:
        print(golfer['Name'] + " got a quintuple bogey on hole " + str(number) + ".")
    elif par - shots == -6:
        print(golfer['Name'] + " got a sextuple bogey on hole " + str(number) + ".")
    else:
        print(golfer['Name'] + " should probably retire from shooting +" + str(shots - par) + " on hole " + str(number))


def play(golfer, hole,watch):
    ball = drive(golfer, hole,watch)
    if watch == "Y":
        location(ball, hole)
    shots = 1
    prev = [0,0]
    while ball != hole['Location']:
        # location(prev,hole)
        # location(ball,hole)
        l = location1(ball,hole)
        if l != 'water':
            prev = ball
        if watch == "Y":
            input("Shot " + str(shots + 1) + "? ")
        if ball == [0,0]:
            ball = drive(golfer, hole, watch)
            shots += 1
        elif l == "Green":
            ball = putt(golfer,hole,ball,watch)
            shots += 1
        elif l == "Sand":
            ball = wedge_shot(golfer,hole,ball,watch)
            shots += 1
        elif l == "water":
            if watch == "Y":
                print("One Stroke Penalty for Hazard")
            ball = prev
            shots += 1
        else:
            if distance(ball,hole) < 110:
                ball = wedge_shot(golfer,hole,ball,watch)
            else:
                ball = iron_shot(golfer,hole,ball,watch)
            shots += 1
        if watch == "Y":
            location(ball, hole)
    return shots


def course(name, difficulty):
    threes = randint(3,6)
    holes = []
    n = 0
    while n < 18:
        if n < threes:
            holes.append(3)
        elif n < threes * 2:
            holes.append(5)
        else:
            holes.append(4)
        n += 1
    course = []
    handicap = 0
    n = 0
    while n < 18:
        number = randint(0,len(holes) - 1)
        par = holes[number]
        del holes[number]
        course.append(create_hole(par,difficulty))
        handicap += par
        n += 1
    course.append(name)
    return course


def day(golfer, course, watch):
    score = 0
    handicap = 0
    n = 0
    while n < 18:
        if watch == "Y":
            print()
            input("Hole " + str(n + 1) + "? ")
            handicap += course[n]['Par']
        h = play(golfer,course[n],watch)
        score += h
        if watch == "Y":
            result(course[n]['Par'], h, golfer, n + 1)
            print(str(score - handicap))
        n += 1
    return score


def summary(score,golfer):
    if score == 72:
        string = "Even"
    elif score > 72:
        string = "+" + str(score - 72)
    else:
        string = "-" + str(72 - score)
    if score >= 70:
        print(golfer['Name'] + " scored " + str(score) + " putting them at " + string + " for the day.")
    else:
        print(color.BOLD + golfer['Name'] + " scored " + str(score) + " putting them at " + string + " for the day." + color.END)


def leaderboard(golfers,scores,par,pros):
    new_scores = copy.copy(scores)
    print()
    n = 1
    while n < 11:
        pos = new_scores.index(min(new_scores))
        if golfers[pos] in pros:
            col = color.BLUE
        else:
            col = color.NONE
        if new_scores[pos] < par:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", -" + str(par - new_scores[pos]) + ")" + color.END)
        elif new_scores[pos] == par:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", E)" + color.END)
        else:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", +" + str(new_scores[pos] - par) + ")" + color.END)
        new_scores[pos] = 1000
        n += 1
    print()


def qualifiers(number,scores,golfers,par,lst,pros):
    new_scores = copy.copy(scores)
    print()
    n = 1
    while n < number + 1:
        pos = new_scores.index(min(new_scores))
        if golfers[pos] in pros:
            col = color.BLUE
        else:
            col = color.NONE
        if new_scores[pos] < par:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", -" + str(par - new_scores[pos]) + ")" + color.END)
        elif new_scores[pos] == par:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", E)" + color.END)
        else:
            print(col + str(n) + ". " + golfers[pos]['Name'] + " (" + str(new_scores[pos]) + ", +" + str(new_scores[pos] - par) + ")" + color.END)
        if golfers[pos] not in lst:
            lst.insert(randint(0,len(lst)),golfers[pos])
        new_scores[pos] = 1000
        if lst == pros:
            golfers[pos]['Money'] += (30 - n) ** 5 / 10
        n += 1
    print()


def qualifying(tournament, players,pros,number):
    lst = []
    u = 0
    while len(lst) <= players:
        golfers = []
        print("Welcome to Qualifying for the " + tournament)
        n = 0
        while n < number:
            if randint(0, int(4000 / (len(pros) + 1))) == 1 and u < len(pros) - 1:
                golfers.append(pros[u])
                u += 1
            if len(lst) / players > 0.9:
                while u < len(pros) - 1:
                    golfers.append(pros[u])
                    u += 1
            golfers.append(create_golfer())
            n += 1
        print()
        print("Welcome to Day 1")
        print()
        c = course("Qualifying Course",randint(0,1))
        scores = []
        n = 0
        while n < len(golfers):
            scores.append(day(golfers[n], c, "N"))
            n += 1
        leaderboard(golfers, scores, 72, pros)
        print()
        print("Welcome to Day 2")
        print()
        n = 0
        while n < len(golfers):
            r = day(golfers[n], c,"N")
            scores[n] += r
            n += 1
        qualifiers(5,scores,golfers,144,lst,pros)
        print()
    return lst


def historical(history,name):
    print()
    print(color.BOLD + "Historical Winners of the " + name + color.END)
    n = 0
    while n < len(history):
        print(str(2017 + n) + " - " + history[n])
        n += 1


def tournament(course,name,golfers,pros,history):
    print()
    print(color.BOLD + "Historical Winners of the " + name + color.END)
    n = 0
    while n < len(history):
        print(str(2017 + n) + " - " + history[n])
        n += 1
    print()
    print("Welcome to the " + name + " Day 1")
    print()
    scores = []
    TV = []
    w = True
    while w == True:
        x = input("Would you like to watch any golfers? ")
        if x == "N":
            w = False
        else:
            TV.append(x)
    input("Begin?")
    n = 0
    while n < len(golfers):
        if golfers[n]['Name'] in TV:
            watch = "Y"
        else:
            watch = "N"
        s = day(golfers[n], course, watch)
        summary(s, golfers[n])
        scores.append(s)
        n += 1
    leaderboard(golfers, scores, 72,pros)
    print()
    print("Welcome to the " + name + " Day 2")
    input("Begin?")
    print()
    n = 0
    while n < len(golfers):
        if golfers[n]['Name'] in TV:
            watch = "Y"
        else:
            watch = "N"
        r = day(golfers[n], course, watch)
        summary(r, golfers[n])
        scores[n] += r
        n += 1
    leaderboard(golfers, scores, 144,pros)
    print()
    print("Welcome to the " + name + " Day 3")
    input("Begin?")
    print()
    n = 0
    while n < len(golfers):
        if golfers[n]['Name'] in TV:
            watch = "Y"
        else:
            watch = "N"
        r = day(golfers[n], course, watch)
        summary(r, golfers[n])
        scores[n] += r
        n += 1
    leaderboard(golfers, scores, 216,pros)
    print()
    print("Welcome to the " + name + " Day 4")
    input("Begin?")
    print()
    n = 0
    while n < len(golfers):
        if golfers[n]['Name'] in TV:
            watch = "Y"
        else:
            watch = "N"
        r = day(golfers[n], course, watch)
        summary(r, golfers[n])
        scores[n] += r
        n += 1
    qualifiers(25,scores,golfers,288,pros,pros)
    winner = golfers[scores.index(min(scores))]
    history.append(winner['Name'] + " (" + str(min(scores)) + ")")
    print(winner['Name'] + " wins the " + name)


def PGA(pros):
    money = []
    n = 0
    while n < len(pros):
        money.append(pros[n]['Money'])
        n += 1
    new_money = copy.copy(money)
    print()
    n = 1
    while n < 21:
        pos = new_money.index(max(new_money))
        print(color.BLUE + str(n) + ". " + pros[pos]['Name'] + " (" + str(round(new_money[pos] / 1000000,2)) + " million)" + color.END)
        new_money[pos] = -500
        n += 1
    print()
    


def season(pros):
    courses = []
    courses.append(course('Augusta',5))
    courses.append(course('Pinehurst',4))
    courses.append(course('The Old Course',3))
    golfers = qualifying('British Open',100,pros, 200)
    tournament(courses[2],'British Open',golfers,pros,British)
    golfers = qualifying('US Open',100,pros,200)
    tournament(courses[1],'US Open',golfers,pros,US)
    golfers = qualifying('Masters', 100, pros, 200)
    tournament(courses[0], 'Masters', golfers, pros,Masters)
    PGA(pros)
    return pros


pros = qualifying("Pro Tour",100,[],1000)
year = 2017
n = 0
while n < 20:
    print()
    print(color.BOLD + "The year is " + str(year) + color.END)
    historical(British, 'British Open')
    historical(US, 'US Open')
    historical(Masters, 'Masters')
    print()
    pros = season(pros)
    u = 0
    while u < len(pros):
        pros[u]['Age'] += 1
        pros[u]['Money'] = 0
        chance = randint(0,75 ** 7)
        if chance < pros[u]['Age'] ** 7:
            print(pros[u]['Name'] + " has retired.")
            del pros[u]
            u -= 1
        u += 1
    year += 1
    n += 1


historical(British, 'British Open')
historical(US, 'US Open')
historical(Masters, 'Masters')