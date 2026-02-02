"""
<Your Name>
<StudentID-no-dash>
P3
"""

from abc import ABC, abstractmethod
from datetime import datetime


# =========================
# Class: Building (Abstract)
# =========================
class Building(ABC):
    total_buildings = 0

    def __init__(self, name, address, year_built=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Building name must be a non-empty string")
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string")

        if year_built is None:
            year_built = datetime.now().year

        if not Building.is_valid_year(year_built):
            raise ValueError("Invalid year_built")

        self.name = name
        self.address = address
        self.year_built = year_built
        Building.total_buildings += 1

    @abstractmethod
    def calculate_maintenance_cost(self):
        pass

    @abstractmethod
    def get_building_type(self):
        pass

    def get_age(self):
        return datetime.now().year - self.year_built

    @classmethod
    def get_total_buildings(cls):
        return cls.total_buildings

    @staticmethod
    def is_valid_year(year):
        current_year = datetime.now().year
        return isinstance(year, int) and 1800 <= year <= current_year

    def show_properties(self):
        return (
            f"Name: {self.name}\n"
            f"Building type: {self.get_building_type()}\n"
            f"Address: {self.address}\n"
            f"Year built: {self.year_built}\n"
            f"Age: {self.get_age()}\n"
        )


# =========================
# Class: ResidentialBuilding
# =========================
class ResidentialBuilding(Building):
    _average_rent_per_unit = 1500.0

    def __init__(self, name, address, year_built, number_of_units, has_parking=True):
        super().__init__(name, address, year_built)

        if not isinstance(number_of_units, int) or number_of_units <= 0:
            raise ValueError("number_of_units must be a positive integer")

        if not isinstance(has_parking, bool):
            raise TypeError("has_parking must be a boolean")

        self.number_of_units = number_of_units
        self.has_parking = has_parking

    def calculate_maintenance_cost(self):
        return self.number_of_units * 500.0

    def get_building_type(self):
        return "Residential"

    def _calculate_total_rent_income(self):
        return self.number_of_units * self._average_rent_per_unit * 12

    @classmethod
    def set_average_rent(cls, new_rent):
        if not isinstance(new_rent, (int, float)) or new_rent <= 0:
            raise ValueError("Average rent must be positive")
        cls._average_rent_per_unit = float(new_rent)

    def show_properties(self):
        yearly_income = self._calculate_total_rent_income()
        yearly_ma = self.calculate_maintenance_cost()
        profit = yearly_income - yearly_ma

        return (
            super().show_properties() +
            "\n= Residential area =\n"
            f"Number of units: {self.number_of_units}\n"
            f"Parking? {'Yes' if self.has_parking else 'No'}\n"
            f"Avg rent/unit: {self._average_rent_per_unit:.2f}\n"
            f"Yearly income: {yearly_income:.2f}\n"
            f"Yearly MA: {yearly_ma:.2f}\n"
            f"Profit: {profit:.2f}\n"
        )


# =========================
# Class: PublicSpace
# =========================
class PublicSpace:
    def __init__(self, space_name="Public space", operating_cost=0.0):
        if not isinstance(space_name, str):
            raise TypeError("space_name must be a string")
        if not isinstance(operating_cost, (int, float)) or operating_cost < 0:
            raise ValueError("operating_cost must be non-negative")

        self.space_name = space_name
        self._operating_cost = float(operating_cost)
        self.__revenue_data = {}

    def add_revenue(self, month, amount):
        if not isinstance(month, str) or not month.strip():
            raise ValueError("Month must be a non-empty string")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Revenue amount must be non-negative")

        self.__revenue_data[month] = float(amount)

    def get_total_revenue(self):
        return sum(self.__revenue_data.values())

    def calculate_profit(self):
        yearly_operating = self._operating_cost * 12
        return self.get_total_revenue() - yearly_operating

    def show_properties(self):
        return (
            "\n= Public area =\n"
            f"Name: {self.space_name}\n"
            f"Yearly revenue: {self.get_total_revenue():.2f}\n"
            f"Yearly operating cost: {self._operating_cost * 12:.2f}\n"
            f"Yearly profit: {self.calculate_profit():.2f}\n"
        )


# =========================
# Class: ResidentialPublicBuilding
# =========================
class ResidentialPublicBuilding(ResidentialBuilding, PublicSpace):
    def __init__(self, name, address, year_built,
                 number_of_units, has_parking,
                 space_name, operating_cost,
                 shared_facilities=None):

        if shared_facilities is None:
            shared_facilities = ["Park", "Pool", "Cafe"]

        if not isinstance(shared_facilities, list) or not all(
                isinstance(f, str) for f in shared_facilities):
            raise TypeError("shared_facilities must be a list of strings")

        ResidentialBuilding.__init__(self, name, address, year_built,
                                     number_of_units, has_parking)
        PublicSpace.__init__(self, space_name, operating_cost)

        self.shared_facilities = shared_facilities

    def calculate_maintenance_cost(self):
        return (
            super().calculate_maintenance_cost() +
            self._operating_cost * 12
        )

    def get_building_type(self):
        return "Residential-Public"

    def get_monthly_profit(self):
        residential_monthly = (
            self._calculate_total_rent_income() / 12 -
            self.calculate_maintenance_cost() / 12
        )
        public_monthly = self.calculate_profit() / 12
        return residential_monthly + public_monthly

    def show_properties(self):
        return (
            super(Building, self).show_properties() +
            "\n= Residential area =\n"
            f"Number of units: {self.number_of_units}\n"
            f"Parking? {'Yes' if self.has_parking else 'No'}\n"
            f"Avg rent/unit: {self._average_rent_per_unit:.2f}\n"
            f"Yearly income: {self._calculate_total_rent_income():.2f}\n"
            f"Yearly MA: {self.calculate_maintenance_cost():.2f}\n"
            f"Profit: {(self._calculate_total_rent_income() - self.calculate_maintenance_cost()):.2f}\n"
            "\n= Public area =\n"
            f"Name: {self.space_name}\n"
            f"Facilities: {', '.join(self.shared_facilities)}\n"
            f"Yearly revenue: {self.get_total_revenue():.2f}\n"
            f"Yearly operating cost: {self._operating_cost * 12:.2f}\n"
            f"Yearly profit: {self.calculate_profit():.2f}\n"
        )
