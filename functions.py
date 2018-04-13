# Q1.Calories from fat and carbohydrates

FAT=9
CARB=4

def main():
    fat_grams=int(input('Enter the number of fat grams:'))
    carb_grams=int(input('Enter the number of carbs grams:'))
    count_calories(fat_grams,carb_grams)
def count_calories(fat,carbs):
    fat_calories=float(fat*FAT)
    carb_calories=float(carbs*CARB)
    total_calories=fat_calories+carb_calories
    print()
    print('Calories from fat=',format(fat_calories,'.2f'))
    print('Calories from carbs=',format(carb_calories,'.2f'))
    print('Total calories=',format(total_calories,'.2f'))
main()


###############################################################################

# Q2.Kilometers to miles

def main():
    kilo=float(input('Enter the number of kilometers:'))
    kilometers_to_miles(kilo)

def kilometers_to_miles(number):
    miles=number*0.621
    print(number,'kilometers is equal to',format(miles,'.2f'),'miles.')
main()

###############################################################################

# Q3.Sales Tax

def main():
    amount=float(input('Enter the amount of purchase:$'))
    print('Amount of purchase= $',format(amount,'.2f'))
    county_tax(amount)
    state_tax(amount)

def county_tax(purchase):
    tax_county=purchase*0.02
    print('County tax= $',format(tax_county,'.2f'))

def state_tax(purchase):
    tax_state=purchase*0.04
    print('State tax= $',format(tax_state,'.2f'))

main()

###############################################################################

# Q4. Stadium Seating

A_COST=15
B_COST=12
C_COST=9

def main():
    A_seat=int(input('Enter the number of A seats:'))
    B_seat=int(input('Enter the number of B seats:'))
    C_seat=int(input('Enter the number of C seats:'))
    ticket_income(A_seat,B_seat,C_seat)

def ticket_income(seatsA,seatsB,seatsC):
    incomeA=seatsA*A_COST
    incomeB=seatsB*B_COST
    incomeC=seatsC*C_COST
    total_income=incomeA+incomeB+incomeC
    print()
    print('Income from A seats = $',format(incomeA,'.2f'))
    print('Income from B seats = $',format(incomeB,'.2f'))
    print('Income from C seats = $',format(incomeC,'.2f'))
    print('Total income = $',format(total_income,'.2f'))

main() 

