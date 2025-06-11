"""
NEED TO FIX ID SO IT DOESN'T GET SKIPPED
"""


class CarManager:
    all_cars = []
    total_cars = 0

    @classmethod
    def add_car_to_list(cls, car):
        cls.all_cars.append(car)
        print(f"*****{car} has been added to the list*****")

    @classmethod
    def view_tasks(cls):
        for car in cls.all_cars:
            print(car)

    @classmethod
    def register_car(cls):
        """
        creating an instance of a car
        """
        def insert_car_make():
            """
            captures user input for car's make
            """
            make = input("Please input your car's make\n")
            if (make.isalnum() and make.title() == make):
                return make
            else:
                print(f"{make} is not in the correct format. Rqrs: Capitalize and alphanumeric")
                return insert_car_make()
        
        def insert_car_model():
            model = input("Please input your car's model\n")
            if (model.isalnum() and model.title() == model):
                return model
            else:
                print(f"{model} is not in the correct format. Rqrs: Capitalize and alphanumeric")
                return insert_car_model()

        def insert_car_year():
            year = input("Please input the year of you car\n")
            if (year.isalnum() and 4 <= len(year) <= 4):
                return year
            else:
                print(f"{year} is not in the correct format. XXXX")
                return insert_car_year()

        def insert_car_mileage():
            mileage = input("Please input the current mileage\n")
            if (int(mileage) >= 0):
                return mileage
            else:
                print(f"{mileage} cannot be a negative number.")
                return insert_car_mileage()
            
        def insert_car_services():
            services = input("Please input the services you need done.\n")
            return services
#           if isinstance(services, str):
#                return services
#            else:
#                print(f"{services} is not in the correct format. Rqrs: alphanumeric")
#                return insert_car_services()
            
        new_make = {"make": insert_car_make()}
        new_model = {"model": insert_car_model()}
        new_year = {"year": insert_car_year()}
        new_mileage = {"mileage": insert_car_mileage()}
        new_services = {"services": insert_car_services()}

        return cls(new_make, new_model, new_year, new_mileage, new_services)


        


    def __init__(self, id: int, make: str, model: str, year, mileage: int, services: str):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = services
        self.add_car_to_list(self)
    
    @property
    def id(self)->int:
        return self._id
    
    @id.setter
    def id(self, new_id:int, all_cars)->int:
        if (new_id not in all_cars):
            all_cars.append(new_id)
            self._id = new_id

    @property
    def make(self)->str:
        return self._make
    
    @make.setter
    def make(self, new_make:str)->str:
        if (new_make.isalnum() and new_make.title() == new_make):
            self._make = new_make
        else:
            raise Exception(f"{new_make} is not in the correct format. Rqrs: Capitalize and alphanumeric")
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        if (new_model.isalnum() and new_model.title() == new_model):
            self._model = new_model
        else:
            raise Exception(f"{new_model} is not in the correct format. Rqrs: Capitalize and alphanumeric")
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, new_year):
        if (new_year.isalnum() and 4 <= len(new_year) <= 4):
            self._year = new_year
        else:
            raise Exception(f"{new_year} is not in the correct format. XXXX")

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage):
        if (new_mileage >= 0):
            self._mileage = new_mileage
        else:
            raise Exception(f"{new_mileage} cannot be a negative number.")
        
    @property
    def services(self):
        return self._services
    
    @services.setter
    def services(self, new_services):
        self._services = new_services



    @staticmethod
    def run_menu():
        menu = """
1. Register a car
2. View all cars
3. Exit
"""
        user_choice = input(menu)
        if user_choice == '1':
            CarManager.register_car()
            return CarManager.run_menu()
        elif user_choice == '2':
            CarManager.all_cars()
            return CarManager.run_menu()
        elif user_choice == '3':
            print("Goodbye")
            return None
        else:
            print("Invalid option")
            return CarManager.run_menu()
    #ADD MATCH-CASE for to get user inputs and match them to functions

CarManager.run_menu()
