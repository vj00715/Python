#################################################################################(mysql connector)
from datetime import datetime
import mysql.connector as mysql
conn = mysql.connect(user='root',password='',host='localhost')
cursor = conn.cursor()
cursor.execute("use hms")
##################################################################################(admin)
class admin():
    def ad_insert(self):
        print('-'* 125)
        a = input("ENTER YOUR NAME.:")
        d = int(input("ENTER YOUR CONTACT.:"))
        b = input("ENTER YOUR USERNAME.:")
        c = input("ENTER YOUR PASSWORD.:")
        q = "insert into admin(ad_name,ad_uname,ad_pass,ad_contact) values('"+a+"','"+b+"','"+c+"','"+str(d)+"')"
        cursor.execute(q)
        conn.commit()
        print("INSERTED")
    def ad_update(self):
        print('-'* 125)
        a = input("ENTER YOUR NEW NAME.:")
        b = input("ENTER YOUR NEW USERNAME.:")
        c = input("ENTER YOUR NEW PASSWORD.:")
        d = int(input("ENTER YOUR NEW CONTACT.:"))
        e = int(input("ENTER YOUR ID IN WHICH YOU NEED TO MAKE CHANGE.:"))
        q = "update admin set ad_name='"+a+"',ad_uname='"+b+"',ad_pass='"+c+"',ad_contact='"+str(d)+"' where ad_id='"+str(e)+"'"
        cursor.execute(q)
        conn.commit()
        print("UPDATED")
    def ad_delete(self):
        print('-'* 125)
        e = int(input("ENTER ID YOU WANT DELETED"))
        q = "delete from admin where ad_id='"+str(e)+"'"
        cursor.execute(q)
        conn.commit()
        print("DELETED")
    def ad_dis(self):
        q = "select * from admin"
        cursor.execute(q)
        res = cursor.fetchall()
        print("DETAIL OF ADMIN")
        for i in res:
            print(i)
###################################################################################(emp)
class emp():
    def emp_insert(self):
        print('-'* 125)
        a = input("ENTER YOUR NAME.:")
        s = float(input("ENTER YOUR SALARY.:"))
        d = int(input("ENTER YOUR CONTACT.:"))
        b = input("ENTER YOUR USERNAME.:")
        c = input("ENTER YOUR PASSWORD.:")
        q = "insert into emp(emp_name,emp_salary,emp_contact,emp_uname,emp_upass) values('"+a+"','"+str(s)+"','"+str(d)+"','"+b+"','"+c+"')"
        cursor.execute(q)
        conn.commit()
        print("INSERTED")
    def emp_update(self):
        print('-'* 125)
        a = input("ENTER YOUR NAME.:")
        s = float(input("ENTER YOUR SALARY.:"))
        d = int(input("ENTER YOUR CONTACT.:"))
        b = input("ENTER YOUR USERNAME.:")
        c = input("ENTER YOUR PASSWORD.:")
        e = int(input("ENTER YOUR ID IN WHICH YOU NEED TO MAKE CHANGE.:"))
        q = "update emp set emp_name='"+a+"',emp_salary='"+str(s)+"',emp_contact='"+str(d)+"',emp_uname='"+b+"',emp_upass='"+c+"' where emp_id='"+str(e)+"'"
        cursor.execute(q)
        conn.commit()
        print("UPDATED")
    def emp_delete(self):
        print('-'* 125)
        e = int(input("ENTER ID YOU WANT DELETED.:"))
        q = "delete from emp where emp_id='"+str(e)+"'"
        cursor.execute(q)
        conn.commit()
        print("DELETED")
    def emp_dis1(self):
        print('-'* 125)
        q = "select * from emp"
        cursor.execute(q)
        res = cursor.fetchall()
        print("DETAIL OF EMPLOYEE")
        for i in res:
            print(i)
    def emp_dis2(self):
        print('-'* 125)
        q = "select emp_id,emp_name,emp_salary,emp_contact,emp_uname from emp"
        cursor.execute(q)
        res = cursor.fetchall()
        print("DETAIL OF EMPLOYEE")
        for i in res:
            print(i)
###################################################################################(user)
class bill():
    def b_dis(self):
        print('-'* 125)
        q = "select * from bill"
        cursor.execute(q)
        res = cursor.fetchall()
        print("DETAIL OF BILL")
        for i in res:
            print(i)
    def b_insert(self):
        print("NEW BILL")
        n = input("ENTER YOUR NAME.:")
        c = int(input("ENTER YOUR CONTACT.:"))
        s = float(input("ENTER YOUR PRICE.:"))
        r = int(input("ENTER THE ROOM NO OR PRESS '0' FOR NO ROOM..:"))
        h = int(input("HOURS CUSTOMER STAY IN ROOM.:"))
        q = "select rm_amount from room where rm_no='"+str(r)+"'"
        cursor.execute(q)
        f = cursor.fetchall()
        for i in f:
            g = i[0]
        p = g * h
        dl = datetime.now()
        d = float(input("ENTER YOUR DISCOUNT IN %.:"))
        d2 = d/100
        t = (s + float(p)) * d2
        t1 = (s + float(p)) - t
        q = "insert into bill(b_name,b_contact,b_amount,b_roomno,rm_hrs,rm_price,b_discount,b_total) values('"+n+"','"+str(c)+"','"+str(s)+"','"+str(r)+"','"+str(h)+"','"+str(p)+"','"+str(t)+"','"+str(t1)+"')"
        cursor.execute(q)
        conn.commit()
        print("BILL ADDED")
    def b_update(self):
        n = input("ENTER YOUR NAME.:")
        c = int(input("ENTER YOUR CONTACT.:"))
        r = int(input("ENTER YOUR ROOM NO..:"))
        q = "insert into bill(b_name,b_contact,b_roomno) values('"+n+"','"+str(c)+"','"+str(r)+"')"
        cursor.execute(q)
        conn.commit()
        print("BILL UPDATED")
    def b_delete(self):
        print('-'* 125)
        e = int(input("ENTER ID YOU WANT DELETED.:"))
        q = "delete from bill where b_id='"+str(e)+"'"
        cursor.execute(q)
        conn.commit()
        print("DELETED")
#############################################################################################################
class room():
    def rm_dis(self):
        print('-'* 125)
        q = "select * from room"
        cursor.execute(q)
        res = cursor.fetchall()
        print("DETAIL OF ROOM")
        for i in res:
            print(i)
    def rm_insert(self):
        f = input("ENTER YOUR FLOOR.:")
        d = datetime.now()
        print("1] FOR AC - SINGLE BED \n2] FOR AC - DOUBLE BED \n3] FOR NON-AC - SINGLE BED \n4] FOR NON-AC - DOUBLE BED")
        n = int(input("ENTER YOUR RESPONSE.:"))
        if(n == 1):
            t = 'FOR AC - SINGLE BED'
        elif(n == 2):
            t = 'FOR AC - DOUBLE BED'
        elif(n == 3):
            t = 'FOR NON-AC - SINGLE BED'
        elif(n == 4):
            t = 'FOR NON-AC - DOUBLE BED'
        else:
            t = 'not specified'
        p = float(input("ENTER YOUR AMOUNT.:"))
        q = "insert into room(rm_floor,rm_amount,rm_date,rm_type) values('"+f+"','"+str(p)+"','"+str(d)+"','"+str(t)+"')"
        cursor.execute(q)
        conn.commit()
        print("INSERTED")        
    def rm_update(self):
        print('-'* 125)
        f = input("ENTER YOUR FLOOR.:")
        d = datetime.now()
        print("1] FOR AC - SINGLE BED \n2] FOR AC - DOUBLE BED \n3] FOR NON-AC - SINGLE BED \n4] FOR NON-AC - DOUBLE BED")
        n = int(input("ENTER YOUR RESPONSE.:"))
        if(n == 1):
            t = 'FOR AC - SINGLE BED'
        elif(n == 2):
            t = 'FOR AC - DOUBLE BED'
        elif(n == 3):
            t = 'FOR NON-AC - SINGLE BED'
        elif(n == 4):
            t = 'FOR NON-AC - DOUBLE BED'
        else:
            t = 'not specified'
        p = float(input("ENTER YOUR AMOUNT.:"))
        r = int(input("ENTER ROOM NO. YOU WANT TO MAKE CHANGE IN.:"))
        q = "update room set rm_floor='"+f+"',rm_amount='"+str(p)+"',rm_date='"+str(d)+"',rm_type='"+str(t)+"' where rm_no='"+str(r)+"'"
        cursor.execute(q)
        conn.commit()
        print("UPDATED")
    def rm_delete(self):
        print('-'* 125)
        r = int(input("ENTER ROOM NO. YOU WANT DELETED.:"))
        q = "delete from room where rm_no='"+str(r)+"'"
        cursor.execute(q)
        conn.commit()
        print("DELETED")
#####################################################################################
class menu():
    def mu_dis(self):
        print("LIST OF MENU")
        q = "select * from menu"
        cursor.execute(q)
        f = cursor.fetchall()
        for i in f:
            print(i)
    def mu_insert():
        n = input("ENTER DISH NAME.:")
        p = float(input("ENTER THE FULL DISH PRICE.:"))
        hp = float(input("ENTER THE HALF DISH PRICE.:"))
        q = "insert into menu(mu_name,mu_price,mu_hprice) values('"+n+"','"+str(p)+"','"+str(hp)+"')"
        cursor.execute(q)
        conn.commit()
        print("MENU HAS BEEN ADDED")
    def mu_update():
        n = input("ENTER DISH NAME.:")
        p = float(input("ENTER THE FULL DISH PRICE.:"))
        hp = float(input("ENTER THE HALF DISH PRICE.:"))
        i = int(input("ENTER ID OF DISH U WANT CHANGE.:"))
        q = "update menu set mu_name='"+n+"',mu_price='"+str(p)+"',mu_hprice='"+str(hp)+"' where mu_id ='"+str(i)+"' "
        cursor.execute(q)
        conn.commit()
        print("MENU HAS BEEN UPDATED")
    def mu_delete():
        r = int(input("ENTER MENU ID YOU WANT DELETED.:"))
        q = "delete from menu where mu_id='"+str(r)+"'"
        cursor.execute(q)
        conn.commit()
        print("DELETED")
###################################################################################(class object)
a = admin()
e = emp()
b = bill()
r = room()
m = menu()
###################################################################################(program execute)
while(True):
    print('-'* 125)
    print("PRESS 1] FOR MENU\n      2] FOR ADMIN AND EMP\n      3] ROOM\n      4] BILLING\n      5] FOR EXIT !!!!")
    n1 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
    if(n1 == 1):
        m.mu_dis()
    elif(n1 == 2):
        print('-'* 125)
        print("PRESS 1] FOR ADMIN LOGIN\n      2] FOR EMPLOYEE LOGIN\n      3] FOR EXIT!!!")
        n2 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
        # admin task
        if(n2 == 1):
            q = "select ad_uname,ad_pass from admin"
            cursor.execute(q)
            res=cursor.fetchall()
            print("-"*125)
            uname = input("ENTER USERNAME.::")
            upass = input("ENTER PASSWORD.::")
            for i in res:
                un = i[0]
                up = i[1]
                if(uname == un and upass == up):
                    count = 1
                else:
                    count = 0
                    print("INVALID USERNAME AND PASSWORD")
                while(count == 1):
                    print("-"*125)
                    print("PRESS 1] YOUR ACCOUNT\n      2] EMPLOYEE\n      3] TO EXIT")
                    n3 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                    if(n3 == 1):
                        print("PRESS 1] TO SEE YOUR DETAILS\n      2] TO EDIT YOUR ACCOUNT DETAILS\n      3] TO EXIT")
                        n4 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                        if(n4 == 1):
                            a.ad_dis()
                        elif(n4 == 2):
                            a.ad_update()
                        elif(n4 == 3):
                            break
                        else:
                            print("YOUR INPUT IS INVALID")
                    elif(n3 == 2):
                        print("PRESS 1] TO DISPLAY EMPLOYEE DETAILS\n      2] TO ADD NEW EMPLOYEE\n      3] TO UPDATE EMPLOYEE DETAILS\n      4] TO REMOVE EMPLOYEE\n      5] TO EXIT")
                        n4 = int(input("ENTER YOUR RESPONSE TO3 ABOVE OPTIONS.:"))
                        if(n4 == 1):
                            e.emp_dis2()
                        elif(n4 == 2):
                            e.emp_insert()
                        elif(n4 == 3):
                            e.emp_update()
                        elif(n4 == 4):
                            e.emp_delete()
                        elif(n4 == 5):
                            break
                        else:
                            print("YOUR INPUT IS INVALID")
                    elif(n3 == 3):
                        break
                    else:
                        print("YOUR INPUT IS INVALID")
        # emp task
        elif(n2 == 2):
            q = "select emp_uname,emp_upass from emp"
            cursor.execute(q)
            res=cursor.fetchall()
            print("-"*125)
            uname = input("ENTER USERNAME.::")
            upass = input("ENTER PASSWORD.::")
            for i in res:
                un = i[0]
                up = i[1]
                while(uname == un and upass == up):
                    print("-"*125)
                    print("PRESS: 1] YOUR ACCOUNT(EMP)\n       2] ROOM DETAILS\n       3] MENU\n       4] EXIT")
                    n3 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                    if(n3 == 1):
                        print("""PRESS 1] TO SEE YOUR DETAILS\n      2] TO EDIT YOUR ACCOUNT DETAILS\n      3] TO EXIT""")
                        n4 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                        if(n4 == 1):
                            e.emp_dis1()
                        elif(n4 == 2):
                            e.emp_update()
                        elif(n4 == 3):
                            break
                        else:
                            print("YOUR INPUT IS INVALID")
                    elif(n3 == 2):
                        r.rm_dis()
                        print("DELETE : 0     UPDATE : 1       INSERT:2      EXIT:3")
                        n6 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                        if(n6 == 2):
                            r.rm_insert()
                        elif(n6 == 1):
                            r.rm_update()
                        elif(n6 == 0):
                            r.rm_delete()
                        elif(n6 == 3):
                            break
                        else:
                            print("YOUR INPUT IS INVALID")
                    elif(n3 == 3):
                        m.mu_dis()
                        print("DELETE : 0     UPDATE : 1       INSERT:2      EXIT:3")
                        n5 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
                        if(n5 == 2):
                            m.mu_insert()
                        elif(n5 == 1):
                            m.mu_update()
                        elif(n5 == 0):
                            m.mu_delete()
                        elif(n5 == 3):
                            break
                        else:
                            print("YOUR INPUT IS INVALID")
                    elif(n3 == 4):
                        break
                    else:
                        print("YOUR INPUT IS INVALID")
        elif(n2 == 3):
            break #
        else:
            print("YOUR INPUT IS INVALID")
    elif(n1 == 3):
        r.rm_dis()
    elif(n1 == 4):
        while(True):
            b.b_insert()
            print("DELETE : 0     UPDATE : 1       HISTORY:2       INSERT: 4     EXIT: 3")
            n7 = int(input("ENTER YOUR RESPONSE TO ABOVE OPTIONS.:"))
            if(n7 == 0):
                b.b_delete()
            elif(n7 == 1):
                b.b_update()
            elif(n7 == 2):
                b.b_dis()
            elif(n7 == 4):
                b.b_insert()
            elif(n7 == 3):
                break
    elif(n1 == 5):
        break
    else:
        print("YOUR INPUT IS INVALID")           