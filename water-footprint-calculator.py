import turtle
print("---WATER FOOTPRINT CALCULATOR--- \nPlease answer the following questions and your water footprint status will be calculated.\n")

dict1 = {"question": "About how soft drinks/tea/coffee do you drink daily? (not including water consumption)", "choices": [("3+", 1), ("2", 2), ("0-1", 3)]}
dict2 = {"question": "Around how many times do you flush the toilet daily? (flushing is good as needed, but not exessively!)", "choices": [("13+", 1), ("8-12", 2), ("1-7", 3)]}
dict3 = {"question": "How many times do you run the dishwasher and washing machine (combined) weekly?", "choices": [("1-2", 3), ("3-5", 2), ("6+", 1)]}
dict4 = {"question": "How long do you leave the water running in the shower during an average use? (showering is a hygenic practice, but keeping them to what is needed is beneficial for the planet AND your water bill)", "choices": [("6-12 minutes", 2), ("1-5 minutes", 3), ("13+ minutes", 1)]}
dict5 = {"question": "About how much additional water usage do you have daily? (other items not listed above, e.g. car wash", "choices": [("0-10 gallons", 3), ("31+ gallons", 1), ("11-30 gallons", 2)]}


def askQuestion(dict):
    print(dict['question'])
    print("Your choices are:")

    letters = ["A", "B", "C"]
    letterIdx = 0
    for choice in dict['choices']:
        print(letters[letterIdx], choice[0])
        letterIdx += 1

    response = input("").upper()
    option = letters.index(response)
    #print("Your points are:", dict['choices'][option][1])
    return dict['choices'][option][1]

totalPoints = askQuestion(dict1) + askQuestion(dict2) + askQuestion(dict3) + askQuestion(dict4) + askQuestion(dict5)

t = turtle.Turtle()
t.width(5)

t.penup()
color = "red"
if totalPoints >= 12:
    color = "lime"
elif totalPoints >= 8:
    color = "gold"
t.goto(0, 0)
t.dot(200, color)

t.goto(-30, 140)
t.write("Status:", font=("Arial", 16, "normal"))

t.goto(-200, 200)
t.color('black')
t.write(f"Thank you for playing. Your score is {totalPoints}.", font=("Arial", 20, "normal"))

turtle.done()
