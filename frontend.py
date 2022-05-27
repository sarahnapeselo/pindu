#importing all modules
from tkinter import *
import backend
backend.connect_database()
#creating window
window = Tk()
window.title("my application")


tk.config()
tk.title('my bank wakb')
tk.minsize(480,360)
tk.config(background='#41B77F')

def check_string_in_account_no(check_acc_no):
    r=check_acc_no.isdigit()
    return r



def create():
    def create_customer_in_database():
        def delete_create():
            create_employee_frame.grid_forget()
            page2()
        name = entry5.get()
        age = entry6.get()
        address = entry7.get()
        balance = entry8.get()
        acc_type = entry9.get()
        mobile_number = entry10.get()
        if len(name) != 0 and len(age) != 0 and len(address) != 0 and len(balance) != 0 and len(acc_type) != 0 and len(
                mobile_number) != 0:

            acc_no = backend.create_customer(name, age, address, balance, acc_type, mobile_number)

            label = Label(create_employee_frame, text='vous detenez comme  compte {}'.format(acc_no))
            label.grid(row=14)

            button = Button(create_employee_frame, text="Quitter", command=delete_create,bg='red',width=20, height=2,font=("Arial", 10, "bold"))
            button.grid(row=15)
        else:
            label = Label(create_employee_frame, text="svp! de grace remplissez toute la page")
            label.grid(row=14)

            button = Button(create_employee_frame, text="Quitter", command=delete_create,bg='yellow',width=20, height=2,font=("Arial", 10, "bold"))
            button.grid(row=15)
    frame1.grid_forget()
    global create_employee_frame
    create_employee_frame=Frame(tk,bg='#96c0eb')
    create_employee_frame.grid(padx=500,pady=150)

    label=Label(create_employee_frame,text='Customer Detail',font='bold')
    label.grid(row=0,pady=4)
    label = Label(create_employee_frame, text='Nom', font='bold')
    label.grid(row=1,pady=4)
    global entry5
    entry5=Entry(create_employee_frame)
    entry5.grid(row=2,pady=4)
    label = Label(create_employee_frame, text='Age', font='bold')
    label.grid(row=3,pady=4)
    global entry6
    entry6=Entry(create_employee_frame)
    entry6.grid(row=4,pady=4)
    label = Label(create_employee_frame, text='addresse', font='bold')
    label.grid(row=5,pady=4)
    global entry7
    entry7=Entry(create_employee_frame)
    entry7.grid(row=6,pady=4)
    label = Label(create_employee_frame, text='Balance', font='bold')
    label.grid(row=7,pady=4)
    global entry8
    entry8=Entry(create_employee_frame)
    entry8.grid(row=8,pady=4)
    label = Label(create_employee_frame, text='Account Type', font='bold')
    label.grid(row=9,pady=4)
    label = Label(create_employee_frame, text='Numero de telephone', font='bold')
    label.grid(row=11,pady=4)
    global entry9
    entry9 = Entry(create_employee_frame)
    entry9.grid(row=10,pady=4)
    global entry10
    entry10 = Entry(create_employee_frame)
    entry10.grid(row=12,pady=4)
    button=Button(create_employee_frame,text='Envoyé',command=create_customer_in_database)
    button.grid(row=13,pady=4)

    mainloop()

def search_acc():
    frame1.grid_forget()
    global search_frame
    search_frame=Frame(tk)
    search_frame.grid(padx=500,pady=300)

    label=Label(search_frame,text="Entre numero de compte",font='bold')
    label.grid(row=0,pady=6)

    global entry11
    entry11=Entry(search_frame)
    entry11.grid(row=1,pady=6)

    button=Button(search_frame,text="rechercher",command=show)
    button.grid(row=3)

    mainloop()

def show():
    def clear_show_frame():
        show_frame.grid_forget()
        page2()
    def back_page2():
        search_frame.grid_forget()
        page2()

    acc_no=entry11.get()
    r=check_string_in_account_no(acc_no)
    if len(acc_no)!=0 and r:
        details=backend.get_details(acc_no)
        if details!=False:
            search_frame.grid_forget()
            global show_frame
            show_frame=Frame(tk)
            show_frame.grid(padx=400,pady=300)

            label=Label(show_frame,text="nom:\t{}".format(details[0]),font='bold')
            label.grid(row=0,pady=6)
            label = Label(show_frame, text="numero de_compte:\t{}".format(details[1]),font='bold')
            label.grid(row=1,pady=6)
            label = Label(show_frame, text="Age:\t{}".format(details[2]),font='bold')
            label.grid(row=2,pady=6)
            label = Label(show_frame, text="Addresse:\t{}".format(details[3]),font='bold')
            label.grid(row=3,pady=6)
            label = Label(show_frame, text="Balance:\t{}".format(details[4]),font='bold')
            label.grid(row=4,pady=6)
            label = Label(show_frame, text="type de_compte:\t{}".format(details[5]),font='bold')
            label.grid(row=5,pady=6)
            label = Label(show_frame, text="numero de de compte:\t{}".format(details[6]),font='bold')
            label.grid(row=6,pady=6)
            button=Button(show_frame,text='Quitter',command=clear_show_frame,width=20,height=2,bg='red',fg='white')
            button.grid(row=7,pady=6)
            mainloop()
        else:
            label=Label(search_frame,text="compte non retrouver")
            label.grid()
            button=Button(search_frame,text='Quitter',command=back_page2,bg='red',width=20, height=2,font=("Arial", 10, "bold"))
            button.grid()

    else:
        label = Label(search_frame, text="Entre un numero de compte correct")
        label.grid()
        button = Button(search_frame, text='Quitter', command=back_page2)
        button.grid()

def add():
    frame1.grid_forget()
    def search_in_database():
        def back_page2():
            search_frame.grid_forget()
            page2()
        global result
        global acc_no
        acc_no = entry11.get()
        r=check_string_in_account_no(acc_no)
        if len(acc_no)!=0 and r:
            result = backend.check_acc_no(acc_no)
            print(result)
            if not result:
                label = Label(search_frame, text="numero de compte invlide")
                label.grid(pady=2)
                button=Button(search_frame, text="Quitter",command=back_page2)
                button.grid()
                mainloop()
            else:
                def update_money():
                    new_money=entry12.get()
                    backend.update_balance(new_money,acc_no)
                    add_frame.grid_forget()
                    page2()

                search_frame.grid_forget()
                global add_frame
                add_frame=Frame(tk)
                add_frame.grid(padx=400,pady=300)

                detail = backend.get_detail(acc_no)

                label = Label(add_frame, text='Nom du proprietaire du compte:   {}'.format(detail[0][0]))
                label.grid(row=0, pady=3)

                label = Label(add_frame, text='Somme actuel:   {}'.format(detail[0][1]))
                label.grid(row=1, pady=3)

                label=Label(add_frame,text='Entre argent')
                label.grid(row=2,pady=3)
                global entry12
                entry12=Entry(add_frame)
                entry12.grid(row=3,pady=3)

                button=Button(add_frame,text='Ajouter',command=update_money)
                button.grid(row=4)

                mainloop()
        else:
            label = Label(search_frame, text="Entre correctement le numero de compte")
            label.grid(pady=2)
            button = Button(search_frame, text="Quitter", command=back_page2)
            button.grid()
            mainloop()
    def search_acc():
        global search_frame
        search_frame = Frame(tk)
        search_frame.grid(padx=500, pady=300)

        label = Label(search_frame, text="Entrer numero de compte", font='bold')
        label.grid(row=0, pady=6)

        global entry11
        entry11 = Entry(search_frame)
        entry11.grid(row=1, pady=6)

        button = Button(search_frame, text="Rechercher", command=search_in_database)
        button.grid(row=3)

        mainloop()
    search_acc()

def withdraw():
    frame1.grid_forget()

    def search_in_database():
        def go_page2():
            search_frame.grid_forget()
            page2()

        global result
        global acc_no
        acc_no = entry11.get()
        r=check_string_in_account_no(acc_no)
        if len(acc_no)!=0 and r:
            result = backend.check_acc_no(acc_no)
            print(result)
            if not result:
                label = Label(search_frame, text="Numero de vompte invalide")
                label.grid(pady=2)
                button = Button(search_frame, text="Quitter", command=go_page2)
                button.grid()
                mainloop()
            else:
                def deduct_money():
                    new_money = entry12.get()
                    result=backend.deduct_balance(new_money, acc_no)
                    if result:
                        add_frame.grid_forget()
                        page2()
                    else:
                        label=Label(search_frame,text="Balance insuffisante")
                        label.grid(row=4)

                        button=Button(search_frame,text='Quitter',command=go_page2)
                        button.grid(row=5)

                        mainloop()
                search_frame.grid_forget()
                global add_frame
                add_frame = Frame(tk)
                add_frame.grid(padx=400, pady=300)
                detail=backend.get_detail(acc_no)

                label=Label(add_frame,text='Nom du proprietaire du compte:   {}'.format(detail[0][0]))
                label.grid(row=0,pady=3)

                label = Label(add_frame, text='Compte actuel:   {}'.format(detail[0][1]))
                label.grid(row=1, pady=3)

                label = Label(add_frame, text='Entre Argent')
                label.grid(row=2, pady=3)
                global entry12
                entry12 = Entry(add_frame)
                entry12.grid(row=3, pady=3)

                button = Button(add_frame, text='Withdraw', command=deduct_money)
                button.grid(row=4)

                mainloop()
        else:
            label = Label(search_frame, text="Entrer correctement le numeros de compte")
            label.grid(row=4)

            button = Button(search_frame, text='Quitter', command=go_page2)
            button.grid(row=5)

            mainloop()
    def search_acc():
        global search_frame
        search_frame = Frame(tk)
        search_frame.grid(padx=500, pady=300)

        label = Label(search_frame, text="Entre le numero de compte", font='bold')
        label.grid(row=0, pady=6)

        global entry11
        entry11 = Entry(search_frame)
        entry11.grid(row=1, pady=6)

        button = Button(search_frame, text="rechercher", command=search_in_database)
        button.grid(row=3)

        mainloop()

    search_acc()

def check():
    frame1.grid_forget()

    def search_in_database():
        def back_page2():
            search_frame.grid_forget()
            page2()
        global result
        global acc_no
        acc_no = entry11.get()
        r=check_string_in_account_no(acc_no)

        if len(acc_no)!=0 and r:
            result = backend.check_acc_no(acc_no)
            print(result)
            if not result:
                label = Label(search_frame, text="numero de compte invalide")
                label.grid(pady=2)
                button = Button(search_frame, text="Quitter", command=back_page2)
                button.grid()
                mainloop()
            else:
                def delete_check_frame():
                    check_frame.grid_forget()
                    page2()
                search_frame.grid_forget()
                balance=backend.check_balance(acc_no)
                global check_frame
                check_frame=Frame(tk)
                check_frame.grid(padx=500,pady=300)

                label=Label(check_frame,text='Balance Is:{}'.format(balance),font='bold')
                label.grid(row=0,pady=4)

                button=Button(check_frame,text='Back',command=delete_check_frame,width=20,height=2,bg='red')
                button.grid(row=1)

                mainloop()
        else:
            label = Label(search_frame, text="Enter correct entry")
            label.grid(pady=2)
            button = Button(search_frame, text="Quitter", command=back_page2)
            button.grid()
            mainloop()

    def search_acc():
        global search_frame
        search_frame = Frame(tk)
        search_frame.grid(padx=500, pady=300)

        label = Label(search_frame, text="Entrer correctement le numero de compte", font='bold')
        label.grid(row=0, pady=6)

        global entry11

        entry11 = Entry(search_frame)
        entry11.grid(row=1, pady=6)

        button = Button(search_frame, text="Rechercher", command=search_in_database)
        button.grid(row=3)

        mainloop()

    search_acc()

def update():
    def back_to_page2():
        search_frame.grid_forget()
        page2()
    def show_all_updateble_content():
        def back_to_page2_from_update():
            update_customer_frame.grid_forget()
            page2()
        #defining a function whose makes a update entry and submit butoon side to name button
        def update_name():
            #def a function eho updates name in database
            def update_name_in_database():
                new_name=entry_name.get()
                r=check_string_in_account_no(new_name)
                if len(new_name)!=0:
                    #function in backend that updates name in table
                    backend.update_name_in_bank_table(new_name,acc_no)
                    entry_name.destroy()
                    submit_button.destroy()
                    name_label.destroy()
                else:
                    tkinter.messagebox.showinfo('Erreur','Please fill blanks')
                    entry_name.destroy()
                    submit_button.destroy()
                    name_label.destroy()
            global entry_name
            global name_label
            name_label=Label(update_customer_frame,text='Entrer nouveau compte')
            name_label.grid(row=1,column=1)
            entry_name=Entry(update_customer_frame)
            entry_name.grid(row=1,column=2,padx=2)
            global submit_button
            submit_button=Button(update_customer_frame,text='Update',command=update_name_in_database)
            submit_button.grid(row=1,column=3)
        #defing a function who make gui fro age
        def update_age():
            # def a function eho updates name in database
            def update_age_in_database():
                new_age = entry_name.get()
                r=check_string_in_account_no(new_age)
                if len(new_age)!=0 and r:
                    # function in backend that updates name in table
                    backend.update_age_in_bank_table(new_age, acc_no)
                    entry_name.destroy()
                    submit_button.destroy()
                    age_label.destroy()
                else:
                    tkinter.messagebox.showinfo('Error','Please enter age')
                    entry_name.destroy()
                    submit_button.destroy()
                    age_label.destroy()
            global age_label
            age_label = Label(update_customer_frame, text='Entrer nouvelle Age:')
            age_label.grid(row=2, column=1)
            global entry_name
            entry_name = Entry(update_customer_frame)
            entry_name.grid(row=2, column=2, padx=2)
            global submit_button
            submit_button = Button(update_customer_frame, text='Update', command=update_age_in_database)
            submit_button.grid(row=2, column=3)

        # defing a function who make gui fro age
        def update_address():
            # def a function eho updates name in database
            def update_address_in_database():
                new_address = entry_name.get()
                if len(new_address)!=0:
                    # function in backend that updates name in table
                    backend.update_address_in_bank_table(new_address, acc_no)
                    entry_name.destroy()
                    submit_button.destroy()
                    address_label.destroy()
                else:
                    tkinter.messagebox.showinfo('Error','Please fill address')
                    entry_name.destroy()
                    submit_button.destroy()
                    address_label.destroy()
            global address_label

            address_label = Label(update_customer_frame, text='Entrer nouvelle Address:')
            address_label.grid(row=3, column=1)
            global entry_name
            entry_name = Entry(update_customer_frame)
            entry_name.grid(row=3, column=2, padx=2)
            global submit_button
            submit_button = Button(update_customer_frame, text='Update', command=update_address_in_database)
            submit_button.grid(row=3, column=3)

        acc_no=entry_acc.get()

        r=check_string_in_account_no(acc_no)
        if r:
            result = backend.check_acc_no(acc_no)
            if result:
                search_frame.grid_forget()
                global update_customer_frame
                update_customer_frame=Frame(tk)
                update_customer_frame.grid(padx=300,pady=300)

                label=Label(update_customer_frame,text='What do you want to update')
                label.grid(row=0)

                name_button=Button(update_customer_frame,text='Nom',command=update_name)
                name_button.grid(row=1,column=0,pady=6)

                age_button=Button(update_customer_frame,text='Age',command=update_age)
                age_button.grid(row=2,column=0,pady=6)

                address_button=Button(update_customer_frame,text='Addresse',command=update_address)
                address_button.grid(row=3,column=0,pady=6)

                exit_button=Button(update_customer_frame,text='Exit',command=back_to_page2_from_update)
                exit_button.grid(row=4)
                mainloop()
            else:
                label = Label(search_frame, text='numero de compte invalide')
                label.grid()

                button = Button(search_frame, text='Quitter', command=back_to_page2)
                button.grid()

        else:
            label=Label(search_frame,text='remplir numero de compte')
            label.grid()

            button=Button(search_frame,text='Quitter',command=back_to_page2)
            button.grid()

    frame1.grid_forget()
    #define gui for enter account number

    global search_frame
    search_frame=Frame(tk)
    search_frame.grid(padx=500,pady=300)

    label=Label(search_frame,text='Enter account number',font='bold')
    label.grid(pady=4)

    entry_acc=Entry(search_frame)
    entry_acc.grid(pady=4)

    button=Button(search_frame,text='update',command=show_all_updateble_content,bg='red')
    button.grid()

def allmembers():
    def clear_list_frame():
        list_frame.grid_forget()
        page2()
    frame1.grid_forget()
    details=backend.list_all_customers()
    global tk


    global list_frame
    list_frame=Frame(tk)
    list_frame.grid(padx=50,pady=50)
    label=Label(list_frame,text="Acc_no\t\t\tNom\t\t\tAge\t\t\tAddresse\t\t\tbalance")
    label.grid(pady=6)
    for i in details:
        label=Label(list_frame,text="{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(i[0],i[1],i[2],i[3],i[4]))
        label.grid(pady=4)

    button=Button(list_frame,text='Retour',width=20,height=2,bg='red',command=clear_list_frame)
    button.grid()
    mainloop()

def delete():
    frame1.grid_forget()

    def search_in_database():
        def back_page2():
            search_frame.grid_forget()
            page2()
        global result
        global acc_no
        acc_no = entry11.get()
        r=check_string_in_account_no(acc_no)
        if len(acc_no)!=0 and r:
            result = backend.check_acc_no(acc_no)
            print(result)
            if not result:

                label = Label(search_frame, text="Numero de compte invalide")
                label.grid(pady=2)
                button = Button(search_frame, text="Quitter", command=back_page2)
                button.grid()
                mainloop()
            else:
                backend.delete_acc(acc_no)
                search_frame.grid_forget()
                page2()
        else:
            label = Label(search_frame, text="Entrer correctement le numero de compte")
            label.grid(pady=2)
            button = Button(search_frame, text="QUITTER", command=back_page2)
            button.grid()
    def search_acc():
        global search_frame
        search_frame = Frame(tk)
        search_frame.grid(padx=500, pady=300)

        label = Label(search_frame, text="Entrer numero de compte", font='bold')
        label.grid(row=0, pady=6)

        global entry11
        entry11 = Entry(search_frame)
        entry11.grid(row=1, pady=6)

        button = Button(search_frame, text="Supprimer", command=search_in_database)
        button.grid(row=3)

        mainloop()

    search_acc()

#main page for employees
def page2():
    def back_to_main_from_page2():
        frame1.grid_forget()
        global frame
        frame = Frame(tk, bg='#96c0eb')
        frame.grid(padx=500, pady=250)

        button = Button(frame, text="Admin", command=admin_login)
        button.grid(row=0, pady=20)

        button = Button(frame, text="Employee", command=employee_login)
        button.grid(row=1, pady=20)

        button = Button(frame, text="Quitter", command=tk.destroy)
        button.grid(row=2, pady=20)
        tk.mainloop()

    frame.grid_forget()
    global frame1
    frame1=Frame(tk,bg='#96c0eb')
    frame1.grid(padx=500,pady=100)
    button1 = Button(frame1, text="Create acounte", command=create,width=20,height=2)
    button1.grid(row=0,pady=6)
    button2 = Button(frame1, text="show Details", command=search_acc,width=20,height=2)
    button2.grid(row=1,pady=6)
    button3 = Button(frame1, text="Add balance", command=add,width=20,height=2)
    button3.grid(row=2,pady=6)
    button4 = Button(frame1, text="withdraw money", command=withdraw,width=20,height=2)
    button4.grid(row=3,pady=6)
    button5 = Button(frame1, text="check balance", command=check,width=20,height=2)
    button5.grid(row=4,pady=6)
    button6 = Button(frame1, text="update acounte", command=update,width=20,height=2)
    button6.grid(row=5,pady=6)
    button7 = Button(frame1, text="List all membres", command=list,width=20,height=2)
    button7.grid(row=6,pady=6)
    button8 = Button(frame1, text="delete compte", command=delete,width=20,height=2)
    button8.grid(row=7,pady=6)

    button9 = Button(frame1, text="Quitter", command=back_to_main_from_page2,width=20,height=2)
    button9.grid(row=8,pady=6)

    mainloop()


#all buttons of page1
def create_employee():
    def create_emp_in_database():
        def back_to_main_page1_from_create_emp():
            frame_create_emp.grid_forget()
            page1()

        name = entry3.get()
        password = entry4.get()
        salary = entry16.get()
        position = entry17.get()
        if len(name) != 0 and len(password) != 0 and len(salary) != 0 and len(position) != 0:
            backend.create_employee(name, password, salary, position)
            frame_create_emp.grid_forget()
            page1()
        else:
            label = Label(frame_create_emp, text="veillez remplir tous les champ")
            label.grid(pady=2)

            button = Button(frame_create_emp, text="Quitter", command=back_to_main_page1_from_create_emp, bg='red')
            button.grid()
    page1_frame.grid_forget()

    global frame_create_emp
    frame_create_emp=Frame(tk,bg='#96c0eb')
    frame_create_emp.grid(padx=500,pady=200)

    label=Label(frame_create_emp,text='Nom:',font='bold')
    label.grid(row=0,pady=4)
    global entry3
    entry3=Entry(frame_create_emp)
    entry3.grid(row=1,pady=4)
    label2=Label(frame_create_emp,text='mot de passe',font='bold')
    label2.grid(row=2,pady=4)
    global entry4
    entry4=Entry(frame_create_emp)
    entry4.grid(row=3,pady=4)
    label3 = Label(frame_create_emp, text='Salaire',font='bold')
    label3.grid(row=4,pady=4)
    global entry16
    entry16 = Entry(frame_create_emp)
    entry16.grid(row=5,pady=4)
    label4 = Label(frame_create_emp, text='Position',font='bold')
    label4.grid(row=6,pady=4)
    global entry17
    entry17 = Entry(frame_create_emp)
    entry17.grid(row=7,pady=4)

    button=Button(frame_create_emp,text='envoye',command=create_emp_in_database,width=15,height=2)
    button.grid(row=8,pady=4)

    mainloop()

def update_employee():
    def update_details_of_staff_member():
        def back_to_page1():
            show_employee_frame.grid_forget()
            page1()
        def update_that_particular_employee():
            show_employee_frame.grid_forget()
            def back_to_page1_from_update():
                update_frame.destroy()
                page1()

            def update_name_in_database():

                def database_calling():
                    new_name = entry19.get()
                    if len(new_name)!=0:
                        old_name=staff_name.get()
                        backend.update_employee_name(new_name,old_name)
                        entry19.destroy()
                        update_button.destroy()
                    else:
                        entry19.destroy()
                        update_button.destroy()
                        tkinter.messagebox.showinfo('Error','Please fill entry')
                global entry19
                entry19 = Entry(update_frame)
                entry19.grid(row=1, column=1, padx=4)
                global update_button
                update_button = Button(update_frame, text='Update', command=database_calling)
                update_button.grid(row=1, column=2, padx=4)

            def update_password_in_database():

                def database_calling():
                    new_password = entry19.get()
                    old_name=staff_name.get()
                    if len(new_password)!=0:
                        backend.update_employee_password(new_password,old_name)
                        entry19.destroy()
                        update_button.destroy()
                    else:
                        entry19.destroy()
                        update_button.destroy()
                        tkinter.messagebox.showinfo('Error','Please Fill Entry')
                global entry19
                entry19 = Entry(update_frame)
                entry19.grid(row=2, column=1, padx=4)
                global update_button
                update_button = Button(update_frame, text='Update', command=database_calling)
                update_button.grid(row=2, column=2, padx=4)

            def update_salary_in_database():

                def database_calling():
                    new_salary = entry19.get()
                    r=check_string_in_account_no(new_salary)
                    if len(new_salary)!=0 and r:

                        old_name=staff_name.get()
                        backend.update_employee_salary(new_salary,old_name)
                        entry19.destroy()
                        update_button.destroy()
                    else:
                        entry19.destroy()
                        update_button.destroy()
                        tkinter.messagebox.showinfo('Error','Invalid Input')

                global entry19
                entry19 = Entry(update_frame)
                entry19.grid(row=3, column=1, padx=4)
                global update_button
                update_button = Button(update_frame, text='Update', command=database_calling)
                update_button.grid(row=3, column=2, padx=4)

            def update_position_in_database():

                def database_calling():
                    new_position = entry19.get()
                    if len(new_position)!=0:

                        old_name=staff_name.get()
                        backend.update_employee_position(new_position,old_name)
                        entry19.destroy()
                        update_button.destroy()
                    else:
                        entry19.destroy()
                        update_button.destroy()
                        tkinter.messagebox.showinfo('Error','Please Fill Entry')

                global entry19
                entry19 = Entry(update_frame)
                entry19.grid(row=4, column=1, padx=4)
                global update_button
                update_button = Button(update_frame, text='Update', command=database_calling)
                update_button.grid(row=4, column=2, padx=4)

            global update_frame
            update_frame = Frame(tk)
            update_frame.grid(padx=400, pady=250)

            label = Label(update_frame, text='press what do you want to update',font='bold')
            label.grid(pady=6)

            button = Button(update_frame, text='Name', command=update_name_in_database,width=14,height=2)
            button.grid(row=1, column=0, padx=2,pady=2)

            button = Button(update_frame, text='password',command=update_password_in_database,width=14,height=2)
            button.grid(row=2, column=0, padx=2,pady=2)

            button = Button(update_frame, text='salary',command=update_salary_in_database,width=14,height=2)
            button.grid(row=3, column=0, padx=2,pady=2)

            button = Button(update_frame, text='position',command=update_position_in_database,width=14,height=2)
            button.grid(row=4, column=0, padx=2,pady=2)

            button = Button(update_frame, text='Back', command=back_to_page1_from_update,width=14,height=2)
            button.grid(row=5, column=0,pady=2)




        name=staff_name.get()
        if len(name)!=0:
            result=backend.check_name_in_staff(name)
            if result:

                update_that_particular_employee()
            else:
                label = Label(show_employee_frame, text='Employee not found')
                label.grid()

                button = Button(show_employee_frame, text='Exit', command=back_to_page1)
                button.grid()

        else:
            label=Label(show_employee_frame,text='Fill the name')
            label.grid()

            button=Button(show_employee_frame,text='Exit',command=back_to_page1)
            button.grid()




    #entering name of staff member
    page1_frame.grid_forget()
    global show_employee_frame
    show_employee_frame=Frame(tk)
    show_employee_frame.grid(padx=300,pady=300)

    label=Label(show_employee_frame,text='Enter name of staff member whom detail would you want to update')
    label.grid()
    global staff_name
    staff_name=Entry(show_employee_frame)
    staff_name.grid()
    global update_butoon_for_staff
    update_butoon_for_staff=Button(show_employee_frame,text='Update Details',command=update_details_of_staff_member)
    update_butoon_for_staff.grid()

def show_employee():
    def back_to_main_page1():
        show_employee_frame.grid_forget()
        page1()
    page1_frame.grid_forget()

    global show_employee_frame
    show_employee_frame=Frame(tk)
    show_employee_frame.grid(padx=50,pady=50)

    label=Label(show_employee_frame,text='Nom\t\t\tSalaire\t\t\tPosition\t\t\tmot de passe',font='bold')
    label.grid(row=0)

    details=backend.show_employees()

    for i in details:
        label=Label(show_employee_frame,text="{}\t\t\t{}\t\t\t{}\t\t\t{}".format(i[0],i[1],i[2],i[3]))
        label.grid(pady=4)

    button=Button(show_employee_frame,text='Quitter',command=back_to_main_page1,width=20,height=2,bg='red',font='bold')
    button.grid()

    mainloop()

def Total_money():
    def back_to_main_page1_from_total_money():
        all_money.grid_forget()
        page1()

    page1_frame.grid_forget()

    all=backend.all_money()

    global all_money
    all_money=Frame(tk)
    all_money.grid(padx=500,pady=300)

    label=Label(all_money,text="Total Amount of money")
    label.grid(row=0,pady=6)

    label=Label(all_money,text='{}'.format(all))
    label.grid(row=1)

    button=Button(all_money,text="Back",command=back_to_main_page1_from_total_money,width=15,height=2)
    button.grid(row=3)

    mainloop()

def back_to_main():
    page1_frame.grid_forget()
    global frame
    frame = Frame(tk, bg='#96c0eb')
    frame.grid(padx=500, pady=250)

    button = Button(frame, text="Admin", command=admin_login)
    button.grid(row=0, pady=20)

    button = Button(frame, text="Employee", command=employee_login)
    button.grid(row=1, pady=20)

    button = Button(frame, text="Quitter", command=tk.destroy)
    button.grid(row=2, pady=20)
    tk.mainloop()

    mainloop()

#mai page for admin
def page1():
    def back_to_main2():
        admin_frame.grid_forget()
        global frame
        frame = Frame(tk, bg='#96c0eb')
        frame.grid(padx=500, pady=250)

        button = Button(frame, text="Admin", command=admin_login)
        button.grid(row=0, pady=20)

        button = Button(frame, text="Employee", command=employee_login)
        button.grid(row=1, pady=20)

        button = Button(frame, text="Quitter", command=tk.destroy)
        button.grid(row=2, pady=20)
        tk.mainloop()

        mainloop()

    name=entry1.get()
    password=entry2.get()
    if len(name)!=0 and len(password)!=0:
        result=backend.check_admin(name,password)
        print(result)
        if result:
            admin_frame.grid_forget()

            global page1_frame
            page1_frame = Frame(tk, bg='#96c0eb')
            page1_frame.grid(padx=500, pady=200)

            button10 = Button(page1_frame, text="Nouvelle Employee", command=create_employee, width=20, height=2)
            button10.grid(row=0, pady=6)

            button11 = Button(page1_frame, text="Actualiser les detail", command=update_employee, width=20, height=2)
            button11.grid(row=1, pady=6)

            button13 = Button(page1_frame, text="Afficher tous les employee", command=show_employee, width=20, height=2)
            button13.grid(row=2, pady=6)

            button11 = Button(page1_frame, text="Total argent", command=Total_money, width=20, height=2)
            button11.grid(row=3, pady=6)

            button12 = Button(page1_frame, text="Retour", command=back_to_main, width=20, height=2)
            button12.grid(row=4, pady=6)

            mainloop()
        else:
            label=Label(admin_frame,text="Identifiant et mot de passe invalide")
            label.grid(row=6,pady=10)
            button=Button(admin_frame,text='Quitter',command=back_to_main2)
            button.grid(row=7)
            mainloop()
    else:
        label = Label(admin_frame, text="Veuillez remplir toutes les entrees")
        label.grid(row=6, pady=10)
        button = Button(admin_frame, text='Quitter', command=back_to_main2)
        button.grid(row=7)
        mainloop()

#Login form for employee
def employee_login():
    def back_to_main3():
        employee_frame.grid_forget()
        global frame
        frame = Frame(tk, bg='#96c0eb')
        frame.grid(padx=400, pady=250)

        button = Button(frame, text="Admin", command=admin_login)
        button.grid(row=0, pady=20)

        button = Button(frame, text="Employee", command=employee_login,bg='yellow',width=20, height=2,font=("Arial", 10, "bold"))
        button.grid(row=1, pady=20)

        button = Button(frame, text="Quitter", command=tk.destroy,bg='#red',width=20, height=2,font=("Arial", 10, "bold"))
        button.grid(row=2, pady=20)
        tk.mainloop()

        mainloop()
    def check_emp():
        name = entry1.get()
        password = entry2.get()
        if len(name) != 0 and len(password) != 0:
            result = backend.check_employee(name, password)
            print(result)
            if result:
                employee_frame.grid_forget()
                page2()
            else:
                label = Label(employee_frame, text="Mot de passe invalide",width=20, height=2,font=("Arial", 15, "bold"))
                label.grid(row=6, pady=10)
                button = Button(employee_frame, text='Quitter', command=back_to_main3,bg='red',width=20, height=2,font=("Arial", 10, "bold"))
                button.grid(row=7)

                mainloop()
        else:
            label = Label(employee_frame, text="veuillez remplir toutes les entrees",width=20, height=2,font=("Arial", 15, "bold"))
            label.grid(row=6, pady=10)
            button = Button(employee_frame, text='Quitter', command=back_to_main3,bg='red',width=20, height=2,font=("Arial", 10, "bold"))
            button.grid(row=7)

            mainloop()
    frame.grid_forget()

    global employee_frame
    employee_frame = Frame(tk, bg='#96c0eb')
    employee_frame.grid(padx=500, pady=200)

    label = Label(employee_frame, text="mot de passe Employee ", font='bold')
    label.grid(row=0, pady=20)

    label1 = Label(employee_frame, text="Nom:",width=20, height=2,font=("Arial", 15, "bold"))
    label1.grid(row=1, pady=10)

    label2 = Label(employee_frame, text="mot de passe:",width=20, height=2,font=("Arial", 15, "bold"))
    label2.grid(row=3, pady=10)
    global entry1
    global entry2
    entry1 = Entry(employee_frame)
    entry1.grid(row=2, pady=10)

    entry2 = Entry(employee_frame,show='*')
    entry2.grid(row=4, pady=10)

    button = Button(employee_frame, text="envoyé", command=check_emp,bg='#96c0eb',width=20, height=2,font=("Arial", 10, "bold"))
    button.grid(row=5, pady=20)
    button=Button(frame,text="Quitter",command=tk.destroy,bg='yellow',width=20, height=2,font=("Arial", 10, "bold"))
    button.grid(row=2,pady=20)
    mainloop()

#Login form for admin
def admin_login():
    frame.grid_forget()
    global admin_frame
    admin_frame = Frame(tk, bg='#96c0eb')
    admin_frame.grid(padx=500, pady=250)

    label = Label(admin_frame, text="Connexion Administrateur", font=("Arial", 20, "bold"))
    label.grid(row=0, pady=20)

    label1 = Label(admin_frame, text="Nom:",font=("Arial", 15, "bold"))
    label1.grid(row=1, pady=10)

    label2 = Label(admin_frame, text="mot de passe:",width=20, height=2,font=("Arial", 15, "bold"))
    label2.grid(row=3, pady=10,)
    global entry1
    global entry2
    entry1 = Entry(admin_frame)
    entry1.grid(row=2, pady=10)

    entry2 = Entry(admin_frame,show='*')
    entry2.grid(row=4, pady=10)

    button = Button(admin_frame, text="envoye",command=page1,bg='yellow',width=20, height=2,font=("Arial", 10, "bold"))
    button.grid(row=5, pady=20)
    mainloop()
global frame
frame=Frame(tk,bg='#96c0eb')
frame.grid(padx=500,pady=20)


button=Button(frame,text="Admin",command=admin_login,width=20, height=2,font=("Arial", 10, "bold"))
button.grid(row=0,pady=20)

button: Button=Button(frame,text="Employee",command=employee_login,bg='#96c0eb',width=20, height=2,font=("Arial", 10, "bold"))
button.grid(row=1,pady=20)

button=Button(frame,text="Quitter",command=tk.destroy,bg='red',width=20, height=2,font=("Arial", 10, "bold"))
button.grid(row=2,pady=20)
tk.mainloop()






