from AlHosn import Person, Vaccination, PCR_Test, AlHosn
from random import randint
import tkinter as tk
from tkinter import *
import smtplib
import datetime

person = AlHosn.Person_ArrList()
vaccination = AlHosn.Vacc_ArrList()
pcrtest = AlHosn.PCR_ArrList()

Person_Arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PCR_Arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Vacc_Arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class PCR_Test:
   def __init__(self, Test_N, Test_R, Date_PCR, ):
       self.Test_N = Test_N
       self.Test_R = Test_R
       self.Date_PCR = Date_PCR

   def PCR_ArrList(self):
       i = 0
       with open("C:\\Users\\Versha\\Downloads\\PCR_info_new.txt",'r') as f:
           for line in f:
               PCR_data = line.strip().split(',')
               PCR_Arr[i] = PCR_data
               i = i + 1
       return PCR_Arr

   def Lat_pcr(eid):
       z = []
       for i in range(12):
           if PCR_Arr[i][0] == eid:
               q = PCR_Arr[i][2]
               r = PCR_Arr[i][3]
       z.append(q)
       z.append(r)
       return z

class Vaccination:
   def __init__(self, Doses, V_N, D_V, ):
       self.Doses = Doses
       self.V_N = V_N
       self.D_V = D_V

   def Vacc_ArrList(self):
       i = 0
       with open("C:\\Users\\Versha\\OneDrive\\Desktop\\AlHosnApp\\Vaccination_info_new.txt", 'r') as f:
           for line in f:
               Vacc_data = line.strip().split(',')
               Vacc_Arr[i] = Vacc_data
               i = i + 1
       return Vacc_Arr

   def Lat_vacc(eid):
       z = []
       for i in range(9):
           if Vacc_Arr[i][0] == eid:
               q = Vacc_Arr[i][1]
               r = Vacc_Arr[i][2]
               s = Vacc_Arr[i][3]
       z.append(q)
       z.append(r)
       z.append(s)
       return z


class Person(Vaccination, PCR_Test):
   def __init__(self, name, PPN, EID, email, DOB, Age):
       self.name = name
       self.PPN = PPN
       self.EID = EID
       self.email = email
       self.DOB = DOB
       self.Age = Age

   def Person_ArrList(self):
       i = 0
       with open("C:\\Users\\Versha\\OneDrive\\Desktop\\AlHosnApp\\Person_info_new.txt",'r') as f:
           for line in f:
               person_data = line.strip().split(',')
               Person_Arr[i] = person_data
               i = i + 1
       return Person_Arr

   def time_P(eid):  # time passed
       a = []
       a = PCR_Test.Lat_pcr(eid)
       P_D = datetime.datetime.strptime(a[1], "%Y-%m-%d")
       now = datetime.datetime.today()
       n = now - P_D
       return n.days


class AlHosn(Person):
   def dis_name(eid):
       for i in range(6):
           if (Person_Arr[i][2] == eid):
               name = Person_Arr[i][0]
       return name

   def dis_PPN(eid):
       for i in range(6):
           if (Person_Arr[i][2] == eid):
               PPN = Person_Arr[i][1]
       return PPN

   def dis_DOB(eid):
       for i in range(6):
           if (Person_Arr[i][2] == eid):
               DOB = Person_Arr[i][4]
       return DOB

   def cal_color(eid):
       a = []
       a = PCR_Test.Lat_pcr(eid)
       P_D = datetime.datetime.strptime(a[1], "%Y-%m-%d")
       now = datetime.datetime.today()
       end_P = P_D + datetime.timedelta(days=30)
       end_V = P_D + relativedelta(months=6)
       if ((now > end_P and now < end_V) or (now < end_P and now > end_V)):
           color = 'grey'
       elif (now < end_P and now < end_V):
           color = 'green'
       elif (a[0] == 'Possitive'):
           color = 'red'
       return color

   def dis_pcr(eid):
       z = []
       j = []
       for i in range(12):
           if (PCR_Arr[i][0] == eid):
               w = PCR_Arr[i][2]
               e = PCR_Arr[i][3]
               j = [w, e]
               z.append(j)
       return z

   def dis_vacc(eid):
       z = []
       j = []
       for i in range(9):
           if Vacc_Arr[i][0] == eid:
               q = Vacc_Arr[i][1]
               r = Vacc_Arr[i][2]
               s = Vacc_Arr[i][3]
               j = [q, r, s]
               z.append(j)
       return z


def age_positive_details():
   P1 = PCR_Test
   P1.PCR_ArrList(P1)
   P2 = Person
   P2.Person_ArrList(P2)
   a = 65
   flag = 0
   x = len(PCR_Arr)
   y = len(Person_Arr)
   print('Details of users above the age of 65 and who have tested positive:')
   for i in range(x):
       if PCR_Arr[i][1] >= str(a):
           if PCR_Arr[i][2] == 'Positive':
               for j in range(y):
                   if Person_Arr[j][2] == PCR_Arr[i][0]:
                       flag = 1
                       print(Person_Arr[j])
   if flag == 0:
       print('No users above the age of 65 who have tested positive currently.')


def disp_count():
   first = second = booster = 0
   for i in range(len_Vacc):
       if Vacc_Arr[i][1] == 'First':
           first = first + 1
       elif Vacc_Arr[i][1] == 'Second':
           second = second + 1
       elif Vacc_Arr[i][1] == 'Booster':
           booster = booster + 1

   print('First Dose: ' + str(first))
   print('Second Dose: ' + str(second))
   print('Booster Dose : ' + str(booster))


def booster_dose():
   print('EID of people who have received their booster dose : ')
   taken = []
   for i in range(len(Vacc_Arr)):

       if 'Booster' == Vacc_Arr[i][1]:
           print('\n' + Vacc_Arr[i][0])


def disp_info(eid):
   for i in range(len(Person_Arr)):
       if eid == Person_Arr[i][2]:
           print('\n\nDetails : ')
           print('\nName : ' + str(Person_Arr[i][0]))
           print('\nPassport Number : ' + str(Person_Arr[i][1]))
           print('\nEmirates ID : ' + str(Person_Arr[i][2]))
           print('\nEmail ID : ' + str(Person_Arr[i][3]))


def spec_vaccine(vaccine):
   taken = []
   for i in range(len(Vacc_Arr)):
       if vaccine == Vacc_Arr[i][2]:
           taken.append(Vacc_Arr[i][0])

   result = []
   for i in taken:
       if i not in result:
           result.append(i)

   print('The EID of people who have recieved ' + vaccine + ' vaccine are : \n')
   print(result)


def disp_positive():
   for i in range(len_PCR):
       if PCR_Arr[i][2] == 'Positive':
           for j in range(len_persons):
               if PCR_Arr[i][0] == Person_Arr[j][2]:
                   print('\n\nDetails : ')
                   print('\nName : ' + str(Person_Arr[j][0]))
                   print('\nPassport Number : ' + str(Person_Arr[j][1]))
                   print('\nEmirates ID : ' + str(Person_Arr[j][2]))
                   print('\nEmail ID : ' + str(Person_Arr[j][3]))


def send_reminder():
   V1 = Vaccination
   V1.Vacc_ArrList(V1)
   V2 = Person
   V2.Person_ArrList(V2)
   p = len(Vacc_Arr)
   l = len(Person_Arr)
   print('Users who have to take their booster shot: ')
   msg1 = 'Dear '
   msg = 'Reminder! It is time to take your Booster shot'
   for i in range(p):
       v = datetime.datetime.strptime(Vacc_Arr[i][3], "%Y-%m-%d")
       now = datetime.datetime.today()
       n = (now - v).days
       if n > 183:
           for j in range(l):
               if Person_Arr[j][2] == Vacc_Arr[i][0] and Vacc_Arr[i][1] == 'Second':
                   print(Person_Arr[j])
                   server = smtplib.SMTP('smtp.gmail.com', 587)
                   server.starttls()
                   server.login('f20200027@dubai.bits-pilani.ac.in', '].B!wC+3S')
                   name = Person_Arr[j][0]
                   server.sendmail('f20200027@dubai.bits-pilani.ac.in', Person_Arr[j][3], msg1 + name + ',' + '\n' + msg)


def admin_info():
   admin_ID = input('Enter admin ID : ')
   admin_password = input('Enter password : ')

   admin(admin_ID, admin_password)


def admin(a_id, a_pw):
   admins = {
       "Chris": "chris027",
       "Isha": "isha039",
       "Juwaria": "juwaria043",
       "Misbaah": "misbaah232"
   }

   access = 0
   x = admins.keys()
   tries = 1
   if a_id in x:
       while (tries <= 3):
           if admins[a_id] == a_pw:
               print("Access Granted")
               access = 1
               break

           else:
               print("Incorrect Password")
               tries = tries + 1

               if tries > 3:
                   print("3 Incorrect tries. *** ACCESS BLOCKED***")
                   break

               a_pw = input('Re-enter password : ')

   else:
       print("Admin User not found")
       again = int(input("Enter 1 to try again"))

       if again == 1:
           admin_info()

   if access == 1:
       admin_menu()


def admin_menu():
   cont = 1
   while cont == 1:
       print('********** ADMIN MENU **********')
       print('1.  To display the users who are above the age of 65 and tested positive. ')
       print('2. To display EID of people who have recieved their booster dose ')
       print('3. To display the total number of people who took each of the doses')
       print(
           '4. To display the EID of people who took a specific vaccine according to user input (Coaxin, sinopharm or pfizer)')
       print('5. To display personal details of a person taking emirates ID as input ')
       print('6. To display the details of people who tested positive')
       print('7. To send reminder mail to get the booster dose when 6 months have exceeded after second vaccine')
       print('0. Exit')
       print('-----------------------------------')

       c = int(input('Enter choice: '))

       if c == 1:
           age_positive_details()
       elif c == 2:
           booster_dose()
       elif c == 3:
           disp_count()
       elif c == 4:
           inp_vaccine = input('Enter vaccine name (Sinopharn, Pfizer, Covaxin) : ')
           spec_vaccine(inp_vaccine)
       elif c == 5:
           inp_eid = input('Enter EID : ')
           disp_info(inp_eid)
       elif c == 6:
           disp_positive()
       elif c == 7:
           send_reminder()
       else:
           cont = 0
           print('--------SESSION OVER---------')
           break


def set_eid(eid):
   global emirates_id
   emirates_id = eid


def get_eid():
   return emirates_id


def get_date(string):
   s = string.split("-")
   m = s[1]
   if m == '01':
       m = 'Jan'
   elif m == '02':
       m = 'Feb'
   elif m == '03':
       m = 'Mar'
   elif m == '04':
       m = 'Apr'
   elif m == '05':
       m = 'May'
   elif m == '06':
       m = 'Jun'
   elif m == '07':
       m = 'Jul'
   elif m == '08':
       m = 'Aug'
   elif m == '09':
       m = 'Sep'
   elif m == '10':
       m = 'Oct'
   elif m == '11':
       m = 'Nov'
   elif m == '12':
       m = 'Dec'
   date = s[2] + ' ' + m + ' ' + s[0]
   return date


def show_details(eid, hide):
   ppn = ''
   dob = ''
   eid_hidden = ''
   ppn_hidden = ''
   dob_hidden = ''
   for i in range(len(person)):
       for j in range(len(person[i])):
           if eid == person[i][2]:
               ppn = person[i][1]
               dob = person[i][4]
               break
   if hide:
       for i in range(len(eid)):
           if i > 8 and i < 16:
               eid_hidden = eid_hidden + '*'
           else:
               eid_hidden = eid_hidden + eid[i]
       for i in range(len(ppn)):
           if i > 3:
               ppn_hidden = ppn_hidden + '*'
           else:
               ppn_hidden = ppn_hidden + ppn[i]
       for i in range(len(dob)):
           dob_hidden = dob_hidden +'*'
   if hide:
       return eid_hidden, ppn_hidden, dob_hidden
   else:
       return eid, ppn, dob


def calc_color(pcr_test_info):
   now = str(datetime.datetime.now().date())
   lat_pcr = pcr_test_info[3]
   now_y, now_m, now_d = now.split("-")
   lat_pcr_y, lat_pcr_m, lat_pcr_d = lat_pcr.split("-")
   date_now = datetime.date(int(now_y),int(now_m),int(now_d))
   date_lat_pcr = datetime.date(int(lat_pcr_y),int(lat_pcr_m),int(lat_pcr_d))
   no_of_days = date_now - date_lat_pcr
   nod = no_of_days.days
   if nod > 30 and pcr_test_info[2] == 'Negative':
       color = 'grey'
   elif pcr_test_info[2] == 'Positive':
       color = 'red'
   elif pcr_test_info[2] == 'Negative':
       color = 'light green'
   return nod, color


def al_hosn():
   green_pass = tk.Tk()
   green_pass.title('Green Pass')
   green_pass.configure(bg='light green')
   info = tk.Frame(green_pass)
   info.config(bg='white', bd=4, relief='sunken', height=400, width=400)
   info.pack(padx=20, pady=10)
   vacc = tk.Frame(green_pass)
   vacc.config(bg='white', bd=2, relief='sunken', height=400, width=400)
   vacc.pack(side='bottom', anchor='sw', padx=20, pady=10)
   pcr = tk.Frame(green_pass)
   pcr.config(bg='white', bd=2, relief='sunken', height=400, width=400)
   pcr.pack(side='bottom', anchor='sw', padx=20, pady=10)
   latest_pcr = tk.Frame(green_pass)
   latest_pcr.config(bg='white', bd=2, relief='sunken', height=400, width=400)
   latest_pcr.pack(anchor='center', padx=20, pady=10)
   eid = get_eid()
   for i in range(len(person)):
       if person[i][2] == eid:
           name = Label(info, text=person[i][0], font=("Arial", "15"), bg='white')
           name.pack(expand=False, padx=10, pady=10)
           eid1, ppn1, dob1 = show_details(eid, True)
           emid = Label(info, text='EID: ' + eid1, font=('Arial', 10, 'bold'), bg='white')
           emid.pack()
           ppn = Label(info, text='PPN: ' + ppn1, font=('Arial', 10, 'bold'), bg='white')
           ppn.pack()
           dob = Label(info, text='DOB: ' + dob1, font=('Arial', 10, 'bold'), bg='white')
           dob.pack()

           msg = 'For medical use only\n\n\n'
           for i in range(len(vaccination)):
               if eid == vaccination[i][0]:
                   msg = msg + vaccination[i][1] + " Dose - "
                   msg = msg + get_date(vaccination[i][3]) + '\n' + vaccination[i][2] + '\n'
           vacc_res = Text(vacc, height=10, width=30)
           vacc_res.pack()
           vacc_res.insert('end', msg)
           vacc_res.config(state='disabled')

           msg1 = 'Previous Results\n\n\n'
           for k in range(len(pcrtest)):
               if eid == pcrtest[k][0]:
                   msg1 = msg1 + get_date(pcrtest[k][3]) + '\n' + 'PCR ' + pcrtest[k][2]+ '\n'
           pcr_res = Text(pcr, height=10, width=30)
           pcr_res.pack()
           pcr_res.insert('end', msg1)
           pcr_res.config(state='disabled')

           pcr_tests = []
           pcr_test_info = []
           for m in range(len(pcrtest)):
               if eid == pcrtest[m][0]:
                   pcr_tests.append(pcrtest[m])
           latest = pcr_tests[0][3]
           pcr_test_info = pcr_tests[0]
           for j in range(len(pcr_tests)):
               if pcr_tests[j][3] > latest:
                   latest = pcr_tests[j][3]
                   pcr_test_info = pcr_tests[j]
           nod, color = calc_color(pcr_test_info)
           msg2 = str(nod) + ' Days - PCR ' + pcr_test_info[2] + '\n'
           msg2 = msg2 + 'Since ' + get_date(pcr_test_info[3])
           lpcr = Label(latest_pcr, text=msg2, font=("Arial", 10, "bold"), bg=color)
           lpcr.pack()
   green_pass.mainloop()


def printeid():
   global entry
   eid = entry.get()
   set_eid(eid)
   count = 0
   receiver = 'c'
   P1 = Person
   P1.Person_ArrList(P1)
   x = len(Person_Arr)
   for a in range(x):
       if eid.__eq__(Person_Arr[a][2]):
           receiver = Person_Arr[a][3]
           openNewWindow(receiver)
       else:
           count = count + 1
   if count == x:
       popup = Tk()
       popup.geometry("250x50")
       popup.title("Incorrect EID")
       txt = Label(popup, text="PLEASE ENTER VALID EID", font=("Arial", "10"))
       txt.pack()


def callback(r):
   w.destroy()
   openNewWindow(r)


def random_otp(n):
   range_start = 10 ** (n - 1)
   range_end = (10 ** n) - 1
   return randint(range_start, range_end)


def send_otp(r):  # r is the email id of receiver
   i = random_otp(6)
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(<mail>, <Password>)
   server.sendmail(<mail>, r, 'This mail is sent using python.\n you otp is ' + str(i))
   print('OTP sent')
   return i


def printresult(i):
   otp = e.get()
   if i == int(otp):
       print('Entry successful!')
       w.destroy()
       window.destroy()
       al_hosn()
   else:
       popup1 = Tk()
       popup1.geometry("250x50")
       popup1.title("Error")
       txt = Label(popup1, text="Incorrect OTP. Try again", font=("Arial", "10"))
       txt.pack()


def openNewWindow(r):
   s = send_otp(r)
   global w
   w = tk.Toplevel()
   w.geometry("230x75")
   w.title("Enter otp")
   message = Label(w, text="Enter 6-digit otp", font=("Arial", "10"))
   message.grid(row=1,column=1)
   global e
   e = Entry(w)
   e.grid(row=1,column=2)
   b = Button(w, text='Submit', command=lambda: printresult(s))
   b.grid(row=3, column=1)
   resend = Button(w, text='Resend OTP', command=lambda: callback(r))
   resend.grid(row=3,column=2)

def user_window():
   global window
   window = tk.Toplevel()
   window.title("Welcome to Al-Hosn!")
   window.geometry("300x100")
   window.configure(bg='cyan')
   ts = Label(window, text="Enter your Emirates ID", bg='white')
   ts.pack()
   tp = Label(window, text=" ", bg='cyan')
   tp.pack()
   global entry
   entry = Entry(window)
   entry.pack()
   tz = Label(window, text=" ", bg='cyan')
   tz.pack()
   button = Button(window, text="Next", command=lambda: printeid(), bg='white')
   button.pack()


menu = tk.Tk()
menu.title('Al-Hosn App')
menu.geometry("250x150")
menu.configure(bg='cyan')
mm = tk.Label(text="--Welcome to Al-Hosn!--", bg='white',font=("FreeSerif","10"))
mm.grid(row=1,column=2)
z = tk.Label(text=" ", bg='cyan')
z.grid(row=2,column=2)
admin = Button(menu, text='Admin', command=lambda: admin_info(), bg='white', height=5, width=10)
admin.grid(row=3,column=2)
user = Button(menu, text='User', command=lambda: user_window(),bg='white', height = 5, width =10)
user.grid(row=3,column=4)

menu.mainloop()
quit()

def user_window():
   global window
   window = tk.Toplevel()
   window.title("Welcome to Al-Hosn!")
   window.geometry("300x100")
   window.configure(bg='cyan')
   ts = Label(window, text="Enter your Emirates ID", bg='white')
   ts.pack()
   tp = Label(window, text=" ", bg='cyan')
   tp.pack()
   global entry
   entry = Entry(window)
   entry.pack()
   tz = Label(window, text=" ", bg='cyan')
   tz.pack()
   button = Button(window, text="Next", command=lambda: printeid(), bg='white')
   button.pack()


menu = tk.Tk()
menu.title('Al-Hosn App')
menu.geometry("250x150")
menu.configure(bg='cyan')
mm = tk.Label(text="--Welcome to Al-Hosn!--", bg='white',font=("FreeSerif","10"))
mm.grid(row=1,column=2)
z = tk.Label(text=" ", bg='cyan')
z.grid(row=2,column=2)
adm = Button(menu, text='Admin', command=lambda: admin_info(), bg='white', height=5, width=10)
adm.grid(row=3,column=2)
user = Button(menu, text='User', command=lambda: user_window(),bg='white', height = 5, width =10)
user.grid(row=3,column=4)

menu.mainloop()
quit()
