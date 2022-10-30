import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):

    WIDTH = 550
    HEIGHT = 400

    def __init__(self):
        super().__init__()

        def event(value=10):
            self.length = customtkinter.CTkLabel(
                master=self.frame_lower,
                text=str(int(value)),
                text_font=("Helvetica", 14, "bold"),
                width=25,
            )
            self.length.grid(row=0, column=1)

        self.title("WolframVault")
        # self.resizable('false', 'false')
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

        self.frame_upper.grid_columnconfigure(5, minsize=10)

        self.password = customtkinter.CTkLabel(
            master=self.frame_upper,
            text="Uxbghrhighj",
            text_font=("MierB03", "20"),
            text_color="white",
        )  # displaying the password
        self.password.grid(row=0, column=0, padx=50)

        self.button = customtkinter.CTkButton(
            master=self.frame_upper,
            text="Copy",
            command=None,
            text_font=("MierB03", "15"),
            corner_radius=15,
        )
        self.button.grid(row=0, column=1, pady=20, padx=30)

        # =============== lower frame configure ===============

        self.label_length = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="Password length:",
            text_font=("Helvetica", "15"),
            text_color="white",
        )
        self.label_length.grid(row=0, column=0, padx=20, pady=20)

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
            padx=20,
            pady=20,
        )

        event()
        self.slider = customtkinter.CTkSlider(
            master=self.frame_lower,
            from_=0,
            to=20,
            width=500,
            command=event,
        )  # slider to adjust the number of characters
        self.slider.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

        # =============== character options ===============

        self.used = customtkinter.CTkLabel(
            master=self.frame_lower,
            text="Characters Used:",
            text_font=("Helvetica", "15"),
            text_color="white",
        )
        self.used.grid(row=2, column=0, padx=20, pady=20)

        self.capital = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" ABCD ",
            onvalue="on",
            offvalue="off",
            corner_radius=10,
            text_font=("Helvetica", "12"),
        )
        self.capital.grid(row=3, column=0, padx=20, pady=10)

        self.numbers = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" 1234 ",
            onvalue="on",
            offvalue="off",
            corner_radius=10,
            text_font=("Helvetica", "12"),
        )
        self.numbers.grid(row=3, column=1, padx=20, pady=10)

        self.punct = customtkinter.CTkCheckBox(
            master=self.frame_lower,
            text=" #$&% ",
            onvalue="on",
            offvalue=" off ",
            corner_radius=10,
            text_font=("Helvetica", "12"),
        )
        self.punct.grid(row=3, column=2, padx=20, pady=10)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
