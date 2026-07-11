"""
Practice script for OOP.

Topic: Abstraction

Abstraction is one of the fundamental principles of object-oriented
programming (OOP). It reduces complexity by exposing only the essential
features of an object while hiding the underlying implementation
details.

Example:
An email service allows users to send emails without needing to know
the internal processes or logic involved in delivering the message.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Without Abstraction
# =================================================
# If connect, authenticate, and disconnect were exposed as public
# methods, the client would need to know the internal steps and call
# them in the correct order:

# email = EmailService()
# email.connect()
# email.authenticate()      # Must follow this order.
# email.send_email()
# email.disconnect()

# This exposes implementation details the user shouldn't need to
# manage and makes the class easier to misuse.


# =================================================
# Example 2: With Abstraction
# =================================================
# The internal steps are hidden behind protected methods (prefixed
# with an underscore). The user only interacts with the public
# send_email method, which handles the correct sequence internally.

class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server")


email = EmailService()
email.send_email()  # The user only has to call send_email.

# Without abstraction, the user would have to manage the connection,
# authentication, and disconnection steps directly, in the correct
# order, every time an email is sent.