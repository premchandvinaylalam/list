#printing in diff ways
#when we give print it will default go's to new line, To avoid this use end in print operator
print("Prem")
print ("sing","dance","cricket")
print(5,end='-')
print(6,end='-')
print(7)

#input function
movie = input("Please enter the movie name")
print("I also love the movie", movie)

#variables
#variable is used as container to store some data in it
#We can't add two diff variable type
#variable name should contain any spaces(ex: user name --- it should be username or user_name)
name = "prem"
age = 26
company = "infosys"
print("name:", name)
print("age:", age)
print("current company:" ,company)
#print(name+age) --  we can't add two diff datatype variables
print(name+str(age)) #changing int to str
#we can overwrite the variable values

name = "prem"
age = 26
random_number = 3
print("name", name)
print(age+random_number)
print(name+str(age))


name = input("enter your name")
age = int(input("enter your age"))
random_number = int(input("enter any number"))
print("name:",name)
print(age+random_number)