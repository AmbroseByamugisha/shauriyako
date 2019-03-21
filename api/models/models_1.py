class User:
    """
    creates a user model.
    """
    def __init__(self, user_id, user_name, email, password, role):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = password

class Products:
    """
    creates a products model.
    """
    def __init__(self, product_id, product_name, price, product_image):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_image = product_image
        
