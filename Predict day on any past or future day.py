mc2={'1':(1,31),'2':(4,29),'3':(4,31),'4':(0,30),'5':(2,31),'6':(5,30),'7':(0,31),'8':(3,31),'9':(6,30),'10':(1,31),'11':(4,31),'12':(6,31)}
mc1={'January':mc2['1'],'February':mc2['2'],'March':mc2['3'],'April':mc2['4'],'May':mc2['5'],'June':mc2['6'],'July':mc2['7'],'August':mc2['8'],'September':mc2['9'],'October':mc2['10'],'November':mc2['11'],'December':mc2['12']}
#print(type(mc1))
#print(type(mc2))
dc=int(input('Enter date: \t\t\t\t\t'))
#asking month
month=input('Enter the month (Full NAME / Month number): \t')
month=month.capitalize()
#month code calculation
if month in mc1:
    mc=mc1[month][0]
elif month in mc2:
    mc=mc2[month][0]
else:
    raise NameError('No such Month number or Month NAME exist. Please check spelling!!!!!!!!!!!!')
#print(dc,type(dc))
#asking year 
y=input('Enter year: \t\t\t\t\t')
#finding year code
y1=y[0]
y2=y[1]
y3=y[2]
y4=y[3]
yc=int(y3+y4)
#print(yc,type(yc))
#checking date:

#finding century code
cent=int(y1+y2)
if cent==19:
    print('Century: \t\t\t\t\t20th Century')
    cc=0
elif cent==20:
    print('Century: \t\t\t\t\t21st Century')
    cc=6
#calculation for leap year
lp=0
if yc%4==0:
    print('\t\t\t\t\t\tLeap year')
    if month in mc1:
        if dc>mc1[month][1]:
            raise NameError('Wrong date!!!!!!!!!!!!!')
    if month in mc2:
        if dc>mc2[month][1]:
            raise NameError('Wrong date!!!!!!!!!!!!!')
    if month=='January' or month=='February':
        lp=-1
    elif month=='1' or month=='2':
        lp=-1
    else:
        lp=0
elif yc%4!=0:
    #checking date
    if month in mc1:
        if month=='February' or month=='2' and dc>mc1[month][1]-1:
            raise NameError('Wrong date!!!!!!!!!!!!!')
        elif dc>mc1[month][1]:
            raise NameError('Wrong date!!!!!!!!!!!!!')
    if month in mc2:
        if month=='February' or month=='2' and dc>mc2[month][1]-1:
            raise NameError('Wrong date!!!!!!!!!!!!!')
        elif dc>mc2[month][1]:
            raise NameError('Wrong date!!!!!!!!!!!!!')


#print(lp)
tt=dc+mc+yc+yc//4+lp+cc
day=tt%7
daylist=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
showday=daylist[day]
print('Day:\t\t\t\t\t       ',showday)

