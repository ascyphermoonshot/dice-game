print('you will bet on whether a simulated dice throw sum is even or odd. The use of cryptographically secure random number generator eliminates the need for a dealer')
from secrets import choice
numpla=int(input('enter the number of players: '))
bets=[]
names=[]
dicesides=[1,2,3,4,5,6]
for x in list(range(0,numpla)):
    names.append(input('what is your name? '))
    bets.append(input('make your bet '))
dice1=choice(dicesides)
dice2=choice(dicesides)
throw=tuple((dice1,dice2))
tsum=sum(throw)
if tsum%2==0:
    betres='even'
else:
    betres='odd'
winum=[i for i, x in enumerate(bets) if x==betres]
winners=[]
print(throw)
for y in winum:
    winners.append(names[y])
print('{} won, the rest have to pay'.format(winners))