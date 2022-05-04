                                                TREASURE MAP
  
  Instructions
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
This is to try and simulate the coordinates on a real map.



Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

23
Example Output 1
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
Example Input 2
column 3, row 1 would be entered as:

31
Example Output 2
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd

Hint
Remember that Lists start at index 0!
map is just a variable that contains a nested list. It's not related to the map function in Python.

              *******************************************************************************************
  
  Solution: 
    
 # 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal =  int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = 'X'

print(f"{row1}\n, {row2} \n, {row3}")



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
