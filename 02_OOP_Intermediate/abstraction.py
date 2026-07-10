"""Practice script for OOP. 
Covers Abstraction principle
"""

# =================================================
# Abstraction
# =================================================
""" 
Reduces the complexity by showing only the necessary functionality 
while hiding the underlying implementation details.
"""
# Email Services:
"""User can send email without the need to know the 
internal functionalities, or logic involved in this operation.
"""
class EmailService:
    
    def _connect(self):
        print("Connecting to email server")
        
    def _authenticate(self):
        print("authenticating...")
        
    def send_email(self):
        self._connect()
        self._authenticate
        print("Sending email...")
        self._disconnect()
        
    def _disconnect(self):
        print("Disconnecting from email server")
        
        
email = EmailService()
email.send_email()   # User only has to send email

# If we didn't make use of the protected methods then user will have to
# face more complex work

"""
email = EmailService()
email.connect()
email.authenticate()             # Must follow the order.
email.send_email()
email.disconnect()      
"""