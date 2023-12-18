
import customtkinter
from PIL import Image
from tkinter import filedialog

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.test_label = None
        self.title("Xử lý ảnh")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Phân lọại giống chó",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_load_img = customtkinter.CTkButton(self.sidebar_frame, command=self.load_image, text="load image")
        self.btn_load_img.grid(row=1, column=0, padx=20, pady=10)
        self.btn_load_model = customtkinter.CTkButton(self.sidebar_frame, text="load model")
        self.btn_load_model.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_o_menu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                          values=["80%", "90%", "100%", "110%", "120%"],
                                                          command=change_scaling_event)
        self.scaling_o_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Output")
        self.entry.grid(row=3, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.scaling_o_menu.set("100%")
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=1, padx=20, pady=20)
        self.forecast_image = customtkinter.CTkLabel(self.frame, text="")
        self.forecast_image.grid(row=0, column=0, sticky="nsew")

    def load_image(self):
        file_path_image = filedialog.askopenfilename()
        pure_image = Image.open(file_path_image)
        w_image = pure_image.width
        h_image = pure_image.height
        image = customtkinter.CTkImage(light_image=pure_image, dark_image=pure_image,size=(w_image, h_image))
        self.forecast_image.configure(image=image)

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
