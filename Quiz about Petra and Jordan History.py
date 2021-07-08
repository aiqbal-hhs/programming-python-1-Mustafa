#Creat a vairable and name it score and set it to zero
score = 0
print("Hello, I made a quick history quiz about Petra/Jordan. The quiz consists of ten questions. \n There is different choices for the answers choose the one that you think is correct like if you think the answer (a) is correct then type (a)\n Best of luck!")
#Creat a vairble and put this question "What is Petra?" and put some different answers 
what_is_petra = input("1. What is Petra? \n A. Building \n B. City \n C. Village \n D. Kingdom \n")
what_is_petra = what_is_petra.lower()
if what_is_petra == "b":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'b' Petra is a big City that is surounded by mountains")

#Creat a vairble and put this question "When was Petra Built??" and put some different answers 
built_date = input("2. When was Petra built? \n A. 5th century BC \n B. 7th century BC \n C. 4th century BC \n D. 2th century BC \n")
built_date = built_date.lower()
if built_date == "a":
    print("Correct!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'a' \n Petra Was built in early 5th century")

#Creat a vairble and put this question "Who built this City?" and put some different answers 
who_built_it = input("3. Who built this city? \n A. Nabataean Kingdom \n B. Pharaon Ramesses 2 \n C. Unknown travellers \n D. Indian people \n")
who_built_it = who_built_it.lower()
if who_built_it == "a":
    print("Excellent!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'a' \n The spectacular sandstone city of Petra was built in the 5th century BC by the Nabataeans, who carved palaces, temples, tombs, storerooms and stables from the soft stone cliffs.")

#Creat a vairble and put this question "Where is Petra Located?" and put some different answers 
where_is_it_located = input("4. Where is Petra located? \n A. Petra \n B. Egypt  \n C. Iraq \n D. Jordan \n")
where_is_it_located = where_is_it_located.lower()
if where_is_it_located == "d":
    print("Bravo!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'd' \n Petra is located in the southern of Jordan")

#Creat a vairble and put this question "What is the capital of Jordan?" and put some different answers including the correct answer 
capital = input("5. What is the capital of Jordan? \n A. Petra \n B. Irbid  \n C. Amman \n D. Hebron \n")
capital = capital.lower()
if capital == "c":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'c' \n The capital of Jordan is Amman")

#Creat a vairble and put this question "What is the official language?" and put some different answers icluding the correct answer
official_language = input("6. What is the official language of Jordan? \n A. English \n B. Arabic  \n C. Italian \n D. Kurdish \n")
official_language = official_language.lower()
if official_language == "b":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'b' The official language of Jordan is Arabic")
    
#Creat a vairble and put this question "When did Jordan become independent?" and put some different answers including the correct answer.
independent_year = input("7. When did Jordan become independent? \n A. 1822 \n B. 1946  \n C. 1948 \n D. 1956 \n")
independent_year = independent_year.lower()
if independent_year == "c":
    print("Well done!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'c' Jordan became independent in 1948")

#Creat a vairble and put this question "When did the battle of Karameh take place? when the forces of the Zionist entity attempted to occupy the Jordan River." and put some different answers including the correct answer.
battle_of_karameh = input("8. When did the battle of Karameh take place? when the forces of the Zionist entity attempted to occupy the Jordan River. \n A. March 21, 1968 \n B.December 10, 1956 \n")
battle_of_karameh = battle_of_karameh.lower()
if battle_of_karameh == "a":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'a' \n The battle of Karameh took place in March 21, 1968")


#Creat a vairble and put this question "Which country is to the north of Jordan?" and put some different answers including the correct answer.
north_of_Jordan = input("9. Which country is to the north of Jordan? \n A. Egypt \n B. Syria  \n C. Yemen \n D. Sudan \n")
north_of_Jordan = north_of_Jordan.lower()
if north_of_Jordan == "b":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'b' \n Syria is to the north of Jordan")

#Creat a vairble and put this question "Who was Jordan’s first king?" and put some different answers including the correct answer.    
first_king = input("10. Who was Jordan’s first king? \n A. Faisal \n B. Abdullah I \n C. Fahd \n D. Hussein \n")
first_king = first_king.lower()
if first_king == "b":
    print("Good Job!")
    score +=1
else:
    print("Incorrect answer,\n the correct answer is 'b' The first king of Jordan was Abdullah I")
#print score
if score >=5 <=7:
  print ("Not bad your scored {}/10".format(score))
elif score >=9:
    print("Well done! Your scored  {}/10".format(score))
else:
    print("Unlucky, try harder next time. Your scored {}/10".format(score))





