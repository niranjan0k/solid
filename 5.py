# 5. D => Dependency Inversion Principle (DIP)
# High Level Modules should not depend on Low Level Module, 
# both should depends on abstractions.

class ClientGmail:
    def send_mail(self, recipient, subject, body):
        # write your email send logic
        pass
class EmailService:
    def __init__(self):
        self.gmail_client = ClientGmail()

    def send_mail(self, recipient, subject, body):
        self.gmail_client.send_mail(recipient, subject, body)

# In this example the EmailService class directly depend on the GmailClient
# a low-level module that implements the details of sending emails using the Gmail API.
# This violates the DIP because the high-level EmailService module is tightly coupled 
# to the low-level GmailClient module.

# To adhere to the DIP as - 

class EmailClient:
    def send_mail(self, recipient, subject, body):
        raise NotImplementedError
    
class GmailClient(EmailClient):
    def send_mail(self, recipient, subject, body):
        # Send email logic is here
        pass

class OutlookClient(EmailClient):
    def send_mail(self, recipient, subject, body):
        # send email logic is here
        pass

class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

# Usages
gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("niranjan@gmail.com", "Test subject", "Test email body message")

# Now, the EmailService class depends on the EmailClient abstraction, and the low level email
# client implementations (GmailClient and OutlookClient) depend on the abstraction.


