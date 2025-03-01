store = {'banana': 2.99, 'apple': 4.99, 'watermelon': 8.99, 'orange': 3.99}
izur_letter = ('a','e','o','i','o')
org = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
new_fruits = []
new_prices = []
x = 0
roles = ['owner', 'an owner', 'customer', 'a customer']
owner = input("Are you an owner or a customer? ").lower()
while owner not in roles:
    print("Invalid identification please try again!\n -Owner\n -Customer")
    owner = input("Are you an owner or a customer? ").lower()
if owner == 'owner' or owner == 'an owner':
    y = input("Would you like to add suply to your store? ")
    if y == 'yes':
        num_new_fruit = int(input("How many fruits would you like to add to your store? "))
        while x < num_new_fruit:
            new_fruit = input(f"What is the {org[x]} fruit that you would like to add to your store? ").lower()
            new_fruits.append(new_fruit)
            while new_fruit in store.keys():
                print("Sorry this item is already in the shop, please choose an item that is not in your supply!")
                new_fruit = input(f"What is the {org[x]} fruit that you would like to add to your store? ").lower()
            new_price = float(input(f"What is going to be the {new_fruit}'s price? "))
            new_prices.append(new_price)
            store[new_fruits[x]] = new_prices[x]
            x += 1

fruit = input('What fruit would you like to buy? ').lower()
a_an = 'an' if fruit[0] in izur_letter else 'a'

store_fruit = ", ".join(store.keys())
while fruit not in store:
    print(f'please pick a fruit that is available in the store!: \n{store_fruit}')
    fruit = input('please pick a fruit again ').lower()

price = store[fruit]
print(f"The price of {a_an} {fruit} is {price}$")
sale = price*0.8
membership = input("Do you have our membership? ")
if membership.lower() == 'yes':
    print(f"The price of {a_an} {fruit} after a sale is {sale:.2f}$")
else:
    sub_membership = input("would you like the be a member? ")
    if sub_membership.lower() == 'yes':
        print(f"Welcome! now the price of {a_an} {fruit} is {sale:.2f}$")
    else:
        print("Have a great day!")
