from tkinter import *
import ttk

root = Tk()                                 #Initiliaze the application window
root.title("PPLPPL Planner")                #Set the title for the application
gymDict = {}                                #Set the dictionary to be used to store
e = Entry(root)                             #input
e.grid(row=0, column=0)
e.insert(0, "Enter your first and last name: ")
f = Entry(root)
f.grid(row=1, column=0)
f.insert(0, "How many push workouts: ")
inputforPull = Entry(root)
inputforPull.grid(row=1, column=2)
inputforPull.insert(0, "How many pull workouts: ")
inputforLegs = Entry(root)
inputforLegs.grid(row=1, column=4)
inputforLegs.insert(0, "How many legs workouts: ")
listofVariables = ['g', 'h', 'i', 'k', 'l', 'm', 'n', 'o']
variablesforWeight = ['gc', 'hc', 'ic', 'kc', 'lc', 'mc', 'nc', 'oc']
listofPullWeight = ['gd', 'hd', 'id', 'kd', 'ld', 'md', 'nd', 'od']
numberofWorkouts = 0
listofPullWeight = ['ge', 'he', 'ie', 'ke', 'le', 'me', 'ne', 'oe']
listofLegWeight = ['gf', 'hf', 'if', 'kf', 'lf', 'mf', 'nf', 'of']
rowPlacement = 0


#tabs
nb = ttk.Notebook(root)
nb.grid(row=4, column=0, columnspan =50, rowspan = 49, sticky= 'NESW')

page1 = ttk.Frame(nb)
nb.add(page1, text ='Push')
#swagLabel = Label(page1, text = 'hello')
#swagLabel.grid(column=13, row=13)



page2 = ttk.Frame(nb)
nb.add(page2, text='Pull')

page3 = ttk.Frame(nb)
nb.add(page3, text='Legs')

#f = Entry(root)
#f.grid(row=1, column=0)



def theClick():
    hello = e.get() +"'s PHUL Plan"
    myLabel = Label(root, text = hello)
    myLabel.grid(row = 5, column=3)

def secondClick():

    global numberofWorkouts
    numberofWorkouts = int(f.get())
    counter = 0
    rowPlacement = 6
    pushLabel = Label(page1, text="Push Workout")
    pushLabel.grid(row=5, column= 0)
    for i in range(0, numberofWorkouts):
        listofVariables[counter] = Entry(page1)
        listofVariables[counter].grid(row=rowPlacement, column= 0)
        variablesforWeight[counter] = Entry(page1)
        variablesforWeight[counter].grid(row=rowPlacement, column=1)
        counter = counter + 1
        rowPlacement = rowPlacement + 1
    confirmPlan = Button(page1, text="Confirm Plan!", command=savePlan)
    confirmPlan.grid(row=rowPlacement, column=0)

def thirdClick():

    listofPullVariables = ['ga', 'ha', 'ia', 'ka', 'la', 'ma', 'na', 'oa']
    numberofPullVariables = int(inputforPull.get())
    counter = 0
    rowPlacementForPull = 6
    pullLabel = Label(page2, text="Pull Workout")
    pullLabel.grid(row=5, column= 0)
    for i in range (0, numberofPullVariables):
        listofPullVariables[counter] = Entry(page2)
        listofPullVariables[counter].grid(row =rowPlacementForPull, column = 0)
        listofPullWeight[counter] = Entry(page2)
        listofPullWeight[counter].grid(row=rowPlacementForPull, column=1)
        counter = counter + 1
        rowPlacementForPull = rowPlacementForPull + 1

def fourthClick():

    listofLegVariables = ['gb', 'hb', 'ib', 'kb', 'lb', 'mb', 'nb', 'ob']
    numberofLegVariables = int(inputforLegs.get())
    counter = 0
    rowPlacementForLeg = 6
    legLabel = Label(page3, text="Leg  Workout")
    legLabel.grid(row=5, column= 0)
    for i in range (0, numberofLegVariables):
        listofLegVariables[counter] = Entry(page3)
        listofLegVariables[counter].grid(row =rowPlacementForLeg, column = 0)
        listofLegWeight[counter] = Entry(page3)
        listofLegWeight[counter].grid(row=rowPlacementForLeg, column=1)
        counter = counter + 1
        rowPlacementForLeg = rowPlacementForLeg + 1

def savePlan():

    saveCounter = 0
    global gymDict
    recommendedLabel = Label(page1, text="Recommended Plan")
    recommendedLabel.grid(row=5, column=2)
    rowPlacement = 6

    for i in range(0, numberofWorkouts):
        excercises = listofVariables[saveCounter].get()
        weightforExcercises = int(variablesforWeight[saveCounter].get())
        recommendedWeightFam = weightforExcercises + 5
        gymDict.setdefault(excercises, weightforExcercises)
        recommendedWorkoutLabel = Label(page1, text=excercises)
        recommendedWorkoutLabel.grid(row=rowPlacement, column=2)
        recommendedWeightLabel = Label(page1, text=recommendedWeightFam)
        recommendedWeightLabel.grid(row=rowPlacement, column=3)
        rowPlacement = rowPlacement + 1
        saveCounter = saveCounter + 1


    return excercises, weightforExcercises


   # listofPullVariables = ['ga', 'ha', 'ia', 'ka', 'la', 'ma', 'na', 'oa']
    #listofPullVariables = ['gb', 'hb', 'ib', 'kb', 'lb', 'mb', 'nb', 'ob']

myButton = Button(root, text="Confirm!", command=theClick)
myButton.grid(row=0, column=1)

secondButton = Button(root, text="Confirm!", command=secondClick)
secondButton.grid(row=1, column=1)

pullButton = Button(root, text="Confirm!", command=thirdClick)
pullButton.grid(row=1, column=3)

legButton = Button(root, text="Confirm!", command =fourthClick)
legButton.grid(row=1, column=5)


root.mainloop()

