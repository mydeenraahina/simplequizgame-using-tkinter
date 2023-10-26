import tkinter as tk
import tkinter.messagebox as mg
window=tk.Tk()#creating window
window.title('login')
frame=tk.Frame(master=window,borderwidth=20,width="100",bg="gray")#creating frame in window
frame.pack()
def main():
    import tkinter as tk
    import tkinter.messagebox as mg
    window=tk.Tk()
    window.title("quiz world")
    frame=tk.Frame(master=window)
    frame.pack()
    def submit():
        def play():
            score=0
            score1=0
            a=entry1.get()
            entry1.delete(0,tk.END)
            if a=="peacock":
                label=tk.Label(master=frame,text="correct")
                label.grid(row=1,column=2)
                score=score+1
            else:
                label=tk.Label(master=frame,text="wrong")
                label.grid(row=1,column=2)
                score1=score1+1
            b=entry2.get()
            entry2.delete(0,tk.END)
            if b=="tiger":
                label=tk.Label(master=frame,text="correct")
                label.grid(row=3,column=2)
                score=score+1
            else:
                label=tk.Label(master=frame,text="wrong")
                label.grid(row=3,column=2)
                score1=score1+1
            c=entry3.get()
            entry3.delete(0,tk.END)
            if c=="mango":
                label=tk.Label(master=frame,text="correct")
                label.grid(row=5,column=2)
                score=score+1
            else:
                label=tk.Label(master=frame,text="wrong")
                label.grid(row=5,column=2)
                score1=score1+1
            d=entry4.get()
            entry4.delete(0,tk.END)
            if c=="seven":
                label=tk.Label(master=frame,text="correct")
                label.grid(row=7,column=2)
                score=score+1
            else:
                label=tk.Label(master=frame,text="wrong")
                label.grid(row=7,column=2)
                score1=score1+1
            e=entry5.get()
            entry5.delete(0,tk.END)
            if e=="developing":
                label=tk.Label(master=frame,text="correct")
                label.grid(row=9,column=2)
                score=score+1
            else:
                label=tk.Label(master=frame,text="wrong")
                label.grid(row=9,column=2)
                score1=score1+1
            label=tk.Label(master=frame,text="correct=")
            label.grid(row=13,column=0)
            label=tk.Label(master=frame,text=score)
            label.grid(row=13,column=1)
            label=tk.Label(master=frame,text="wrong=")
            label.grid(row=13,column=2)
            label=tk.Label(master=frame,text=score1)
            label.grid(row=13,column=3)
            label=tk.Label(master=frame,text="total score")
            label.grid(row=14,column=2)
            label=tk.Label(master=frame,text=score)
            label.grid(row=14,column=3)
        x=entry.get()
        entry.delete(0,tk.END)
        if x=="yes":
            window=tk.Tk()
            frame=tk.Frame(master=window)
            frame.pack()
            label=tk.Label(master=frame,text="question1:National bird of india")
            label.grid(row=0,column=1)
            entry1=tk.Entry(master=frame)
            entry1.grid(row=0,column=2)
            label=tk.Label(master=frame,text="question2:Nation animal of india")
            label.grid(row=2,column=1)
            entry2=tk.Entry(master=frame)
            entry2.grid(row=2,column=2)
            label=tk.Label(master=frame,text="question3:national friut of india:")
            label.grid(row=4,column=1)
            entry3=tk.Entry(master=frame)
            entry3.grid(row=4,column=2)
            label=tk.Label(master=frame,text="question4:How many days in a week:")
            label.grid(row=6,column=1)
            entry4=tk.Entry(master=frame)
            entry4.grid(row=6,column=2)
            label=tk.Label(master=frame,text="question5:india is a ____ country")
            label.grid(row=8,column=1)
            entry5=tk.Entry(master=frame)
            entry5.grid(row=8,column=2)
            btn1=tk.Button(master=frame,text="submit",command=play)
            btn1.grid(row=11,column=2)
        else:
            mg.showinfo("thanks for ur response")
    label=tk.Label(master=frame,text="welcome to quis world")
    label.grid(row=0,column=2)
    label=tk.Label(master=frame,text="Do you want to play this game")
    label.grid(row=1,column=2)
    entry=tk.Entry(master=frame)
    entry.grid(row=2,column=2)
    btn=tk.Button(master=frame,text="submit",command=submit)
    btn.grid(row=3,column=3)
#displaying label:userid
label=tk.Label(master=frame,text="userid:",bg="skyblue",width=5,relief=tk.RAISED)
label.grid(row=0,column=0)
#display entrybox for userid
entry=tk.Entry(master=frame,bg="pink",relief=tk.RAISED,width=30)
entry.grid(row=0,column=3)
#display label:pwd
label1=tk.Label(master=frame,text="password:",bg="skyblue",width=8,relief=tk.RAISED)
label1.grid(row=1,column=0)
#diplay entrybox for pwd
entry1=tk.Entry(master=frame,bg="pink",relief=tk.RAISED,width=30)
entry1.grid(row=1,column=3)
#function to clear
def cut():
    entry.delete(0,tk.END)
    entry1.delete(0,tk.END)
def login():
    #getting details from user
    user=entry.get()
    pwd=entry1.get()
    if user=="system" and pwd=="@1234":
        main()
    else:
        mg.showinfo("try again")
button=tk.Button(master=frame,text="login",bg="wheat",command=login)#buttton for getting input
button.grid(row=3,column=2)
#clear button
button1=tk.Button(master=frame,text="clear",bg="wheat",command=cut)
button1.grid(row=3,column=3)
