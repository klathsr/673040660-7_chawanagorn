"""
<Your Name>
<StudentID-withDash>
P4
"""

from P3 import *


def test_ResidentialBuilding():
    print("\n--- Residential Building ---")
    rb = ResidentialBuilding("Luxu KKU Campus", "Kangsadarn", 2020, 30)
    print(rb.show_properties())

    print("Changing average rent...")
    ResidentialBuilding.set_average_rent(1800)
    print(rb.show_properties())

    try:
        ResidentialBuilding("Bad", "Nowhere", 2020, -5)
    except ValueError as e:
        print("Caught error:", e)


def test_PublicSpace():
    print("\n--- Public Space ---")
    ps = PublicSpace("Living KKU Campus", 20000)
    ps.add_revenue("January", 14500)
    ps.add_revenue("February", 23000)
    ps.add_revenue("March", 18000)

    print(ps.show_properties())

    try:
        ps.add_revenue("", -100)
    except ValueError as e:
        print("Caught error:", e)


def test_ResidentialPublicBuilding():
    print("\n--- Residential-Public Building ---")
    rpb = ResidentialPublicBuilding(
        "Luxu KKU Campus",
        "Kangsadarn",
        2020,
        30,
        True,
        "Living KKU Campus",
        20000,
        ["Park", "Pool", "Cafe", "Gym"]
    )

    rpb.add_revenue("January", 14500)
    rpb.add_revenue("February", 23000)

    print(rpb.show_properties())
    print("Monthly profit:", rpb.get_monthly_profit())


def main():
    test_ResidentialBuilding()
    test_PublicSpace()
    test_ResidentialPublicBuilding()


if __name__ == "__main__":
    main()
