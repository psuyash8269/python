import random
player=[0,0]
print("***********\nGame begin\n**********")
pl_1=input("Enter first playe name")
pl_2=input("Enter second player name")
i=0
while (player[0]!=50 or player[1]!=50):
    i+=1
    if i==1:
      print("\t\t\t\t" + pl_1 + "!!!!!!!!!!!!!!! ")
    else:
      print("\t\t\t\t" + pl_2 + "!!!!!!!!!!!!!!! ")
    a=int(input("\t\t\t\tplz enter 1 for spin the dice : "))
    if a==1:
        dice_value=random.randint(1,6)
        print(f"\t\t\t\t\t\t\t\tyour dice value {dice_value}")
        k=player[i]
        player[i]+=dice_value
        if player[i]>50:
          player[i]=k
        if player[i]==50:
            if i==1:
              print("\t\t\t\t\t\t\t\tyou gone",player[i],"congrtulation !!!!!" + pl_1 + "You win the match")
            else:
              print("\t\t\t\t\t\t\t\tyou gone",player[i],"congrtulation !!!!! " + pl_2 + "You win the match")
            break         
    if(player[i]==6 or player[i]==11 or player[i]==17 or player[i]==18 or player[i]==27 or player[i]==37):
        print("\n\n\t\t\t\t\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!\n\t\t\t\t\t\t\t\tyou are lucky you get ladder and up**********************")
        if player[i]==6:
            player[i]=14
        if player[i]==11:
            player[i]=29
        if player[i]==17:
            player[i]=36
        if player[i]==18:
            player[i]=39
        if player[i]==27:
            player[i]=33
        if player[i]==37:
            player[i]=43
    if(player[i]==16 or player[i]==22 or player[i]==34 or player[i]==47):
        print("\n\n\t\t\t\t\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!\n\t\t\t\t\t\t\t\tyou have badluck you get snak and down^^^^^^^^$$$$$")
        if player[i]==16:
            player[i]=3
        if player[i]==22:
            player[i]=20
        if player[i]==34:
            player[i]=26
        if player[i]==47:
            player[i]=36
    if i==1:
      print("\t\t\t\t\t\t\t\tplayer"+ pl_1 +"you gone  ",player[i])
    else:
      print("\t\t\t\t\t\t\t\tplayer"+ pl_1 +"you gone  ",player[i])
    i=(i+1)%2
