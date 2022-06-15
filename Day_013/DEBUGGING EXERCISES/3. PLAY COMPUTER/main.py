# # Play Computer - Solution 

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:  # here the year 1994 is included in this condition, hence debugged!!
  print("You are a Gen Z.")
