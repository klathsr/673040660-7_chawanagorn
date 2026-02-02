"""
<Your Name>
<StudentID-withDash>
P1
"""

from abc import ABC, abstractmethod


# =========================
# Class: Building
# =========================
class Building(ABC):
    total_buildings = 0

    def __init__(self, name="Unknown", address="Unknown", year_built=2024):
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
        pass

    @classmethod
    def get_total_buildings(cls):
        pass

    @staticmethod
    def is_valid_year(year):
        pass

    def show_properties(self):
        pass


# =========================
# Class: ResidentialBuilding
# =========================
class ResidentialBuilding(Building):
    _average_rent_per_unit = 1500.0

    def __init__(self, name="Unknown", address="Unknown", year_built=2024,
                 number_of_units=1, has_parking=True):
        super().__init__(name, address, year_built)
        self.number_of_units = number_of_units
        self.has_parking = has_parking

    def calculate_maintenance_cost(self):
        pass

    def get_building_type(self):
        pass

    def _calculate_total_rent_income(self):
        pass

    @classmethod
    def set_average_rent(cls, new_rent):
        pass

    def show_properties(self):
        pass


# =========================
# Class: PublicSpace
# =========================
class PublicSpace:
    def __init__(self, space_name="Public space", operating_cost=0.0):
        self.space_name = space_name
        self._operating_cost = operating_cost
        self.__revenue_data = {}

    def add_revenue(self, month, amount):
        pass

    def get_total_revenue(self):
        pass

    def calculate_profit(self):
        pass

    def show_properties(self):
        pass


# =========================
# Class: ResidentialPublicBuilding
# =========================
class ResidentialPublicBuilding(ResidentialBuilding, PublicSpace):
    """
    Attributes:
    name (str): Name of the building
    address (str): Building address
    year_built (int): Construction year
    number_of_units (int): Total residential units
    has_parking (bool): Parking availability
    space_name (str): Name of public space
    operating_cost (float): Monthly operating cost
    shared_facilities (list): Shared facilities list
    """

    def __init__(self, name="Unknown", address="Unknown", year_built=2024,
                 number_of_units=1, has_parking=True,
                 space_name="Public space", operating_cost=0.0,
                 shared_facilities=None):

        ResidentialBuilding.__init__(self, name, address, year_built,
                                     number_of_units, has_parking)
        PublicSpace.__init__(self, space_name, operating_cost)

        if shared_facilities is None:
            shared_facilities = ["Park", "Pool", "Cafe"]

        self.shared_facilities = shared_facilities

    def calculate_maintenance_cost(self):
        pass

    def get_building_type(self):
        pass

    def get_monthly_profit(self):
        pass

    def show_properties(self):
        pass
