# holiday.py

def hotel_cost(num_nights):
    """Return the total cost of the hotel stay at $100 per night"""
    price_per_night = 100
    return num_nights * price_per_night

def plane_cost(city_flight):
    """Return the flight cost based on chosen city."""
    if city_flight == "chicago":
        cost = 400
    elif city_flight == "los angles":
        cost = 500
    elif city_flight == "boston":
        cost = 450
    elif city_flight == "new york":
        cost = 600
    elif city_flight == "dallas":
        cost = 350
    else:
        cost = 0 
    return cost

def car_rental(rental_days):
    """Return the total cost of the car rental at $50 per day."""
    daily_rental_cost = 50
    return rental_days * daily_rental_cost

def holiday_cost(num_nights, city_flight, rental_days): 
    """Return the total cost of the holiday by calling the three cost functions and adding their results together."""
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental (rental_days)
    return total

print("Available destintations: Chicago, Los Angles, Boston, New York or Dallas")
print()

city_flight = input("Which city will you be flying to? ").strip().lower()

num_nights = int(input("How many night will you be staying at the hotel? "))

rental_days = int(input("How many days will you be renting a car? "))

hol_total = holiday_cost(num_nights, city_flight, rental_days)

print("Holiday Summary")
print(f"Destination:  {city_flight.title()}")
print(f"Flight cost: ${plane_cost(city_flight):.2f}")
print(f"Hotel cost: ${hotel_cost(num_nights):.2f} ({num_nights} at $100 per night)")
print(f"Car Rental Cost:  ${car_rental(rental_days):.2f} ({rental_days} days at $50 per day)")
print()
print(f"Total holiday cost: ${hol_total:.2f}")
