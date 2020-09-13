from random import choices
ntrials=15000
player1wins=0
for i in range(ntrials):
    total1 = 0
    total2 = 0
    playerdice2=choices(range(1,7) , k=2)
    if playerdice2[0]== playerdice2[1]:
        continue
    total2 = total2 + playerdice2[0] + playerdice2[1]

    player1dice=choices(range(1,7) , k=3)
    player1dice.sort(reverse=True)
    count = player1dice.count(2)
    if count >= 2:
        continue
    total1 = total1 + player1dice[0] + player1dice[1]

    if total1 > total2 :
        player1wins = player1wins+1
print("Ratio =",player1wins/ntrials)

#The ratio should become smaller since the ratio is closer to 50%.