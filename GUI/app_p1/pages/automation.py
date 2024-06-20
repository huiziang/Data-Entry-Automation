# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import pandas as pd
from tkinter import Canvas, Button, PhotoImage, Frame, BOTH, Toplevel, Label
from idlelib.tooltip import Hovertip
from backend.automationprocess import create_input
from backend.excel_methods import ExcelHandler
from backend.display_methods import hideElement, showElement

excel_handler = ExcelHandler()

class automation:
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, root):

        BASE_PATH = Path(__file__).resolve().parent.parent

        # Define the relative path to the assets directory
        ASSETS_REL_PATH = Path("assets/frame2")

        # Define the absolute path to the assets directory
        self.ASSETS_PATH = BASE_PATH / ASSETS_REL_PATH

        self.window = Frame(root)

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 550,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            62.0,
            fill="#00116B",
            outline="")

        self.canvas.create_text(
            15.0,
            14.0,
            anchor="nw",
            text="Entry Automation",
            fill="#FFFFFF",
            font=("Inter Bold", 28 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            252.0,
            700.0,
            550.0,
            fill="#2A2A2A",
            outline="")

        self.canvas.create_rectangle(
            244.0,
            292.0,
            670.0,
            523.0,
            fill="#363636",
            outline="")

        self.canvas.create_rectangle(
            31.0,
            292.0,
            220.0,
            523.0,
            fill="#363636",
            outline="")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            350.0,
            157.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            190.0,
            113.0,
            510.0,
            213.0,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.automate_btn = Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            command=lambda: create_input(excel_handler.file_path),
            relief="flat"
        )
        self.automate_btn.place(
            x=213.0,
            y=133.0,
            width=195.0,
            height=64.0
        )

        self.automate_tip = Hovertip(self.automate_btn,
                                        'Automates data entry process.\nTo enable this button, input a valid excel file and click on verify\nRun time will take approximately 3 minuites per each run. \nErrors will be displayed apon any blockers or interruptions.', hover_delay=10)

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.settings_btn = Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.settings_btn.place(
            x=425.0,
            y=133.0,
            width=64.0,
            height=64.0
        )

        self.settings_tip = Hovertip(self.settings_btn,
                                     'Customizes Automation Process.\nCurrently unavailable.', hover_delay=10)

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.upload_excel_btn = Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadExcel(),
            relief="flat"
        )
        self.upload_excel_btn.place(
            x=62.0,
            y=449.0,
            width=128.0,
            height=32.0
        )   

        self.upload_excel_tip = Hovertip(self.upload_excel_btn,
                                        'Button to import excel.\nExcel uploaded will not dissapear unless deleted and replaced with another excel.', hover_delay=10)

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            125.0,
            374.0,
            image=self.image_image_2
        )
  

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            457.0,
            313.0,
            image=self.image_image_3
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.prev_sheet_btn = Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: excel_handler.changeSheet(-1, self.canvas, self.label, 255, 350, 400, 155),
            relief="flat"
        )
        self.prev_sheet_btn.place(
            x=362.0,
            y=303.0,
            width=20.0,
            height=20.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.next_sheet_btn = Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: excel_handler.changeSheet(1, self.canvas, self.label, 255, 350, 400, 155),
            relief="flat"
        )
        self.next_sheet_btn.place(
            x=532.0,
            y=303.0,
            width=20.0,
            height=20.0
        )


        self.label = self.canvas.create_text(
            382.0,
            306.0,
            anchor="nw",
            text='',
            fill="#FFFFFF",
            font=("Inter Bold", 12 * -1)
        )




        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            460.0,
            412.0,
            image=self.image_image_4
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.delete_excel_btn = Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.deleteExcel(),
            relief="flat"
        )

        self.delete_excel_tip = Hovertip(self.delete_excel_btn,
                                     'Deletes Current Excel File\nOnly active when the Excel sheet is displayed on the page.\nWill disable the Automate button and verification will reset.', hover_delay=10)

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.verify_btn = Button(
            self.window,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.verifyExcel(),
            relief="flat"
        )
       
        self.verify_tip = Hovertip(self.verify_btn,
                                     'Verifies Excel tables\nButton will turn green on successful verification and enable the Automate button.\nIf verification fails, a message will appear on this page.', hover_delay=10)

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            self.window,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        # self.button_9.place(
        #     x=345.0,
        #     y=422.0,
        #     width=80.0,
        #     height=38.0
        # )

    # Excel Local Functions


    # Page Functions
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def pack(self):
        self.window.pack(fill=BOTH, expand=True)

    def pack_forget(self):
        self.window.pack_forget()

    def deleteExcel(self):
        excel_handler.deleteSheet()
        self.canvas.itemconfig(self.label, text="")
        self.automate_btn["state"] = "disabled"
        hideElement(self.verify_btn)
        hideElement(self.delete_excel_btn)
        showElement(self.upload_excel_btn)
        self.canvas.itemconfig(self.image_2, state="normal")

    def uploadExcel(self):
        excel_handler.uploadExcel()
        if (excel_handler.file_path):
            self.automate_btn["state"] = "normal"
            hideElement(self.upload_excel_btn)
            self.canvas.itemconfig(self.image_2, state='hidden')
            self.verify_btn.place(
                x=85.0,
                y=335.0,
                width=80.0,
                height=38.0
            )
            self.delete_excel_btn.place(
                x=85.0,
                y=435.0,
                width=80.0,
                height=38.0
            )
            excel_handler.loadSheet(self.canvas, self.label, 255, 350, 400, 155)

    def verifyExcel(self):
        err_msg = excel_handler.verifyExcel()
        if err_msg:
            popup = Toplevel()
            popup.resizable(False, False)
            popup.title("Error")
            myFrame = Frame(popup)
            myFrame.pack(fill="both", expand=True)

            # Calculate position for centering popup window relative to main window
            window_position_x = self.canvas.winfo_rootx() + int(self.canvas.winfo_width() / 2 - popup.winfo_reqwidth() / 2 - 100)
            window_position_y = self.canvas.winfo_rooty() + int(self.canvas.winfo_height() / 2 - popup.winfo_reqheight() / 2)
            
            # Set position for centering popup window
            popup.geometry("+{}+{}".format(window_position_x, window_position_y))
            
            label = Label(popup, text=err_msg)
            label.pack(pady=20, padx=20)
        
            close_button = Button(popup, text="Close", command=popup.destroy)
            close_button.pack(pady=10)