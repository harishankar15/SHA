import mysql.connector

#--------- DB CONNECTION
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='qpslogin'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE timesheet (name VARCHAR(255), start_time VARCHAR(5))")
# sql = "INSERT into timesheet (name,start_time) VALUES (%s, %s)"
# i = input("Enter name:")
# j = input("Enter the starttime:")
# k = (i,j)
# print(k)
#mycursor.execute(sql,k)
#mydb.commit()
# print(f"{i} yours start time {j} is recorded")

#------------ FETCHING THE DATA IN DB
mycursor.execute("SELECT name FROM timesheet")

myresult = mycursor.fetchall()
ab = ', '.join([' '.join(sub) for sub in myresult]).split(', ') #spliting the elements in list
print(ab)
# for y in myresult:
#     print(y)
#     for x in y:
#         print(x)
for x in ab:
    if x == 'hari':
        print(x)
        a = 9.52
        b = int(input("Quantity:"))
        sp_cost = float(a * b)
        print(sp_cost)
        gst_rate = float(5)
        cgst = sp_cost * ((gst_rate / 2) / 100)
        sgst = cgst
        amt = sp_cost + (cgst + sgst)
        print("CGST (@", (gst_rate / 2), "%) :", (cgst))
        print("SGST(@", (gst_rate / 2), "%) :", (sgst))
        print("Amount payable: ", (amt))
    elif x == 'aravind':
        print(x)
        a = 22.86
        b = int(input("Quantity:"))
        sp_cost=float(a*b)
        print(sp_cost)
        gst_rate=float(5)
        cgst=sp_cost*((gst_rate/2)/100)
        sgst=cgst
        amt=sp_cost+(cgst+sgst)
        print("CGST (@",(gst_rate/2),"%) :",(cgst))
        print("SGST(@",(gst_rate/2),"%) :",(sgst))
        print("Amount payable: ",(amt))
