
'''
Dataclass demonstrating defaults, field(), generated methods,
validation, and useful dataclasses utilities.
'''

from dataclasses import ( dataclass, field, asdict, fields, replace )


@dataclass(order=True)
class Product:
    # With order=True, comparisons use fields in declaration order.
    # Put the field used for ordering first.
    product_id: int
    name: str
    price: float
    quantity: int = 0  # Default value if quantity is not supplied
    category: str = "General"  # Another default value

    # default_factory creates a fresh list for every Product object.
    tags: list[str] = field(default_factory=list)

    # This field appears in the object but is hidden from generated repr().
    internal_note: str = field(default="", repr=False)

    # This field does not affect the generated equality comparison.
    supplier: str = field(default="Unknown", compare=False)

    # init=False prevents callers from passing this field to __init__().
    # repr=False hides it from the generated representation.
    total_value: float = field(init=False, repr=False)

    def __post_init__(self) -> None:
        # Runs automatically after the generated __init__().
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Calculate a derived attribute after the fields are initialized.
        self.total_value = self.price * self.quantity

    def calculate_total(self) -> float:
        # Return the current inventory value for this product.
        return self.price * self.quantity

    def restock(self, amount: int) -> None:
        # Add stock after checking that the amount is valid.
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self.quantity += amount
        self.total_value = self.calculate_total()

    def add_tag(self, tag: str) -> None:
        # Avoid adding duplicate tags.
        if tag not in self.tags:
            self.tags.append(tag)


# Create an object using required fields and some default values.
product1 = Product(
    product_id=101,
    name="Rice",
    price=4.50,
    quantity=20,
    tags=["grocery", "essential"],
    internal_note="Store in a dry area",
    supplier="ABC Foods",
)

# __repr__() is generated automatically.
print(product1)

# Custom methods work like they do in a regular class.
print(product1.calculate_total())
product1.restock(5)
product1.add_tag("popular")

print(product1.quantity)
print(product1.tags)
print(product1.total_value)

# asdict() converts the dataclass into a dictionary.
print(asdict(product1))

# fields() provides metadata about the declared dataclass fields.
print([item.name for item in fields(Product)])

# replace() creates a new object with selected fields changed.
product2 = replace(product1, price=5.00)
print(product2)

# __eq__() compares fields except those marked compare=False.
product3 = replace(product1, supplier="Different Supplier")
print(product1 == product3)  # True: supplier is excluded from comparison

# order=True enables comparisons using declared field order.
product4 = Product(102, "Beans", 3.00)
print(product1 < product4)  # True: 101 is less than 102
