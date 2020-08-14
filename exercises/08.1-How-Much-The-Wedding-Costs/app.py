user_input = int(input('How many people are coming to your wedding?\n'))

if user_input < 51:
    price = 4000
elif user_input < 101:
    price = 10000
elif user_input < 201:
    price = 15000
else: 
    price = 20000

print('Your wedding will cost '+str(price)+' dollars')