# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

four = year % 4

hundred = year % 100

fourHundred = year % 400

if four == 0:
  print("Leap year.")
  if hundred == 0:
    print("Leap year")
    if fourHundred == 0:
      print("Leap year")
    else:
      print("Not a Leap year")
  else:
    print("Not a Leap year")
else:
  print("Not a Leap year")


