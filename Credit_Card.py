import datetime
import random
while True:
    card_no = str(input('enter a credit card : '))
    if len(card_no)==16:
        print('valid no. ')
    else:
        print('invalid length')
    user_name = input('enter user name FN MN LN ').split()

    date=datetime.datetime.now()

    yyyy=int(input('please enter the year on your credit card'))
    yy=str(yyyy)
    if len(yy)==4:
        print('length of the year is valid')
    else:
        print('invalid length try again')
    if yyyy <date.year:
        print('your card not exist')
    else:
        print('year is valid')

    mm=int(input('please enter the month on your credit card'))
    if mm >12:
        print('invalid month, plz try again')
    else:
        print('valid month')
    if mm < date.month:
        print('month is not valid')
    else:
        print('valid month')
    
    CVV=str(input('enter your CVV'))
    if len(CVV)==4:
        print('valid CVV ')
        cvv_list=[]
        cvv_list.append(CVV)
    else:
        print('invalid cvv')
    
    mob_no=str(input('enter your valid mobile no. '))
    if len(mob_no)==10:
        print('valid no')
        mob=[]
        mob.append(mob_no)
    else:
        print('invalid no.')
    otp=[]
    a=random.randint(1000,9999)
    otp.append(a)
    print('OTP', a)
    details = {mob_no:{card_no:{CVV:user_name}}}
    print(details)
    
    pw=int(input(''))
