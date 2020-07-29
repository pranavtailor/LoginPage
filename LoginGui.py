import tkinter as tk
import tkinter.font as font

root = tk.Tk()

HEIGHT = 400
WIDTH = 300

# Create account Page
def createAccount():
    topCreate = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topCreate.title("Register")

    # put info in text doc
    def storeData():
        Users = open('Users.txt', 'a')
        username = user_login_entry.get()
        password = pass_login_entry.get()
        Users.write(username + ', ' + password + "\n")
        Users.close()
        topCreate.destroy()


    # Enter username 
    user_login_label = tk.Label(topCreate, text = "Enter Username: ")
    user_login_label.place(relx = .3, rely = .1)
    user_login_label['font'] = myFont

    user_login_entry = tk.Entry(topCreate)
    user_login_entry.place(relx = .3, rely = .2, relwidth = .4, relheight = .1)

    # Enter password
    pass_login_label = tk.Label(topCreate, text = "Enter Password: ")
    pass_login_label.place(relx = .3, rely = .4)
    pass_login_label['font'] = myFont

    pass_login_entry = tk.Entry(topCreate)
    pass_login_entry.place(relx = .3, rely = .5, relwidth = .4, relheight = .1)

    # Enter button
    enter_login_button = tk.Button(topCreate, text = "Enter", command = storeData)
    enter_login_button.place(relx = .3, rely = .7, relwidth = .4, relheight = .1)

    
# Login page
def login():
    topLogin = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topLogin.title("Login")

    # check login info with text doc
    def checkData():
        Users = open('Users.txt', 'r')
        text = Users.readlines()
        newList = []
        for line in text:
            newList.append(line.strip())
            
        username = user_login_entry.get()
        password = pass_login_entry.get()
        cred = (username + ', ' + password)


        v = tk.StringVar()
        successLabel = tk.Label(topLogin, textvariable = v)
        successLabel.place(relx = .1, rely = .85, relwidth = .8)

        if cred in newList:
            v.set("Login successful!")
            successLabel.configure(fg = 'green')
            
        else:
            v.set("Invalid credentials, try again.")
            successLabel.configure(fg = 'red')
        
        Users.close()


    # Enter username 
    user_login_label = tk.Label(topLogin, text = "Enter Username: ")
    user_login_label.place(relx = .3, rely = .1)
    user_login_label['font'] = myFont

    user_login_entry = tk.Entry(topLogin)
    user_login_entry.place(relx = .3, rely = .2, relwidth = .4, relheight = .1)

    # Enter password
    pass_login_label = tk.Label(topLogin, text = "Enter Password: ")
    pass_login_label.place(relx = .3, rely = .4)
    pass_login_label['font'] = myFont

    pass_login_entry = tk.Entry(topLogin)
    pass_login_entry.place(relx = .3, rely = .5, relwidth = .4, relheight = .1)


    # Enter button
    enter_login_button = tk.Button(topLogin, text = "Enter", command = checkData)
    enter_login_button.place(relx = .3, rely = .7, relwidth = .4, relheight = .1)


# define font
myFont = font.Font(family = 'Helvetica', size = 12)

# Homepage
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

login_button = tk.Button(canvas, text = "Login", command = login)
login_button.place(relx = .3, rely = .3, relwidth = .4, relheight = .1)

create_button = tk.Button(canvas, text = "Create an account", command = createAccount)
create_button.place(relx = .3, rely = .5, relwidth = .4, relheight = .1)

 
root.mainloop()
