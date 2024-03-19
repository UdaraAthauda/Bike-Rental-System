import datetime
import bike_rental

bike_system = bike_rental.BikeRental(100)
customer = bike_rental.Customer()

while True:
    print(""" 
          ====== Bike Rental App ======
    1. display available bikes
    2. request a bike on hourly basis - $5
    3. request a bike on daily basis - $20
    4. request a bike on weekly basis - $60
    5. return a bike(s)
    6. exit""")

    choice = input("enter choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("the choice has to be from the available choice.")
        continue

    if choice == 1:
        bike_system.display_stock()
    elif choice == 2:
        requested_bikes = customer.request_bike()
        rental_time = bike_system.rent_bike_on_hourly_basis(requested_bikes)
        customer.rental_time = rental_time
        customer.rental_basis = 2
    elif choice == 3:
        customer.rental_time = bike_system.rent_bike_on_daily_basis(customer.request_bike())
        customer.rental_basis = 3
    elif choice == 4:
        customer.rental_time = bike_system.rent_bike_on_weekly_basis(customer.request_bike())
        customer.rental_basis = 4
    elif choice == 5:
        request_tuple = customer.return_bike()
        bill = bike_system.return_bike(request_tuple)
        customer.bill = bill
        customer.rental_basis, customer.rental_time, customer.bikes = 0, 0, 0
    elif choice == 6:
        break
    else:
        print("invalid input: please enter a number between 1-6")

print("thank you for using the bike rental system.")
