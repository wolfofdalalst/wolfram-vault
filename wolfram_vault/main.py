import customtkinter
import pyperclip

from wolfram_vault.passgen import random_password

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


class Font:
    def helvetica(size=15):
        return ("helvetica", size)

    def mier(size=20):
        return ("MierB03", size)


class App(customtkinter.CTk):

    WIDTH = 550
    HEIGHT = 400

    PADX = 20
    PADY = 20

    def __init__(self):
        super().__init__()

        self.title("WolframVault")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed

        # =============== create two frames ===============

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_upper = customtkinter.CTkFrame(
            master=self,
            height=100,
            corner_radius=20,
            fg_color=("white", "gray38"),
        )
        self.frame_upper.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.frame_lower = customtkinter.CTkFrame(corner_radius=10)
        self.frame_lower.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        # =============== upper frame configure ===============

        self.password = customtkinter.CTkLabel(
            master=self.frame_upper,
            text="Uxbghrhighj",
            text_font=Font.mier(),
            text_color="white",
        )  # displaying the password
        self.password.grid(row=0, column=0, padx=50)

        # TODO: fix the position of the copy button
        self.copy_button = customtkinter.CTkButton(
            master=self.frame_upper,
            text="Copy",
            text_font=Font.mier(size=15),
            corner_radius=15,
            command=self.on_copy,
        )
        self.copy_button.grid(row=0, column=1, pady=20, padx=30, sticky="nswe")

        # TODO: create a reload button at r=0, c=2

        # =============== lower frame configure ===============

        self.label_length = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="Password length:",
            text_font=Font.helvetica(),
            text_color="white",
        )
        self.label_length.grid(row=0, column=0, padx=self.PADX, pady=self.PADY)

        # TODO: show interactive strength for different password length
        self.interactive_strength = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="VERY STRONG",
            fg_color="green",
            text_color="white",
            corner_radius=10,
            width=50,
            height=35,
        )
        self.interactive_strength.grid(
            row=0,
            column=2,
            padx=self.PADX,
            pady=self.PADY,
        )

        # shows the password length on screen
        # TODO: reduce the padding in x-direction
        self.length = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="10",
            text_font=Font.helvetica(size=14) + ("bold",),
            width=25,
        )
        self.length.grid(row=0, column=1)

        self.slider = customtkinter.CTkSlider(
            master=self.frame_lower,
            from_=0,
            to=20,
            width=500,
            command=self.slide_event,
        )  # slider to adjust the number of characters
        self.slider.grid(
            row=1, column=0, columnspan=3, padx=self.PADX, pady=self.PADY, sticky="nsew"
        )

        # =============== character options ===============
        # TODO: use objects to reduce code repetition

        self.options_label = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="Characters Used:",
            text_font=Font.helvetica(),
            text_color="white",
        )
        self.options_label.grid(row=2, column=0, padx=self.PADX, pady=self.PADY)

        self.uppercase = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" ABCD ",
            corner_radius=10,
            text_font=("Helvetica", "12"),
            command=self.checkbox_event,
        )
        self.uppercase.grid(row=3, column=0, padx=20, pady=10)

        self.digits = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" 1234 ",
            corner_radius=10,
            text_font=("Helvetica", "12"),
            command=self.checkbox_event,
        )
        self.digits.grid(row=3, column=1, padx=20, pady=10)

        self.punct = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" #$&% ",
            corner_radius=10,
            text_font=("Helvetica", "12"),
            command=self.checkbox_event,
        )
        self.punct.grid(row=3, column=2, padx=20, pady=10)

        # start the password generator
        self.checkbox_event() 

    def on_copy(self):
        pyperclip.copy(self.password.text)

    def get_char_len(self):
        # returns the character length from slider
        return int(self.slider.get())

    def slide_event(self, value):
        self.password.configure(text=random_password(length=self.get_char_len()))
        self.length.configure(text=int(value))
        self.checkbox_event()

    # TODO: save the last options to text file
    def checkbox_event(self):
        self.password.configure(
            text=random_password(
                length=self.get_char_len(),
                lowercase=True,
                uppercase=self.uppercase.get(),
                digits=self.digits.get(),
                punctuation=self.punct.get(),
            )
        )

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
