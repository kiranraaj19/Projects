#declarations
category1 = {}
category2 = {}
category3 = {}
category4= {}
rooms_available_cat1,rooms_available_cat2,rooms_available_cat3,rooms_available_cat4,flag = 10,50,18,20,1

#functions
def booking(customer,rooms_available_cat1,rooms_available_cat2,rooms_available_cat3,rooms_available_cat4):
    if len(customer) == 1:
        if rooms_available_cat1 >0 :
            category1.update({len(category1)+1:customer})
            rooms_available_cat1 -= 1
        else :
            print("No rooms available")
    if len(customer) == 2:
        if rooms_available_cat2 >0 :
            for i in range(len(customer)):
                category2.update({len(category2)+1:customer[i]})
                rooms_available_cat2 -= 1
        else :
            print("No rooms available")
    if len(customer) == 3:
        if rooms_available_cat3 >0:
            for m in range(len(customer)):
                category3.update({len(category3)+1:customer[m]})
                rooms_available_cat3 -= 1
        else:
            print("No Rooms Available")
    if len(customer) == 4:
        if rooms_available_cat4 >0 :
            for n in range(len(customer)):
                category4.update({len(category4)+1:customer[n]})
                rooms_available_cat4 -= 1
        else:
            print("No Rooms available")
def rooms_info():
    print(category1)
    print(category2)
    print(category3)
    print(category4)
def Checkin_checkout(category,inp,category1,category2,category3,category4):
    if category == 1:
        print(category1[inp-1][3:])
    elif category == 2:
        print(category2[inp-1][3:])
    elif category == 3:
        print(category3[inp-1][3:])
    elif category == 4:
        print(category4[inp-1][3:])
    

def exit1():
    print(category1)
    print(category2)
    print(category3)
    print(category4)
    exit()

print("Welcome To Hotel KS")
print("1.Booking")
print("#Enter the details of the customers")
print("2.rooms info")
print("#Prints the rooms info in all categories")
print("3.Checkin checkout timings")
print("#Prints checkin and check out timing")
print("4.exit")

#switch case
while flag != 0:
    n = int(input("Choose from 1 - 4: \n"))
    if n == 1:    
        required_rooms = int(input("Enter the no. of rooms: "))
        customer = []
        for i in range(required_rooms):
            customer_name = input(f"Enter Customer name of customer{i+1}: ")
            customer_age = int(input(f"Enter Age of customer{i+1}: "))
            customer_gender = input(f"Enter Gender of customer{i+1}: ")
            customer_checkin = input(f"Enter Checkin of customer{i+1}: ")
            customer_checkout = input(f"Enter Checkout of customer{i+1}: ")
            customer.append([customer_name, customer_age, customer_gender,customer_checkin,customer_checkout])
        booking(customer,rooms_available_cat1,rooms_available_cat2,rooms_available_cat3,rooms_available_cat4) 
        customer = []   
    if n ==  2:
        rooms_info()
    if n == 3:
        category_inp = int(input("Enter The category: "))
        inp = input("Enter Room no alloted: ")
        Checkin_checkout(category_inp,inp,category1,category2,category3,category4)
    if n == 4:
        exit1()
    check = input("Do you want to perform more operations: ")
    if check == 0:
        flag = 0
    else:
        flag = 1
    
    
    
