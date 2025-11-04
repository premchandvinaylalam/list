#marks = 30
#if (marks>33):
#    print("Failed")
#elif (marks>33 and marks<50):
#    print("appear for re-exam")
#elif (marks>50 and marks<90):
#    print("pass")
#elif (marks>=90):
#    print("A+ grade and top ranker")


marks = int(input("enter the marks"))

if marks < 33:
    print("Failed")
elif marks >= 33 and marks < 50:
    print("Appear for re-exam")
elif marks >= 50 and marks < 90:
    print("Pass")
elif marks >= 90:
    print("A+ grade and top ranker")



#if only one if stmt is there and condition was wrong it will print anything and won't give any error
#ex: marks = 30
#        if marks < 30:
#            print("Failed")
#       print("code completed")  ---> it will directly come to this line bcuz condition is not vaild, if vaild it will print both



#SLICING AND LENGTH OF STRING
name = "PremChandVinay"
print(len(name))

#slicing -- string characters are stored in form of index starting from 0 and n [0-n]
#forward   0  1  2  3  4  5  6
#          a  n  i  m  a  l  s
#backwards-7 -6 -5 -4 -3 -2 -1

print(name[0:2]) #it will print first two chars
print(name[-1]) # print last character
print(name[0:]) #print from starting char and remaining




