# absolute import statement this is by pep 8 mostly used
# from ecommerce.customer import contact

# from ..customer import contact  # relative import statement (optional)

print("Sales initialized", __name__)

# contact.contact_customer()


def calc_shipping():
    pass


def calc_tax():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
