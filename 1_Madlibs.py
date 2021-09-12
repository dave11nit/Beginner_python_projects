# this is a python project
# sep 12 
# freecodecamp from kylie yang
# number 1 fro 12 project series

''' project description
in this project we are going to use string concatanation
where we will give a paragraph and the user will give a word 
then we will fill the word in all the black spaces in the paragraph 
'''
icon = input()
team1 = input()
team2 = input()
shirt_number = int(input())
revenue = input()

madlib = f"{icon} has recently returned to Manchester United. After 12 years of playing for {team1} and 3 years in {team2} \
he has returned to where he belongs. He is wearing his famous number {shirt_number} jersey and fans have gone beserk for buying that \
shirt. This has brought {revenue} million dollor of revenue for manchester united."

print(madlib)