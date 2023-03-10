print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
total_name = lower_name1 + lower_name2
t_word = total_name.count('t')
r_word = total_name.count('r')
u_word = total_name.count('u')
e_word = total_name.count('e')
l_word = total_name.count('l')
o_word = total_name.count('o')
v_word = total_name.count('v')
lower_name1 = str(t_word + r_word + u_word + e_word)
lower_name2 = str(l_word + o_word + v_word + e_word)
total_name = int(lower_name1 + lower_name2)

if total_name < 10 or total_name > 90:
  print(f"Your score is {total_name}, you go together like coke and mentos.")
elif total_name >= 40 and total_name <= 50:
  print(f"Your score is {total_name}, you are alright together.")
else:
  print(f"Your score is {total_name}.")