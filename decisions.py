# Q1.Areas of Rectangles

def main():
    len1=float(input('Enter the length of the 1st rectangle:'))
    wid1=float(input('Enter the width of the 1st rectangle:'))
    len2=float(input('Enter the length of the 2nd rectangle:'))
    wid2=float(input('Enter the width of the 2nd rectangle:'))
    area1=len1*wid1
    area2=len2*wid2
    WhichOneIsLarger(area1,area2)

def WhichOneIsLarger(a1,a2):
    if a1>a2:
        print('Area1',a1,'>','Area2',a2)
    elif a1<a2:
        print('Area1',a1,'<','Area2',a2)
    else:
        print('Area1',a1,'=','Area2',a2)

main()

###########################################################################################

# Q2. Color Mixer

def main():
    color1=input('Enter one primary color:')
    color2=input('Enter another primary color:')
    if color1 not in ['red','blue','yellow'] or color2 not in ['red','blue','yellow'] :
        print('What you entered is not primary color!')
    else:
        mixColors(color1,color2)

def mixColors(c1,c2):
    if( c1=='red' and c2=='blue') or (c1=='blue' and c2=='red'):
        print('Mixing',c1,'and',c2,', you get purple.')
    elif (c1=='red' and c2=='yellow') or (c1=='yellow' and c2=='red'):
        print('Mixing',c1,'and',c2,', you get orange.')
    elif (c1=='blue' and c2=='yellow') or (c1=='yellow' and c2=='blue'):
        print('Mixing',c1,'and',c2,', you get green.')
    else:
        print("I don't know what you get mixing",c1,'and',c2)
main()

###########################################################################################

# Q3. Roman Numerals

def main():
    number=int(input('Please enter a number within the range of 1 through 10:'))
    NumberToRoman(number)  

def NumberToRoman(number):
    if number==1:
        print("Number 1 is Roman I.")
    elif number==2:
        print('Number 2 is Roman II.')
    elif number ==3:
        print('Number 3 is Roman III.')
    elif number==4:
        print('Number 4 is Roman IV.')
    elif number==5:
        print('Number 5 is Roman V.')
    elif number==6:
        print('Number 6 is Roman VI.')
    elif number==7:
        print('Number 7 is Roman VII.')
    elif number==8:
        print('Number 8 is Roman VIII.')
    elif number==9:
        print('Number 9 is Roman IX.')
    elif number==10:
        print('Number 10 is Roman X.')
    else:
        print('The number you entered is out of range!')

main()
