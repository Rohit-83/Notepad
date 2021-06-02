from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file,"w")
        TextArea.insert(1.0, f.read())
        f.close()


def rate_us():
    value = msg.askquestion("Experience", "was your experience good?")
    if value == "yes":
        msg1 = "Rate us on Play Store!"
    else:
        msg1 = "Tell us your problem we will contact you"
    msg.showinfo("Info", msg1)


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= "Untitled.txt" ,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    #cut copy paste are inbuilt in tkinter so we use that to make
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    msg.showinfo(" Notepad "," Notepad by Rohit..")

if __name__  == '__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("450x450+300+300")
    root.wm_iconbitmap("n.png")

    #add text area
    TextArea = Text(root,font="lucida 16 italic")
    file=None
    TextArea.pack(fill=BOTH , expand=True)


    #menubar
    my_menu= Menu(root)
    #file menu starts
    File_Menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="File",menu=File_Menu)
    #to open new file
    File_Menu.add_command(label="New",command=newFile)

    #to open exist file
    File_Menu.add_command(label="Open",command=openFile)

    #to save current file
    File_Menu.add_command(label="Save",command=saveFile)
    File_Menu.add_separator()
    File_Menu.add_command(label="Exit",command=quitApp)
    #file menu end and edit menu start

    Edit_Menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit",menu=Edit_Menu)
    #feature
    Edit_Menu.add_command(label="Cut",command=cut)
    Edit_Menu.add_command(label="Copy", command=copy)
    Edit_Menu.add_command(label="Paste", command=paste)
    #edit menu ends and help menus end

    Help_Menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Help",menu=Help_Menu)
    Help_Menu.add_command(label="About..",command=about)
    #end

    #rate menu
    rate_menu = Menu(my_menu)
    my_menu.add_cascade(label="Rate us", menu=rate_menu)
    rate_menu.add_command(label="Rate us", command=rate_us)

    root.config(menu=my_menu)

    #adding scroll bar
    scrollbar=Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)


    root.mainloop()