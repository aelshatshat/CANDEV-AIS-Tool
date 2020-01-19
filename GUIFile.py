from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename

def buttonClicked ():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    return

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Data Select")

        #title
        self.label = Label(master, text="Please enter the directory of the data for parsing, or browse for the data file", font=("Helvetica", 16))
        self.label.pack()

        #Entry bar for path
        path = "";
        E1 = Entry(master, bd =5, width = 50, textvariable = path)
        E1.place(relx = 0,rely = 0.1)

        #Browse button
        self.close_button = Button(master, text="Browse",height = 5, width = 10, command=buttonClicked)
        self.close_button.place(relwidth = 0.1, relheight = 0.05, relx = 0.4, rely = 0.09)

        #filter button
        def filterVessels ():
            selectedRegion = region.get()
            
            if (selectedRegion = "Maritime"):
                selectedRegion = "M"
            if (selectedRegion = "Pacific"):
                selectedRegion = "P"
            if (selectedRegion = "Quebec"):
                selectedRegion = "Q"
            if (selectedRegion = "Golf"):
                selectedRegion = "G"
            if (selectedRegion = "Central and Arctic"):
                selectedRegion = "C"
            if (selectedRegion = "Newfoundland and Labrador"):
                selectedRegion = "N"
                
            speedChecked = var1.get()
            if (speedChecked == True):
                maxSpeed = E3.get()
                if(maxSpeed == ""):
                    print("error")
                else:
                    int(maxSpeed)
                    
                minSpeed = E2.get()
                if (minSpeed == ""):
                    print ("error")
                else:
                    int(minSpeed)

            locChecked = var2.get()
            if (locChecked == True):
                initX = xEntry.get()
                initY = yEntry.get()
                xSelect = directionX.get()
                ySelect = directionY.get()

                if (initX != "" and xSelect == "East" or "West"):
                    int(initX)
                else:
                    print("Validate all fields")
                if (initY != "" and ySelect == "North" or "South"):
                    int(initY)
                else:
                    print("Validate all fields")
                
            print ("filter")

        def parseData ():
            E1.get()
            print ("parse")

        #filter button
        self.filterButton = Button(master, text="Filter",height = 5, width = 10, command=filterVessels)
        self.filterButton.place(relwidth = 0.1, relheight = 0.05, relx = .750, rely = 0.750)

        #parse Button 
        self.parseButton = Button(master, text="Parse",height = 5, width = 10, command=parseData)
        self.parseButton.place(relwidth = 0.1, relheight = 0.05, relx = .750, rely = 0.700)

        #Speed check box
        var1 = BooleanVar()
        speedButton = Checkbutton(master, text="Speed", variable=var1).place(relx = 0.1, rely = 0.3)

        #Entry bar 1
        minSpeed = "";
        E2 = Entry(master, bd =5, width = 25, textvariable = minSpeed)
        E2.place(relx = 0.1,rely = 0.35)

        self.label = Label(master, text="Minimum Speed", font=("Helvetica", 10))
        self.label.place(relx = 0.1,rely = 0.4)

        #Entry bar 2
        maxSpeed = "";
        E3 = Entry(master, bd =5, width = 25, textvariable = maxSpeed)
        E3.place(relx = 0.31,rely = 0.35)

        self.label = Label(master, text="Maximum Speed",font=("Helvetica", 10))
        self.label.place(relx = 0.31,rely = 0.4)


        #Location check box
        var2 = BooleanVar()
        locationButton = Checkbutton(master, text=" Restrict Location", variable=var2).place(relx = 0.10, rely = 0.5)

        initX = "";
        xEntry = Entry(master, bd =5, width = 25, textvariable = initX)
        xEntry.place(relx = 0.1,rely = 0.575)

        self.label = Label(master, text="X Coordinate", font=("Helvetica", 10))
        self.label.place(relx = 0.1,rely = 0.61)
        
        directionX = StringVar(master)
        directionX.set("Select") # default value
        xSelect = OptionMenu(master, directionX, "East","West")
        xSelect.place(relwidth = 0.1, relheight = 0.03, relx = .3, rely = 0.575)

        initY = "";
        yEntry = Entry(master, bd =5, width = 25, textvariable = initY)
        yEntry.place(relx = 0.1,rely = 0.65)

        self.label = Label(master, text="Y Coordinate", font=("Helvetica", 10))
        self.label.place(relx = 0.1,rely = 0.685)

        directionY = StringVar(master)
        directionY.set("Select") # default value
        ySelect = OptionMenu(master, directionY, "North","South")
        ySelect.place(relwidth = 0.1, relheight = 0.03, relx = .3, rely = 0.65)

        #region drop down mentu
        region = StringVar(master)
        region.set("All Regions") # default value
        w = OptionMenu(master, region, "Central and Arctic", "Maritime", "Newfoundland and Labrador","Pacific","Quebec","Golf")
        w.place(relwidth = 0.2, relheight = 0.0750, relx = .750, rely = 0.085)


    def greet(self):
        print("Greetings!")

    def buttonClicked ():
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)

root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("800x800")
root.mainloop()
