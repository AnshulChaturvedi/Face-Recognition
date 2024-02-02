import customtkinter as ctk

window = ctk.CTk()
window.title('Student_Attendance')
window.geometry("650x400")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def generate_dataset():
    print("Test")

def detect_face():
    print("Test")

def train_classifier():
    print("Test")

def Excel():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("green")  

    app = ctk.CTk() 
    app.geometry("650x400")
    app.title('Authorized_Login')

    def button_function():
        print("Done")

    frame = ctk.CTkFrame(app)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    l2=ctk.CTkLabel(master=frame, text="Teacher's Login",font=('Century Gothic', 25))
    l2.place(x=50, y=45)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2=ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
    button1.place(x=50, y=240)

    app.mainloop()

frame = ctk.CTkFrame(window)
frame.pack(pady=10, padx=50, fill="both", expand=True)
    
label = ctk.CTkLabel(master=frame, text="Student's Login", font=("Century Gothic", 30 ),text_color='white')
label.grid(row=0 , column=0 , sticky='nsew' , pady= 20)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Student Name", width=150)
entry1.grid(row=1 , column=0 , sticky='ew' , padx = 70 , pady=30)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Student ID" , width=150)
entry2.grid(row=1 , column=1 , sticky='ew', padx = 20 , pady =30)

button1 = ctk.CTkButton(master=frame, text="Generate Dataset" ,width=220 , font= ("Comic Sans MS",15) , command = generate_dataset , corner_radius=6 )
button1.grid(row=2 , column=0 , sticky='se' , pady = 20)

button2 = ctk.CTkButton(master=frame, text="Detect Face", width=220 , font= ("Comic Sans MS",15 ) , command = detect_face , corner_radius=6)
button2.grid(row=2 , column=1, sticky='s' ,  pady = 20)

button3 = ctk.CTkButton(master=frame, text="Train Classifier", width=220 , font= ("Comic Sans MS",15)  , command = train_classifier , corner_radius=6 )
button3.grid(row=3 , column=0 , sticky='ne' )

button4 = ctk.CTkButton(master=frame, text="View Excel", width=220 , font= ("Comic Sans MS",15 ) , command = Excel , corner_radius=6)
button4.grid(row=3 , column=1 , sticky='n' , padx = 5)


window.columnconfigure((0,1,2,3) , weight= 1)
window.rowconfigure((0,1,2,3) , weight= 1)

window.mainloop()