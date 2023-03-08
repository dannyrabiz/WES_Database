import tkinter as tk
from tkinter import ttk
import  os

def clicked1():
    print("Button 1 was clicked!")
    user_input = entry.get()
    print(user_input)
    user_cohort = combobox.get()
    print(user_cohort)
    lunch = listbox.get(listbox.curselection())
    print(lunch)
    user_agreement = check_var.get()
    print("Agreement:", user_agreement)
    root.destroy()

def clicked2():
    os.system('python Second.py')
    root.destroy()


root = tk.Tk()
root.title('Isaacs WES database')
#root.configure(background='gray')

GP = tk.Label(root, text='Search by Gene/Variant', font=("Arial", 14,  "underline"))
GP.pack()

frameA = tk.LabelFrame(root, relief="flat")
frameA.pack()

blank= tk.Label(frameA, text='           ')
blank.grid(row=1, column=1)

label_var2 = tk.IntVar()
lv2 = tk.Checkbutton(frameA, text="Gene(s)", variable=label_var2)
lv2.grid(row=1, column=0)

label_var3 = tk.IntVar()
lv3 = tk.Checkbutton(frameA, text="Position \n (ex: chr12-10028781)", variable=label_var3)
lv3.grid(row=1, column=2)

#label0 = tk.Label(frameA, text="Search Gene(s):")
#label0.grid(row=0, column=0)

entry0 = tk.Entry(frameA, width=10)
entry0.grid(row=2, column=0)

#label01 = tk.Label(frameA, text="Search Position:")
#label01.grid(row=0, column=2)

entry01 = tk.Entry(frameA, width = 10)
entry01.grid(row=2, column=2)

label1 = tk.Label(root, text="Select Cohort:")
label1.pack()

combobox = ttk.Combobox(root, values=["HPC", "AA", "Other"])
combobox.pack()

label2 = tk.Label(root, text="Select Sample:")
label2.pack()

listbox = tk.Listbox(root, height=5, width=10)
listbox.insert(0, "All Samples")
listbox.insert(1, "JHU101")
listbox.insert(2, "JHU102")
listbox.insert(3, "JHU103")
listbox.insert(4, "JHU104")
listbox.insert(5, "JHU105")
listbox.insert(6, "JHU106")
label2.pack()
listbox.pack()


framelabel1 = tk.Label(root, text="Annotation", font=("Arial", 14,  "underline"))
framelabel1.pack()

frame1 = tk.LabelFrame(root, relief="sunken")
frame1.pack()

check_varA = tk.IntVar(value=1)
checkA = tk.Checkbutton(frame1, text="RefSeq", variable=check_varA)
checkA.grid(row=1, column=1)

check_varB = tk.IntVar(value=1)
checkB = tk.Checkbutton(frame1, text="Ensembl", variable=check_varB)
checkB.grid(row=1, column=2)

check_varC = tk.IntVar(value=1)
checkC = tk.Checkbutton(frame1, text="gnomAD", variable=check_varC)
checkC.grid(row=1, column=3)

check_varD = tk.IntVar(value=1)
checkD = tk.Checkbutton(frame1, text="COSMIC", variable=check_varD)
checkD.grid(row=1, column=4)

check_varE = tk.IntVar(value=1)
checkE = tk.Checkbutton(frame1, text="ClinVar", variable=check_varE)
checkE.grid(row=2, column=1)

check_varE = tk.IntVar(value=1)
checkE = tk.Checkbutton(frame1, text="ClinVar", variable=check_varE)
checkE.grid(row=2, column=1)

check_varF = tk.IntVar(value=1)
checkF = tk.Checkbutton(frame1, text="In Silico", variable=check_varF)
checkF.grid(row=2, column=2)

check_varG = tk.IntVar(value=1)
checkG = tk.Checkbutton(frame1, text="SupDups", variable=check_varG)
checkG.grid(row=2, column=3)

check_varI = tk.IntVar(value=1)
checkI = tk.Checkbutton(frame1, text="CADD", variable=check_varI)
checkI.grid(row=2, column=4)



framelabel3 = tk.Label(root, text="Clinical Info", font=("Arial", 14,  "underline"))
framelabel3.pack()

frame3= tk.LabelFrame(root, relief="flat")
frame3.pack()

check_varA3 = tk.IntVar(value=0)
checkA3 = tk.Checkbutton(frame3, text="Gleason", variable=check_varA3)
checkA3.grid(row=1, column=1)

check_varB3 = tk.IntVar(value=0)
checkB3 = tk.Checkbutton(frame3, text="Fx", variable=check_varB3)
checkB3.grid(row=1, column=2)

check_varC3 = tk.IntVar(value=0)
checkC3 = tk.Checkbutton(frame3, text="Race", variable=check_varC3)
checkC3.grid(row=1, column=3)


framelabel2 = tk.Label(root, text="Output", font=("Arial", 14,  "underline"))
framelabel2.pack()

frame0 = tk.LabelFrame(root,relief ='flat')
frame0.pack()

label3 = tk.Label(frame0, text="File type:")
label3.grid(row=1, column = 0)

check_var = tk.IntVar(value=1)
check = tk.Checkbutton(frame0, text=".xlsx", variable=check_var)
check.grid(row=1, column=1)

check_var1 = tk.IntVar()
check1 = tk.Checkbutton(frame0, text=".csv", variable=check_var1)
check1.grid(row=1, column=2)

check_var2 = tk.IntVar()
check2 = tk.Checkbutton(frame0, text=".txt", variable=check_var2)
check2.grid(row=1, column=3)

label = tk.Label(frame0, text="File Name:")
label.grid(row=3, column =0)

entry = tk.Entry(frame0,  width=10)
entry.grid(row=3, column =1)

button1 = tk.Button(root, text="Run", command=clicked1,  fg='green', bg='blue' )
button1.pack()

button2 = tk.Button(root, text="Cancel", command=clicked2, fg = 'red')
button2.pack()

button3 = tk.Button(root, text="Custom", command=clicked2, fg = 'orange')
button3.pack()

root.mainloop()
