def welcoming_message():
    print(
        """
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie
Beverages
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

        """
)

welcoming_message()


menu_items = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
# ordered_items =[]
# how_many_items = Counter(ordered_items)
how_many_items = {item:0 for item in menu_items}
while True:
    user_order = input("> ")

    if user_order in menu_items:
        how_many_items[user_order] +=1
        print(f'** {how_many_items[user_order]} order of {user_order} have been added to your meal **')
    
    elif user_order == 'quit':
        break
    
    # Allow ordering items not on menu but giving custom reply and the chance to re-order
    else:
        print(f'This {user_order} isnt on the snakes_cafe menu. Kindly order again!')
        while True:
                choice = input('Would you like to order again? (Yes/No) ')
                if choice == 'Yes' or choice == 'yes':
                    user_order = input('> ')
                    if user_order in menu_items:
                        # occurance = how_many_items[user_order]
                        how_many_items[user_order] +=1
                        print(f'** {how_many_items[user_order]} order of {user_order} have been added to your meal **')

                elif choice == 'No' or choice == 'no':
                    break



# prinitng out a summary of the orders
print('summary of complete order',how_many_items)
    




