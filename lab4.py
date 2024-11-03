from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, title, message):
        pass

class EmailNotification(Notification):
    def __init__(self, admin_email):
        self.admin_email = admin_email

    def send(self, title, message):
        print(f"From '{self.admin_email}',  Email : Title '{title}'\nText :    '{message}'\n")

class Slack:
    def __init__(self, login, api_key, chat_id):
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    def send_message(self, title, message):
        print(f"ChatId '{self.chat_id}',  message : Title '{title}'\nText :  '{message}'\n")

class Sms:
    def __init__(self, phone, sender):
        self.phone = phone
        self.sender = sender

    def send_sms(self, title, message):
        print(f"From '{self.sender}',  sms : to phone number '{self.phone}'\nText :  '{message}'\n")

class SlackNotificationAdapter(Notification):
    def __init__(self, login, api_key, chat_id):
        self.slack_service = Slack(login, api_key, chat_id)

    def send(self, title, message):
        self.slack_service.send_message(title, message)

class SmsNotificationAdapter(Notification):
    def __init__(self, phone, sender):
        self.sms_service = Sms(phone, sender)

    def send(self, title, message):
        self.sms_service.send_sms(title, message)

# Main code
if __name__ == "__main__":
    email_notification = EmailNotification("admin@gmail.com")
    email_notification.send("Update", "New Update of forum")

    slack_notification = SlackNotificationAdapter("Boss", "gfhghrtyh", "2801")
    slack_notification.send("Meet", "Meet at 6:40 PM >")

    sms_notification = SmsNotificationAdapter("+380123456789", "Shop")
    sms_notification.send("Sales", "New product on sale <link>")
