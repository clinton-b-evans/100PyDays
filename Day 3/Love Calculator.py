# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
both_name = lower_case_name1 + " " + lower_case_name2

true_count = 0
love_count = 0

for char in "true":
    true_count += both_name.count(char)

for char in "love":
    love_count += both_name.count(char)
    
total_score = str(true_count) + str(love_count)
total_score = int(total_score)
if total_score < 0 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
