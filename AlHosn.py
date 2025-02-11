import datetime
#from dateutil.relativedelta import relativedelta

Person_Arr=[0,0,0,0,0,0]
PCR_Arr=[0,0,0,0,0,0,0,0,0,0,0,0]
Vacc_Arr=[0,0,0,0,0,0,0,0,0]

class PCR_Test:
 def __init__(self,Test_N,Test_R,Date_PCR,):
   self.Test_N=Test_N
   self.Test_R=Test_R
   self.Date_PCR=Date_PCR

 def PCR_ArrList():
   i=0
   with open("C:\\Users\\Versha\\OneDrive\\Desktop\\AlHosnApp\\PCR_info.txt", 'r') as f:
     for line in f:
       PCR_data = line.strip().split(',')
       PCR_Arr[i]=PCR_data
       i=i+1
   return PCR_Arr

 def Lat_pcr(eid):
     z=[]
     for i in range(12):
         if PCR_Arr[i][0] == eid:
             q=PCR_Arr[i][2]
             r=PCR_Arr[i][3]
         z.append(q)
         z.append (r)
         return z


class Vaccination:
 def __init__(self,Doses,V_N,D_V,):
   self.Doses=Doses
   self.V_N=V_N
   self.D_V=D_V

 def Vacc_ArrList():
   i=0
   with open("C:\\Users\\Versha\\OneDrive\\Desktop\\AlHosnApp\\Vaccination_info.txt", 'r') as f:
     for line in f:
       Vacc_data= line.strip().split(',')
       Vacc_Arr[i]=Vacc_data
       i=i+1
   return Vacc_Arr

 def Lat_vacc(eid):
   z=[]
   for i in range(9):
     if Vacc_Arr[i][0] == eid:
       q=Vacc_Arr[i][1]
       r=Vacc_Arr[i][2]
       s=Vacc_Arr[i][3]
   z.append(q)
   z.append (r)
   z.append (s)
   return z


class Person(Vaccination, PCR_Test):
 def __init__(self, name, PPN, EID, email, DOB, Age):
   self.name = name
   self.PPN = PPN
   self.EID = EID
   self.email = email
   self.DOB = DOB
   self.Age = Age

 def Person_ArrList():
   i=0
   with open("C:\\Users\\Versha\\OneDrive\\Desktop\\AlHosnApp\\Person_info.txt", 'r') as f:
       for line in f:
           person_data= line.strip().split(',')
           Person_Arr[i]=person_data
           i=i+1
   return Person_Arr

 def time_P(eid):                                           #time passed
   a=[]
   a=PCR_Test.Lat_pcr(eid)
   P_D = datetime.datetime.strptime(a[1],"%Y-%m-%d")
   now= datetime.datetime.today()
   n=now - P_D
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
       if (a[0] == 'Possitive'):
           color = 'red'
       elif ((now > end_P and now < end_V) or (now < end_P and now > end_V)):
           color = 'grey'
       elif (now < end_P and now < end_V):
           color = 'green'
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
