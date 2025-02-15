# x : int = input("What's x? ")
# y : int = input("What's y? ")
# if x != y:
#     print(" x is not equal to y")
# else:
#     print ("x is equal to y")

# planets = "mercury venus earth mars jupiter saturn uranus neptune"
# # convert the string to a list with the first letter of each word capitalized
# list_of_planets = planets.title().split()
# # convert the list of words to a dictionary
# dictionary_of_planets = {planet: planet[0] for planet in list_of_planets}
# # print out the results
# print('{}\n{}'.format(list_of_planets, dictionary_of_planets), "M" in dictionary_of_planets)

# for planet in dictionary_of_planets:
#     print(f"{planet} = {dictionary_of_planets[planet]}\n")

# weight converter program

weight : int = int(input("What is your weight? "))
unit : str = input("(L)bs or (K)g: ").upper()

if unit == "L":
    converted = weight * 0.45
elif unit == "K":
    converted = weight / 0.45

print(f"{converted:.2f}")

