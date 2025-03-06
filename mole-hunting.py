import tkinter as tk
from tkinter import messagebox as msb
import tki
import time
import random
import threading
import sys

"""Local Photo Path (LP²)
Picture Files   "./assets/images/"
Build No.       "./Visual Studio Code/Files/TXT File/mola-hunting/buildNo.sys"
User Setting    "./Visual Studio Code/Files/TXT File/mola-hunting/userfile.cfg"
"""

class ShootingGame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.system_version_name = "WELCOME"
        self.system_version = "v1.0.0"
        self.system_lastupdated = "2025.03.06"
        self.system_buildNo = 0
        self.system_mola_apper_from = 1500
        self.system_mola_apper_until = 2000
        self.system_mola_wait = 5
        self.system_show_mode = False

        self.lock = False

        self.flag_gameover = False
        self.point = 0
        self.time = 0

        self.get_buildNo()
        self.Start_Up()

        self.system_width = 600
        self.system_height = 620
        self.system_LogNo = 0
        self.system_Log = []



        self.master.geometry(f"{self.system_width}x{self.system_height}")
        self.master.title(f"Mola Hunting - {self.system_version} - Build No.{self.system_buildNo}")
        self.master.protocol("WM_DELETE_WINDOW", self.isWindowClosed)

        self.canvas = tki.create_canvas(f=self.master, w=self.system_width, h=self.system_height, b="#345e27")
        self.master.bind("<Button>", self.KeyEv_btn_press)
        self.master.bind("<ButtonRelease>", self.KeyEv_btn_release)
        self.master.bind("<Motion>", self.KeyEv_motion)
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_clicked = 0

        self.num = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

        self.create_menu()

        self.pic_mola_cd = [
            "./assets/images/hole-2.png",
            "./assets/images/hit-2.png",
            "./assets/images/mole-3.png",
            "./assets/images/hammer.png"
        ]
        self.pic_mola_u = [
            "./assets/images/hole2.png",
            "./assets/images/hit2.png",
            "./assets/images/mole-2.png"
        ]
        self.add_pic()

        self.hammer()

        self.click_place = 0
        self.hit_judge()

        self.master_version = None
        self.master_varriable = None
        self.detail_isDetailOpen=False
        self.master_settings = None

        self.point=0

        self.mola_status=[
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        self.mola_flag = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        self.mola_before_place_1 = [0, 0]
        self.mola_before_place_2 = [0, 0]

        self.replace_pic()
        self.place_mola_parent()



    def get_buildNo(self):
        with open("./assets/sys/buildNo.sys", "r") as f:
            self.system_buildNo = f.readline()
            f.close()
        
        if getattr(sys, 'frozen', False):
            with open("./assets/sys/buildNo.sys", "w") as f:
                f.write(str(int(self.system_buildNo) + 1))
                f.close()

    def Start_Up(self):
        output = [
            f"\n",
            f"Mola Hunting Game",
            f" Author      : Sora",
            f" License     : CC BY-NC-ND 4.0",
            f" Last Update : {self.system_lastupdated}",
            f" VersionName : {self.system_version_name}",
            f" Version     : {self.system_version}",
            f" Build No    : {self.system_buildNo}",
            f"\n"
        ]
        for i in range(len(output)):
            print(output[i])

        self.time = 0
        th1 = threading.Thread(target=self.countup_timer)
        th1.start()

    def countup_timer(self):
        while 1:
            self.time += 1
            time.sleep(1)
            if self.flag_gameover:
                    break

    def point_system(self, status):
        if status == "clear":
            self.point += 100

    def KeyEv_motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

        self.Log(102, f"MOUSE MOVED [x={event.x} y={event.y}]")

    def KeyEv_btn_press(self, event):
        self.mouse_clicked = 1
        self.num2+=1

        self.Log(103, f"MOUSE CLICKED [status={self.mouse_clicked}]")

    def KeyEv_btn_release(self, event):
        self.mouse_clicked = 0
        self.num2=0

        self.Log(104, f"MOUSE RELEASED [status={self.mouse_clicked}]")

    def create_menu(self):
        self.menu = tki.menu(master=self.master)

        self.menu_view = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="View", menu=self.menu_view)
        self.menu_view.add_command(label="version", command=self.subwindow_version)
        self.menu_view.add_command(label="variable", command=self.subwindow_varriable)

        self.menu_settings = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Settings", menu=self.menu_settings)
        self.menu_settings.add_cascade(label="settings", command=self.subwindow_settings)

        self.menu_run = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Run", menu=self.menu_run)
        self.menu_run.add_cascade(label="restart", command=self.restart)

    def restart(self):
        self.canvas.pack_forget()
        self.canvas = tki.create_canvas(f=self.master, w=self.system_width, h=self.system_height, b="#345e27")
        self.canvas.delete("all")
        self.flag_gameover=False
        
        
        self.point = 0
        self.time = 0

        self.Start_Up()

        self.num = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

        self.add_pic()
        self.hammer()

        self.click_place = 0
        self.hit_judge()

        self.mola_status=[
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        self.mola_flag = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        
        self.replace_pic()

        self.mola_before_place_1 = [0, 0]
        self.mola_before_place_2 = [0, 0]

        
        self.place_mola_parent()


    def subwindow_version(self):
        if self.master_version == None or not self.master_version.winfo_exists():
            self.master_version = tk.Toplevel(width=200, height=100)

            self.version_Label1 = tki.label(t_s=15, f=self.master_version, t="VERSION INFORMATION")
            self.version_Label2 = tki.label(t_s=12, f=self.master_version, t=f"{self.system_version_name} : {self.system_version}")
            self.version_Label3 = tki.label(t_s=10, f=self.master_version, t=f"last update : {self.system_lastupdated}")
            self.version_Label4 = tki.label(t_s=10, f=self.master_version, t=f"Build No. : {self.system_buildNo}")

        else:
            msb.showerror("400", "WINDOW WAS EXISTS")

    def subwindow_varriable(self):
        if self.master_varriable == None or not self.master_varriable.winfo_exists():

            self.master_varriable = tk.Toplevel(width=200, height=100)
            self.detail_isDetailOpen = True

            self.detail_Label01 = tki.label(t_s=15, f=self.master_varriable, t=f"DETAIL")
            self.detail_label02 = tki.label(t_s=12, f=self.master_varriable, t=f"System")
            self.detail_label03 = tki.label(t_s=10, f=self.master_varriable, t=f"system_width   : {self.system_width}")
            self.detail_label04 = tki.label(t_s=10, f=self.master_varriable, t=f"system_height  : {self.system_height}")
            self.detail_label05 = tki.label(t_s=10, f=self.master_varriable, t=f"system_LogNo   : {self.system_LogNo}")
            self.detail_label06 = tki.label(t_s=12, f=self.master_varriable, t=f"Normal")
            self.detail_label07 = tki.label(t_s=10, f=self.master_varriable, t=f"mouse_x        : {self.mouse_x}")
            self.detail_label08 = tki.label(t_s=10, f=self.master_varriable, t=f"mouse_y        : {self.mouse_y}")
            self.detail_label09 = tki.label(t_s=10, f=self.master_varriable, t=f"mouse_clicked  : {self.mouse_clicked}")
            self.detail_label10 = tki.label(t_s=10, f=self.master_varriable, t=f"num            : {self.num}")
            self.detail_label11 = tki.label(t_s=10, f=self.master_varriable, t=f"num2           : {self.num2}")
            self.detail_label12 = tki.label(t_s=10, f=self.master_varriable, t=f"num3           : {self.num3}")
            self.detail_label13 = tki.label(t_s=10, f=self.master_varriable, t=f"click_place    : {self.click_place}")
            self.detail_label14 = tki.label(t_s=10, f=self.master_varriable, t=f"point          : {self.point}")
            self.detail_label15 = tki.label(t_s=12, f=self.master_varriable, t=f"Master")
            self.detail_label16 = tki.label(t_s=10, f=self.master_varriable, t=f"master_vrsion : {self.master_version}")
            self.detail_label17 = tki.label(t_s=10, f=self.master_varriable, t=f"master_varriable  : {self.master_varriable}")

            self.values_update()

        else:
            msb.showerror("400", "WINDOW WAS EXISTS")

    def isWindowClosed(self):
        self.master.destroy()
        if self.master_varriable.winfo_exists():
            self.master_varriable.destroy()
        #self.master_version.destroy()

        if self.master_settings.winfo_exists():
            self.master_settings.destroy()

    def values_update(self):
        if self.detail_isDetailOpen:
            self.detail_label03.config(text=f"system_width   : {self.system_width}")
            self.detail_label04.config(text=f"system_height  : {self.system_height}")
            self.detail_label05.config(text=f"system_LogNo   : {self.system_LogNo}")
            self.detail_label07.config(text=f"mouse_x        : {self.mouse_x}")
            self.detail_label08.config(text=f"mouse_y        : {self.mouse_y}")
            self.detail_label09.config(text=f"mouse_clicked  : {self.mouse_clicked}")
            self.detail_label10.config(text=f"num            : {self.num}")
            self.detail_label11.config(text=f"num2           : {self.num2}")
            self.detail_label12.config(text=f"num3           : {self.num3}")
            self.detail_label13.config(text=f"click_place    : {self.click_place}")
            self.detail_label14.config(text=f"point          : {self.point}")
            self.detail_label16.config(text=f"master_version : {self.master_version}")
            self.detail_label17.config(text=f"master_varriable  : {self.master_varriable}")

        self.after(10,self.values_update)

    def subwindow_settings(self):
        if self.master_settings == None or not self.master_settings.winfo_exists():
            self.master_settings = tk.Toplevel(width=400, height=200)

            self.settings_Label1 = tki.label(t_s=13, f=self.master_settings, t="---*SETTINGS*---")
            self.settings_Label2 = tki.label(t_s=12, f=self.master_settings, t="Mola")
            self.settings_Label3 = tki.label(t_s=9, f=self.master_settings, t="Apper Time", anchor=tk.W, width=30, height=3)
            self.settings_Label4 = tki.label(t_s=9, f=self.master_settings, t="FROM", m=1, x=100, y=50)
            self.settings_Label5 = tki.label(t_s=9, f=self.master_settings, t="ms", m=1, x=190, y=50)
            self.settings_Label6 = tki.label(t_s=9, f=self.master_settings, t="UNTIL", m=1, x=100, y=70)
            self.settings_Label7 = tki.label(t_s=9, f=self.master_settings, t="ms", m=1, x=190, y=70)
            self.settings_Label8 = tki.label(t_s=9, f=self.master_settings, t="Wait Time", anchor=tk.W, width=30, height=2)
            self.settings_Label9 = tki.label(t_s=9, f=self.master_settings, t="s", m=1, x=190, y=94)

            
            self.settings_Text1 = tki.new.text(t_s=10, fr=self.master_settings, m=1, x=150, y=50, wid=5, hei=1)
            self.settings_Text2 = tki.new.text(t_s=10, fr=self.master_settings, m=1, x=150, y=70, wid=5, hei=1)
            self.settings_Text3 = tki.new.text(t_s=10, fr=self.master_settings, m=1, x=150, y=94, wid=5, hei=1)

            #FIXME APPLY FOR TKI LIB V1.18
            self.settings_Button1 = tki.button(t_s=12, f=self.master_settings, t="Save", c=lambda:Save(self.settings_Text1.get, self.settings_Text2.get, self.settings_Text3.get))
            
            def Save(Text1, Text2, Text3):
                self.system_mola_apper_from = Text1
                self.system_mola_apper_until = Text2
                self.system_mola_wait = Text3
                
                msb.showinfo("", "Save OK")
                self.master_settings.destroy()


            self.settings_Text1.insert(tk.END, self.system_mola_apper_from)
            self.settings_Text2.insert(tk.END, self.system_mola_apper_until)
            self.settings_Text3.insert(tk.END, self.system_mola_wait)
            
        else:
            msb.showerror("400", "WINDOW WAS EXISTS")

    def add_pic(self):
        self.mola_1 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[0], x=100, y=460, tag="11")
        self.mola_2 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[0], x=300, y=460, tag="12")
        self.mola_3 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[0], x=500, y=460, tag="13")
        self.mola_4 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=100, y=280, tag="21")
        self.mola_5 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=300, y=280, tag="22")
        self.mola_6 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=500, y=280, tag="23")
        self.mola_7 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=100, y=100, tag="31")
        self.mola_8 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=300, y=100, tag="32")
        self.mola_9 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[0], x=500, y=100, tag="33")

    def hammer(self):
        if not self.flag_gameover:
            self.hammer = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[3], x=0, y=0, tag="hammer")
            self.hammer_pos = self.canvas.bbox("hammer")

            self.hammer_x = self.hammer_pos[0] + 90
            self.hammer_y = self.hammer_pos[1] + 75

            self.hammer_move()

    def hammer_move(self):
        if not self.flag_gameover:
            self.canvas.delete("hammer")
            self.hammer = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[3], x=self.mouse_x, y=self.mouse_y, tag="hammer")
            self.master.after(20, self.hammer_move)

    def hit_judge(self):
        """ #FIXME IS IT OK TO USE IT FOR RELEASE VERSION?
        ==========UL==========  ==========UC==========  ==========UR==========
        A(30,50)    B(120,50)   A(230,50)   B(320,50)   A(430,50)   B(520,50)
        |-----------|           |-----------|           |-----------|
        |           |           |           |           |           |
        |           |           |           |           |           |
        |-----------|           |-----------|           |-----------|
        C(30,120)   D(120,120)  C(230,120)  D(320,120)  C(430,120)  D(520,120)

        ==========CL==========  ==========CC==========  ==========CR==========
        A(30,230)   B(120,230)  A(230,230)  B(320,230)  A(430,230)  B(520,230)
        |-----------|           |-----------|           |-----------|
        |           |           |           |           |           |
        |           |           |           |           |           |
        |-----------|           |-----------|           |-----------|
        C(30,300)   D(120,300)  C(230,300)  D(320,300)  C(430,300)  D(520,300)

        ==========DL==========  ==========DC==========  ==========DR==========
        A(30,410)   B(120,410)  A(230,410)  B(320,410)  A(430,410)  B(520,410)
        |-----------|           |-----------|           |-----------|
        |           |           |           |           |           |
        |           |           |           |           |           |
        |-----------|           |-----------|           |-----------|
        C(30,480)   D(120,480)  C(230,480)  D(320,480)  C(430,480)  D(520,480)
        """

        # PROGRAMS
        if self.num3 == 0:
            self.num3+=1
        if self.num2 == 1:
            self.num2+=1

            if self.mouse_clicked == 1:
                if self.mouse_y >= 50 and self.mouse_y <= 120:
                    if self.mouse_x >= 30 and self.mouse_x <= 120:
                        self.click_place = 11

                        self.Log(101, "MOUSE IS ON THE OBJ [UL]")

                    if self.mouse_x >= 230 and self.mouse_x <= 320:
                        self.click_place = 12

                        self.Log(101, "MOUSE IS ON THE OBJ [UC]")

                    if self.mouse_x >= 430 and self.mouse_x <= 520:
                        self.click_place = 13

                        self.Log(101, "MOUSE IS ON THE OBJ [UR]")

                if self.mouse_y >= 230 and self.mouse_y <= 300:
                    if self.mouse_x >= 50 and self.mouse_x <= 120:
                        self.click_place = 21

                        self.Log(101, "MOUSE IS ON THE OBJ [CL]")

                    if self.mouse_x >= 230 and self.mouse_x <= 320:
                        self.click_place = 22

                        self.Log(101, "MOUSE IS ON THE OBJ [CC]")

                    if self.mouse_x >= 430 and self.mouse_x <= 520:
                        self.click_place = 23

                        self.Log(101, "MOUSE IS ON THE OBJ [CR]")

                if self.mouse_y >= 410 and self.mouse_y <= 480:
                    if self.mouse_x >= 50 and self.mouse_x <= 120:
                        self.click_place = 31

                        self.Log(101, "MOUSE IS ON THE OBJ [DR]")

                    if self.mouse_x >= 230 and self.mouse_x <= 320:
                        self.click_place = 32

                        self.Log(101, "MOUSE IS ON THE OBJ [DC]")

                    if self.mouse_x >= 430 and self.mouse_x <= 520:
                        self.click_place = 33

                        self.Log(101, "MOUSE IS ON THE OBJ [DL]")

                self.hit_judge_U()
            else:
                self.click_place = 0

        self.num += 1
        self.canvas.after(100, self.hit_judge)

    def hit_judge_U(self):
        if self.calc_placeNo_1(self.click_place) == 0:
            self.Log(101, "MOUSE IS ON THE OBJ [U]")

        elif self.calc_placeNo_1(self.click_place) == 1:
            self.Log(101, "MOUSE IS ON THE OBJ [C]")

        elif self.calc_placeNo_1(self.click_place) == 2:
            self.Log(101, "MOUSE IS ON THE OBJ [D]")

        th1 = threading.Thread(target=lambda:self.hit_SystemMove(place=self.click_place))
        th1.start()

    def hit_SystemMove(self, place):
        if not self.flag_gameover:
            if self.mola_status[self.calc_placeNo_1(place)][self.calc_placeNo_2(place)] == 2:
                self.Log(200, f"OBJECT DELETE SUCCESS [{place}]")
                th1 = threading.Thread(target=lambda:self.hit_SystemMove_kill(place))
                th1.start()

                self.point_system(status="clear")

                self.replace_pic()

            else:
                self.Log(105, f"OBJECT HAS ALREADY DELETED [{place}]")

    def hit_SystemMove_kill(self, place):
        self.mola_status[self.calc_placeNo_1(place)][self.calc_placeNo_2(place)] = 1
        time.sleep(0.7)
        self.mola_status[self.calc_placeNo_1(place)][self.calc_placeNo_2(place)] = 0

    def Log(self, id, name):
        if not self.flag_gameover:
            self.system_LogNo += 1
            self.system_LogNoLetter = "{:0=5}".format(self.system_LogNo)
            print(f"NO. {self.system_LogNoLetter}       {id} : {name}")

    def calc_placeNo_1(self, place):
        if place == 11 or place == 12 or place == 13:
            return 0

        elif place == 21 or place == 22 or place == 23:
            return 1

        elif place == 31 or place == 32 or place == 33:
            return 2
        
        else:
            return 0

    def calc_placeNo_2(self, place):
        if place == 11 or place == 21 or place == 31:
            return 0

        elif place == 12 or place == 22 or place == 32:
            return 1

        elif place == 13 or place == 23 or place == 33:
            return 2
        else:
            return 0

    def change_mola_status(self, a, t, status, wait):
        time.sleep(wait)
        self.mola_status[a][t] = status
        self.replace_pic()

    def place_mola_parent(self):
        th1 = threading.Thread(target=self.place_mola_main)
        th2 = threading.Thread(target=self.place_mola_main_2)

        th1.start()
        th2.start()

    def place_mola_main(self):
        if not self.flag_gameover:
            mola_place, mola_place2 = self.place_mola_decidemolaplace()
            self.change_mola_status(mola_place, mola_place2, 2, 0)

            th1 = threading.Thread(target=lambda:self.place_mola_thread(mola_place, mola_place2))
            th1.start()

            self.canvas.after(random.randint(self.system_mola_apper_from, self.system_mola_apper_until), self.place_mola_main)

    def place_mola_main_2(self):
        if not self.flag_gameover:
            mola_place, mola_place2 = self.place_mola_decidemolaplace()
            self.change_mola_status(mola_place, mola_place2, 2, 0)

            th1 = threading.Thread(target=lambda:self.place_mola_thread_2(mola_place, mola_place2))
            th1.start()

            self.canvas.after(random.randint(self.system_mola_apper_from, self.system_mola_apper_until), self.place_mola_main_2)

    def place_mola_decidemolaplace(self):
        if not self.flag_gameover:
            while 1:
                random1 = random.randint(0,2)
                random2 = random.randint(0,2)
                print(f"Try: ({random1})({random2})")
                if self.mola_status[random1][random2] == 0 and self.mola_flag[random1][random2] == 0:
                    return random1, random2

    def place_mola_thread(self, mola_place, mola_place2):
        if not self.flag_gameover:
            self.mola_flag[mola_place][mola_place2] = 1

            time.sleep(self.system_mola_wait)
            if not self.mola_status[mola_place][mola_place2] == 2:
                pass
            else:
                self.gameover()

        self.mola_flag[mola_place][mola_place2] = 0
        self.mola_before_place_1 = [mola_place, mola_place2]

    def place_mola_thread_2(self, mola_place, mola_place2):
        if not self.flag_gameover:
            self.mola_flag[mola_place][mola_place2] = 1
            
            time.sleep(self.system_mola_wait)
            if not self.mola_status[mola_place][mola_place2] == 2:
                pass
            else:
                self.gameover()

        self.mola_flag[mola_place][mola_place2] = 0
        self.mola_before_place_2 = [mola_place, mola_place2]

    def gameover(self):
        if self.num4 == 0:
            self.flag_gameover = True
            self.num4 += 1
            if self.system_show_mode:
                msb.showinfo("201", "ゲームオーバーです。")
            else:
                msb.showinfo("201", "ゲームオーバーです。 \n\n GAME WAS ENDED(201)")
            msb.showinfo("結果",f"ゲーム結果 \n\n得点(点) : {self.point}\nクリアタイム(秒) : {self.time}")

    def replace_pic(self, place="all"):
        if place == "all":
            self.canvas.delete("all")

            self.mola_1 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[self.mola_status[0][0]], x=100, y=100, tag="11")
            self.mola_2 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[self.mola_status[0][1]], x=300, y=100, tag="12")
            self.mola_3 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[self.mola_status[0][2]], x=500, y=100, tag="13")

            self.mola_4 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[1][0]], x=100, y=280, tag="21")
            self.mola_5 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[1][1]], x=300, y=280, tag="22")
            self.mola_6 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[1][2]], x=500, y=280, tag="23")

            self.mola_7 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[2][0]], x=100, y=460, tag="31")
            self.mola_8 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[2][1]], x=300, y=460, tag="32")
            self.mola_9 = tki.pic(canvas=self.canvas, Path=self.pic_mola_cd[self.mola_status[2][2]], x=500, y=460, tag="33")

        else:
            if place == 12:
                self.canvas.delete("12")
                self.mola_2 = tki.pic(canvas=self.canvas, Path=self.pic_mola_u[self.mola_status[0][1]], x=300, y=100, tag="12")

        self.canvas.update()

def main():
    root = tk.Tk()
    app = ShootingGame(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()