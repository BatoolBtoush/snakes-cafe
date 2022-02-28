from ast import Pass, While


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
how_many_items = 0
ordered_items =[]

while True:
    user_order = input("> ")
    ordered_items.append(user_order)


    if user_order in menu_items and user_order not in ordered_items:
        print(f'** 1 order of {user_order} have been added to your meal **')
        
    elif user_order in menu_items and user_order in ordered_items:
        how_many_items += 1
        print(f'** {how_many_items} order of {user_order} have been added to your meal **')
    
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
                        ordered_items.append(user_order)
                        how_many_items +=1
                        print(f'** {how_many_items} order of {user_order} have been added to your meal **')

                elif choice == 'No' or choice == 'no':
                    break



# prinitng out a summary of the orders
print('summary of complete order',ordered_items)
    




