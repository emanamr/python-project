
import random
#nested list to film =[[list to age<16],[age>16]]
film_list = [["Toy story","Nemo","Frozen","Tangled","How to train your dragon"],
             ["Harry Potter and the Sorcerer’s Stone","The Lord of the Rings",
              "Harry Potter and the Goblet of Fire","Adopt a Highway","Red Spring"]]
#gift list=[[age<16[list to female],[list to male]],[age>16[female],[male]]]
gift_list =[[["Doll","Dress","Necklace","Teddy bear"],["video games","football","Bicycle"]],
            [["Jewelery","Purse","Perfume"],["Perfume","Washed away","Wristwatch"]]]

#restaurant list=[[list<16],[list>16]]
resturant_list =[["kentucky","hardezz","pizza hut","Macdonalze","prego"],["crave","Roastery","Hosny","Akla baity"]]


age = input("How old are you?")

if age<0:
    print "The age not be negative, please try again"
    age = input("How old are you?")

    
gender = input("What is your gender? Enter 'F' for female and 'M' for male")

if (gender!='F'and gender!='f') and (gender!='M'and gender!='m'):
    print "Please enter 'F' for female and 'M' for male"
    gender=input("What is your gender? Enter 'F' for female and 'M' for male")

    
recomend = input("What would me to recomend? a'gift' ,'resturant' or 'film'")

if recomend!='gift' and recomend!='resturant' and recomend!='film':
    print "please enter a'gift' ,'resturant' or 'film'"
    recomend = input("What would me to recomend? a'gift' ,'resturant' or 'film'")

if age<16:
    if recomend =='gift':
        
        if gender=='F' or gender=='f':
            print(random.choice(gift_list[0][0]))
        else:
            print(random.choice(gift_list[0][1]))

    elif recomend =='film':
        print(random.choice(film_list[0]))

    else:
        print(random.choice(resturant_list[0]))

elif age>16:
    if recomend =='gift':
        if gender=='F'or gender=='f':
            print(random.choice(gift_list[1][0]))
        else:
            print(random.choice(gift_list[1][1]))
        
    elif recomend =='film':
        print(random.choice(film_list[1]))

    else:
        print(random.choice(resturant_list[1]))

add_recomend=input("Would you like to add recomendations? enter 'y' for (yes)and 'N' for(No)")
if add_recomend!='n' and add_recomend!='N' and add_recomend!='y' and add_recomend!='Y':
    print("please enter either y or n")
    add_recomend=input("Would you like to add recomendations? enter 'y' for (yes)and 'N' for(No)")

if add_recomend=='n' or add_recomend=='N':
    print("thank you for using my programm")

if add_recomend=='y' or add_recomend=='Y':
    again1=raw_input("For what age? if you don't want to specify just click on enter")
    if len(again1)== 0:
        again2=raw_input("For what gender? if you don't want to specify just click on enter")
        if len(again2)==0:
            recomend=input("What type of recomendation is it?")
            new_recomend=input("please enter your recomendation")
        else:
            gender=again2
            recomend=input("What type of recomendation is it?")
            new_recomend=input("please enter your recomendation")        
    else:
        age=again1
        again2=raw_input("For what gender? if you don't want to specify just click on enter")
        if len(again2)==0:
            recomend=input("What type of recomendation is it?")
            new_recomend=input("please enter your recomendation")
        else:
            gender=again2
            recomend=input("What type of recomendation is it?")
            new_recomend=input("please enter your recomendation")
        
if age<16:
    if recomend =='gift':
        
        if gender=='F' or gender=='f':
            (gift_list[0][0]).append(new_recomend)
        else:
            (gift_list[0][1]).append(new_recomend)

    elif recomend =='film':
        (film_list[0]).append(new_recomend)

    else:
        (resturant_list[0]).append(new_recomend)

elif age>16:
    if recomend =='gift':
        if gender=='F'or gender=='f':
            (gift_list[1][0]).append(new_recomend)
        else:
            (gift_list[1][1]).append(new_recomend)
        
    elif recomend =='film':
        (film_list[1]).append(new_recomend)

    else:
        (resturant_list[1]).append(new_recomend)

print("Thank you for your recomendation...")        
        
        

