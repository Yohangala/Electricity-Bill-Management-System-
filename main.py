import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="yohan12@34",
    database = "electricity"
  )
  

def showusers():
    c1 = db1.cursor()
    c1.execute("select * from users")
    res = c1.fetchall()
    #print(res)
    print("List of Users ")
    for val in res:
        print("UserName = "+val[0] + " Password = " + val[1])

def login():
    print("-" * 50)
    print("\t Electricity Bill Generation System")
    print("-" * 50)
    print("\t LOGIN")
    un = input("Enter User Name : ")
    pw = input("Enter Password : ")
    q = "select * from users where username = %s and passw = %s"
    val = (un,pw)
    c2 = db1.cursor()
    c2.execute(q,val)
    res = c2.fetchall()
    print("-" * 50)
    if len(res) == 0:
        print("Invalid User Name or Password ")
        print("-" * 50)
        return False
    else:
        print("Access Granted !!!")
        print("-" * 50)
        return True
def addcustomer():
  print("*" * 50)
  print("\tWelcome to Electricity Management")
  print("*" * 50)
  cid = input("Enter Customer Id : ")
  cname = input("Enter Customer Name : ")
  addr = input("Enter Address : ")
  phone = input("Enter Phone Number : ")
  email = input("Enter Email :")
  mtr = input("Enter meter no : ")
  cursor1 = db1.cursor()
  q = "insert into customer values (%s,%s,%s,%s,%s,%s)"
  val = (cid,cname,addr,phone,email,mtr)
  cursor1.execute(q,val)
  db1.commit()
  print("Customer Added Successfully")

def showcustomers():
  cur3 = db1.cursor()
  sqq="Select * from customer"
  cur3.execute(sqq)
  res = cur3.fetchall()
  for k in res:
    print(k)

def dell():
    cur2 = db1.cursor()
    dd=int(input("Enter CID to delete the record:"))
    cur2=db1.cursor()
    sq="delete from customer where cid='%d'" %dd
    cur2.execute(sq)
    db1.commit()
    print("Record Deleted Successfully!!")


def generatebill():
    c2 = db1.cursor()
    mtr = input("Enter Meter No .: ")
    dt = input("Enter the date of Bill Generation : ")
    cunits = int(input("Enter Current Units on Meter : "))
    punits = int(input("Enter Previous Units of Meter : "))
    consumed = cunits - punits
    if consumed < 200:
        bill = 4 * consumed
    elif consumed <400:
        bill = 6 * consumed
    else:
        bill = 8 * consumed
    print("Total Units Consumed ",consumed)
    print("Total Amount to be paid ",bill)
    duedt = input("Enter the Due Date of Payment : ")
    NO=input("Paid or Unpaid:")
    q = "insert into bill (meterno,billdate,current_units,previous_units,consumed,amount,duedate,paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(mtr,dt,cunits,punits,consumed,bill,duedt,NO)
    c2.execute(q,val)
    db1.commit()
    print("Values inserted Successfully !!!")
    
def showunpaid():
    cur4 = db1.cursor()
    sqq="Select * from bill where paid='Unpaid'"
    cur4.execute(sqq)
    res = cur4.fetchall()
    for k in res:
        print(k)

connect()
print("Connected")
if login():
    while True:
        print("-" * 50)
        print("\t CHOOSE AN OPERATION ")
        print("-" * 50)
        print("Press 1 - Add a New Customer")
        print("Press 2 - Delete an Existing Customer")
        print("Press 3 - Show all Customers")
        print("Press 4 - Generate the Bill")
        #print("Press 5 - Mark the Bill as Paid")
        print("Press 5 - Show All Unpaid Bills")
        print("Press 6 - Quit")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            addcustomer()
        elif ch == 2:
            dell()
            
        elif ch == 3:
            showcustomers()
        elif ch == 4:
            generatebill()
        #elif ch == 5:
           # paybill()
            print("Bill Paid")
        elif ch == 5:
            showunpaid()
            
        elif ch == 6:
            break
    
