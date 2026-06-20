# print("""Twinkle, twinkle, little star,
#  How I wonder what you are!
#  Up above the world so high,
#  Like a diamond in the sky.

#  When the blazing sun is gone,
#  When he nothing shines upon,
#  Then you show your little light,
#  Twinkle, twinkle, all the night.

#  Then the traveler in the dark
#  Thanks you for your tiny spark,
#  How could he see where to go,
#  If you did not twinkle so?

#  In the dark blue sky you keep,
#  Often through my curtains peep
#  For you never shut your eye,
#  Till the sun is in the sky.

#  As your bright and tiny spark
#  Lights the traveler in the dark,
#  Though I know not what you are,
#  Twinkle, twinkle, little star.""")
#  import pyttsx3
#  pyttsx3.speak("rupali sejal ki maa hai aur sejal tanker hai")
#  import pyttsx3
#  engine = pyttsx3.init()  object creation

#   RATE
#  rate = engine.getProperty('rate')    getting details of current speaking rate
#  print (rate)                         printing current voice rate
#  engine.setProperty('rate', 125)      setting up new voice rate

#   VOLUME
#  volume = engine.getProperty('volume')    getting to know current volume level (min=0 and max=1)
#  print (volume)                           printing current volume level
#  engine.setProperty('volume',1.0)         setting up volume level  between 0 and 1

#   VOICE
#  voices = engine.getProperty('voices')        getting details of current voice
#  engine.setProperty('voice', voices[0].id)   changing index, changes voices. o for male
#  engine.setProperty('voice', voices[1].id)    changing index, changes voices. 1 for female

#  engine.say("sejal is tanker!")
#  engine.say('My current speaking rate is ' + str(rate))
#  engine.runAndWait()
#  engine.stop()

#   Saving Voice to a file
#   On Linux, make sure that 'espeak-ng' is installed
#  engine.save_to_file('Hello World', 'test.mp3')
#  engine.runAndWait()


#  import os

#  file_path = os.path.abspath(__file__)

#  with open(file_path, "r", encoding="utf-8") as file:
#      for line in file:
#          if "" in line:
#              comment = line[line.index(""):].strip()
#              print(comment)
#  a=7-4
#  b=5
#  b/=3
#  c=a+b
#  print(c)
#  d=4>6
#  print(d)
#  variable=None
#  print(type(variable))
#  a="45"
#  b=int(a)
#  print(type(b))
#  print(type(b))
#  a=23
#  b=7
#  print(a%b)
#  a=34
#  b=80
#  if(a>b):
#      print("True")
#  elif(a<b):
#      print("False")
#  print("hello world")
#  a=6
#  b=a**2
#  print(b)
#  "string"
#  name="vanshisgodnodoubtandgodnodoubt"
#  print(name[1:20:6])

#  name="vanshisgodnodoubtandgodnod"
#  print(name.replace("is","are"))
#  a="vansh is a good boy \nbut not a right \"boy\""
#  print(a)
#  name=input("enter user name:",)
#  print(f"good afternoon,{name}")
#  letter="""Dear <|name|>,
#  you are selected!
#  <|date|>"""

#  print(letter.replace("<|name|>","vansh").replace("<|date|>","15 june 2069"))

#  name="vansh is a  good  boy"
#  print(name.replace("  "," "))
#  friends=["rohan","rachin",8,175.66,"orange"]
#  friends[1]="grapes"
#  print(friends)
#  list=["rohan","rachin",8,175.66,"orange"]
#  real=list.append("real world")
#  print(list)
#  tup=(1,2,3,4,5,6,7)
#  fruit=[]
#  f1=input("enter fruit name:")
#  fruit.append(f1)
#  f2=input("enter fruit name:")
#  fruit.append(f2)
#  f3=input("enter fruit name:")
#  fruit.append(f3)
#  f4=input("enter fruit name:")
#  fruit.append(f4)
#  f5=input("enter fruit name:")
#  fruit.append(f5)
#  f6=input("enter fruit name:")
#  fruit.append(f6)
#  print(fruit)
# dict={
#     "name":"vansh",
#     "marks":90,
#     "cgpa":9
# }

#  print(dict,type(dict))
#  print(dict["name"])
#  print(dict.items())
#  print(dict.keys())
#  print(dict.keys())
#  print(dict.values())
#  dict.update({"name":"king"})
#  print(dict)

#  e=set()
#  s={1,2,3,4}
#  s.union({8,12})
#  print(s)
#  s1={1,2,3,4,5}
#  s2={6,7,8,9}
#  print(s1.union(s2))
#  print(s1.intersection(s2))
#  words={
#      "madad":"help",
#      "kya":"what",
#      "morning":"subah"

#  }
#  word=input("enter the word you want the meaning of:",)
#  print(words[word])
#  s=set()
#  n=int(input("enter number 1:",))
#  s.add(n)
#  n=int(input("enter number 2:",))
#  s.add(n)
#  n=int(input("enter number 3:",))
#  s.add(n)
#  n=int(input("enter number 4:",))
#  s.add(n)
#  n=int(input("enter number 5:",))
#  s.add(n)
#  n=int(input("enter number 6:",))
#  s.add(n)
#  n=int(input("enter number 7:",))
#  s.add(n)
#  n=int(input("enter number 8:",))
#  s.add(n)

#  print(s)
#  s=set()
#  s.add(18)
#  s.add("18")
#  print(s)
#  d={}
#  name=input("enter person name:",)
#  lang=input("enter person language",)
#  d.update({name:lang})

#  name=input("enter person name:",)
#  lang=input("enter person language",)
#  d.update({name:lang})

#  name=input("enter person name:",)
#  lang=input("enter person language",)
#  d.update({name:lang})

#  name=input("enter person name:",)
#  lang=input("enter person language",)
#  d.update({name:lang})
#  print(d)\
# age=int(input("enter you age:",))
# if(age>18):
#     print("you can drive")
# elif(age<0):
#     print("are you serious bakchod hai kya")
# else:
#     print("you can not drive")
# a1=int(input("enter number 1:",))
# a2=int(input("enter number 2:",))
# a3=int(input("enter number 3:",))

# if(a1>a2 and a1>a3):
#     print("greatest number is :", a1)
# elif(a2>a1 and a2>a3):
#      print("greatest number is :", a2)
# elif(a3>a1 and a3>a2):
#      print("greatest number is :", a3)
# marks1=int(input("enter 1st sub mark:",))
# marks2=int(input("enter 2nd sub mark:",))
# marks3=int(input("enter 3rd sub mark:",))


# total_percentage=((marks1+marks2+marks3)*100)/300
# print(total_percentage)

# marks1=int(input("enter 1st sub mark:",))
# marks2=int(input("enter 2nd sub mark:",))
# marks3=int(input("enter 3rd sub mark:",))


# total_percentage=(100)*(marks1+marks2+marks3)/300


# if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
#     print("you are pass!",total_percentage)

# else:
#     print("you are fail!",total_percentage)


# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message=input('enter your comment:',)

# if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this comment is a spam")

# else:
#     print("this comment is not a spam")

    
# l=["sejal","shreya","tanker","fridge","bulldozer"]

# name=input("enter your name:",)

# if (name in l):
#     print("your name is in list")

# else:
#     print("your name is not in list")




# post="hey harry is good Harry is very great guy"
# if("harry" in post):
#     print("this fucker is talkin about harry")

# i=0

# while(i<=100):
#     print("vansh")
#     i+=1
# l=[1,"vansh",False,"shubhi","rohan",18,"topper"]
# i=0

# while(i<len(l)):
#     print(l(i))
#     i+=1

# for i in range(4,44,4):
#     print(i)

# l=[,1,2,3,4,5,6,"vansh"]
# for i in l:
#     print(i)
# s="vansh"

# for i in s:
#     print(i)

# s="vansh"

# for i in s:
#     print(i)

# else:
#     print("successfully executed")

# for i in range(100):
    
#     if(i==77):
#         break
#     print(i)

# for i in range(100):
   
#     if(i==3):
#         continue
    
#     print(i)


# for i in range(88):
#     pass
    
# n=int(input("enter number:",))


# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
# l=["raman","sahil","shibum","harish"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"hello {name}")
# n=int(input("enter number:",))
# i=1


# while(i<11):
#     print(f"{n}x{i}={n*i}")
#     i+=1
# n=int(input("enter number:",))

# for i in range(2,n):
#     if(n%i)==0:
#         print("number is not prime")
#         break
#     else:
#         print("this is a prime number")
# 
# n=int(input("enter number:",))

# product=1

# for i in range(1, n+1):
#     product=product*i
# print(f"the factorial of {n} is {product}")

n=int(input("enter your number:",))

for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")