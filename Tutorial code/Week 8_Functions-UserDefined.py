#!/usr/bin/env python
# coding: utf-8

# In[2]:


def  square_root( sq_rand: float ) -> float:
    ret_val  =  sq_rand
    diff  =  sq_rand - ret_val*ret_val
    while  abs(diff) > 0.000001:
        diff  =  sq_rand - ret_val*ret_val
        ret_val  =  ret_val + (diff / 2.0)
        return  ret_val


# In[3]:


square_root(144)


# In[4]:


def display_welcome():

    """
    Returns string 'Welcome to MinMax'
    >>> display_welcome()
    'Welcome to MinMax!'
    """
    print("Welcome to MinMax!")
    
#This function is to set values for Universal Price Codes (UPC) per product to scan
def get_barcode(item_scanned):
    """
    (str) -> str
    Returns  the type of item that has been scanned based on the UPC of the item that has been scanned i.e. the "item_scanned" parameter

    >>>get_barcode('111111')
    'SINGLES'

    >>>get_barcode('666666')
    'SMALL'

    >>>get_barcode('242424')
    'LARGE'

    """
    if item_scanned == '111111':
        return 'SINGLES'
    elif item_scanned == '666666':
        return 'SMALL'
    elif item_scanned == '242424':
        return 'LARGE'
    elif item_scanned == '0':
        return 'done'
    else: print ("Oops! You entered an unrecognized Universal Price Code (UPC). Please enter an appropriate UPC for your item")



#This function calculates the subtotal as a running total, which updates each time an item is scanned
def calculate_subtotal(product_scanned):
    """
    (str) -> int
    Returns the subtotal of the customer's purchase before tax by using the price of the item that has been scanned
    (i.e. the parameter "product_scanned")which is determined by using the UPC_SINGLE, UPC_SMALL and UPC_LARGE variables

    >>> calculate_subtotal('111111')
    1

    >>> calculate_subtotal('666666')
    5

    >>> calculate_subtotal('242424')
    19

    """
    subtotal_before_tax = 0
    PRICE_SINGLE = 1
    PRICE_SMALL = 5
    PRICE_LARGE = 19
    UPC_SINGLE = '111111'
    UPC_SMALL = '666666'
    UPC_LARGE = '242424'
    if product_scanned == UPC_SINGLE:
        subtotal_before_tax +=PRICE_SINGLE
    elif product_scanned == UPC_SMALL:
        subtotal_before_tax +=PRICE_SMALL
    elif product_scanned == UPC_LARGE:
        subtotal_before_tax += PRICE_LARGE

    return subtotal_before_tax




#This function gets how much the customer gives i.e. input("enter your stuff")
def get_amount_tendered():
    """
    Returns either the end of this program or the value of the amount tendered by the customer by using an input prompt.
    If the cashier hits '0', the program is ended due to cancellation. If the customer provides any other value, this is
    captured as the amount tendered by the customer i.e. the 'amount_tendered' variable


    >>> get_amount_tendered(30)
    30

    >>> get_amount_tendered(40)
    40

    >>>get_amount_tendered(50)
    50

    >>>get_amount_tendered(0)
    Thanks for shopping at MinMax! You have cancelled your order. If you'd like to try again, please repeat the process and scan your items again.
    """

    amount_tendered = input("Using the total displayed, please pay the complete amount owed via cash only. If you'd like to cancel this purchase, just hit 0 again.")
    if amount_tendered == 0:
        return "end"
    else:
        return amount_tendered




#This function displays the change given to the customer
def display_change(total_bill,amount_tendered):
    """
    (float,float) -> float
    Returns the difference as the variable "difference" in value between total_bill and amount_tendered, thus indicating
    how much change is owed to the customer, or still owed to the MinMax store. The variable "difference" is formatted
    to return as a float with two decimal points, including zeroes (i.e. 10.50 instead of 10.5).

    "difference" is then rounded to the nearest 5 cents using the following nickel rounding scheme standard rules in Canada:
    0.01 to 0.02 will round down to 0.00. 0. 03 to 0.04 will round up to 0.05. 0.06 to 0.07 will round down to 0.05.
    0.08 to 0.09 will round up to 0.10

    >>> display_change(10.0,7.97)
    2.05

    >>> display_change(10.5,2.0)
    8.50

    >>> display_change(10.7,1.4)
    9.30
    """
    difference = abs(total_bill-amount_tendered)
    return (format(difference, '.2f'))

#This function calculates the total cost as a running total
def calculate_total_bill(subtotal):
    """
    (float) -> float

    subtotal is passed through as an input
    HST_RATE variable in this function is multiplied by inputted variable
    Function returns the resulting variable "total", rounded and formatted to 2 decimal points.
    Variable "total" is then rounded to the nearest 5 cents using the following nickel rounding scheme standard rules in Canada:
    0.01 to 0.02 will round down to 0.00. 0. 03 to 0.04 will round up to 0.05. 0.06 to 0.07 will round down to 0.05.
    0.08 to 0.09 will round up to 0.10


    >>> calculate_total_bill(3.0)
    3.40

    >>> calculate_total_bill(6.67)
    7.55

    >>> calculate_total_bill(2.05)
    2.30

    """
    HST_RATE = 1.13
    total_bill = subtotal *HST_RATE


    return format(round(0.05 * round(float(total_bill)/0.05), 2), '.2f')



#This function displays the final total bill
def display_totalbill():

# Returns a series of print functions for the total bill which includes: subtotal before tax, HST added to the bill, Total price before rounding to the nearest nickel, total price after rounding, payment from the customer , any change owed to the customer and a farewell greeting
#All values returned are displayed with two decimal points in the format of $0.00

    print("\nHere is your bill! \nSubtotal: $", format(subtotal_before_tax, '.2f'))
    print("HST: $", format(0.13 * subtotal_before_tax, '.2f'))
    print("Total price before rounding: $", format(subtotal_before_tax * 1.13, '.2f'))
    print("Total price after rounding: $", format(total_bill, '.2f'))
    print("Payment: $", format(amount_tendered, '.2f'))
    print("----------------\nChange: $", display_change(amount_tendered, total_bill))
    print("\nThank you for shopping with MinMax!")




#The main function starts here
if __name__ == "__main__":

#Sets the values of subtotal_before_tax and item to be used in the upcoming loops
    subtotal_before_tax = 0
    amount_tendered = 0
    item = True


#This displays the welcome sign to the MinMax Store
    display_welcome()

#This while loop represents the scanning input, the cashier will continue to scan items until he is done (i.e. hits 0)
    while get_barcode(item)!= 'done':
            item = input("Scan your items that you would like to purchase here, hit 0 when you're ready to finish up! ")
            subtotal_before_tax += calculate_subtotal(item)

# As the loop continues, the customer's subtotal so far will continue to accumulate and show on the screen for them to view
            print("Your subtotal so far is: $", format(subtotal_before_tax,'.2f'))

#Once the loop is over and 0 has been pressed (because 0 means done), the total price ('total_bill') after HST is shown to the customer
#'total_bill' is rounded to the nearest 5 cents using the nickel rounding scheme mentioned already

    total_bill = float(calculate_total_bill(subtotal_before_tax))
    print("\nAfter taxes, you owe: $",format(round(0.05 * round((total_bill) / 0.05), 2), '.2f'))


#Sets the value for the amount of change either owed by the customer or given to the customer
    amount_of_change = round(0.05*round(float(amount_tendered - total_bill)/0.05),2)


#This while loop represents the payment for the customer, it repeats until the full amount of the bill is paid  then thanks the customer and provides a final receipt
#All values returned are displayed with two decimal points in the format of $0.00

    while amount_of_change < 0:

            amount_tendered = float(get_amount_tendered())

#If customer enters 0, the the order is cancelled. The customer can repeat the process again by re-running the program.
            if amount_tendered == 0:
                sys.exit("Thanks for shopping at MinMax! You have cancelled your order. If you'd like to try again, please repeat the process and scan your items again.")

            amount_of_change = round(0.05*round(float(amount_tendered - total_bill)/0.05),2)

#If the amount tendered by the customer is less than the cost of the total bill, the customer is prompted to try again to pay full amount
            if amount_of_change < 0:
                print("Sorry about that! You are short by: $",format(abs(amount_of_change),'.2f'),"Please try again and enter the full amount of $",total_bill)

#If the customer pays the full amount owed on the total bill, the receipt of the total bill is displayed and the program ends
            elif amount_of_change == 0:
                print ("You've entered the full amount owed!")
                display_totalbill()
#If the customer pays more than the full amount owed on the total bill, the receipt of the total bil is displayed, change is given to the customer and the program ends.
            elif amount_of_change > 0:
                print ("\nHere is your change!: $",display_change(amount_tendered,total_bill))
                display_totalbill()







# In[ ]:




