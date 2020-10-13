#range inputs
start = 1
end = int(input("Enter a Number Here: "))
#defs
num_list = range(start, end + 1)
finalsum = sum(num_list)

print("Final Sum of Range = ", finalsum)


#Exes
#You have 5 exes. One night you are feeling lonely and decide to call one of them. Please choose an ex 1-5 to call tonight.

#Ex List
# = Jennifer 2 = Emily 3 = Jessica 4 = Stacy 5 = Sophia


def call_my_ex(name):
    if name == 1:
       print("Calling Jennifer now.")
    elif name == 2:
       print("Calling Emily now.")
    elif name == 3:
        print("Calling Jessica now.")
    elif name == 4:
        print("Calling Stacy's Mom instead becasue she has it going on.")
    elif name == 5:
        print("Calling Sophia now.")
    else:
        print("Ok stay lonely then, I don't care.")


name = int(input("Who would you like to call:"))
  

call_my_ex(name)

