import os
try:
    import time
except:
    os.system("cmd/kpip install time")
try:
    import mysql.connector as ms
except:
    os.system("cmd/kpip install mysql-connector-python")
try:
    import customtkinter
except:
    os.system("cmd/kpip install customtkinter")
try:
    from PIL import Image
except:
    os.system("cmd/kpip install Pillow")
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import Image
customtkinter.set_appearance_mode("dark")
import mysql.connector as ms
try:
    file=open("user_pass.txt","r")
except:
    user_=input("Enter your MySql user name:")
    passw=input("Enter your MySql password:")
    while True:
        try:
            db= ms.connect(host="localhost",user=user_,passwd=passw)
            file=open("user_pass.txt","w")
            file.write(user_+"\n"+passw)
            file.close()
            break
        except:
            print("Wrong username or password")
            user_=input("Enter your MySql user name:")
            passw=input("Enter your MySql password:")
file=open("user_pass.txt","r")
file_str=file.read()
file_list=file_str.split("\n")
sql_user=file_list[0]
sql_pass=file_list[1]
file.close()
db= ms.connect(host="localhost",user=sql_user,passwd=sql_pass)
mycursor=db.cursor()
mycursor.execute("show databases")
database_name=mycursor.fetchall()
main_database_name=("ticketbuddy",)
if main_database_name not in database_name:
    mycursor.execute("create database ticketbuddy")
    db= ms.connect(host="localhost",user=sql_user,passwd=sql_pass,database="ticketbuddy")
    mycursor=db.cursor()
    mycursor.execute("create table user_details(username varchar(100) primary key,phone_number varchar(10) not null unique,password varchar(30) not null)")
    mycursor.execute("create table user_seats(movie_name varchar(50),seat_name varchar(100),movie_date varchar(30),movie_timings varchar(30),user_name varchar(100))")
db= ms.connect(host="localhost",user=sql_user,passwd=sql_pass,database="ticketbuddy")
mycursor=db.cursor()
mainwindow = customtkinter.CTk()
mainwindow.geometry("600x600")
mainwindow.title("TICKETBUDDY")
mainwindow.configure(background="black")
def main_screen():
    global frame
    frame=customtkinter.CTkFrame(mainwindow,height=600,width=600)
    frame.pack()
    main_frame=customtkinter.CTkScrollableFrame(frame,label_text="Select a film to book the tickets",fg_color="white",height=500,width=500)
    main_frame.pack()
    pt_sir_photo=customtkinter.CTkImage(light_image=Image.open("pt-sir.png"),size=(200,200))
    pt_sir_button=customtkinter.CTkButton(main_frame,text="PT SIR",image=pt_sir_photo,compound="top",command=pt_sir)
    pt_sir_button.pack(pady=10)
    aranmanai_4_photo=customtkinter.CTkImage(light_image=Image.open("aranmanai-4.png"),size=(200,200))
    aranmanai_4_button=customtkinter.CTkButton(main_frame,text="ARANMANAI 4",image=aranmanai_4_photo,compound="top",command=aranmanai_4)
    aranmanai_4_button.pack(pady=10)
    garudan_photo=customtkinter.CTkImage(light_image=Image.open("garudan.png"),size=(200,200))
    garudan_button=customtkinter.CTkButton(main_frame,text="GARUDAN",image=garudan_photo,compound="top",command=garudan)
    garudan_button.pack(pady=10)
    the_akaali_photo=customtkinter.CTkImage(light_image=Image.open("the-akaali.png"),size=(200,200))
    the_akaali_button=customtkinter.CTkButton(main_frame,text="THE AKAALI",image=the_akaali_photo,compound="top",command=the_akaali)
    the_akaali_button.pack(pady=10)
    furiosa_photo=customtkinter.CTkImage(light_image=Image.open("furiosa.png"),size=(200,200))
    furiosa_button=customtkinter.CTkButton(main_frame,text="FURIOSA",image=furiosa_photo,compound="top",command=furiosa)
    furiosa_button.pack(pady=10)
    deadpool_and_wolverine_photo=customtkinter.CTkImage(light_image=Image.open("deadpool-and-wolverine.png"),size=(200,200))
    deadpool_and_wolverine_button=customtkinter.CTkButton(main_frame,text="DEADPOOL AND WOLVERINE",image=deadpool_and_wolverine_photo,compound="top",command=deadpool_and_wolverine)
    deadpool_and_wolverine_button.pack(pady=10)
    star_photo=customtkinter.CTkImage(light_image=Image.open("star.png"),size=(200,200))
    star_button=customtkinter.CTkButton(main_frame,text="STAR",image=star_photo,compound="top",command=star)
    star_button.pack(pady=10)
    profile_pic_photo=customtkinter.CTkImage(light_image=Image.open("pfp.png"))
    profile_button=customtkinter.CTkButton(frame,compound="top",text="PROFILE",image=profile_pic_photo,command=profile_pic)
    profile_button.pack(pady=40)
'''------------------------------------------------PROFILE STARTING-------------------------------------------------------------------------------------'''  
def profile_pic():
    global profile_pic_frame
    global edit_profile_button
    global ticket_details_button
    global go_back_ms_button
    frame.destroy()
    profile_pic_frame=customtkinter.CTkFrame(mainwindow,width=150)
    profile_pic_frame.pack()
    edit_profile_button=customtkinter.CTkButton(profile_pic_frame,text="Edit profile",font=("calibri",18,"bold"),corner_radius=50,command=edit_profile)
    edit_profile_button.pack(side=TOP and LEFT,padx=20)
    ticket_details_button=customtkinter.CTkButton(profile_pic_frame,text="Ticket deatails",font=("calibri",18,"bold"),corner_radius=50,command=ticket_details)
    ticket_details_button.pack(padx=20)
    go_back_ms_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=go_back_ms,corner_radius=50)
    go_back_ms_button.pack(pady=20,side="bottom")
def go_back_ms():
    try:
        user_details_frame.destroy()
    except:
        pass
    chumma_frame.destroy()
    profile_pic_frame.destroy()
    go_back_ms_button.destroy()
    main_screen()

'''------------------------------------------------------EDIT PROFILE STARTING----------------------------------------------------------------------------------------------------------------------'''

def edit_profile():
    global user_details_frame
    global data_user
    edit_profile_button.configure(state=DISABLED)
    ticket_details_button.configure(state=ACTIVE)
    try:
        chumma_frame.destroy()
    except:
        pass
    q="select * from user_details where username='{}'".format(c)
    mycursor.execute(q)
    data_user=mycursor.fetchone()
    user_details_frame=customtkinter.CTkFrame(mainwindow,fg_color="white")
    user_details_frame.pack(pady=50,anchor=S)
    label=customtkinter.CTkLabel(user_details_frame,text="DO YOU WANT TO:",font=("calibri",20,"bold"),text_color="black")
    label.pack(padx=55,pady=10)
    edit_username_button=customtkinter.CTkButton(user_details_frame,text="Edit User Name",corner_radius=50,command=username)
    edit_username_button.pack(pady=10)
    edit_mobile_button=customtkinter.CTkButton(user_details_frame,text="Edit Mobile Number",corner_radius=50,command=mobileno)
    edit_mobile_button.pack(pady=10)
    edit_password_button=customtkinter.CTkButton(user_details_frame,text="Edit Password",corner_radius=50,command=password)
    edit_password_button.pack(pady=10)

def password():
    global change_password_frame
    global new_password_entry
    global old_password_entry
    global password_confirm_button
    user_details_frame.destroy()
    profile_pic_frame.destroy()
    go_back_ms_button.destroy()
    change_password_frame=customtkinter.CTkFrame(mainwindow)
    change_password_frame.pack()
    new_password_entry=customtkinter.CTkEntry(change_password_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="New Password",placeholder_text_color="black",text_color="black",width=205)
    new_password_entry.pack(pady=20,padx=60)
    old_password_entry=customtkinter.CTkEntry(change_password_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Current password",placeholder_text_color="black",text_color="black",width=205)
    old_password_entry.pack(pady=20,padx=60)
    password_go_back_ud_button=customtkinter.CTkButton(change_password_frame,text="Go Back",corner_radius=50,command=password_go_back_ud)
    password_go_back_ud_button.pack(padx=10,side=LEFT)
    password_confirm_button=customtkinter.CTkButton(change_password_frame,text="Confirm",corner_radius=50,command=password_confirm)
    password_confirm_button.pack(padx=10,side=RIGHT)
def password_go_back_ud():
    change_password_frame.destroy()
    profile_pic()
def password_confirm():
    q="select * from user_details where username='{}'".format(c)
    mycursor.execute(q)
    data_user_password=mycursor.fetchone()
    new_password=new_password_entry.get()
    old_password=old_password_entry.get()
    if new_password==data_user_password[2] or new_password=="":
        if new_password==data_user_password[2]:
            change_notok_messagebox=messagebox.showerror("","NEW PASSWORD CAN'T BE YOUR OLD PASSWORD!!")
        elif new_password=="":
            change_notok_messagebox=messagebox.showerror("","NEW PASSWORD CAN'T BE EMPTY!!")
    elif old_password!=data_user_password[2] or old_password=="":
        if old_password=="":
            change_notok_messagebox=messagebox.showerror("","OLD PASSWORD CAN'T BE EMPTY!!")
        elif old_password!=data_user_password[2]:
            change_notok_messagebox=messagebox.showerror("","OLD PASSWORD DOESN'T MATCH!!")
    else:
        change_ok_messagebox=messagebox.askquestion("","ARE SURE YOU WANT TO CHANGE YOUR PASSWORD?")
        if change_ok_messagebox=="yes":
            give_info_messagebox=messagebox.showinfo("","PASSWORD CHANGED SUCCESSFULLY")
            q="update user_details set password='{}' where username='{}'".format(new_password,data_user[0])
            mycursor.execute(q)
            db.commit()

def username():
    global change_username_frame
    global new_username_entry
    global username_password_entry
    global username_confirm_button
    user_details_frame.destroy()
    profile_pic_frame.destroy()
    go_back_ms_button.destroy()
    change_username_frame=customtkinter.CTkFrame(mainwindow)
    change_username_frame.pack()
    new_username_entry=customtkinter.CTkEntry(change_username_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="New Username",placeholder_text_color="black",text_color="black",width=205)
    new_username_entry.pack(pady=20,padx=60)
    username_password_entry=customtkinter.CTkEntry(change_username_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Current password",placeholder_text_color="black",text_color="black",width=205)
    username_password_entry.pack(pady=20,padx=60)
    username_go_back_ud_button=customtkinter.CTkButton(change_username_frame,text="Go Back",corner_radius=50,command=username_go_back_ud)
    username_go_back_ud_button.pack(padx=10,side=LEFT)
    username_confirm_button=customtkinter.CTkButton(change_username_frame,text="Confirm",corner_radius=50,command=username_confirm)
    username_confirm_button.pack(padx=10,side=RIGHT)
def username_go_back_ud():
    change_username_frame.destroy()
    profile_pic()
def username_confirm():
    new_username=new_username_entry.get()
    username_password=username_password_entry.get()
    mycursor.execute("select username from user_details")
    usernames_tuple=mycursor.fetchall()
    if new_username==data_user[0] or new_username=="":
        if new_username==data_user[0]:
            change_notok_messagebox=messagebox.showerror("","NEW USERNAME CAN'T BE YOUR OLD USERNAME!!")
        elif new_username=="":
            change_notok_messagebox=messagebox.showerror("","NEW USERNAME CAN'T BE EMPTY!!")
    elif username_password!=data_user[2] or username_password=="":
        if username_password!=data_user[2]:
            change_notok_messagebox=messagebox.showerror("","PASSWORD DOESN'T MATCH!!")
        elif username_password=="":
            change_notok_messagebox=messagebox.showerror("","PASSWORD CAN'T BE EMPTY!!")
    elif (new_username,) in usernames_tuple:
        change_notok_messagebox=messagebox.showerror("","USERNAME ALREADY EXIST!!")
    else:
        change_ok_messagebox=messagebox.askquestion("","ARE SURE YOU WANT TO CHANGE YOUR USERNAME?")
        if change_ok_messagebox=="yes":
            give_info_messagebox=messagebox.showinfo("","USERNAME CHANGED SUCCESSFULLY")
            q="update user_details set username='{}' where username='{}'".format(new_username,data_user[0])
            mycursor.execute(q)
            db.commit()

def mobileno():
    global change_mobileno_frame
    global new_mobileno_entry
    global current_mobileno_entry
    global mobileno_password_entry
    global mobileno_confirm_button
    user_details_frame.destroy()
    profile_pic_frame.destroy()
    go_back_ms_button.destroy()
    change_mobileno_frame=customtkinter.CTkFrame(mainwindow)
    change_mobileno_frame.pack()
    current_mobileno_entry=customtkinter.CTkEntry(change_mobileno_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Current Phone Number",placeholder_text_color="black",text_color="black",width=205)
    current_mobileno_entry.pack(pady=20,padx=60)
    new_mobileno_entry=customtkinter.CTkEntry(change_mobileno_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="New Phone Number",placeholder_text_color="black",text_color="black",width=205)
    new_mobileno_entry.pack(pady=20,padx=60)
    mobileno_password_entry=customtkinter.CTkEntry(change_mobileno_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Current password",placeholder_text_color="black",text_color="black",width=205)
    mobileno_password_entry.pack(pady=20,padx=60)
    mobileno_go_back_ud_button=customtkinter.CTkButton(change_mobileno_frame,text="Go Back",corner_radius=50,command=mobileno_go_back_ud)
    mobileno_go_back_ud_button.pack(padx=10,side=LEFT)
    mobileno_confirm_button=customtkinter.CTkButton(change_mobileno_frame,text="Confirm",corner_radius=50,command=mobileno_confirm)
    mobileno_confirm_button.pack(padx=10,side=RIGHT)
def mobileno_go_back_ud():
    change_mobileno_frame.destroy()
    profile_pic()
def mobileno_confirm():
    new_mobileno=new_mobileno_entry.get()
    current_mobileno=current_mobileno_entry.get()
    mobileno_password=mobileno_password_entry.get()
    mycursor.execute("select phone_number from user_details")
    phonenumbers_tuple=mycursor.fetchall()
    try:
        if current_mobileno!=data_user[1] or current_mobileno=="":
            if current_mobileno!=data_user[1]:
                change_notok_messagebox=messagebox.showerror("","WRONG CURRENT NUMBER!!")
            elif current_mobileno=="":
                change_notok_messagebox=messagebox.showerror("","NEW NUMBER CAN'T BE EMPTY!!")
        elif new_mobileno==data_user[1] or new_mobileno=="":
            if new_mobileno==data_user[1]:
                change_notok_messagebox=messagebox.showerror("","NEW NUMBER CAN'T BE YOUR OLD NUMBER!!")
            elif new_mobileno=="":
                change_notok_messagebox=messagebox.showerror("","NEW NUMBER CAN'T BE EMPTY!!")
        elif len(new_mobileno)!=10:
            change_notok_messagebox=messagebox.showerror("","INVAILD NEW NUMBER!!")
        elif mobileno_password!=data_user[2] or mobileno_password=="":
            if mobileno_password!=data_user[2]:
                change_notok_messagebox=messagebox.showerror("","PASSWORD DOESN'T MATCH!!")
            elif mobileno_password=="":
                change_notok_messagebox=messagebox.showerror("","PASSWORD CAN'T BE EMPTY!!")
        elif (new_mobileno,) in phonenumbers_tuple:
            change_notok_messagebox=messagebox.showerror("","PHONE NUMBER ALREADY EXIST!!")
        else:
            change_ok_messagebox=messagebox.askquestion("","ARE SURE YOU WANT TO CHANGE YOUR NUMBER?")
            if change_ok_messagebox=="yes":
                give_info_messagebox=messagebox.showinfo("","MOBILE NUMBER CHANGED SUCCESSFULLY")
                q="update user_details set phone_number='{}' where phone_number='{}'".format(new_mobileno,data_user[1])
                mycursor.execute(q)
                db.commit()
        int(float(new_mobileno))
    except ValueError:
        change_notok_messagebox=messagebox.showerror("","NUMBER CAN'T CONTAIN LETTERS!!")        
    
'''--------------------------------------------------EDIT PROFILE ENDING----------------------------------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------TICKET STARTING--------------------------------------------------------------------------------------------------------------------------'''
def ticket_details():
    global ticket_details_frame
    global chumma_frame
    try:
        user_details_frame.destroy()
    except:
        pass
    edit_profile_button.configure(state=ACTIVE)
    ticket_details_button.configure(state=DISABLED)
    chumma_frame=customtkinter.CTkFrame(mainwindow)
    chumma_frame.pack(pady=40)
    ticket_details_frame=customtkinter.CTkScrollableFrame(chumma_frame,height=500,width=1000)
    ticket_details_frame.pack()
    search_label=customtkinter.CTkLabel(ticket_details_frame,text="SEARCH BY:",font=("calibri",20,"bold"))
    search_label.pack(pady=10,padx=20)
    options_list=["All","Date","Time"]
    search_menu=customtkinter.CTkOptionMenu(ticket_details_frame,values=options_list,font=("calibri",20,"bold"),command=search_option)
    search_menu.pack(pady=10,padx=20)
def search_option(choice):
    global movie_date_entry
    global time_movie_entry
    if choice=="All":
        all_confirm()
    elif choice=="Date":
        try:
            all_title_label.destroy()
            for i in all_delete_list:
                i[0].destroy()
                i[1].destroy()
        except:
            pass
        movie_date_entry=customtkinter.CTkEntry(ticket_details_frame,placeholder_text="DATE TO BE SEARCHED")
        movie_date_entry.pack(padx=20,pady=10)
        date_confirm_button=customtkinter.CTkButton(ticket_details_frame,text="Confirm",command=date_confirm)
        date_confirm_button.pack(pady=10,padx=20)
    elif choice=="Time":
        global time_movie_entry
        try:
            all_title_label.destroy()
            for i in all_delete_list:
                i[0].destroy()
                i[1].destroy()
        except:
            pass
        time_movie_entry=customtkinter.CTkEntry(ticket_details_frame,placeholder_text="TIME TO BE SEARCHED")
        time_movie_entry.pack(padx=20,pady=10)
        time_confirm_button=customtkinter.CTkButton(ticket_details_frame,text="Confirm",command=time_confirm)
        time_confirm_button.pack(pady=10,padx=20)


def all_confirm():
    global all_delete_ticket_button
    global all_title_label
    global all_user_ticket_details_label
    global all_user_tickets
    global all_delete_list
    all_delete_list=[]
    try:
        date_title_label.destroy()
        date_user_ticket_details_label.destroy()
        date_delete_ticket_button.destroy()
    except:
        pass
    all_title_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\tMOVIE NAME\t|\tSEATS BOOKED\t|\tDATE\t|\tTIME\t|",font=("calibri",20,"bold"))
    all_title_label.pack(pady=10,padx=20)
    mycursor.execute("select * from user_seats where user_name='{}'".format(c))
    all_user_tickets=mycursor.fetchall()
    for i in range(len(all_user_tickets)):
        all_user_ticket_details_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\t"+all_user_tickets[i][0]+"|\t"+all_user_tickets[i][1]+"\t|\t" +all_user_tickets[i][2]+"\t|\t"+all_user_tickets[i][3]+"\t|\t",font=("calibri",20,"bold"))
        all_user_ticket_details_label.pack(pady=10,padx=20)
        all_delete_ticket_button=customtkinter.CTkButton(ticket_details_frame,text="Delete Ticket",command=lambda index=i:all_delete(index))
        all_delete_ticket_button.pack(pady=10,padx=20)
        all_delete_list.append([all_user_ticket_details_label,all_delete_ticket_button])


def date_confirm():
    global date_title_label
    global date_user_ticket_details_label
    global date_delete_ticket_button
    global date_delete_list
    date_delete_list=[]
    try:
        all_delete_ticket_button.destroy()
        all_title_label.destroy()
        all_user_ticket_details_label.destroy()
    except:
        pass
    date_title_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\tMOVIE NAME\t|\tSEATS BOOKED\t|\tDATE\t|\tTIME\t|",font=("calibri",20,"bold"))
    date_title_label.pack(pady=10,padx=20)
    mycursor.execute("select * from user_seats where user_name='{}' and movie_date='{}'".format(c,movie_date_entry.get()))
    date_user_tickets=mycursor.fetchall()
    print(date_user_tickets)
    if date_user_tickets!=[]:
        for i in range(len(date_user_tickets)):
            date_user_ticket_details_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\t"+date_user_tickets[i][0]+"|\t"+date_user_tickets[i][1]+"\t|\t" +date_user_tickets[i][2]+"\t|\t"+date_user_tickets[i][3]+"\t|\t",font=("calibri",20,"bold"))
            date_user_ticket_details_label.pack(pady=10,padx=20)
            date_delete_ticket_button=customtkinter.CTkButton(ticket_details_frame,text="Delete Ticket",command=lambda index=i:date_delete(index))
            date_delete_ticket_button.pack(pady=10,padx=20)
            date_delete_list.append([date_user_ticket_details_label,date_delete_ticket_button])
    else:
        date_not_found_label=customtkinter.CTkLabel(ticket_details_frame,text="NO MOVIES WERE FOUND!!",font=("calibri",30,"bold"))
        date_not_found_label.pack(pady=10,padx=20)

def time_confirm():
    global time_title_label
    global time_user_ticket_details_label
    global time_delete_ticket_button
    global time_delete_list
    time_delete_list=[]
    try:
        all_delete_ticket_button.destroy()
        all_title_label.destroy()
        all_user_ticket_details_label.destroy()
    except:
        pass
    time_title_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\tMOVIE NAME\t|\tSEATS BOOKED\t|\tDATE\t|\tTIME\t|",font=("calibri",20,"bold"))
    time_title_label.pack(pady=10,padx=20)
    mycursor.execute("select * from user_seats where user_name='{}' and movie_timings='{}'".format(c,time_movie_entry.get()))
    time_user_tickets=mycursor.fetchall()
    if time_user_tickets!=[]:
        for i in range(len(time_user_tickets)):
            time_user_ticket_details_label=customtkinter.CTkLabel(ticket_details_frame,text=" |\t"+time_user_tickets[i][0]+"|\t"+time_user_tickets[i][1]+"\t|\t" +time_user_tickets[i][2]+"\t|\t"+time_user_tickets[i][3]+"\t|\t",font=("calibri",20,"bold"))
            time_user_ticket_details_label.pack(pady=10,padx=20)
            time_delete_ticket_button=customtkinter.CTkButton(ticket_details_frame,text="Delete Ticket",command=lambda index=i:time_delete(index))
            time_delete_ticket_button.pack(pady=10,padx=20)
            time_delete_list.append([time_user_ticket_details_label,time_delete_ticket_button])
    else:
        time_not_found_label=customtkinter.CTkLabel(ticket_details_frame,text="NO MOVIES WERE FOUND!!",font=("calibri",30,"bold"))
        time_not_found_label.pack(pady=10,padx=20)

def all_delete(index):
    delete_messagebox=messagebox.askquestion("","ARE YOU SURE YOU WANT TO DELETE YOUR TICKECT!!")
    if delete_messagebox=="yes":
        info=all_delete_list[index][0].cget("text")
        info=info.split("|")
        movie_name=info[1].strip()
        seat_booked=info[2].strip()
        movie_date=info[3].strip()
        movie_time=info[4].strip()
        q="delete from user_seats where movie_name='{}' and seat_name='{}' and movie_date='{}' and movie_timings='{}' and user_name='{}'".format(movie_name,seat_booked,movie_date,movie_time,c)
        mycursor.execute(q)
        db.commit()
        done_messagebox=messagebox.showinfo("","TICKET DELTED SUCCESSFULLY!!")
        all_delete_list[index][0].destroy()
        all_delete_list[index][1].destroy()

def date_delete(index):
    delete_messagebox=messagebox.askquestion("","ARE YOU SURE YOU WANT TO DELETE YOUR TICKECT!!")
    if delete_messagebox=="yes":
        info=date_delete_list[index][0].cget("text")
        info=info.split("|")
        movie_name=info[1].strip()
        seat_booked=info[2].strip()
        movie_date=info[3].strip()
        movie_time=info[4].strip()
        q="delete from user_seats where movie_name='{}' and seat_name='{}' and movie_date='{}' and movie_timings='{}' and user_name='{}'".format(movie_name,seat_booked,movie_date,movie_time,c)
        mycursor.execute(q)
        db.commit()
        done_messagebox=messagebox.showinfo("","TICKET DELTED SUCCESSFULLY!!")
        date_delete_list[index][0].destroy()
        date_delete_list[index][1].destroy()

def time_delete(index):
    delete_messagebox=messagebox.askquestion("","ARE YOU SURE YOU WANT TO DELETE YOUR TICKECT!!")
    if delete_messagebox=="yes":
        info=time_delete_list[index][0].cget("text")
        info=info.split("|")
        movie_name=info[1].strip()
        seat_booked=info[2].strip()
        movie_date=info[3].strip()
        movie_time=info[4].strip()
        q="delete from user_seats where movie_name='{}' and seat_name='{}' and movie_date='{}' and movie_timings='{}' and user_name='{}'".format(movie_name,seat_booked,movie_date,movie_time,c)
        mycursor.execute(q)
        db.commit()
        done_messagebox=messagebox.showinfo("","TICKET DELTED SUCCESSFULLY!!")
        time_delete_list[index][0].destroy()
        time_delete_list[index][1].destroy()

'''---------------------------------------------------TICKET ENDING------------------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------PROFILE ENDING---------------------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------PT SIR STARTING---------------------------------------------------------------------------------------------------------------------'''
def pt_sir_pay():
    pt_sir_pay_button.configure(state=DISABLED)
    ins_name="pt sir"
    ins_seat=""
    for i in pt_sir_selected_seats:
        if pt_sir_selected_seats.index(i)==len(pt_sir_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=pt_sir_date
    ins_timings=pt_sir_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    pt_sir_payment_label=customtkinter.CTkLabel(pt_sir_details_frame,text="Your payment is successful\nReturning to movie selection page\nPlease wait for few seconds",font=("calibri",20,"bold"))
    pt_sir_payment_label.pack()
    main_screen()
    pt_sir_details_frame.destroy()
    time.sleep(4)
def pt_sir_confirm():
    pt_sir_seat_frame.destroy()
    pt_sir_button_frame.destroy()
    global pt_sir_details_frame
    global pt_sir_pay_button
    pt_sir_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    pt_sir_details_frame.pack()
    details_label=customtkinter.CTkLabel(pt_sir_details_frame,text="PT SIR"+"\n"+"Tickets booked: "+str(pt_sir_selected_seats)+"\nnumber of tickets: "+str(len(pt_sir_selected_seats))+"\n\n"+pt_sir_tim+"     |     "+pt_sir_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    pt_sir_price=customtkinter.CTkLabel(pt_sir_details_frame,text="170 * "+str(len(pt_sir_selected_seats))+" : "+str(170*len(pt_sir_selected_seats)))
    pt_sir_price.pack()
    pt_sir_pay_button=customtkinter.CTkButton(pt_sir_details_frame,text="Pay now",command=pt_sir_pay)
    pt_sir_pay_button.pack()
def pt_sir_go_back_st():
    pt_sir_seat_frame.destroy()
    pt_sir_button_frame.destroy()
    pt_sir_book_tickets()
def pt_sir_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = pt_sir_seat_buttons[row][col]
    if seat_id in pt_sir_selected_seats:
        pt_sir_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        pt_sir_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(pt_sir_selected_seats)==0:
        pt_sir_confirm_button.configure(state=DISABLED)
    else:
        pt_sir_confirm_button.configure(state=ACTIVE)
def maris_timing(tim):
    pt_sir_booking_frame.destroy()
    pt_sir_go_back_bt_button.destroy()
    global pt_sir_seat_buttons
    global pt_sir_selected_seats
    global pt_sir_seat_frame
    global pt_sir_go_back_st_button
    global pt_sir_seat_button
    global pt_sir_button_frame
    global pt_sir_confirm_button
    global pt_sir_tim
    pt_sir_tim=tim
    pt_sir_seat_buttons=[]
    pt_sir_selected_seats=[]
    pt_sir_seat_frame=customtkinter.CTkFrame(mainwindow)
    pt_sir_seat_frame.pack()
    pt_sir_button_frame=customtkinter.CTkFrame(mainwindow)
    pt_sir_button_frame.pack(pady=10)
    no_of_row=5
    no_of_column=10
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            pt_sir_seat_button=customtkinter.CTkButton(pt_sir_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: pt_sir_seat(row, col))
            pt_sir_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(pt_sir_seat_button)
        pt_sir_seat_buttons.append(button_row)
    pt_sir_confirm_button=customtkinter.CTkButton(pt_sir_button_frame,text="Confirm Booking",command=pt_sir_confirm,state=DISABLED)
    pt_sir_confirm_button.pack(side=LEFT,padx=10)
    pt_sir_go_back_st_button=customtkinter.CTkButton(pt_sir_button_frame,text="Go Back",command=pt_sir_go_back_st)
    pt_sir_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='pt sir' and  movie_date='{}' and movie_timings='{}'".format(pt_sir_date,pt_sir_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    pt_sir_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    pt_sir_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def pt_sir_go_back_bt():
    pt_sir_booking_frame.destroy()
    pt_sir_go_back_bt_button.destroy()
    pt_sir()
def pt_sir_change_date(v):
    pt_sir_theater_frame.destroy()
    pt_sir_theater(v)
def pt_sir_theater(v):
    global pt_sir_theater_frame
    global pt_sir_maris_timing_button
    global pt_sir_date
    pt_sir_date=v
    pt_sir_theater_frame=customtkinter.CTkFrame(pt_sir_booking_frame,height=50,width=50)
    pt_sir_theater_frame.pack(pady=10)
    pt_sir_theater_01_label=customtkinter.CTkLabel(pt_sir_theater_frame,text="LA MARIS:TRICHY",font=("calibri",18,"bold"))
    pt_sir_theater_01_label.grid(column=1,row=1)
    pt_sir_timing_list=["11:00 am","2:30 pm","6:00 pm"]
    for i in range(len(pt_sir_timing_list)):
        pt_sir_maris_timing_button=customtkinter.CTkButton(pt_sir_theater_frame,text=pt_sir_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=pt_sir_timing_list[i]: maris_timing(tim))
        pt_sir_maris_timing_button.grid(column=i,row=3,pady=10,padx=5)
    pt_sir_date_button.configure(command=pt_sir_change_date)
def pt_sir_book_tickets():
    pt_sir_frame.destroy()
    global pt_sir_booking_frame
    global pt_sir_date_button
    global pt_sir_go_back_bt_button
    pt_sir_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    pt_sir_booking_frame.pack()
    pt_sir_select_label=customtkinter.CTkLabel(pt_sir_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    pt_sir_select_label.pack()
    pt_sir_date_button=customtkinter.CTkSegmentedButton(pt_sir_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=pt_sir_theater)
    pt_sir_date_button.pack(pady=20)
    pt_sir_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=pt_sir_go_back_bt)
    pt_sir_go_back_bt_button.pack(pady=20)
def pt_sir_go_back_ms():
     pt_sir_frame.destroy()
     main_screen() 
def pt_sir():
    global pt_sir_language_label
    frame.destroy()
    global pt_sir_frame
    pt_sir_frame=customtkinter.CTkFrame(mainwindow)
    pt_sir_frame.pack()
    pt_sir_photo=customtkinter.CTkImage(light_image=Image.open("pt-sir.png"),size=(400,200))
    pt_sir_label=customtkinter.CTkLabel(pt_sir_frame,image=pt_sir_photo,compound="top",text="")
    pt_sir_label.pack(pady=10)
    pt_sir_rating_label=customtkinter.CTkLabel(pt_sir_frame,text="8.9/10",width=40)
    pt_sir_rating_label.pack()
    pt_sir_language_label=customtkinter.CTkLabel(pt_sir_frame,text="Tamil",font=("bold",15))
    pt_sir_language_label.pack(pady=10)
    pt_sir_other_details_label=customtkinter.CTkLabel(pt_sir_frame,text="02:10:00 Hrs . comedy,drama . U . 2024-05-24",font=("bold",15))
    pt_sir_other_details_label.pack(pady=10)
    pt_sir_description_label=customtkinter.CTkLabel(pt_sir_frame,text="Pt sir is a movie starring Hiphop Thamizha,Kashmira Pardeshi,Anika Surendran and Munishkanth\nin prominent roles.It is directed by Karthik Venugopalan",font=("bold",15))
    pt_sir_description_label.pack(pady=10)
    pt_sir_book_ticket_button=customtkinter.CTkButton(pt_sir_frame,text="Book Tickects",command=pt_sir_book_tickets)
    pt_sir_book_ticket_button.pack(pady=10)
    pt_sir_go_back_ms_button=customtkinter.CTkButton(pt_sir_frame,text="Go Back",command=pt_sir_go_back_ms)
    pt_sir_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------PT SIR ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''--------------------------------------------------ARANMANAI 4 STARTING---------------------------------------------------------------------------------------------------------------------'''
def aranmanai_4_pay():
    aranmanai_4_pay_button.configure(state=DISABLED)
    ins_name="aranmanai 4"
    ins_seat=""
    for i in aranmanai_4_selected_seats:
        if aranmanai_4_selected_seats.index(i)==len(aranmanai_4_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=aranmanai_4_date
    ins_timings=aranmanai_4_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    aranmanai_4_payment_label=customtkinter.CTkLabel(aranmanai_4_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    aranmanai_4_payment_label.pack()
    main_screen()
    aranmanai_4_details_frame.destroy()
    time.sleep(4)
def aranmanai_4_confirm():
    aranmanai_4_seat_frame.destroy()
    aranmanai_4_button_frame.destroy()
    global aranmanai_4_details_frame
    global aranmanai_4_pay_button
    aranmanai_4_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    aranmanai_4_details_frame.pack()
    details_label=customtkinter.CTkLabel(aranmanai_4_details_frame,text="ARANMANAI 4"+"\n"+"Tickets booked: "+str(aranmanai_4_selected_seats)+"\nnumber of tickets: "+str(len(aranmanai_4_selected_seats))+"\n\n"+aranmanai_4_tim+"     |     "+aranmanai_4_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    aranmanai_4_price=customtkinter.CTkLabel(aranmanai_4_details_frame,text="170 * "+str(len(aranmanai_4_selected_seats))+" : "+str(170*len(aranmanai_4_selected_seats)))
    aranmanai_4_price.pack()
    aranmanai_4_pay_button=customtkinter.CTkButton(aranmanai_4_details_frame,text="Pay now",command=aranmanai_4_pay)
    aranmanai_4_pay_button.pack()
def aranmanai_4_go_back_st():
    aranmanai_4_seat_frame.destroy()
    aranmanai_4_button_frame.destroy()
    aranmanai_4_book_tickets()
def aranmanai_4_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = aranmanai_4_seat_buttons[row][col]
    if seat_id in aranmanai_4_selected_seats:
        aranmanai_4_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        aranmanai_4_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(aranmanai_4_selected_seats)==0:
        aranmanai_4_confirm_button.configure(state=DISABLED)
    else:
        aranmanai_4_confirm_button.configure(state=ACTIVE)
def sona_mina_timing(tim):
    aranmanai_4_booking_frame.destroy()
    aranmanai_4_go_back_bt_button.destroy()
    global aranmanai_4_seat_buttons
    global aranmanai_4_selected_seats
    global aranmanai_4_seat_frame
    global aranmanai_4_go_back_st_button
    global aranmanai_4_seat_button
    global aranmanai_4_button_frame
    global aranmanai_4_confirm_button
    global aranmanai_4_tim
    aranmanai_4_tim=tim
    aranmanai_4_seat_buttons=[]
    aranmanai_4_selected_seats=[]
    aranmanai_4_seat_frame=customtkinter.CTkFrame(mainwindow)
    aranmanai_4_seat_frame.pack()
    aranmanai_4_button_frame=customtkinter.CTkFrame(mainwindow)
    aranmanai_4_button_frame.pack(pady=10)
    no_of_row=6
    no_of_column=10
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            aranmanai_4_seat_button=customtkinter.CTkButton(aranmanai_4_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: aranmanai_4_seat(row, col))
            aranmanai_4_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(aranmanai_4_seat_button)
        aranmanai_4_seat_buttons.append(button_row)
    aranmanai_4_confirm_button=customtkinter.CTkButton(aranmanai_4_button_frame,text="Confirm Booking",command=aranmanai_4_confirm,state=DISABLED)
    aranmanai_4_confirm_button.pack(side=LEFT,padx=10)
    aranmanai_4_go_back_st_button=customtkinter.CTkButton(aranmanai_4_button_frame,text="Go Back",command=aranmanai_4_go_back_st)
    aranmanai_4_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='aranmanai 4' and  movie_date='{}' and movie_timings='{}'".format(aranmanai_4_date,aranmanai_4_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    aranmanai_4_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    aranmanai_4_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def aranmanai_4_go_back_bt():
    aranmanai_4_booking_frame.destroy()
    aranmanai_4_go_back_bt_button.destroy()
    aranmanai_4()
def aranmanai_4_change_date(v):
    aranmanai_4_theater_frame.destroy()
    aranmanai_4_theater(v)
def aranmanai_4_theater(v):
    global aranmanai_4_theater_frame
    global aranmanai_4_sona_mina_timing_button
    global aranmanai_4_date
    aranmanai_4_date=v
    aranmanai_4_theater_frame=customtkinter.CTkFrame(aranmanai_4_booking_frame,height=50,width=50)
    aranmanai_4_theater_frame.pack(pady=10)
    aranmanai_4_theater_01_label=customtkinter.CTkLabel(aranmanai_4_theater_frame,text="LA SONA MINA:TRICHY",font=("calibri",18,"bold"))
    aranmanai_4_theater_01_label.grid(column=1,row=1)
    aranmanai_4_timing_list=["11:30 am","3:30 pm","7:00 pm"]
    for i in range(len(aranmanai_4_timing_list)):
        aranmanai_4_sona_mina_timing_button=customtkinter.CTkButton(aranmanai_4_theater_frame,text=aranmanai_4_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=aranmanai_4_timing_list[i]: sona_mina_timing(tim))
        aranmanai_4_sona_mina_timing_button.grid(column=i,row=3,pady=10,padx=5)
    aranmanai_4_date_button.configure(command=aranmanai_4_change_date)
def aranmanai_4_book_tickets():
    aranmanai_4_frame.destroy()
    global aranmanai_4_booking_frame
    global aranmanai_4_date_button
    global aranmanai_4_go_back_bt_button
    aranmanai_4_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    aranmanai_4_booking_frame.pack()
    aranmanai_4_select_label=customtkinter.CTkLabel(aranmanai_4_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    aranmanai_4_select_label.pack()
    aranmanai_4_date_button=customtkinter.CTkSegmentedButton(aranmanai_4_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=aranmanai_4_theater)
    aranmanai_4_date_button.pack(pady=20)
    aranmanai_4_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=aranmanai_4_go_back_bt)
    aranmanai_4_go_back_bt_button.pack(pady=20)
def aranmanai_4_go_back_ms():
     aranmanai_4_frame.destroy()
     main_screen() 
def aranmanai_4():
    global aranmanai_4_language_label
    frame.destroy()
    global aranmanai_4_frame
    aranmanai_4_frame=customtkinter.CTkFrame(mainwindow)
    aranmanai_4_frame.pack()
    aranmanai_4_photo=customtkinter.CTkImage(light_image=Image.open("aranmanai-4.png"),size=(200,200))
    aranmanai_4_label=customtkinter.CTkLabel(aranmanai_4_frame,image=aranmanai_4_photo,compound="top",text="")
    aranmanai_4_label.pack(pady=10)
    aranmanai_4_rating_label=customtkinter.CTkLabel(aranmanai_4_frame,text="7.7/10",width=40)
    aranmanai_4_rating_label.pack()
    aranmanai_4_language_label=customtkinter.CTkLabel(aranmanai_4_frame,text="Tamil",font=("bold",15))
    aranmanai_4_language_label.pack(pady=10)
    aranmanai_4_other_details_label=customtkinter.CTkLabel(aranmanai_4_frame,text="02:28:00 Hrs . comedy,horror . U . 2024-05-3",font=("bold",15))
    aranmanai_4_other_details_label.pack(pady=10)
    aranmanai_4_description_label=customtkinter.CTkLabel(aranmanai_4_frame,text="Aranmanai 4 is a movie starring Sundar C,Tamannah Bhatia,Raashi Khanna,Yogi Babu\nin prominent roles.It is directed by Sundar C",font=("bold",15))
    aranmanai_4_description_label.pack(pady=10)
    aranmanai_4_book_ticket_button=customtkinter.CTkButton(aranmanai_4_frame,text="Book Tickects",command=aranmanai_4_book_tickets)
    aranmanai_4_book_ticket_button.pack(pady=10)
    aranmanai_4_go_back_ms_button=customtkinter.CTkButton(aranmanai_4_frame,text="Go Back",command=aranmanai_4_go_back_ms)
    aranmanai_4_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------ARANMANAI 4 ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------GARUDAN STARTING---------------------------------------------------------------------------------------------------------------------'''
def garudan_pay():
    garudan_pay_button.configure(state=DISABLED)
    ins_name="garudan"
    ins_seat=""
    for i in garudan_selected_seats:
        if garudan_selected_seats.index(i)==len(garudan_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=garudan_date
    ins_timings=garudan_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    garudan_payment_label=customtkinter.CTkLabel(garudan_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    garudan_payment_label.pack()
    main_screen()
    garudan_details_frame.destroy()
    time.sleep(4)
def garudan_confirm():
    garudan_seat_frame.destroy()
    garudan_button_frame.destroy()
    global garudan_details_frame
    global garudan_pay_button
    garudan_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    garudan_details_frame.pack()
    details_label=customtkinter.CTkLabel(garudan_details_frame,text="GARUDAN"+"\n"+"Tickets booked: "+str(garudan_selected_seats)+"\nnumber of tickets: "+str(len(garudan_selected_seats))+"\n\n"+garudan_tim+"     |     "+garudan_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    garudan_price=customtkinter.CTkLabel(garudan_details_frame,text="190 * "+str(len(garudan_selected_seats))+" : "+str(190*len(garudan_selected_seats)))
    garudan_price.pack()
    garudan_pay_button=customtkinter.CTkButton(garudan_details_frame,text="Pay now",command=garudan_pay)
    garudan_pay_button.pack()
def garudan_go_back_st():
    garudan_seat_frame.destroy()
    garudan_button_frame.destroy()
    garudan_book_tickets()
def garudan_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = garudan_seat_buttons[row][col]
    if seat_id in garudan_selected_seats:
        garudan_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        garudan_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(garudan_selected_seats)==0:
        garudan_confirm_button.configure(state=DISABLED)
    else:
        garudan_confirm_button.configure(state=ACTIVE)
def ramba_timing(tim):
    garudan_booking_frame.destroy()
    garudan_go_back_bt_button.destroy()
    global garudan_seat_buttons
    global garudan_selected_seats
    global garudan_seat_frame
    global garudan_go_back_st_button
    global garudan_seat_button
    global garudan_button_frame
    global garudan_confirm_button
    global garudan_tim
    garudan_tim=tim
    garudan_seat_buttons=[]
    garudan_selected_seats=[]
    garudan_seat_frame=customtkinter.CTkFrame(mainwindow)
    garudan_seat_frame.pack()
    garudan_button_frame=customtkinter.CTkFrame(mainwindow)
    garudan_button_frame.pack(pady=10)
    no_of_row=5
    no_of_column=10
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            garudan_seat_button=customtkinter.CTkButton(garudan_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: garudan_seat(row, col))
            garudan_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(garudan_seat_button)
        garudan_seat_buttons.append(button_row)
    garudan_confirm_button=customtkinter.CTkButton(garudan_button_frame,text="Confirm Booking",command=garudan_confirm,state=DISABLED)
    garudan_confirm_button.pack(side=LEFT,padx=10)
    garudan_go_back_st_button=customtkinter.CTkButton(garudan_button_frame,text="Go Back",command=garudan_go_back_st)
    garudan_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='garudan' and  movie_date='{}' and movie_timings='{}'".format(garudan_date,garudan_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    garudan_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    garudan_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def garudan_go_back_bt():
    garudan_booking_frame.destroy()
    garudan_go_back_bt_button.destroy()
    garudan()
def garudan_change_date(v):
    garudan_theater_frame.destroy()
    garudan_theater(v)
def garudan_theater(v):
    global garudan_theater_frame
    global garudan_ramba_timing_button
    global garudan_date
    garudan_date=v
    garudan_theater_frame=customtkinter.CTkFrame(garudan_booking_frame,height=50,width=50)
    garudan_theater_frame.pack(pady=10)
    garudan_theater_01_label=customtkinter.CTkLabel(garudan_theater_frame,text="RAMBA:TRICHY",font=("calibri",18,"bold"))
    garudan_theater_01_label.grid(column=1,row=1)
    garudan_timing_list=["10:45 am","1:30 pm","4:55 pm"]
    for i in range(len(garudan_timing_list)):
        garudan_ramba_timing_button=customtkinter.CTkButton(garudan_theater_frame,text=garudan_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=garudan_timing_list[i]: ramba_timing(tim))
        garudan_ramba_timing_button.grid(column=i,row=3,pady=10,padx=5)
    garudan_date_button.configure(command=garudan_change_date)
def garudan_book_tickets():
    garudan_frame.destroy()
    global garudan_booking_frame
    global garudan_date_button
    global garudan_go_back_bt_button
    garudan_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    garudan_booking_frame.pack()
    garudan_select_label=customtkinter.CTkLabel(garudan_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    garudan_select_label.pack()
    garudan_date_button=customtkinter.CTkSegmentedButton(garudan_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=garudan_theater)
    garudan_date_button.pack(pady=20)
    garudan_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=garudan_go_back_bt)
    garudan_go_back_bt_button.pack(pady=20)
def garudan_go_back_ms():
     garudan_frame.destroy()
     main_screen() 
def garudan():
    global garudan_language_label
    frame.destroy()
    global garudan_frame
    garudan_frame=customtkinter.CTkFrame(mainwindow)
    garudan_frame.pack()
    garudan_photo=customtkinter.CTkImage(light_image=Image.open("garudan.png"),size=(400,200))
    garudan_label=customtkinter.CTkLabel(garudan_frame,image=garudan_photo,compound="top",text="")
    garudan_label.pack(pady=10)
    garudan_rating_label=customtkinter.CTkLabel(garudan_frame,text="9/10",width=40)
    garudan_rating_label.pack()
    garudan_language_label=customtkinter.CTkLabel(garudan_frame,text="Tamil",font=("bold",15))
    garudan_language_label.pack(pady=10)
    garudan_other_details_label=customtkinter.CTkLabel(garudan_frame,text="02:14:00 Hrs . action,drama . U . 2024-05-24",font=("bold",15))
    garudan_other_details_label.pack(pady=10)
    garudan_description_label=customtkinter.CTkLabel(garudan_frame,text="Garudan is a movie starring Soori,M.Sasikumar,Unni Mukundan,Samuthirakani\nin prominent roles.It is directed by R.S.Durai Senthilkumar",font=("bold",15))
    garudan_description_label.pack(pady=10)
    garudan_book_ticket_button=customtkinter.CTkButton(garudan_frame,text="Book Tickects",command=garudan_book_tickets)
    garudan_book_ticket_button.pack(pady=10)
    garudan_go_back_ms_button=customtkinter.CTkButton(garudan_frame,text="Go Back",command=garudan_go_back_ms)
    garudan_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------GARUDAN ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''--------------------------------------------------THE AKAALI STARTING---------------------------------------------------------------------------------------------------------------------'''
def the_akaali_pay():
    the_akaali_pay_button.configure(state=DISABLED)
    ins_name="the akaali"
    ins_seat=""
    for i in the_akaali_selected_seats:
        if the_akaali_selected_seats.index(i)==len(the_akaali_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=the_akaali_date
    ins_timings=the_akaali_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    the_akaali_payment_label=customtkinter.CTkLabel(the_akaali_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    the_akaali_payment_label.pack()
    main_screen()
    the_akaali_details_frame.destroy()
    time.sleep(4)
def the_akaali_confirm():
    the_akaali_seat_frame.destroy()
    the_akaali_button_frame.destroy()
    global the_akaali_details_frame
    global the_akaali_pay_button
    the_akaali_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    the_akaali_details_frame.pack()
    details_label=customtkinter.CTkLabel(the_akaali_details_frame,text="THE AKAALI"+"\n"+"Tickets booked: "+str(the_akaali_selected_seats)+"\nnumber of tickets: "+str(len(the_akaali_selected_seats))+"\n\n"+the_akaali_tim+"     |     "+the_akaali_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    the_akaali_price=customtkinter.CTkLabel(the_akaali_details_frame,text="170 * "+str(len(the_akaali_selected_seats))+" : "+str(170*len(the_akaali_selected_seats)))
    the_akaali_price.pack()
    the_akaali_pay_button=customtkinter.CTkButton(the_akaali_details_frame,text="Pay now",command=the_akaali_pay)
    the_akaali_pay_button.pack()
def the_akaali_go_back_st():
    the_akaali_seat_frame.destroy()
    the_akaali_button_frame.destroy()
    the_akaali_book_tickets()
def the_akaali_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = the_akaali_seat_buttons[row][col]
    if seat_id in the_akaali_selected_seats:
        the_akaali_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        the_akaali_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(the_akaali_selected_seats)==0:
        the_akaali_confirm_button.configure(state=DISABLED)
    else:
        the_akaali_confirm_button.configure(state=ACTIVE)
def venkateshwara_timing(tim):
    the_akaali_booking_frame.destroy()
    the_akaali_go_back_bt_button.destroy()
    global the_akaali_seat_buttons
    global the_akaali_selected_seats
    global the_akaali_seat_frame
    global the_akaali_go_back_st_button
    global the_akaali_seat_button
    global the_akaali_button_frame
    global the_akaali_confirm_button
    global the_akaali_tim
    the_akaali_tim=tim
    the_akaali_seat_buttons=[]
    the_akaali_selected_seats=[]
    the_akaali_seat_frame=customtkinter.CTkFrame(mainwindow)
    the_akaali_seat_frame.pack()
    the_akaali_button_frame=customtkinter.CTkFrame(mainwindow)
    the_akaali_button_frame.pack(pady=10)
    no_of_row=5
    no_of_column=8
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            the_akaali_seat_button=customtkinter.CTkButton(the_akaali_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: the_akaali_seat(row, col))
            the_akaali_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(the_akaali_seat_button)
        the_akaali_seat_buttons.append(button_row)
    the_akaali_confirm_button=customtkinter.CTkButton(the_akaali_button_frame,text="Confirm Booking",command=the_akaali_confirm,state=DISABLED)
    the_akaali_confirm_button.pack(side=LEFT,padx=10)
    the_akaali_go_back_st_button=customtkinter.CTkButton(the_akaali_button_frame,text="Go Back",command=the_akaali_go_back_st)
    the_akaali_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='the akaali' and  movie_date='{}' and movie_timings='{}'".format(the_akaali_date,the_akaali_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    the_akaali_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    the_akaali_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def the_akaali_go_back_bt():
    the_akaali_booking_frame.destroy()
    the_akaali_go_back_bt_button.destroy()
    the_akaali()
def the_akaali_change_date(v):
    the_akaali_theater_frame.destroy()
    the_akaali_theater(v)
def the_akaali_theater(v):
    global the_akaali_theater_frame
    global the_akaali_venkateshwara_timing_button
    global the_akaali_date
    the_akaali_date=v
    the_akaali_theater_frame=customtkinter.CTkFrame(the_akaali_booking_frame,height=50,width=50)
    the_akaali_theater_frame.pack(pady=10)
    the_akaali_theater_01_label=customtkinter.CTkLabel(the_akaali_theater_frame,text="VENKATESHWARA:TRICHY",font=("calibri",18,"bold"))
    the_akaali_theater_01_label.grid(column=1,row=1)
    the_akaali_timing_list=["11:00 am","2:30 pm","6:00 pm"]
    for i in range(len(the_akaali_timing_list)):
        the_akaali_venkateshwara_timing_button=customtkinter.CTkButton(the_akaali_theater_frame,text=the_akaali_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=the_akaali_timing_list[i]: venkateshwara_timing(tim))
        the_akaali_venkateshwara_timing_button.grid(column=i,row=3,pady=10,padx=5)
    the_akaali_date_button.configure(command=the_akaali_change_date)
def the_akaali_book_tickets():
    the_akaali_frame.destroy()
    global the_akaali_booking_frame
    global the_akaali_date_button
    global the_akaali_go_back_bt_button
    the_akaali_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    the_akaali_booking_frame.pack()
    the_akaali_select_label=customtkinter.CTkLabel(the_akaali_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    the_akaali_select_label.pack()
    the_akaali_date_button=customtkinter.CTkSegmentedButton(the_akaali_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=the_akaali_theater)
    the_akaali_date_button.pack(pady=20)
    the_akaali_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=the_akaali_go_back_bt)
    the_akaali_go_back_bt_button.pack(pady=20)
def the_akaali_go_back_ms():
     the_akaali_frame.destroy()
     main_screen() 
def the_akaali():
    global the_akaali_language_label
    frame.destroy()
    global the_akaali_frame
    the_akaali_frame=customtkinter.CTkFrame(mainwindow)
    the_akaali_frame.pack()
    the_akaali_photo=customtkinter.CTkImage(light_image=Image.open("the-akaali.png"),size=(400,200))
    the_akaali_label=customtkinter.CTkLabel(the_akaali_frame,image=the_akaali_photo,compound="top",text="")
    the_akaali_label.pack(pady=10)
    the_akaali_rating_label=customtkinter.CTkLabel(the_akaali_frame,text="7.5/10",width=40)
    the_akaali_rating_label.pack()
    the_akaali_language_label=customtkinter.CTkLabel(the_akaali_frame,text="Tamil",font=("bold",15))
    the_akaali_language_label.pack(pady=10)
    the_akaali_other_details_label=customtkinter.CTkLabel(the_akaali_frame,text="02:25:00 Hrs . crime,thriller . A . 2024-05-24",font=("bold",15))
    the_akaali_other_details_label.pack(pady=10)
    the_akaali_description_label=customtkinter.CTkLabel(the_akaali_frame,text="The akaali is a movie starring Nassar,Thalaivasal Vijay,Jayakumar,Vinoth Kishan\nin prominent roles.It is directed by Mohamed Asif Hameed",font=("bold",15))
    the_akaali_description_label.pack(pady=10)
    the_akaali_book_ticket_button=customtkinter.CTkButton(the_akaali_frame,text="Book Tickects",command=the_akaali_book_tickets)
    the_akaali_book_ticket_button.pack(pady=10)
    the_akaali_go_back_ms_button=customtkinter.CTkButton(the_akaali_frame,text="Go Back",command=the_akaali_go_back_ms)
    the_akaali_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------THE AKAALI ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------FURIOSA STARTING---------------------------------------------------------------------------------------------------------------------'''
def furiosa_pay():
    furiosa_pay_button.configure(state=DISABLED)
    ins_name="furiosa"
    ins_seat=""
    for i in furiosa_selected_seats:
        if furiosa_selected_seats.index(i)==len(furiosa_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=furiosa_date
    ins_timings=furiosa_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    furiosa_payment_label=customtkinter.CTkLabel(furiosa_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    furiosa_payment_label.pack()
    main_screen()
    furiosa_details_frame.destroy()
    time.sleep(4)
def furiosa_confirm():
    furiosa_seat_frame.destroy()
    furiosa_button_frame.destroy()
    global furiosa_details_frame
    global furiosa_pay_button
    furiosa_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    furiosa_details_frame.pack()
    details_label=customtkinter.CTkLabel(furiosa_details_frame,text="FURIOSA"+"\n"+"Tickets booked: "+str(furiosa_selected_seats)+"\nnumber of tickets: "+str(len(furiosa_selected_seats))+"\n\n"+furiosa_tim+"     |     "+furiosa_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    furiosa_price=customtkinter.CTkLabel(furiosa_details_frame,text="200 * "+str(len(furiosa_selected_seats))+" : "+str(200*len(furiosa_selected_seats)))
    furiosa_price.pack()
    furiosa_pay_button=customtkinter.CTkButton(furiosa_details_frame,text="Pay now",command=furiosa_pay)
    furiosa_pay_button.pack()
def furiosa_go_back_st():
    furiosa_seat_frame.destroy()
    furiosa_button_frame.destroy()
    furiosa_book_tickets()
def furiosa_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = furiosa_seat_buttons[row][col]
    if seat_id in furiosa_selected_seats:
        furiosa_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        furiosa_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(furiosa_selected_seats)==0:
        furiosa_confirm_button.configure(state=DISABLED)
    else:
        furiosa_confirm_button.configure(state=ACTIVE)
def vijay_timing(tim):
    furiosa_booking_frame.destroy()
    furiosa_go_back_bt_button.destroy()
    global furiosa_seat_buttons
    global furiosa_selected_seats
    global furiosa_seat_frame
    global furiosa_go_back_st_button
    global furiosa_seat_button
    global furiosa_button_frame
    global furiosa_confirm_button
    global furiosa_tim
    furiosa_tim=tim
    furiosa_seat_buttons=[]
    furiosa_selected_seats=[]
    furiosa_seat_frame=customtkinter.CTkFrame(mainwindow)
    furiosa_seat_frame.pack()
    furiosa_button_frame=customtkinter.CTkFrame(mainwindow)
    furiosa_button_frame.pack(pady=10)
    no_of_row=6
    no_of_column=8
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            furiosa_seat_button=customtkinter.CTkButton(furiosa_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: furiosa_seat(row, col))
            furiosa_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(furiosa_seat_button)
        furiosa_seat_buttons.append(button_row)
    furiosa_confirm_button=customtkinter.CTkButton(furiosa_button_frame,text="Confirm Booking",command=furiosa_confirm,state=DISABLED)
    furiosa_confirm_button.pack(side=LEFT,padx=10)
    furiosa_go_back_st_button=customtkinter.CTkButton(furiosa_button_frame,text="Go Back",command=furiosa_go_back_st)
    furiosa_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='furiosa' and  movie_date='{}' and movie_timings='{}'".format(furiosa_date,furiosa_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    furiosa_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    furiosa_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def furiosa_go_back_bt():
    furiosa_booking_frame.destroy()
    furiosa_go_back_bt_button.destroy()
    furiosa()
def furiosa_change_date(v):
    furiosa_theater_frame.destroy()
    furiosa_theater(v)
def furiosa_theater(v):
    global furiosa_theater_frame
    global furiosa_vijay_timing_button
    global furiosa_date
    furiosa_date=v
    furiosa_theater_frame=customtkinter.CTkFrame(furiosa_booking_frame,height=50,width=50)
    furiosa_theater_frame.pack(pady=10)
    furiosa_theater_01_label=customtkinter.CTkLabel(furiosa_theater_frame,text="VIJAY CINEMAS:TRICHY",font=("calibri",18,"bold"))
    furiosa_theater_01_label.grid(column=1,row=1)
    furiosa_timing_list=["8:00 am","12:30 pm","4:00 pm"]
    for i in range(len(furiosa_timing_list)):
        furiosa_vijay_timing_button=customtkinter.CTkButton(furiosa_theater_frame,text=furiosa_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=furiosa_timing_list[i]: vijay_timing(tim))
        furiosa_vijay_timing_button.grid(column=i,row=3,pady=10,padx=5)
    furiosa_date_button.configure(command=furiosa_change_date)
def furiosa_book_tickets():
    furiosa_frame.destroy()
    global furiosa_booking_frame
    global furiosa_date_button
    global furiosa_go_back_bt_button
    furiosa_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    furiosa_booking_frame.pack()
    furiosa_select_label=customtkinter.CTkLabel(furiosa_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    furiosa_select_label.pack()
    furiosa_date_button=customtkinter.CTkSegmentedButton(furiosa_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=furiosa_theater)
    furiosa_date_button.pack(pady=20)
    furiosa_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=furiosa_go_back_bt)
    furiosa_go_back_bt_button.pack(pady=20)
def furiosa_go_back_ms():
     furiosa_frame.destroy()
     main_screen() 
def furiosa():
    global furiosa_language_label
    frame.destroy()
    global furiosa_frame
    furiosa_frame=customtkinter.CTkFrame(mainwindow)
    furiosa_frame.pack()
    furiosa_photo=customtkinter.CTkImage(light_image=Image.open("furiosa.png"),size=(400,200))
    furiosa_label=customtkinter.CTkLabel(furiosa_frame,image=furiosa_photo,compound="top",text="")
    furiosa_label.pack(pady=10)
    furiosa_rating_label=customtkinter.CTkLabel(furiosa_frame,text="7.5/10",width=40)
    furiosa_rating_label.pack()
    furiosa_language_label=customtkinter.CTkLabel(furiosa_frame,text="English",font=("bold",15))
    furiosa_language_label.pack(pady=10)
    furiosa_other_details_label=customtkinter.CTkLabel(furiosa_frame,text="02:28:00 Hrs . action,sci-fi,thriller . A . 2024-05-23",font=("bold",15))
    furiosa_other_details_label.pack(pady=10)
    furiosa_description_label=customtkinter.CTkLabel(furiosa_frame,text="Pt sir is a movie starring Anya Taylor-Joy,Chris Hemsworth,Tom Bruke,Alyla Browne\nin prominent roles.It is directed by George Miller",font=("bold",15))
    furiosa_description_label.pack(pady=10)
    furiosa_book_ticket_button=customtkinter.CTkButton(furiosa_frame,text="Book Tickects",command=furiosa_book_tickets)
    furiosa_book_ticket_button.pack(pady=10)
    furiosa_go_back_ms_button=customtkinter.CTkButton(furiosa_frame,text="Go Back",command=furiosa_go_back_ms)
    furiosa_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------FURIOSA ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------DEADPOOL AND WOLVERINE STARTING---------------------------------------------------------------------------------------------------------------------'''
def deadpool_and_wolverine_pay():
    deadpool_and_wolverine_pay_button.configure(state=DISABLED)
    ins_name="deadpool and wolverine"
    ins_seat=""
    for i in deadpool_and_wolverine_selected_seats:
        if deadpool_and_wolverine_selected_seats.index(i)==len(deadpool_and_wolverine_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=deadpool_and_wolverine_date
    ins_timings=deadpool_and_wolverine_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    deadpool_and_wolverine_payment_label=customtkinter.CTkLabel(deadpool_and_wolverine_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    deadpool_and_wolverine_payment_label.pack()
    main_screen()
    deadpool_and_wolverine_details_frame.destroy()
    time.sleep(4)
def deadpool_and_wolverine_confirm():
    deadpool_and_wolverine_seat_frame.destroy()
    deadpool_and_wolverine_button_frame.destroy()
    global deadpool_and_wolverine_details_frame
    global deadpool_and_wolverine_pay_button
    deadpool_and_wolverine_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    deadpool_and_wolverine_details_frame.pack()
    details_label=customtkinter.CTkLabel(deadpool_and_wolverine_details_frame,text="DEADPOOL AND WOLVERINE"+"\n"+"Tickets booked: "+str(deadpool_and_wolverine_selected_seats)+"\nnumber of tickets: "+str(len(deadpool_and_wolverine_selected_seats))+"\n\n"+deadpool_and_wolverine_tim+"     |     "+deadpool_and_wolverine_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    deadpool_and_wolverine_price=customtkinter.CTkLabel(deadpool_and_wolverine_details_frame,text="210 * "+str(len(deadpool_and_wolverine_selected_seats))+" : "+str(210*len(deadpool_and_wolverine_selected_seats)))
    deadpool_and_wolverine_price.pack()
    deadpool_and_wolverine_pay_button=customtkinter.CTkButton(deadpool_and_wolverine_details_frame,text="Pay now",command=deadpool_and_wolverine_pay)
    deadpool_and_wolverine_pay_button.pack()
def deadpool_and_wolverine_go_back_st():
    deadpool_and_wolverine_seat_frame.destroy()
    deadpool_and_wolverine_button_frame.destroy()
    deadpool_and_wolverine_book_tickets()
def deadpool_and_wolverine_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = deadpool_and_wolverine_seat_buttons[row][col]
    if seat_id in deadpool_and_wolverine_selected_seats:
        deadpool_and_wolverine_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        deadpool_and_wolverine_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(deadpool_and_wolverine_selected_seats)==0:
        deadpool_and_wolverine_confirm_button.configure(state=DISABLED)
    else:
        deadpool_and_wolverine_confirm_button.configure(state=ACTIVE)
def megastar_timing(tim):
    deadpool_and_wolverine_booking_frame.destroy()
    deadpool_and_wolverine_go_back_bt_button.destroy()
    global deadpool_and_wolverine_seat_buttons
    global deadpool_and_wolverine_selected_seats
    global deadpool_and_wolverine_seat_frame
    global deadpool_and_wolverine_go_back_st_button
    global deadpool_and_wolverine_seat_button
    global deadpool_and_wolverine_button_frame
    global deadpool_and_wolverine_confirm_button
    global deadpool_and_wolverine_tim
    deadpool_and_wolverine_tim=tim
    deadpool_and_wolverine_seat_buttons=[]
    deadpool_and_wolverine_selected_seats=[]
    deadpool_and_wolverine_seat_frame=customtkinter.CTkFrame(mainwindow)
    deadpool_and_wolverine_seat_frame.pack()
    deadpool_and_wolverine_button_frame=customtkinter.CTkFrame(mainwindow)
    deadpool_and_wolverine_button_frame.pack(pady=10)
    no_of_row=7
    no_of_column=10
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            deadpool_and_wolverine_seat_button=customtkinter.CTkButton(deadpool_and_wolverine_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: deadpool_and_wolverine_seat(row, col))
            deadpool_and_wolverine_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(deadpool_and_wolverine_seat_button)
        deadpool_and_wolverine_seat_buttons.append(button_row)
    deadpool_and_wolverine_confirm_button=customtkinter.CTkButton(deadpool_and_wolverine_button_frame,text="Confirm Booking",command=deadpool_and_wolverine_confirm,state=DISABLED)
    deadpool_and_wolverine_confirm_button.pack(side=LEFT,padx=10)
    deadpool_and_wolverine_go_back_st_button=customtkinter.CTkButton(deadpool_and_wolverine_button_frame,text="Go Back",command=deadpool_and_wolverine_go_back_st)
    deadpool_and_wolverine_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='deadpool and wolverine' and  movie_date='{}' and movie_timings='{}'".format(deadpool_and_wolverine_date,deadpool_and_wolverine_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    deadpool_and_wolverine_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    deadpool_and_wolverine_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def deadpool_and_wolverine_go_back_bt():
    deadpool_and_wolverine_booking_frame.destroy()
    deadpool_and_wolverine_go_back_bt_button.destroy()
    deadpool_and_wolverine()
def deadpool_and_wolverine_change_date(v):
    deadpool_and_wolverine_theater_frame.destroy()
    deadpool_and_wolverine_theater(v)
def deadpool_and_wolverine_theater(v):
    global deadpool_and_wolverine_theater_frame
    global deadpool_and_wolverine_megastar_timing_button
    global deadpool_and_wolverine_date
    deadpool_and_wolverine_date=v
    deadpool_and_wolverine_theater_frame=customtkinter.CTkFrame(deadpool_and_wolverine_booking_frame,height=50,width=50)
    deadpool_and_wolverine_theater_frame.pack(pady=10)
    deadpool_and_wolverine_theater_01_label=customtkinter.CTkLabel(deadpool_and_wolverine_theater_frame,text="MEGASTAR:TRICHY",font=("calibri",18,"bold"))
    deadpool_and_wolverine_theater_01_label.grid(column=1,row=1)
    deadpool_and_wolverine_timing_list=["11:00 am","2:30 pm","6:00 pm"]
    for i in range(len(deadpool_and_wolverine_timing_list)):
        deadpool_and_wolverine_megastar_timing_button=customtkinter.CTkButton(deadpool_and_wolverine_theater_frame,text=deadpool_and_wolverine_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=deadpool_and_wolverine_timing_list[i]: megastar_timing(tim))
        deadpool_and_wolverine_megastar_timing_button.grid(column=i,row=3,pady=10,padx=5)
    deadpool_and_wolverine_date_button.configure(command=deadpool_and_wolverine_change_date)
def deadpool_and_wolverine_book_tickets():
    deadpool_and_wolverine_frame.destroy()
    global deadpool_and_wolverine_booking_frame
    global deadpool_and_wolverine_date_button
    global deadpool_and_wolverine_go_back_bt_button
    deadpool_and_wolverine_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    deadpool_and_wolverine_booking_frame.pack()
    deadpool_and_wolverine_select_label=customtkinter.CTkLabel(deadpool_and_wolverine_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    deadpool_and_wolverine_select_label.pack()
    deadpool_and_wolverine_date_button=customtkinter.CTkSegmentedButton(deadpool_and_wolverine_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=deadpool_and_wolverine_theater)
    deadpool_and_wolverine_date_button.pack(pady=20)
    deadpool_and_wolverine_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=deadpool_and_wolverine_go_back_bt)
    deadpool_and_wolverine_go_back_bt_button.pack(pady=20)
def deadpool_and_wolverine_go_back_ms():
     deadpool_and_wolverine_frame.destroy()
     main_screen() 
def deadpool_and_wolverine():
    global deadpool_and_wolverine_language_label
    frame.destroy()
    global deadpool_and_wolverine_frame
    deadpool_and_wolverine_frame=customtkinter.CTkFrame(mainwindow)
    deadpool_and_wolverine_frame.pack()
    deadpool_and_wolverine_photo=customtkinter.CTkImage(light_image=Image.open("deadpool-and-wolverine.png"),size=(400,200))
    deadpool_and_wolverine_label=customtkinter.CTkLabel(deadpool_and_wolverine_frame,image=deadpool_and_wolverine_photo,compound="top",text="")
    deadpool_and_wolverine_label.pack(pady=10)
    deadpool_and_wolverine_rating_label=customtkinter.CTkLabel(deadpool_and_wolverine_frame,text="8.7/10",width=40)
    deadpool_and_wolverine_rating_label.pack()
    deadpool_and_wolverine_language_label=customtkinter.CTkLabel(deadpool_and_wolverine_frame,text="English",font=("bold",15))
    deadpool_and_wolverine_language_label.pack(pady=10)
    deadpool_and_wolverine_other_details_label=customtkinter.CTkLabel(deadpool_and_wolverine_frame,text="02:08:00 Hrs . comedy,action,adventure . A . 2024-05-26",font=("bold",15))
    deadpool_and_wolverine_other_details_label.pack(pady=10)
    deadpool_and_wolverine_description_label=customtkinter.CTkLabel(deadpool_and_wolverine_frame,text="Deadpool and wolverine is a movie starring Ryan Reynolds,Hugh Jackman,Morena Baccrin,Matthew Macfadyen\nin prominent roles.It is directed by Shawn Levy",font=("bold",15))
    deadpool_and_wolverine_description_label.pack(pady=10)
    deadpool_and_wolverine_book_ticket_button=customtkinter.CTkButton(deadpool_and_wolverine_frame,text="Book Tickects",command=deadpool_and_wolverine_book_tickets)
    deadpool_and_wolverine_book_ticket_button.pack(pady=10)
    deadpool_and_wolverine_go_back_ms_button=customtkinter.CTkButton(deadpool_and_wolverine_frame,text="Go Back",command=deadpool_and_wolverine_go_back_ms)
    deadpool_and_wolverine_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------DEADPOOL AND WOLVERINE ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------STAR STARTING---------------------------------------------------------------------------------------------------------------------'''
def star_pay():
    star_pay_button.configure(state=DISABLED)
    ins_name="star"
    ins_seat=""
    for i in star_selected_seats:
        if star_selected_seats.index(i)==len(star_selected_seats)-1:
            ins_seat=ins_seat+i
        else:
            ins_seat=ins_seat+i+","
    ins_date=star_date
    ins_timings=star_tim
    q="insert into user_seats values('{}','{}','{}','{}','{}')".format(ins_name,ins_seat,ins_date,ins_timings,c)
    mycursor.execute(q)
    db.commit()
    star_payment_label=customtkinter.CTkLabel(star_details_frame,text="Your payment is successful\n\n\nPlease wait for few seconds",font=("calibri",20,"bold"))
    star_payment_label.pack()
    main_screen()
    star_details_frame.destroy()
    time.sleep(4)
def star_confirm():
    star_seat_frame.destroy()
    star_button_frame.destroy()
    global star_details_frame
    global star_pay_button
    star_details_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    star_details_frame.pack()
    details_label=customtkinter.CTkLabel(star_details_frame,text="STAR"+"\n"+"Tickets booked: "+str(star_selected_seats)+"\nnumber of tickets: "+str(len(star_selected_seats))+"\n\n"+star_tim+"     |     "+star_date,height=20,width=20,font=("calibri",18,"bold"))
    details_label.pack(pady=20)
    star_price=customtkinter.CTkLabel(star_details_frame,text="170 * "+str(len(star_selected_seats))+" : "+str(170*len(star_selected_seats)))
    star_price.pack()
    star_pay_button=customtkinter.CTkButton(star_details_frame,text="Pay now",command=star_pay)
    star_pay_button.pack()
def star_go_back_st():
    star_seat_frame.destroy()
    star_button_frame.destroy()
    star_book_tickets()
def star_seat(row,col):
    seat_id = f"{row+1}-{col+1}"
    button = star_seat_buttons[row][col]
    if seat_id in star_selected_seats:
        star_selected_seats.remove(seat_id)
        button.configure(fg_color="green")
    else:
        star_selected_seats.append(seat_id)
        button.configure(fg_color="red")
    if len(star_selected_seats)==0:
        star_confirm_button.configure(state=DISABLED)
    else:
        star_confirm_button.configure(state=ACTIVE)
def oorvasi_timing(tim):
    star_booking_frame.destroy()
    star_go_back_bt_button.destroy()
    global star_seat_buttons
    global star_selected_seats
    global star_seat_frame
    global star_go_back_st_button
    global star_seat_button
    global star_button_frame
    global star_confirm_button
    global star_tim
    star_tim=tim
    star_seat_buttons=[]
    star_selected_seats=[]
    star_seat_frame=customtkinter.CTkFrame(mainwindow)
    star_seat_frame.pack()
    star_button_frame=customtkinter.CTkFrame(mainwindow)
    star_button_frame.pack(pady=10)
    no_of_row=7
    no_of_column=7
    for i in range(no_of_row):
        button_row=[]
        for j in range(no_of_column):
            star_seat_button=customtkinter.CTkButton(star_seat_frame,text=f"{i+1}-{j+1}",height=40,width=40,fg_color="green",command=lambda row=i,col=j: star_seat(row, col))
            star_seat_button.grid(row=i,column=j+1,padx=10,pady=10)
            button_row.append(star_seat_button)
        star_seat_buttons.append(button_row)
    star_confirm_button=customtkinter.CTkButton(star_button_frame,text="Confirm Booking",command=star_confirm,state=DISABLED)
    star_confirm_button.pack(side=LEFT,padx=10)
    star_go_back_st_button=customtkinter.CTkButton(star_button_frame,text="Go Back",command=star_go_back_st)
    star_go_back_st_button.pack(side=RIGHT,padx=10)
    q="select seat_name from user_seats where movie_name='star' and  movie_date='{}' and movie_timings='{}'".format(star_date,star_tim)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
        for j in i:
            for k in j.split(","):
                if k.endswith("10"):
                    star_seat_buttons[int(float(k[0]))-1][int(float(k[2]+k[3]))-1].configure(state=DISABLED,fg_color="yellow")
                else:
                    star_seat_buttons[int(float(k[0]))-1][int(float(k[2]))-1].configure(state=DISABLED,fg_color="yellow")
def star_go_back_bt():
    star_booking_frame.destroy()
    star_go_back_bt_button.destroy()
    star()
def star_change_date(v):
    star_theater_frame.destroy()
    star_theater(v)
def star_theater(v):
    global star_theater_frame
    global star_oorvasi_timing_button
    global star_date
    star_date=v
    star_theater_frame=customtkinter.CTkFrame(star_booking_frame,height=50,width=50)
    star_theater_frame.pack(pady=10)
    star_theater_01_label=customtkinter.CTkLabel(star_theater_frame,text="BHELC:TRICHY",font=("calibri",18,"bold"))
    star_theater_01_label.grid(column=1,row=1)
    star_timing_list=["11:30 am","3:30 pm","6:30 pm"]
    for i in range(len(star_timing_list)):
        star_oorvasi_timing_button=customtkinter.CTkButton(star_theater_frame,text=star_timing_list[i],font=("calibri",14,"bold"),command=lambda tim=star_timing_list[i]: oorvasi_timing(tim))
        star_oorvasi_timing_button.grid(column=i,row=3,pady=10,padx=5)
    star_date_button.configure(command=star_change_date)
def star_book_tickets():
    star_frame.destroy()
    global star_booking_frame
    global star_date_button
    global star_go_back_bt_button
    star_booking_frame=customtkinter.CTkFrame(mainwindow,height=100,width=100)
    star_booking_frame.pack()
    star_select_label=customtkinter.CTkLabel(star_booking_frame,text="SELECT A DATE TO BOOK THE TICKECT(S)",font=("calibri",20,"bold"))
    star_select_label.pack()
    star_date_button=customtkinter.CTkSegmentedButton(star_booking_frame,values=["JULY 1","JULY 2","JULY 3"],command=star_theater)
    star_date_button.pack(pady=20)
    star_go_back_bt_button=customtkinter.CTkButton(mainwindow,text="Go Back",command=star_go_back_bt)
    star_go_back_bt_button.pack(pady=20)
def star_go_back_ms():
     star_frame.destroy()
     main_screen() 
def star():
    global star_language_label
    frame.destroy()
    global star_frame
    star_frame=customtkinter.CTkFrame(mainwindow)
    star_frame.pack()
    star_photo=customtkinter.CTkImage(light_image=Image.open("star.png"),size=(400,200))
    star_label=customtkinter.CTkLabel(star_frame,image=star_photo,compound="top",text="")
    star_label.pack(pady=10)
    star_rating_label=customtkinter.CTkLabel(star_frame,text="7.9/10",width=40)
    star_rating_label.pack()
    star_language_label=customtkinter.CTkLabel(star_frame,text="Tamil",font=("bold",15))
    star_language_label.pack(pady=10)
    star_other_details_label=customtkinter.CTkLabel(star_frame,text="02:38:00 Hrs . family,drama . U . 2024-05-14",font=("bold",15))
    star_other_details_label.pack(pady=10)
    star_description_label=customtkinter.CTkLabel(star_frame,text="Star is a movie starring Kavin raj,Lal,Priety Mukundhan,Aditi Pohankar\nin prominent roles.It is directed by Elan",font=("bold",15))
    star_description_label.pack(pady=10)
    star_book_ticket_button=customtkinter.CTkButton(star_frame,text="Book Tickects",command=star_book_tickets)
    star_book_ticket_button.pack(pady=10)
    star_go_back_ms_button=customtkinter.CTkButton(star_frame,text="Go Back",command=star_go_back_ms)
    star_go_back_ms_button.pack(pady=10)


'''---------------------------------------------------STAR ENDING------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def login_submit():
    file=open("user_pass.txt","r")
    file_str=file.read()
    file_list=file_str.split("\n")
    sql_user=file_list[0]
    sql_pass=file_list[1]
    file.close()
    global c
    import mysql.connector as ms
    db= ms.connect(host="localhost",user=sql_user,passwd=sql_pass,database="ticketbuddy")
    mycursor=db.cursor()
    c=login_username_entry.get()
    d=login_password_entry.get()    
    q="select password from user_details where username='{}'".format(c,)
    mycursor.execute(q)
    z=mycursor.fetchone()
    if z!=None:
        while d not in z:
            if d not in z:
                m=messagebox.showerror("PASSWORD","WRONG PASSWORD!! TRY AGAIN")
                if m=="ok":
                    break
            else:
                break
        else:
             login_frame.destroy()
             frame_1.destroy()
             Label1.destroy()
             main_screen()      
    else:
        while z==None:
            if z==None:
                m=messagebox.showerror("USERNAME","USERNAME DOES NOT EXIST!! TRY AGAIN")
                if m=="ok":
                    break
def phonenumber():
     a=signin_username_entry.get()
     p=signin_phone_entry.get()
     mycursor.execute("select phone_number from user_details")
     ph=mycursor.fetchall()
     po=(p,)
     try:
        int(float(p))
     except:
            phonenumber_letter_message=messagebox.showerror("","PHONE NUMBER SHOULD NOT CONTAIN LETTERS!!")
     while po in ph or len(p)!=10 or p=="":
          if po in ph:
               info=messagebox.showinfo("PHONE NUMBER","THIS PHONE NUMBER IS ALREADY IN USE!PLEASE TRY AGAIN")
               p=signin_phone_entry.get()
               po=(p,)
               if info=="ok":
                   break
          elif p=="":
              info=messagebox.showinfo("PHONE NUMBER","PHONE NUMBER SHOULD NOT BE EMPTY!")
              p=signin_phone_entry.get()
              po=(p,)
              if info=="ok":
                   break
          elif len(p)!=10:
              info=messagebox.showinfo("PHONE NUMBER","PLEASE ENTER A VALID PHONE NUMBER!")
              p=signin_phone_entry.get()
              po=(p,)
              if info=="ok":
                   break
          else:
            break
     else:
         b=signin_password_entry.get()
         while b=="":
             if b=="":
                 info=messagebox.showinfo("PASSWORD","PASSWORD SHOULD NOT BE EMPTY!")
                 b=signin_password_entry.get()
                 if info=="ok":
                   break
             else:
                 break
         else:
            q="insert into user_details(username,phone_number,password) values('{}','{}','{}')".format(a,p,b)
            mycursor.execute(q)
            db.commit()
            success_label=customtkinter.CTkLabel(signin_frame,text="YOUR ACCOUNT IS SUCCESSFULLY CREATED!!",font=("calibri",20),text_color="black")
            success_label.pack(padx=20,pady=50)
            question=messagebox.askquestion("","DO YOU WANT TO LOG-IN")
            if question=="yes":
                signin_frame.destroy()
                login()
            else:
                signin_frame.destroy()
def signin_submit():
    file=open("user_pass.txt","r")
    file_str=file.read()
    file_list=file_str.split("\n")
    sql_user=file_list[0]
    sql_pass=file_list[1]
    file.close()
    import mysql.connector as ms
    db= ms.connect(host="localhost",user=sql_user,passwd=sql_pass,database="ticketbuddy")
    mycursor=db.cursor()
    a=signin_username_entry.get()
    mycursor.execute("select username from user_details")
    dt=mycursor.fetchall()
    ee=(a,)
    while a=="":
        a=signin_username_entry.get()
        info=messagebox.showinfo("USERNAME","USERNAME SHOULD NOT BE EMPTY!")
        if info=="ok":
             break
    else:
        while ee in dt:
            a=signin_username_entry.get()
            ee=(a,)
            if ee in dt:
                info=messagebox.showinfo("USERNAME","THIS USER NAME IS ALREADY IN USE!PLEASE TRY AGAIN")
                if info=="ok":
                    break
            else:
             phonenumber()
        else:
            phonenumber()
    db.close()
def signin():
    global signin_username_entry
    global signin_phone_entry
    global signin_password_entry
    global signin_frame
    signin_button.configure(state=DISABLED)
    login_button.configure(state=ACTIVE)
    try:
        login_frame.destroy()
    except:
        pass
    signin_frame=customtkinter.CTkFrame(mainwindow,fg_color="white")
    signin_frame.pack(pady=10, padx=50)
    signin_username_entry=customtkinter.CTkEntry(signin_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Username",placeholder_text_color="black",text_color="black")
    signin_username_entry.pack(pady=10, padx=50)
    signin_phone_entry=customtkinter.CTkEntry(signin_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Phone Number",placeholder_text_color="black",text_color="black")
    signin_phone_entry.pack(pady=10, padx=50)
    signin_password_entry=customtkinter.CTkEntry(signin_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Password",placeholder_text_color="black",text_color="black")
    signin_password_entry.pack(pady=10, padx=50)
    signin_submit_button=customtkinter.CTkButton(signin_frame,text="Submit",command=signin_submit,corner_radius=20)
    signin_submit_button.pack(pady=10, padx=50)
def login():
    global login_username_entry
    global login_password_entry
    global login_frame
    login_button.configure(state=DISABLED)
    signin_button.configure(state=ACTIVE)
    try:
        signin_frame.destroy()
    except:
        pass
    login_frame=customtkinter.CTkFrame(mainwindow,fg_color="white")
    login_frame.pack(pady=10, padx=50)
    login_username_entry=customtkinter.CTkEntry(login_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Username",placeholder_text_color="black",text_color="black")
    login_username_entry.pack(pady=10, padx=50)
    login_password_entry=customtkinter.CTkEntry(login_frame,font=("calibri",20,"bold"),fg_color="white",placeholder_text="Password",placeholder_text_color="black",text_color="black")
    login_password_entry.pack(pady=10, padx=50)
    login_submit_button=customtkinter.CTkButton(login_frame,text="Submit",command=login_submit,corner_radius=20)
    login_submit_button.pack(pady=10, padx=50)
Label1=customtkinter.CTkLabel(mainwindow,text="Welcome To TicketBudddy",font=("cooper black",27))
Label1.pack(pady=10)
frame_1=customtkinter.CTkFrame(mainwindow)
frame_1.pack(pady=50)
signin_button=customtkinter.CTkButton(frame_1,text="SIGN IN",command=signin,font=("arial black",17),fg_color="#008080",corner_radius=20)
signin_button.pack(side=LEFT,padx=10)
login_button=customtkinter.CTkButton(frame_1,text="LOG IN",command=login,font=("arial black",17),fg_color="#008080",corner_radius=20)
login_button.pack(side=RIGHT,padx=10)
mainwindow.mainloop()
