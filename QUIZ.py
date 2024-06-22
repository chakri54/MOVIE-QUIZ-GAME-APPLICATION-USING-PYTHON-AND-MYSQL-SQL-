import random
print('*'*26)
print('*'*10,"QUIZ",'*'*10)
print('*'*26)

Name=input("enter Your Name :").upper()


q1='''1. Who directed the film "Pushpa: The Rise," starring Allu Arjun?
   a) Trivikram Srinivas
   b) Sukumar
   c) Koratala Siva
   d) Vamsi Paidipally
   '''

q2='''2. Which actress played the role of "Sravani" in the film "Love Story" alongside Naga Chaitanya?
   a) Rashmika Mandanna
   b) Sai Pallavi
   c) Pooja Hegde
   d) Keerthy Suresh
   '''

q3 = '''3. Who composed the music for the film "RRR," directed by S.S. Rajamouli?
   a) Thaman S
   b) Devi Sri Prasad
   c) Amit Trivedi
   d) M.M. Keeravani
   '''

q4 = '''4. In which film did Vijay Deverakonda portray the role of a fighter pilot named "Anand"?
   a) Liger
   b) World Famous Lover
   c) Dear Comrade
   d) Geetha Govindam
   '''

q5 = '''5. Who among the following directed the film "Jathi Ratnalu" starring Naveen Polishetty?
   a) Nag Ashwin
   b) Anudeep KV
   c) Sandeep Reddy Vanga
   d) Venky Kudumula
   '''

q6 = '''6. Which actor won the National Film Award for Best Actor for his performance in the film "Jersey"?
   a) Nani
   b) Vijay Deverakonda
   c) Naga Chaitanya
   d) Sharwanand
   '''

q7 = '''7. Who composed the music for the film "Acharya," starring Chiranjeevi and Kajal Aggarwal?
   a) Thaman S
   b) Devi Sri Prasad
   c) Mani Sharma
   d) Anirudh Ravichander
   '''

q8 = '''8. Which actress won the Filmfare Award for Best Actress (Telugu) for her role in the film "Uppena"?
   a) Krithi Shetty
   b) Rashmika Mandanna
   c) Sai Pallavi
   d) Pooja Hegde
   '''

q9 = '''9. Who among the following actors starred in the film "Vakeel Saab," a remake of the Hindi film "Pink"?
   a) Allu Arjun
   b) Ram Charan
   c) Pawan Kalyan
   d) Prabhas
   '''

q10 = '''10. Who directed the film "Wild Dog," starring Nagarjuna in the lead role?
    a) Vamsi Paidipally
    b) Ahishor Solomon
    c) Sudheer Varma
    d) Gopichand Malineni
    '''

q11 = '''11. In which film did Rashmika Mandanna make her debut in Telugu cinema?
    a) Chalo
    b) Geetha Govindam
    c) Dear Comrade
    d) Sarileru Neekevvaru
    '''

q12 = '''12. Who composed the music for the film "Most Eligible Bachelor," starring Akhil Akkineni and Pooja Hegde?
    a) Thaman S
    b) Devi Sri Prasad
    c) Gopi Sundar
    d) Anirudh Ravichander
    '''

q13 = '''13. Which Telugu film won the National Film Award for Best Feature Film in 2022?
    a) Rang De
    b) Jathi Ratnalu
    c) Shyam Singha Roy
    d) Bheemla Nayak
    '''

q14 = '''14. Who directed the film "Love Story," starring Naga Chaitanya and Sai Pallavi?
    a) Sekhar Kammula
    b) Mohan Krishna Indraganti
    c) Trivikram Srinivas
    d) Kishore Tirumala
    '''

q15 = '''15. Which actress won the Filmfare Award for Best Actress (Telugu) for her role in the film "Rang De"?
    a) Keerthy Suresh
    b) Rashmika Mandanna
    c) Sai Pallavi
    d) Nithya Menen
    '''


questions = {q1: 'b', q2: 'a', q3: 'd', q4: 'c', q5: 'd', q6: 'a', q7: 'b', q8: 'a', q9: 'c', q10: 'b', q11: 'a', q12: 'a', q13: 'c', q14: 'a', q15: 'b'}
score=0
qno=1
score_report={}
report={}
for q in questions:
   print(q)
   ch= input("choose the option :")
   if ch == questions[q]:
      print("Correct ")
      score=score+1
      score_report[qno]=1
      report[qno]='Correct'
   else:
      print("Incorrect")
      score=score-0.5
      score_report[qno]=0.5
      report[qno]="Incorrect"
   qno=qno+1 # to increment ques in report
print()
print()
print()
wrong_count=0
correct_count=0
# for iterating report and score data 
for i in report.keys():
   print(i,' '*20,":"*5, report[i],":"*5,' '*20,score_report[i])
   if report[i]== "Incorrect":
      wrong_count+=1
   elif report[i]== "Correct":
      correct_count+=1
print()
print()
print(f"TOTAL CORRECT : {correct_count}   TOTAL INCORRECT : {wrong_count}")
print("Total Points :",score)
print()   
if score==15:
   print("You Rocked it ")
   print(f"{Name} You won CASH Price: ",score*100)
   gift_items = ["smart Watch","Power Bank","Headset","additional Cash Back"]
   # Randomly choose 3 gifts from the list
   gift = random.choice(gift_items)
   #print(gift)
   
   if gift == gift_items[3]:
      print("You Have Received Additional Cash Back of ₹ : ",1000)
      print(f"{Name} Total Amount You Won :",score*100 + 1000)
   elif gift == gift_items[2]:
      print(f"Congrats Dude {Name} Additionally You Won Headset Worth ₹1000")
   elif gift == gift_items[1]:
      print(f"Congats Dude {Name}  Additionally You Won Power Bank ₹ 500")
   elif gift == gift_items[0]:
      print(f"Congrats Dude {Name} Additionally You Won Smart Watch ₹ 2000")
      
elif score>10 and score<15:
   print("Thats Great!")
   print()
   print(f"{Name} You won CASH Price: ",score*50)
elif score>7 and score<10:
   print(f"Thats Good! {Name}")
   print()
elif score<7:
   print(f"{Name} Best Of Luck for the Next time :")
   print()
   


      
      



  
    
        
