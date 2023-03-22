year = int(input("Which year do you want to check? "))

# year_4_divide = year / 4
# year_100_divide = year / 100
# year_400_divide = year / 400

# if (year_4_divide % 2 == 0): #leap
#   if(year_100_divide % 2 == 0): #not leap
#     if(year_400_divide % 2 == 0): #leap
#       print(f'the year {year} is a leap year')
#     else: #year_400_divide not leap
#       print(f'the year {year} is not a leap year')
#   else: #year_100_divide not leap
#     print(f'the year {year} is a leap year')
# else: #year_4_divide not leap
#   print(f'the year {year} is not a leap year')

#   or

if (year % 4 == 0): #leap
  if(year % 100 == 0): #not leap
    if(year % 400 == 0): #leap
      print(f'the year {year} is a leap year')
    else: #year_400_divide not leap
      print(f'the year {year} is not a leap year')
  else: #year_100_divide not leap
    print(f'the year {year} is a leap year')
else: #year_4_divide not leap
  print(f'the year {year} is not a leap year')  