#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Quiz Game
def check_guess(guess, answer):              
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Answer is incorrect,please try again :")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is :",answer )
    
score = 0
print("Guess the Answer")
guess1 = input("1. Who created Python? ")
check_guess(guess1, "Guido Van Rossum")
guess2 = input("2. When was Python created? ")
check_guess(guess2, "1991")
guess3 = input("3. What is the old name of Python? ")
check_guess(guess3, "ABC")
guess4=input("4. In Python strings are mutable? ")
check_guess(guess4, "No")
guess5=input("5. What is the extension of Python file? ")
check_guess(guess5, ".py")
guess6=input("6. Are dictionaries in python have unique key values? ")
check_guess(guess6, "yes")
guess7=input("7. Lists are mutable or not? ")
check_guess(guess7, "mutable")
guess8=input("8. In which language is Python written? ")
check_guess(guess8, "C")
guess9=input("9. Are nested if-else are allowed in python? ")
check_guess(guess9, "No")
guess10=input("10. What is the output of 19%2 in python? ")
check_guess(guess10, "1")
guess11=input("11. what is the sign of floor division? ")
check_guess(guess11, "//")
guess12=input("12. In Python Pass is a null statement? ")
check_guess(guess12, "Yes")
guess13=input("13. Which statement is used to create an empty set in Python? ")
check_guess(guess13, "set()")
guess14=input("14. What is the output of 5**2: ")
check_guess(guess14, "25")
guess15=input("15. The % operator returns the ........")
check_guess(guess15, "remainder")
print("Your Score is "+ str(score))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




