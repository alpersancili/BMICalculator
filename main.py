import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=200)

def calculate_bmi():
    weight = weight_input.get()
    height = height_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
            result_label.place(x=20, y=135)
        except:
            result_label.config(text="Enter a valid number!")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are "
    if bmi < 18.5:
        result_string += "under weight."
    elif 18.5 < bmi < 24.9:
        result_string += "normal."
    elif 25 < bmi < 29.9:
        result_string += "over weight."
    elif 30 < bmi < 34.9:
        result_string += "obese (class1)"
    elif 35 < bmi < 39.9:
        result_string += "obese (class2)"
    elif bmi >40:
        result_string += "extreme obese"
    return result_string


weight_label = tkinter.Label(text="Enter your weight (kg)")
weight_label.place(x=60,y=20)

weight_input = tkinter.Entry()
weight_input.place(x=60,y=40)

height_label = tkinter.Label(text="Enter your height (cm)")
height_label.place(x=60,y=60)

height_input = tkinter.Entry()
height_input.place(x=60,y=80)

calculate_button = tkinter.Button(text="Calculate",command=calculate_bmi)
calculate_button.place(x=70,y=105,width=100)

result_label = tkinter.Label()


tkinter.mainloop()