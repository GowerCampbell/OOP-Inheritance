class Property:
    def __init__(self, location, price, property_type):
        # Initialize property attributes
        self.location = location
        if price < 50000:  # Ensure price is at least 50,000
            price = 0
        self.price = price
        self.property_type = property_type

    def __str__(self):
        # Return a formatted string representation of the property
        return f"This {self.property_type} is located at: {self.location}, and costs {self.price} USD"

class Apartment(Property):
    def __init__(self, location, price, property_type, floor):
        # Call the parent class constructor to initialize common attributes
        super().__init__(location, price, property_type)
        self.floor = floor  # Additional attribute for apartments

    def __str__(self):
        # Extend the string representation to include the floor
        return super().__str__() + f". It is located on floor {self.floor}"

class House(Property):
    def __init__(self, location, price, property_type, bedrooms, garden_size):
        # Call the parent class constructor to initialize common attributes
        super().__init__(location, price, property_type)
        self.bedrooms = bedrooms  # Additional attribute for houses
        self.garden_size = garden_size

    def __str__(self):
        # Extend the string representation to include the number of bedrooms and garden size
        return super().__str__() + f".\n It has {self.bedrooms} bedrooms and a garden with size {self.garden_size} sq.m."

class CommercialSpace(Property):
    def __init__(self, location, price, property_type, business_type):
        # Call the parent class constructor to initialize common attributes
        super().__init__(location, price, property_type)
        self.business_type = business_type  # Additional attribute for commercial spaces

    def __str__(self):
        # Extend the string representation to include the business type
        return super().__str__() + f". It is suitable for {self.business_type}."

class Parking:
    def __init__(self, parking_slots):
        self.parking_slots = parking_slots  # Number of parking slots available

    def __str__(self):
        return f"\nIt has {self.parking_slots} parking slots."

class CommercialWithParking(CommercialSpace, Parking):
    def __init__(self, location, price, property_type, business_type, parking_slots):
        # Initialize both CommercialSpace and Parking
        CommercialSpace.__init__(self, location, price, property_type, business_type)
        Parking.__init__(self, parking_slots)

    def __str__(self):
        # Combine the string representations from both CommercialSpace and Parking
        return CommercialSpace.__str__(self) + " " + Parking.__str__(self)

# Creating instances of Apartment, House, and CommercialSpace
prop_1 = Apartment("London", 12345678, "Apartment", 5)
print(prop_1)  # Prints details of the apartment

apartment = Apartment("Downtown", 120000, "Apartment", 2)
print(apartment)  # Prints details of another apartment

house_1 = House("Capetown", 123300, "House", 3, 250)
print(house_1)  # Prints details of the house

commercial _space_1 = CommercialSpace("New York", 500000, "Commercial Space", "Retail Store")
print(commercial_space_1)  # Prints details of the commercial space

commercial_parking = CommercialWithParking("Johannesburg", 700000, "Office", "Corporate Office", 50)
print(commercial_parking)  # Prints details of the commercial space with parking
