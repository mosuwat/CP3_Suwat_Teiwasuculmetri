from tkinter import *
import math

def Calculate(event):
    BMI = float(TextBoxWeight.get())/math.pow(float(TextBoxHeight.get())/100,2)
    labelResult.configure(text="Your BMI is :" + str(BMI))
    if BMI >= 30.0:
        labelResult2.configure(text="You are Obese")
    elif BMI >= 25.0:
        labelResult2.configure(text="You are Fat")
    elif BMI >= 23.0:
        labelResult2.configure(text="You are Overweight")
    elif BMI >= 18.6:
        labelResult2.configure(text="You are Normal or Healthy Weight")
    else:
        labelResult2.configure(text="You are Underweight")


MainWindow = Tk()
labelHeight = Label(MainWindow,text = "Height(cm.)")
labelHeight.grid(row=0,column=0)
TextBoxHeight = Entry(MainWindow)
TextBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text = "Weight(kg.)")
labelWeight.grid(row=1,column=0)
TextBoxWeight = Entry(MainWindow)
TextBoxWeight.grid(row=1,column=1)
CalculateButton = Button(MainWindow,text = "Calculate")
CalculateButton.bind('<Button-1>',Calculate)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text = "Result")
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow,text = "State")
labelResult2.grid(row=3,column=1)
MainWindow.mainloop()