questions = [
  [
    "What is the capital of Australia?", " Sydney"," Melbourne" ,"Canberra "," Brisbane",3
  ],
  [
    "what is the smallest planet in our solar system ?","mercury","venus","earth ","mars",1
  ],
  [
    "what is the largest ocean on the earth?","atlantic ocean ","indian ocean ","pacific ocean ","arctic ocean ",3
  ],
  [ 
      "What is the largest country in the world by land area?","russia ","china ","canada","unites states",1
      ],
      
    [
        "What is the largest mammal in the world?","african elephant ","blue whale","hippopotamus","giraffe",2
        
        ]      
] #list ke ander list me traverse by fstring / indexing / last index pe answer [-1] . 
 
print("WELCOME TO QUIZ \n ")
x=0 #initialise count 
for i in range(0, len(questions)):
  
  question = questions[i]
  
  print(f"{question[0]} ")
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  user = int(input("Enter your answer or  0 to quit:\n" ))
  if(user==0):
      print("thank you for playing  ")
      print("you give correct answer of qustions",x)
      break
  if(user == question[-1]):
    print("Correct answer" )
    x +=1#im trying to count repeatation on correct answer 
  else:
    print("Wrong answer!")
    print("you give correct answer of",x,"questions")
    print("try next time ")
    break 
  
if(x==len(questions)):#final question complete hone ke baad isko print 
      print("YOU WON THE QUIZ , THANKS FOR PLAYING")
