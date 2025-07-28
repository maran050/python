print('                  تكليف الدكتور محسن')
while True:
    x=int(input('select the question number from 1 to 7: '))
    match x:
#السوال الاول : اطلب من المستخدم إدخال رقم ثم قم بتحديد إذا كان زوجي ام فردي  
        case 1:
            z=int(input('1-Source code  2-Run the code  :'))
            if z==1:
                print("""--------------------------------------------------

                num=int(input('Enter the number'))
                if num%2==0:
                    print("The number is even")
                else:
                    print('The number is odd')
                      
----------------------------------------------------""")
    
            else:
                num=int(input('Enter the number : '))
                if num%2==0:
                    print("The number is even")
                else:
                    print('The number is odd')
#السوال الثاني : اطلب من المستخدم إدخال ثلاث ارقام ثم قم بتحديد اكبر عدد بينهم
        case 2:
            z=int(input('1-Source code  2-Run the code'))
            if z==1:
                print("""
---------------------------------------------
                n1=int(input('Enter the number'))
                n2=int(input('Enter the number'))
                n3=int(input('Enter the number'))
                if n1>n2 and n1>n3:
                    print(f'max ={n1}')
                elif n2>n3:
                     print(f'max ={n2}')
                else:
                     print(f'max ={n3}')
                      
-----------------------------------------------

""")
            else:  
                n1=int(input('Enter the number'))
                n2=int(input('Enter the number'))
                n3=int(input('Enter the number'))
                if n1>n2 and n1>n3:
                    print(f'max ={n1}')
                elif n2>n3:
                     print(f'max ={n2}')
                else:
                     print(f'max ={n3}')
#السؤال الثالث: اطلب من المستخدم ادخال درجات 5 مواد ,ثم احسب المتوسط وحدد التقدير

        case 3:
            z=int(input('1-Source code  2-Run the code'))
            if z==1:
                print("""
-------------------------------------
                sum=0
                for i in range(5):
                    grt=int(input('Enter the grt:'))
                    sum+=grt
                v=sum/5
                if v>90:
                    print('Exland')
                elif v>=80 and v<90:
                    print('very good')
                elif v>=70 and v<80:
                    print('good')
                else:
                    print('fild')
--------------------------------------
""")
            else:
                sum=0
                for i in range(5):
                    grt=int(input('Enter the grt: '))
                    sum+=grt
                v=sum/5
                if v>90:
                    print('Exland')
                elif v>=80 and v<90:
                    print('very good')
                elif v>=70 and v<80:
                    print('good')
                else:
                    print('fild')
# السؤال الرابع : اطلب من المستخدم ادخال جملة ثم احسب عدد الكلمات فيها
        case 4:
            z=int(input('1-Source code  2-Run the code  :'))
            if z==1:
                print('''
-------------------------------------------
                texet=input('Enter the syntex :')
                print(len(texet.split()))
-------------------------------------------

                       ''')
            else:
                texet=input('Enter the syntex  :')
                print(len(texet.split()))
#   يدخلها المستخدم n,احسب مجموع الاعداد الزوجية ومجموع الاعداد الفردية   n السؤال الخامس : من 1 الى 
        case 5:
            z=int(input('1-Source code  2-Run the code  :'))
            if z==1:
                print('''
-------------------------------------------------------
                n=int(input('Enter the number :'))
                marital=0
                individual=0
                for i in range(1,n+1):
                    if i%2==0:
                        marital+=i
                    else:
                        individual+=i
                print(f'Total marital numbers={marital}')
                print(f'Total individual numbers={individual}')
---------------------------------------------------------
''')
            else:
                n=int(input('Enter the number :'))
                marital=0
                individual=0
                for i in range(1,n+1):
                    if i%2==0:
                        marital+=i
                    else:
                        individual+=i
                print(f'Total marital numbers={marital}')
                print(f'Total individual numbers={individual}')
# السؤال السادس : اطلب من المستخدم ادخال جملة ثم احسب عدد الحروف الكبيره وعدد الحروف الصغيره وعدد الارقام وعدد المسافات 
        
        case 6:
            z=int(input('1-Source code  2-Run the code  :'))
            if z==1:
                print('''
-----------------------------------------------------
                texet=input('Enter the syntax  :')
                bigletter=0
                small=0
                spec=0
                number=0
                for i in texet:
                    if i.isupper():
                        bigletter+=1
                    elif i.islower():
                        small+=1
                    elif i==' ':
                        spec+=1
                    else:
                        number+=1
                print(bigletter)
                print(small)
                print(spec)
                print(number)
--------------------------------------------------------

''')
            else:
                texet=input('Enter the syntax  :')
                bigletter=0
                small=0
                spec=0
                number=0
                for i in texet:
                    if i.isupper():
                        bigletter+=1
                    elif i.islower():
                        small+=1
                    elif i==' ':
                        spec+=1
                    else:
                        number+=1
                print(bigletter)
                print(small)
                print(spec)
                print(number)
#السؤال السابع : ترتيب 3 ارقام من الاكبر الى الاصغر  بدون استخدام دوال جاهزه 
        case 7:
            z=int(input('1-Source code  2-Run the code  :'))
            if z==1:
                print('''
-----------------------------------------------
                      
                ls=[]
                for i in range(3):
                    num=int(input('Enter the number :'))
                    ls+=[num]
                for i in range(3):
                    for j in range(3):
                        if x[i]>x[j]:
                           temp=x[i]
                           x[i]=x[j]
                           x[j]=temp
                print(x)

-----------------------------------------------
''')
            else:
                ls=[]
                for i in range(3):
                    num=int(input('Enter the number :'))
                    ls+=[num]
                for i in range(3):
                    for j in range(3):
                        if x[i]>x[j]:
                           temp=x[i]
                           x[i]=x[j]
                           x[j]=temp
                print(x)
        case _:
            print("There is no question with this number")


