class User:
    def __init__(self, id, email, nombre): 
        self.id = id 
        self.email = email  
        self.nombre = nombre  
        
class PasswordResetToken:
    def __init__(self, userio_id):
        self.userio_id = userio_id 