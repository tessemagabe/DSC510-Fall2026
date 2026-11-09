

# my practice page Final
#                               10.1 Programming Assignment
"""
Purpose:
        To demonstrate Python object-oriented
        programming concepts by creating a simple cash register program.
        The CashRegister class encapsulates the cart state (total price and item count)
        and exposes methods to add items and read that state. Totals are formatted as
        currency using the locale module.


    prepared by: Gebriel Tessema
    Course: DSC 510
    Programming Assignment:  Week 10
    program title: simple cash register program
    Date 11/07/2026
    presented to instructor: Michael Eller

"""
import locale


class CashRegister:
    """ This class represents a cash register.
        It keeps track of the total price of all items
        and the number of items in the register.
    """

    def __init__(self, total_price, item_count):
        """ Initializes a CashRegister object.
            Args:
                total_price (float): The total cost of all items.
                item_count (int): The number of items.
        """
        self.total_price = total_price
        self.item_count = item_count

    def get_total(self):
        return self.total_price

    def get_count(self):
        return self.item_count

    def add_item(self, price):
        self.total_price += price
        self.item_count += 1


def main():
    """Runs the cash register program."""

    locale.setlocale(locale.LC_ALL, '')
    # locale class formatting the out put as currency

    print("\n" + "=" * 50)
    print("Welcome to my simple cash register program: ")
    print("=" * 50)

    # creating CashRegister object
    register = CashRegister(0, 0)

    while True:
        select = input("Please, enter your choice to add an Item Yes or No: ").lower()

        if select in ("no", "n"):
            print("-" * 25)
            print("\tHave a good time")
            print("-" * 25)
            break

        try:
            price = float(input("Enter item price: "))
            if price <= 0:
                print("Please enter a positive number.")
                continue
            register.add_item(price)

            print(f"Items: {register.get_count()}")
            print(f"Current Total: "
                  f"{locale.currency(register.get_total(), grouping=True)}")
        except ValueError:

            print("=" * 50)
            print("Please enter a numeric value: ")
            print("=" * 50)

    print("\nFinal Receipt")
    print(f"Total items: {register.get_count()}")
    print(f"Total price: "
          f"{locale.currency(register.get_total(), grouping=True)}"
          )


if __name__ == "__main__":
    main()



