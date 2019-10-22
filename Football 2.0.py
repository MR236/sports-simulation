import numpy as np
from random import randint
import copy
from operator import lt, gt

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
    ORANGE = '\033[31m'


First_Names = ['Oliver', 'Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Muhammad', 'Leo', 'Oscar', 'Charlie', 'William', 'Henry', 'Alfie', 'Thomas', 'Joshua', 'Freddie', 'James', 'Arthur', 'Archie', 'Logan', 'Lionel', 'Christiano', 'Alex', 'Edward', 'Theo', 'Paul', 'Isaac', 'Lucas', 'Curtis', 'Samuel', 'Moses', 'Malcolm', 'Kabongo', 'Saikou', 'Lee', 'Alan', 'Mario', 'Vincent', 'Raheem']
Last_Names = ['Smith', 'Jones', 'Williams', 'Brown', 'Taylor', 'Davies', 'Wilson', 'Evans', 'Thomas', 'Roberts', 'Murphy', 'Walsh', 'Smith', 'Byrne', 'Anderson', 'Martin', 'Taylor', 'Singh', 'Salah', 'Messi', 'Ronaldo', 'Rooks', 'Maybee', 'Risk', 'Kane', 'Sane', 'Pogba', 'Rowe', 'Cheek', 'Muldoon', 'Emmanuel', 'Philips', 'Boden', 'Tshimanga', 'Bonne', 'Ballotelli', 'McCallum', 'Company', 'Stirling', 'Mandela', 'Cattermole', 'McGeady', 'Shearer']
Formations = [[4, 3, 3], [4, 4, 2], [4, 5, 1], [5, 4, 1], [3, 5, 2], [5, 3, 2], [3, 4, 3]]


def hundred_scale(rate, side):
    total = 0
    for x in range(100):
        p = np.random.poisson(rate)
        opp = np.random.poisson(1.4)
        if side(p, opp):
            total += 3
        elif p == opp:
            total += 1
    return round(total / 3, 1)


def strength(lineup):
    O = 0
    D = 0
    sumO = 2
    sumD = 32
    D += lineup['GK'][0].defence / (lineup['GK'][0].energy / 100) * 32
    O += lineup['GK'][0].offence * (lineup['GK'][0].energy / 100) * 2
    for i in lineup['DF']:
        D += i.defence / (i.energy / 100) * 8
        O += i.offence * (i.energy / 100) * 4
        sumO += 4
        sumD += 8
    for i in lineup['MF']:
        D += i.defence / (i.energy / 100) * 5
        O += i.offence * (i.energy / 100) * 10
        sumO += 10
        sumD += 5
    for i in lineup['FW']:
        D += i.defence / (i.energy / 100) * 2
        O += i.offence * (i.energy / 100) * 16
        sumO += 16
        sumD += 2
    return [round(O / sumO, 2), round(D / sumD, 2)]


def goal_distribution(goals, lineup):
    distribution = dict()
    players = dict()
    distribution[lineup['GK'][0].name] = lineup['GK'][0].offence * (lineup['GK'][0].energy / 100) * 0.01
    players[lineup['GK'][0].name] = lineup['GK'][0]
    for n in lineup['DF']:
        distribution[n.name] = n.offence * (n.energy / 100) * 0.03
        players[n.name] = n
    for n in lineup['MF']:
        distribution[n.name] = n.offence * (n.energy / 100)* 0.1
        players[n.name] = n
    for n in lineup['FW']:
        distribution[n.name] = n.offence * (n.energy / 100) * 0.23
        players[n.name] = n
    x = sum(distribution.values())
    for n in distribution:
        distribution[n] = distribution[n] / x * goals
    return [distribution, players]


def game(hometeam, awayteam):
    HL = hometeam.temp_substitutes()
    AL = awayteam.temp_substitutes()
    t1strength = strength(HL)
    t2strength = strength(AL)
    t1goalsadd = (t1strength[0] + t2strength[1] - 1.4) * 1.3
    t1goalsmult = (t1strength[0] / 1.4) * (t2strength[1] / 1.4) * 1.4 * 1.3
    t2goalsadd = (t1strength[1] + t2strength[0] - 1.4) * 0.7
    t2goalsmult = (t1strength[1] / 1.4) * (t2strength[0] / 1.4) * 1.4 * 0.7
    if t1goalsadd < 0:
        t1goals = (t1strength[0] / 1.4) * (t2strength[1] / 1.4) * 1.4 * 1.3
    else:
        t1goals = t1goalsadd * 0.9 + t1goalsmult * 0.1
    if t2goalsadd < 0:
        t2goals = (t1strength[1] / 1.4) * (t2strength[0] / 1.4) * 1.4 * 0.7
    else:
        t2goals = t2goalsadd * 0.9 + t2goalsmult * 0.1
    distplayers1 = goal_distribution(t1goals, HL)
    distplayers2 = goal_distribution(t2goals, AL)
    home_goals = []
    away_goals = []
    for i in distplayers1[0]:
        for z in range(np.random.poisson(distplayers1[0][i])):
            home_goals.append({'Scorer': i, 'Minute': randint(1, 90)})
            distplayers1[1][i].careergoals += 1
            distplayers1[1][i].seasongoals += 1
    for i in distplayers2[0]:
        for z in range(np.random.poisson(distplayers2[0][i])):
            away_goals.append({'Scorer': i, 'Minute': randint(1, 90)})
            distplayers2[1][i].careergoals += 1
            distplayers2[1][i].seasongoals += 1
    HG = len(home_goals)
    AG = len(away_goals)
    print(hometeam.color + hometeam.name + " " + color.END + str(HG) + "-" + str(AG) + " " + awayteam.color + awayteam.name + color.END)
    if isinstance(hometeam, PC):
        hometeam.weeklygames.append(hometeam.color + hometeam.name + " " + color.END + str(HG) + "-" + str(AG) + " " + awayteam.color + awayteam.name + color.END)
    if isinstance(awayteam, PC):
        awayteam.weeklygames.append(hometeam.color + hometeam.name + " " + color.END + str(HG) + "-" + str(AG) + " " + awayteam.color + awayteam.name + color.END)
    hometeam.GF += HG
    hometeam.GA += AG
    awayteam.GF += AG
    awayteam.GA += HG
    if HG > AG:
        hometeam.points += 3
        hometeam.wins += 1
        awayteam.losses += 1
    elif AG > HG:
        awayteam.points += 3
        hometeam.losses += 1
        awayteam.wins += 1
    else:
        hometeam.points += 1
        awayteam.points += 1
        hometeam.ties += 1
        awayteam.ties += 1
    for i in HL:
        for x in HL[i]:
            if x.position == 'GK':
                x.energy *= (x.fitness + 1) / 2
            else:
                x.energy *= x.fitness
    for i in AL:
        for x in AL[i]:
            if x.position == 'GK':
                x.energy *= (x.fitness + 1) / 2
            else:
                x.energy *= x.fitness
    hometeam.fixtures[hometeam.wins+hometeam.losses+hometeam.ties-1]['Score'] = str(HG) + "-" + str(AG)
    awayteam.fixtures[awayteam.wins+awayteam.losses+awayteam.ties-1]['Score'] = str(AG) + "-" + str(HG)
    return [home_goals, away_goals]


class Player(object):

    def __init__(self, offence, defence, age, team):
        coefficient = 1.2*np.e**((-1/20)*abs(27-age))
        coefficient2 = 1.2*np.e**((-1/20)*abs(24-age))
        self.offence = round(np.random.gamma(5/coefficient, offence*coefficient*(1/5)), 2)
        self.defence = round(np.random.gamma(5*coefficient, defence/coefficient*(1/5)), 2)
        self.fitness = round(1/(1+np.e**-(np.random.normal(0, 1) + 2*coefficient2)), 3)
        self.energy = 100
        self.age = age
        self.name = First_Names[randint(0,len(First_Names) - 1)] + " " + Last_Names[randint(0,len(Last_Names) - 1)]
        self.orating = hundred_scale(self.offence, gt)
        self.drating = hundred_scale(self.defence, lt)
        self.frating = round(self.fitness * 100, 1)
        self.careergoals = 0
        self.seasongoals = 0
        self.team = team


    def summary(self):
        print(self.name + " " + self.position + " (Age: " + str(self.age) + ", Overall: " + str(self.overall) + ")")

    def recovery(self):
        self.energy = 100 - (100 - self.energy) / 2


class Forward(Player):

    def __init__(self, offence, defence, age, team):
        super().__init__(offence, defence, age, team)
        self.position = 'FW'
        self.overall = round(0.72 * self.orating + 0.18 * self.drating + 0.1 * self.frating, 1)

    def pos_summary(self):
        self.summary()
        print("Offence: " + str(self.orating) + ", " + "Defence: " + str(self.drating))


class Midfielder(Player):

    def __init__(self, offence, defence, age, team):
        super().__init__(offence, defence, age, team)
        self.position = 'MF'
        self.overall = round(0.45 * self.orating + 0.45 * self.drating + 0.1 * self.frating, 1)

    def pos_summary(self):
        self.summary()
        print("Offence: " + str(self.orating) + ", " + "Defence: " + str(self.drating))


class Defender(Player):

    def __init__(self, offence, defence, age, team):
        super().__init__(offence, defence, age, team)
        self.position = 'DF'
        self.overall = round(0.18 * self.orating + 0.72 * self.drating + 0.1 * self.frating, 1)

    def pos_summary(self):
        self.summary()
        print("Offence: " + str(self.orating) + ", " + "Defence: " + str(self.drating))


class Goalkeeper(Player):

    def __init__(self, offence, defence, age, team):
        super().__init__(offence, defence, age, team)
        self.position = 'GK'
        self.overall = round(0.04 * self.orating + 0.91 * self.drating + 0.05 * self.frating, 1)

    def pos_summary(self):
        self.summary()
        print("Distribution: " + str(self.orating) + ", " + "Shot Stopping: " + str(self.drating))


class Team(object):

    def __init__(self, offence, defence, name, teamcolor, value):
        self.name = name
        self.color = teamcolor
        self.value = value
        self.GK = []
        self.DF = []
        self.MF = []
        self.FW = []
        self.fixtures = []
        for i in range(randint(2,4)):
            self.GK.append(Goalkeeper(offence, defence, int(np.random.normal(27, 3)), self))
        for i in range(randint(3,5)):
            self.FW.append(Forward(offence, defence, int(np.random.normal(27, 3)), self))
        for i in range(randint(7,11)):
            self.MF.append(Midfielder(offence, defence, int(np.random.normal(27, 3)), self))
        for i in range(25 - len(self.FW) - len(self.GK) - len(self.MF)):
            self.DF.append(Defender(offence, defence, int(np.random.normal(27, 3)), self))
        self.players = self.GK + self.DF + self.MF + self.FW
        self.formation = Formations[randint(0, len(Formations) - 1)]
        self.lineup = self.startinglineup()
        self.points = 0
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.GF = 0
        self.GA = 0
        self.bench = self.substitutes()

    def summary(self):
        print(self.color + self.name + color.END)
        for z in self.players:
            z.summary()

    def starters(self):
        print()
        for i in ['GK', 'DF', 'MF', 'FW']:
            print(color.BOLD + i + color.END)
            for x in self.lineup[i]:
                print(x.name + " (O: " + str(x.orating) + " D: " + str(x.drating) + " Fitness: " + str(x.frating) + " Ovr: "+ str(x.overall) + ") Goals: " + str(x.seasongoals))
        print(color.BOLD + 'Substitutes' + color.END)
        n = 1
        for x in self.bench:
            print(str(n) + ". " + x.name + " " + x.position + " (O: " + str(x.orating) + " D: " + str(x.drating) + " Fitness: " + str(x.frating) + " Ovr: " + str(x.overall) + ") Goals: " + str(x.seasongoals))
            n += 1

    def startinglineup(self):
        lineup = {'DF': [], 'MF': [], 'FW': [], 'GK': []}
        self.GK.sort(key=lambda x: x.overall, reverse=True)
        lineup['GK'].append(self.GK[0])
        self.DF.sort(key=lambda x: x.overall, reverse=True)
        self.MF.sort(key=lambda x: x.overall, reverse=True)
        for i in range(0,self.formation[0]):
            lineup['DF'].append(self.DF[i])
        for i in range(0, self.formation[1]):
            lineup['MF'].append(self.MF[i])
        self.FW.sort(key=lambda x: x.overall, reverse=True)
        for i in range(0,self.formation[2]):
            lineup['FW'].append(self.FW[i])
        return lineup

    def substitutes(self):
        substitutes = []
        available = []
        avail_pos = {'GK': [], 'DF': [], 'MF': [], 'FW': []}
        for i in self.GK:
            if i not in self.lineup['GK']:
                available.append(i)
                avail_pos['GK'].append(i)
        for i in self.DF:
            if i not in self.lineup['DF']:
                available.append(i)
                avail_pos['DF'].append(i)
        for i in self.MF:
            if i not in self.lineup['MF']:
                available.append(i)
                avail_pos['MF'].append(i)
        for i in self.FW:
            if i not in self.lineup['FW']:
                available.append(i)
                avail_pos['FW'].append(i)
        for i in avail_pos:
            if len(avail_pos[i]) > 0:
                avail_pos[i].sort(key=lambda x: x.overall, reverse=True)
                substitutes.append(avail_pos[i][0])
        available.sort(key=lambda x: x.overall, reverse=True)
        n = 0
        while len(substitutes) < 7:
            if available[n] not in substitutes:
                substitutes.append(available[n])
            n += 1
        return substitutes

    def temp_substitutes(self):
        lineup = {'GK': [], 'DF': [], 'MF': [], 'FW': []}
        for z in self.bench:
            lineup[z.position].append(z)
        for x in self.lineup:
            for i in self.lineup[x]:
                lineup[x].append(i)
        lineup['GK'].sort(key=lambda x: x.overall * x.energy, reverse=True)
        while len(lineup['GK']) > 1:
            del lineup['GK'][len(lineup['GK']) - 1]
        lineup['DF'].sort(key=lambda x: x.overall * x.energy, reverse=True)
        while len(lineup['DF']) > self.formation[0]:
            del lineup['DF'][len(lineup['DF']) - 1]
        lineup['MF'].sort(key=lambda x: x.overall * x.energy, reverse=True)
        while len(lineup['MF']) > self.formation[1]:
            del lineup['MF'][len(lineup['MF']) - 1]
        lineup['FW'].sort(key=lambda x: x.overall * x.energy, reverse=True)
        while len(lineup['FW']) > self.formation[2]:
            del lineup['FW'][len(lineup['FW']) - 1]
        return lineup

    def recovery(self):
        for i in self.players:
            i.recovery()

    def games(self):
        print()
        for i in self.fixtures:
            print("Week " + i['Week'] + ": " + i['Opponent'].name + " (" + i['Location'] + ") " + i['Score'])


class League(object):

    def __init__(self, teamslist, name, promotion, relegation):
        self.teams = teamslist
        self.players = []
        for i in teamslist:
            for z in i.players:
                self.players.append(z)
        self.schedule = self.scheduling()
        self.name = name
        self.promotion = promotion
        self.relegation = relegation

    def scheduling(self):
        games = []
        schedule = []
        teamsplaying = []
        unfilled = []
        for i in self.teams:
            i.league = self
            for z in self.teams:
                if i.name != z.name:
                    games.append([i, z])
        for x in range(len(self.teams) * 2 + 15):
            unfilled.append(len(schedule))
            schedule.append([])
            teamsplaying.append([])
        while len(games) > 0:
            n = randint(0, len(games) - 1)
            g = games[n]
            t = randint(0, len(unfilled) - 1)
            placement = unfilled[t]
            if g[0].name not in teamsplaying[placement] and g[1].name not in teamsplaying[placement]:
                schedule[placement].append(g)
                teamsplaying[placement].append(g[0].name)
                teamsplaying[placement].append(g[1].name)
                del games[n]
                if len(schedule[placement]) == int(np.floor(len(self.teams) / 2)):
                    del unfilled[t]
        n = 0
        while n + 1 < len(schedule):
            schedule[n] += schedule[n+1]
            del schedule[n+1]
            n += 1
        for n in range(0, len(schedule)):
            for i in schedule[n]:
                i[0].fixtures.append({'Week': str(n + 1), 'Opponent': i[1], 'Location': 'Home', 'Score': ""})
                i[1].fixtures.append({'Week': str(n + 1), 'Opponent': i[0], 'Location': 'Away', 'Score': ""})
        return schedule

    def leadingscorers(self):
        self.players.sort(key=lambda x: x.seasongoals, reverse=True)
        print(self.name + " Leading Scorers")
        for i in range(0, 10):
            print(str(i+1) + ". " + self.players[i].name + " (" + self.players[i].position + ", " + self.players[i].team.name + ") " + str(self.players[i].seasongoals))

    def leaguetable(self):
        ranks = copy.copy(self.teams)
        ranks.sort(key=lambda x: x.GF - x.GA, reverse=True)
        ranks.sort(key=lambda x: x.points, reverse=True)
        print(self.name + " Table")
        string = "Club"
        for i in range(20):
            string += " "
        string += "GP  W   D   L   GF  GA  GD  Pts"
        print(string)
        for i in range(0, len(ranks)):
            t = ranks[i]
            string = ""
            if i < self.promotion:
                string += color.GREEN
            if i > len(self.teams) - self.relegation - 1:
                string += color.RED
            string += str(i + 1) + ". " + t.name
            string += " " * (2-len(str(i+1)))
            for i in range(20 - len(t.name)):
                string += " "
            string += str(t.wins + t.losses + t.ties) + " " * (4 - len(str(t.wins + t.losses + t.ties)))
            string += str(t.wins) + " " * (4 - len(str(t.wins)))
            string += str(t.ties) + " " * (4 - len(str(t.ties)))
            string += str(t.losses) + " " * (4 - len(str(t.losses)))
            string += str(t.GF) + " " * (4 - len(str(t.GF)))
            string += str(t.GA) + " " * (4 - len(str(t.GA)))
            string += str(t.GF - t.GA) + " " * (4 - len(str(t.GF - t.GA)))
            string += str(t.points)
            print(string + color.END)

    def top_players(self):
        self.players.sort(key=lambda x: x.overall, reverse=True)
        print(self.name + " Top Players")
        for i in range(0, 10):
            print(str(i + 1) + ". " + self.players[i].name + " (" + self.players[i].position + ", " + self.players[i].team.name + ") " + str(self.players[i].overall))


class PC(Team):

    def dashboard(self):
        ranks = copy.copy(self.league.teams)
        ranks.sort(key=lambda x: x.GF - x.GA, reverse=True)
        ranks.sort(key=lambda x: x.points, reverse=True)
        print()
        print(self.name + " Dashboard")
        if len(self.weeklygames) > 0:
            print()
            print("This Week")
            for i in self.weeklygames:
                print(i)
            self.weeklygames = []
        print()
        print("Upcoming Games")
        n = 0
        while n < len(self.fixtures) and self.fixtures[n]['Score'] != "":
            n += 1
        if n == len(self.fixtures):
            print("Season Over")
        else:
            for i in range(0,3):
                if n+i < len(self.fixtures):
                    print("Week " + self.fixtures[n+i]['Week'] + ": " + self.fixtures[n+i]['Opponent'].name + " (" + self.fixtures[n+i]['Location'] + ") " + self.fixtures[n+i]['Score'])
        print()
        print(str(self.wins) + "-" + str(self.ties) + "-" + str(self.losses) + ", " + str(self.points) + " points")
        string = str(ranks.index(self) + 1)
        if string == "1":
            string += "st"
        elif string == "2":
            string += "nd"
        elif string == "3":
            string += "rd"
        else:
            string += "th"
        string += " in " + self.league.name
        print(string)
        print()
        print("Leading Scorers")
        self.players.sort(key=lambda x: x.seasongoals, reverse=True)
        for i in range(0,3):
            print(str(i+1) + ". " + self.players[i].name + " " + self.players[i].position + " " + str(self.players[i].seasongoals))

    def main_menu(self, leagues):
        print()
        print(self.name + " Main Menu")
        print("[1] See Stats and Standings")
        print("[2] View Team Roster")
        print("[3] Adjust Starting Lineup")
        print("[4] See Fixtures")
        print("[5] Play Week")
        action = input("Action? ")
        try:
            action = int(action)
        except ValueError:
            self.main_menu(leagues)
            return 1
        if action not in [1, 2, 3, 4, 5]:
            self.main_menu(leagues)
            return 1
        elif action == 1:
            self.league_menu(leagues)
        elif action == 2:
            self.roster_menu(leagues)
        elif action == 3:
            self.lineup_menu(leagues)
        elif action == 4:
            self.games()
            input("Press Enter to return to Main Menu ")
            self.main_menu(leagues)

    def league_menu(self, leagues):
        print()
        print("Leagues Menu")
        for i in range(0, len(leagues)):
            print("[" + str(i+1) + "] " + leagues[i].name)
        print("[" + str(len(leagues) + 1) + "] Return to Main Menu")
        action = input("Choose League? ")
        try:
            action = int(action)
        except ValueError:
            self.league_menu(leagues)
            return 1
        if action < 1 or action > len(leagues) + 1:
            self.league_menu(leagues)
            return 1
        elif action == len(leagues) + 1:
            self.main_menu(leagues)
        else:
            self.stats_standings_menu(leagues[action - 1], leagues)

    def stats_standings_menu(self, league, leagues):
        print()
        print(league.name + " Stats/Standings Menu")
        print("[1] League Table")
        print("[2] Leading Scorers")
        print("[3] Top Players")
        print("[4] Return to Main Menu")
        action = input("Choose Option? ")
        try:
            action = int(action)
        except ValueError:
            self.stats_standings_menu(league, leagues)
            return 1
        if action not in [1,2,3,4]:
            self.stats_standings_menu(league, leagues)
            return 1
        elif action == 1:
            print()
            league.leaguetable()
            input("Press Enter to return to Main Menu ")
            self.main_menu(leagues)
        elif action == 2:
            print()
            league.leadingscorers()
            input("Press Enter to return to Main Menu ")
            self.main_menu(leagues)
        elif action == 3:
            print()
            league.top_players()
            input("Press Enter to return to Main Menu ")
            self.main_menu(leagues)
        else:
            self.main_menu(leagues)

    def roster_menu(self, leagues):
        print()
        print(self.name + " Roster Menu")
        print("[1] Sort By Player Rating")
        print("[2] Sort By Position")
        print("[3] Sort By Age")
        print("[4] Return to Main Menu")
        action = input("Choose Option? ")
        try:
            action = int(action)
        except ValueError:
            self.roster_menu(leagues)
            return 1
        if action not in [1,2,3,4]:
            self.roster_menu(leagues)
            return 1
        elif action == 1:
            self.players.sort(key=lambda x: x.overall, reverse=True)
            print()
            self.summary()
        elif action == 2:
            self.players.sort(key=lambda x: x.position, reverse=True)
            print()
            self.summary()
        elif action == 3:
            self.players.sort(key=lambda x: x.age, reverse=True)
            print()
            self.summary()
        self.main_menu(leagues)

    def formation_menu(self, leagues):
        print()
        print("Choose New Formation")
        print("[1] 4-3-3")
        print("[2] 4-4-2")
        print("[3] 4-5-1")
        print("[4] 5-4-1")
        print("[5] 3-5-2")
        print("[6] 5-3-2")
        print("[7] 3-4-3")
        print("[8] Return to Main Menu")
        action = input("Choose Option? ")
        try:
            action = int(action)
        except ValueError:
            self.formation_menu(leagues)
            return 1
        if action not in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.formation_menu(leagues)
            return 1
        elif action == 8:
            self.main_menu(leagues)
        else:
            self.formation = Formations[action-1]
            self.lineup = self.startinglineup()
            self.bench = self.substitutes()
            self.lineup_menu(leagues)

    def depthchart(self, leagues, players, position):
        if position == 'Bench':
            starters = self.bench
        else:
            starters = self.lineup[position]
        if len(players) == len(starters):
            print("Not enough players to make this change")
            self.main_menu(leagues)
        else:
            print()
            print("Player to be Removed")
            for z in range(0, len(starters)):
                print("[" + str(z + 1) + "] " + starters[z].name + " " + starters[z].position + " (O: " + str(starters[z].orating) + " D: " + str(starters[z].drating) + " Fitness: " + str(starters[z].frating) + " Ovr: "+ str(starters[z].overall) + ") ")
            print("[" + str(len(starters) + 1) + "] Return to Main Menu")
            action = input("Choose Player? ")
            try:
                action = int(action)
            except ValueError:
                self.depthchart(leagues, players, position)
                return 1
            if action < 1 or action > len(starters) + 1:
                self.depthchart(leagues, players, position)
                return 1
            elif action == len(starters) + 1:
                self.main_menu(leagues)
            else:
                spot = action - 1
                print()
                print("Player to be Added")
                eligible = list(set(players) - set(starters))
                for z in range(0, len(eligible)):
                    print("[" + str(z + 1) + "] " + eligible[z].name + " " + eligible[z].position + " (O: " + str(eligible[z].orating) + " D: " + str(eligible[z].drating) + " Fitness: " + str(eligible[z].frating) + " Ovr: " + str(eligible[z].overall) + ") ")
                print("[" + str(len(eligible) + 1) + "] Replace a different player")
                action = input("Choose Player? ")
                try:
                    action = int(action)
                except ValueError:
                    self.depthchart(leagues, players, position)
                    return 1
                if action < 1 or action > len(eligible) + 1:
                    self.depthchart(leagues, players, position)
                    return 1
                elif action == len(eligible) + 1:
                    self.depthchart(leagues, players, position)
                else:
                    if position == 'Bench':
                        self.bench[spot] = eligible[action - 1]
                    else:
                        if eligible[action - 1] in self.bench:
                            self.bench[self.bench.index(eligible[action - 1])] = self.lineup[position][spot]
                        self.lineup[position][spot] = eligible[action - 1]
                self.depthchart(leagues, players, position)

    def lineup_menu(self, leagues):
        print()
        print(self.name + " Lineup Menu")
        print("[1] Change Formation")
        print("[2] See Current Lineup")
        print("[3] Auto Sort Lineup")
        print("[4] Change Goalkeeper")
        print("[5] Change Defenders")
        print("[6] Change Midfielders")
        print("[7] Change Forwards")
        print("[8] Change Substitutes")
        print("[9] Return to Main Menu")
        action = input("Choose Option? ")
        try:
            action = int(action)
        except ValueError:
            self.lineup_menu(leagues)
            return 1
        if action not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.lineup_menu(leagues)
            return 1
        elif action == 1:
            self.formation_menu(leagues)
        elif action == 3:
            self.lineup = self.startinglineup()
            self.bench = self.substitutes()
            self.lineup_menu(leagues)
        elif action == 9:
            self.main_menu(leagues)
        elif action == 2:
            self.starters()
            self.lineup_menu(leagues)
        elif action == 4:
            self.depthchart(leagues, self.GK, 'GK')
        elif action == 5:
            self.depthchart(leagues, self.DF, 'DF')
        elif action == 6:
            self.depthchart(leagues, self.MF, 'MF')
        elif action == 7:
            self.depthchart(leagues, self.FW, 'FW')
        elif action == 8:
            self.depthchart(leagues, list(set(self.players) - set(self.lineup['GK']) - set(self.lineup['DF']) - set(self.lineup['MF']) - set(self.lineup['FW'])), 'Bench')


Man_City = Team(3.1, 0.2, 'Manchester City', color.CYAN, 2474)
Liverpool = Team(3, 0.3, 'Liverpool', color.RED, 1944)
Man_U = Team(2.2, 0.7, 'Manchester United', color.RED, 4123)
Arsenal = Team(2.3, 0.7, 'Arsenal', color.RED, 2238)
Tottenham = Team(2.3, 0.5, 'Tottenham', color.BLUE, 1237)
Chelsea = Team(2.4, 0.5, 'Chelsea', color.BLUE, 2062)
Huddersfield_Town = Team(1.4, 1.1, 'Huddersfield Town', color.BLUE, 8)
BH_Albion = Team(1.5, 1, 'Brighton', color.BLUE, 12)
Fulham = Team(1.7, 1.1, 'Fulham', color.RED, 45)
Cardiff = Team(1.6, 1.0, 'Cardiff City', color.BLUE, 29)
Southampton = Team(1.9, 0.9, 'Southhampton', color.RED, 165)
Burnley = Team(1.8, 0.9, 'Burnley', color.YELLOW, 25)
Newcastle = Team(1.7, 0.8, 'Newcastle', color.CYAN, 185)
Bournemouth = Team(2, 1.1, 'Bournemouth', color.RED, 21)
Palace = Team(1.9, 0.8, 'Crystal Palace', color.BLUE, 62)
West_Ham = Team(1.8, 1, 'West Ham', color.BROWN, 634)
Leicester_City = Team(2, 0.7, 'Leicester City', color.BLUE, 413)
Watford = Team(1.9, 1, 'Watford', color.BOLD, 21)
Everton = Team(1.9, 0.6, 'Everton', color.BLUE, 250)
Wolverhampton = Team(1.9, 0.7, 'Wolverhampton', color.ORANGE, 26)
Norwich = Team(1.9, 1.2, 'Norwich City', color.GREEN, 110)
Sheffield = Team(1.6, 0.9, 'Sheffield United', color.RED, 40)
Leeds = Team(1.8, 1, 'Leeds United', color.YELLOW, 180)
Villa = Team(1.7, 1, 'Aston Villa', color.PURPLE, 200)
Wolverhampton.__class__ = PC
Wolverhampton.weeklygames = []


def season(leagues):
    for i in range(0, max([len(x.schedule) for x in leagues])):
        print()
        print("Week " + str(i + 1))
        for q in leagues:
            for z in q.teams:
                z.recovery()
                if isinstance(z, PC) is True:
                    z.dashboard()
                    z.main_menu(leagues)
            print()
            print(q.name + " Scores")
            print()
            if len(q.schedule[i]) > 0:
                for z in q.schedule[i]:
                    game(z[0], z[1])
            else:
                print("No " + q.name + " games this week")
            print()
    for q in leagues:
        q.leadingscorers()
        print()
        q.leaguetable()
        print()
        q.top_players()


Prem = League([Man_City, Man_U, Liverpool, Arsenal, Watford, Everton, Wolverhampton, Tottenham, Leicester_City, West_Ham, Chelsea, Norwich, Palace, BH_Albion, Sheffield, Villa, Southampton, Burnley, Newcastle, Bournemouth], 'Premier League', 0, 3)
season([Prem])