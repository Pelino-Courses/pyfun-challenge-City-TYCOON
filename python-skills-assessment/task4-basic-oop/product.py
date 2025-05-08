class InvalidQuantityError(Exception):
    """Custom exception for invalid quantity values."""
    pass

# In the Product class
@property
def quantity(self):
    return self._quantity

@quantity.setter
def quantity(self, value):
    if value < 0:
        raise InvalidQuantityError("Quantity cannot be negative.")
    self._quantity = value