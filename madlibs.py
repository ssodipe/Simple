#Simple Madlibs with Python string concactenation
#Author: Solomon Sodipe



adj = input("Adjective: ")
noun1 = input("Noun: ")
pverb = input("Past tense verb: ")
adj2 = input("second Adjective: ")
noun2 = input("second noun: ")
noun3 = input("third noun: ")
adj3 = input("third adjective: ")
verb2 = input("second verb: ")
pverb2 = input("second past tense verb: ")
adj4 = input("fourth adjective: ")


madlib = f" Today I went to the zoo. I saw a(n){adj} {noun1} jumping up and down in its tree. \"" \
         f"He {pverb} through the large tunnel that led to its {adj2} {noun2}. I got some peanuts and\
         passed them through the cage to the gigantic gray {noun3} towering above my head. Feeding that \
         animal made me hungry. I went to get a(n) {adj3} scoop of ice cream. It filled my stomach. \
         Afterwards, I had to {verb2} to catch our bus. When I got home, I {pverb2} my mom for a {adj4} day \
         at the zoo."

print(madlib)
