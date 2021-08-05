def tournamentWinner(competitions, results):
    # Write your code here.

    competition_count = 0
    teams = {}

    for competitors in competitions:

        home_team, away_team = competitors
        if not home_team in teams:
            teams[home_team] = 0

        if not away_team in teams:
            teams[away_team] = 0

        if results[competition_count] == 1:
            teams[home_team] += 3
        else:
            teams[away_team] += 3
        competition_count += 1

    return max(teams,key=lambda k: teams[k])

def main():
    competitions= [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournamentWinner(competitions,results))

main()