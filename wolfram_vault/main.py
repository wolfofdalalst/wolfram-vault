import tkinter
import customtkinter 


customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):

    WIDTH=2000
    HEIGHT=1500

    def __init__(self):
        super().__init__()

        self.title("WolframVault")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left=customtkinter.CTkFrame(master=self, width=350, corner_radius=0, height=150)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right=customtkinter.CTkFrame(master=self, width=200, height=200)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # left frame 

        self.frame_left.grid_rowconfigure(0, minsize=0)   
        self.frame_left.grid_rowconfigure(3, weight=1)  
        self.frame_left.grid_rowconfigure(11, minsize=0)

        self.title=customtkinter.CTkLabel(master=self.frame_left, text='WolframPass', text_font=('Overpass', 20))
        self.title.grid(row=1, column=0, pady=10, padx=10) 

        self.about=customtkinter.CTkButton(master=self.frame_left, text='About', text_font=('Overpass', '15'))
        self.about.grid(row=2, column=0, pady=10, padx=20) 

    
if __name__ == '__main__':
    app=App()
    app.mainloop()