import tkinter as tk
import winsound
import winsound
from random import randint
def play(sound):
    return winsound.PlaySound(sound,winsound.SND_FILENAME)
#winsound.PlaySound("piano_keys",winsound.SND_FILENAME)
allnotes={
    "silence":0,
    "shake":1,
    "pop":2,
    "knock":3,
    "kick":4
    }

notes=list()
def deletelast():
    if len(notes)>0:
        print("last note deleted")
        notes.pop()
        if len(notes)==1:
            print("all removed")
    else:
        print("all removed")
def  play_all():
    if len(notes)>0:
        print("playing")
        for i in range(len(notes)):
            if notes[i]==allnotes["silence"]:
                play("silence")
            elif notes[i]==allnotes["shake"]:
                play("shake")
            elif notes[i]==allnotes["pop"]:
                play("pop")
            elif notes[i]==allnotes["knock"]:
                play("knock")
            elif notes[i]==allnotes["kick"]:
                play("kick")
        print("ready")
    else:
        print("all empty")
    #rint(notes)


def playrand():
    print("playing random")
    for i in range(len(rand)):
        if rand[i]==allnotes["silence"]:
            play("silence")
        elif rand[i]==allnotes["shake"]:
            play("shake")
        elif rand[i]==allnotes["pop"]:
            play("pop")
        elif rand[i]==allnotes["knock"]:
            play("knock")
        elif rand[i]==allnotes["kick"]:
            play("kick")
        else:
            play("aaaaa")

    print("ready playing random with lenght",len(rand))
        #print(rand)



def delete():
    print("all deleted")
    for i in range(len(notes)):
        notes.pop()



def record(item):
    notes.append(item)


def record_silence():
    record(allnotes["silence"])


def record_shake():
    play("shake")
    record(allnotes["shake"])


def record_pop():
    play("pop")
    record(allnotes["pop"])


def record_knock():
    play("knock")
    record(allnotes["knock"])

def record_kick():
    play("kick")
    record(allnotes["kick"])


def generaterandom():
    print("Generated random")
    if len(rand)>0 and (rand[-1]==0 and rand[-1]==allnotes["kick"]):
        return randint(1,len(allnotes)-1)
    else:
        return randint(0,len(allnotes)-1)
rand=[]
def addrandom():
    rand.append(generaterandom())



first=tk.Tk()
first.title("My first window")
first.geometry("400x400")

label1=tk.Label(text="welcome")
label1.grid(column=0,row=0)

#nameentry=tk.Entry()
#nameentry.grid(column=1,row=1)

#mytext=tk.Label(text="hello",font=("Times New Roman",30))
#mytext.grid(column=0,row=3)

empty=tk.Button(text="empty",bg="white",command=record_silence)
empty.grid(column=0,row=1)

shakebtn=tk.Button(text="shake",bg="pink",command=record_shake)
shakebtn.grid(column=1,row=1)

popbtn=tk.Button(text="pop",bg="light green",command=record_pop)
popbtn.grid(column=2,row=1)

knockbtn=tk.Button(text="knock",bg="light blue",command=record_knock)
knockbtn.grid(column=3,row=1)
print("all removed")
kickbtn=tk.Button(text="kick",bg="cyan",command=record_kick)
kickbtn.grid(column=4,row=1)

playbtn=tk.Button(text="play",bg="red",command=play_all)
playbtn.grid(column=0,row=2)

randbtn=tk.Button(text="generate random",bg="light gray",command=addrandom)
randbtn.grid(column=1,row=2)

playrandbtn=tk.Button(text="play random",bg="light gray",command=playrand)
playrandbtn.grid(column=2,row=2)



delbtn=tk.Button(text="delete all recorded",bg="white",command=delete)
delbtn.grid(column=0,row=3)

delbtnlast=tk.Button(text="delete last recorded",bg="white",command=deletelast)
delbtnlast.grid(column=1,row=3)
'''
pr=tk.Button(text="pr",bg="white",command=sounds.whatnotes)
pr.grid(column=0,row=6)
'''


welcome=tk.Label(text="welcome")
welcome.grid(column=0,row=0)



first.mainloop()
#print(notes)
