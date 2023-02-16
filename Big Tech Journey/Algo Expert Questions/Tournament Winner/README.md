
Home Team
Away Team

Always one winner and one loser.
Win = 3 Points
Lose = 0 Points
More Points = tournament winner.

Two arrays : matches and results
mathes = [homeTeam,AwayTeam]

results away func:
1 - home team won
0 - away team won.

-> use hashmap to track the points of the teams -> 
 competitions = [
     ['HTML','C#'],
     ['C#','Python'],
     ["Python","HTML"]
 ]
 results = [0,0,1]
 Output = Python

{
python : 6,
C# : 3,
HTML : 0
}

Loop thourgh the competitions array 
competitions[0][i]
if results[i] == 0 map[competitions[0][i][1]] += 1 
if results[i] == 1 map[competitions[0][i][0]] += 1

Me Alone -> Big Fail


# Tim Ruscuca Help : Video Explanation

2 inputs -> competitions and results

competitions array -> all competitions in the tournament, arrays of pairs with string´s 
results array -> same length of the competitions array

the indices correspond
always at least two teams.

algorithm ?
-> keep track of all teams and their points
and after that find the team that have more points

1- initialize an data structure used to map the points -> hashMap 

Scores = {}
"HTML" : 0....

2- Loop through the competitions and see which team won
3- Loop thouugh both arrays at same time. [1nd loop]
4- See which team one with one if statement 0 or 1 in the results array
5- See if the team is already in the map, if not , add the team , if he already are there, just add 3 points.
6- Update the score [If not in the scores data structure , points = 0]

7- After you finalize the check of the results, need to se which team has many points
8- loop through or score datastructure and see which team has the best score [2nd loop]
9- return the team.


-> Optimazation to don´t have two for loops
-> new variable -> keep track the highest score, the team that has the highest score
-> after add the winner into the scores hashmap , compare the score of the team that we add with the current bestTeam.
add an "" : 0 to the scores data structure to avoid mistakes with the comparsing with the variable.
-> keep doing the comparsing and changing bestteam
-> return bestTeam

Time Complexity
O(N) Time N = Number of Competitions
O(K) Space = Number of Teams in the competition. -> [comes fore the scores data structure]
k + 1(empty string)
O(30K + 1) -> O(K)

-> always 30teams max.


# Solution Code


```python
def tournamentWinner(competitions, results):

    HOME_TEAM_WON = 1

    currentBestTeam = ""

    scores = {currentBestTeam: 0}

  

    for index,competition in enumerate(competitions):

        result = results[index]

        homeTeam, awayTeam = competition

        #array[home,away]

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

  

        updateScores(winningTeam,3,scores)

  

        if scores[winningTeam] > scores[currentBestTeam]:

            currentBestTeam = winningTeam

    return currentBestTeam

  
  

def updateScores(team,points,scores):

    if team not in scores:

        scores[team] = 0

  

    scores[team] += points
```
