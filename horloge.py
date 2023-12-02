# "afficher_heure"  / fonction "afficher l'heure" /paramètre : tuple (heures,minutes, secondes) + mise à jour

import time    #galery time

# print(time.localtime())  #galery time.fonction local time

# Step 1: printer l'heure

hour = time.localtime().tm_hour
# print(hour)                              #print =fonction 

# Step 2: printer les minutes
min = time.localtime().tm_min
# print(min)                              #print =fonction 

# Step 3: printer les secondes
sec = time.localtime().tm_sec
# print(sec)                              #print =fonction 

# print(str(hour) + ":"+ str(min) + ":" + str(sec))

    


#fonction: def: nom de la fonction():



# def afficher_heure():
#     hour = time.localtime().tm_hour
#     min = time.localtime().tm_min
#     sec = time.localtime().tm_sec
#     print(str(hour) + ":"+ str(min) + ":" + str(sec))

# afficher_heure()


# Afficher l'heure avec le package `datetime`

import datetime

# print(datetime.datetime.now())

current_time = datetime.datetime.now()                #Assigner _ Variable

# print(str(current_time).split())

my_temp_list = str(current_time).split()
current_time = my_temp_list[1]

# print(current_time)


my_temp_list = current_time.split(".")
current_time = my_temp_list[0]

# print(current_time)


#Votre programme doit actualiser l’heure toutes les secondes jusqu'à l’arrêt de ce dernier.

def afficher_heure():
    
    while True:
        current_time = datetime.datetime.now() 
        my_temp_list = str(current_time).split()
        current_time = my_temp_list[1]
        my_temp_list = current_time.split(".")
        current_time = my_temp_list[0]
        print(current_time)
        time.sleep(1)






afficher_heure()






