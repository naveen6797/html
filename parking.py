import os
import time
import datetime
def two_wheeler_parking():
    customer_name = input("enter_customer_name:")
    vehicle_number = input("enter_vehicle_number:")
    vehicle_entry_time = datetime.datetime.now().strftime("%y,%m,%d,%H,%M")
    data = "{},{},\n{}".format(customer_name, vehicle_number, vehicle_entry_time)
    f = open(vehicle_number + '.txt', 'a+')
    f.write(data + "\n")
    f.close()
             
def three_wheeler_parking():
    customer_name = input("enter_customer_name:")
    vehicle_number = input("enter_vehicle_number:")
    vehicle_entry_time = datetime.datetime.now().strftime("%y,%m,%d,%H,%M")
    data = "{},{}\n{}".format(customer_name, vehicle_number, vehicle_entry_time)
    f = open(vehicle_number + ".txt", 'a+')
    f.write(data + "\n")
    f.close()

def four_wheeler_parking():
    customer_name = input("enter_customer_name:")
    vehicle_number = input("enter_vehicle_number:")
    vehicle_entry_time = datetime.datetime.now().strftime("%y,%m,%d,%H,%M")                  
    data = "{},{}\n{}".format(customer_name, vehicle_number,vehicle_entry_time)
    f = open(vehicle_number + ".txt", 'a+')
    f.write(data + "\n")
    f.close()
    
def two_or_above_up_to_eight_wheeler_parking():
    customer_name = input("enter_customer_name:")
    vehicle_number = input("enter_customer_number:")
    vehicle_entry_time = datetime.datetime.now().strftime("%y,%m,%d,%H,%M")
    data = "{},{}\n{}".format(customer_name, vehicle_number,vehicle_entry_time)
    f = open(vehicle_number + ".txt", 'a+')
    f.write(data + "\n")
    f.close()
def vehicle_exit():
    print(""" 1. two_wheeler vehicle
    2.three_wheeler vehicle
    3.four_wheeler vehicle
    4.Above_4_wheeler_upto_8_wheeler""")
    type_of_vehicle = int(input("enter your choice 1 OR 2 0R 3 OR 4 ::"))
    vehicle_number = input("enter your vehicle number:")
    vehicle_number1 = vehicle_number + '.txt'
    current_directory = os.getcwd()
    if type_of_vehicle == 1:
        change_directory = os.chdir(current_directory + '\\two_wheeler_vehicle')
    elif type_of_vehicle == 2:
        change_directory = os.chdir(current_directory + '\\three_wheeler_vehicle')
    elif type_of_vehicle == 3:
        change_directory = os.chdir(current_directory + '\\four_wheeler_vehicle')
    elif type_of_vehicle == 4:
        change_directory = os.chdir(current_directory + '\\upto_eight_wheeler_vehicle')
    else:
        print("something wrong")
    file_location = os.getcwd()
    booked_slots = os.listdir(change_directory)
    for searching_vehicle in booked_slots:
        if searching_vehicle == vehucle_number1:
            vehicle_number = input("enter your vehicle number")
            f = open(vehicle_number + '.txt')
            file_line =f.readlines()
            vehicle_number_matching = file_line[0].split(",")[1].strip()
            f.close()
            vehicle_exit_time = datetime.datetime.now().strftime("%y,%m,%d,%H,%M")
            if vehicle_number_matching == vehicle_number:
                    minutes_per_hour=60
                    tota_minutes_day=1440
                    t1 = int(file_line[1].split(",")[0])
                    t2 = int(file_line[1].split(",")[1])
                    t3 = int(file_line[1].split(",")[2])
                    t4 = int(file_line[1].split(",")[3])
                    t5 = int(file_line[1].split(",")[4].strip())
                    t6 = int(vehicle_exit_time.split(",")[0])
                    t7 = int(vehicle_exit_time.split(",")[1])
                    t8 = int(vehicle_exit_time.split(",")[2])
                    t9 = int(vehicle_exit_time.split(",")[3])
                    t10 = int(vehicle_exit_time.split(",")[4].strip())
                    vehicle_enter_time1 = datetime.datetime(t1,t2,t3,t4,t5)
                    vehicle_exit_time1 = datetime.datetime(t6,t7,t8,t9,t10)
                    vehicle_parked_time = vehicle_exit_time1 - vehicle_enter_time1
                    print(vehicle_parked_time)
                    actuall_time_parked = str(vehicle_parked_time)
                    time_in_hours = actuall_time_parked.split(":")
                    hour = int(time_in_hours[0])
                    minutes = int(time_in_hours[1])
                    total_time = hour * minutes_per_hour
                    total_time = total_time + minutes
                    per_minute = int(2)
                    payable_amount = per_minute * total_time
                    print("total bill",payable_amount)
                    ask_money = int(input("pay total bill:"))
                    if ask_money == payable_amount:
                        file_name = vehicle_number +'.txt'
                        location = file_location
                        path = os.path.join(file_location,file_name)
                        os.remove(path)
                        print("""gates opened
                              HAPPY JOURNEY""")
                    else:
                        print("you have to pay total")
            else:
                print("your vehicle number wrong")
        else:
            print("there not such type of vehicle")
        
            
            

    


print("""1.vehicle enter
      2.vehicle exit""")
choice = int(input("enter 1 or 2:"))
if choice == 1:
    print("""1.two wheeler parking:
    2.three wheeler parking:
    3.four wheeler parking:
    4.two_or_above_up_to_eight_wheeler_parking""")
    choice = int(input("enter your choice 1 or 2 or 3 or 4:"))
    if choice == 1:
        current_directory = os.getcwd()
        change_directory = os.chdir(current_directory + "\\two_wheeleer_vehicle")
        booked_slots = os.listdir(change_directory)
        booked_slots_count = len(booked_slots)
        if booked_slots_count <= 2:
            two_wheeler_vehicle()
        else:
            print("slots are not available")

    if choice == 2:
        f=open('three_wheeler_vehicle.txt','a+')
        f.seek(0)
        storage_of_vehicle = f.readlines()
        number_of_vehicle = len(storage_of_vehicle)
        if number_of_vehicle <= 4:
            three_wheeler_parking()
        else:
            print("there is no place for parking")
        f.close()

    if choice == 3:
        f=open('four_wheeler_vehicle.txt','a+')
        f.seek(0)
        storage_of_vehicle = f.readlines()
        number_of_vehicle = len(storage_of_vehicle)
        if number_of_vehicle <= 4:
            four_wheeler_parking()
        else:
            print("there is no place for parking")
        f.close()
    
    if choice == 4:
        f=open("two_or_above_up_to_eight_wheeler_vehicle.txt", 'a+')
        f.seek(0)
        storage_of_vehicle = f.readlines()
        number_of_vehicle = len(storage_of_vehicle)
        if number_of_vehicle <= 4:
            four_wheeler_parking()
        else:
            print("there is no place for parking")
elif choice == 2:
    vehicle_exit()




    
