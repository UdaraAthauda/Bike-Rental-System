import datetime as dt

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"we have {self.stock} bikes available in the system")
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        if n <= 0:
            print("the number of bikes must be positive number!")
            return None
        elif n > self.stock:
            print(f"sorry! we have only {self.stock} bikes available for rent")
            return None
        else:
            now = dt.datetime.now()
            print(f"you have rented {n} bike(s) on hourly basis today at {now.hour}:{now.minute}:{now.second}")
            print("you will be charged $5 for each bike per hour")
            print("we hope that you enjoy our service.")
            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        if n <= 0:
            print("the number of bikes must be positive number!")
            return None
        elif n > self.stock:
            print(f"sorry! we have only {self.stock} bikes available for rent")
            return None
        else:
            now = dt.datetime.today()
            print(f"you have rented {n} bike(s) on daily basis today on {now}")
            print("you will be charged $20 for each bike daily")
            print("we hope that you enjoy our service.")
            self.stock -= n
            return now

    def rent_bike_on_weekly_basis(self, n):
        if n <= 0:
            print("the number of bikes must be positive number!")
            return None
        elif n > self.stock:
            print(f"sorry! we have only {self.stock} bikes available for rent")
            return None
        else:
            now = dt.datetime.today()
            print(f"you have rented {n} bike(s) on weekly basis today on {now}")
            print("you will be charged $60 for each bike weekly")
            print("we hope that you enjoy our service.")
            self.stock -= n
            return now

    def return_bike(self, request):
        rental_time, rental_basis, num_of_bikes = request
        bill = 0
        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = dt.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.second / 3600) * 5 * num_of_bikes
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes

            if 3 <= num_of_bikes >= 6:
                print("you are eligible for family rental promotion which 30%")
                bill = bill * 0.7

            print("thanks for returning your bike. hope you enjoyed the service!")
            print(f"the total bill is: ${bill}")
            return bill
        else:
            print("are you sure you rented a bke with us?")
            return None


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_bike(self):
        bikes = input("how many bikes would you like to rent?")
        try:
            bikes = int(bikes)

        except ValueError:
            print("invalid input: the number of bikes has to be positive integer!")
            return -1

        if bikes < 1:
            print("invalid input: the number of bikes has to be positive integer!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0, 0, 0





