import customtkinter
import tkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

class App(customtkinter.CTk):
    
    WIDTH=800
    HEIGHT=600

    

    def __init__(self):
        super().__init__()

        def event(value):
            self.length=customtkinter.CTkLabel(master=self.frame, text=str(int(value)), text_font=('Helvetica', '14'), width=25)
            self.length.place(relx=0.3, rely=0.4)


        self.title('WolframVault')
        self.resizable('false', 'false')
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        self.frame=customtkinter.CTkFrame(master=self, width=1000, height=600)
        self.frame.grid(row=0, column=0, sticky='nswe')


        self.password=customtkinter.CTkLabel(master=self.frame, text='Uxbghrhighj', text_font=('MierB03','20'), text_color='white') # displaying the password 
        self.password.place(relx=0.4, rely=0.2, anchor=tkinter.CENTER)

        self.copy=customtkinter.CTkButton(master=self.frame, text='Copy', text_font=('MierB03', '15'), width=10) # copy button 
        self.copy.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)


        self.set=customtkinter.CTkSlider(master=self.frame, from_=0, to=20, width=600, command=event)   # slider to adjust the number of characters 
        self.set.place(relx=0.1, rely=0.3)

        self.label_length=customtkinter.CTkLabel(master=self.frame, text='Length:', text_font=('Helvetica', '20'), text_color='white') 
        self.label_length.place(relx=0.1, rely=0.4)
       
        self.label_strength=customtkinter.CTkLabel(master=self.frame, text=('Strength:', 'Very Strong'), text_font=('Helvetica', '20'), text_color='white') # displaying the strength of the password 
        self.label_strength.place(relx=0.3, rely=0.4)
       
        self.used=customtkinter.CTkLabel(master=self.frame, text='Characters Used:', text_font=('MierB03', '20'), text_color='white')
        self.used.place(relx=0.1, rely=0.6)

        self.char_buttons1=customtkinter.CTkRadioButton(master=self.frame, text='ABC', text_font=('MierB03', '14'), text_color='white') # to choose the characters to be used 
        self.char_buttons1.place(relx=0.4, rely=0.6)

        self.char_buttons2=customtkinter.CTkRadioButton(master=self.frame, text='abc', text_font=('MierB03', '14'), text_color='white')
        self.char_buttons2.place(relx=0.5, rely=0.6)

        self.char_buttons3=customtkinter.CTkRadioButton(master=self.frame, text='123', text_font=('MierB03', '14'), text_color='white')
        self.char_buttons3.place(relx=0.6, rely=0.6)

        self.char_buttons4=customtkinter.CTkRadioButton(master=self.frame, text='#$&', text_font=('MierB03', '14'), text_color='white')
        self.char_buttons4.place(relx=0.7, rely=0.6)
        

if __name__=='__main__':
    app=App()
    app.mainloop()