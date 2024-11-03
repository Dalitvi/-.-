from abc import ABC, abstractmethod

class ISocialNetwork(ABC):
    @abstractmethod
    def authenticate(self, login, password):
        pass

    @abstractmethod
    def publish_post(self, message):
        pass

class Facebook(ISocialNetwork):
    def __init__(self):
        self.username = None
        self.password = None

    def authenticate(self, username, password):
        self.username = username
        self.password = password
        print(f"Logged in Facebook with username: {self.username}")

    def publish_post(self, message):
        print(f"Sent message in Facebook: {message}")

class LinkedIn(ISocialNetwork):
    def __init__(self):
        self.email = None
        self.password = None

    def authenticate(self, email, password):
        self.email = email
        self.password = password
        print(f"Logged in LinkedIn with email: {self.email}")

    def publish_post(self, message):
        print(f"Sent message in LinkedIn: {message}")

class SocialNetworkCreator(ABC):
    @abstractmethod
    def create_social_network(self):
        pass

    def publish(self, login, password, message):
        network = self.create_social_network()
        network.authenticate(login, password)
        network.publish_post(message)

class FacebookFactory(SocialNetworkCreator):
    def create_social_network(self):
        return Facebook()

class LinkedInFactory(SocialNetworkCreator):
    def create_social_network(self):
        return LinkedIn()

if __name__ == "__main__":
    facebook_factory = FacebookFactory()
    facebook_factory.publish("user_test", "password_test1", "Facebook")

    linkedin_factory = LinkedInFactory()
    linkedin_factory.publish("user_mail@gmail.com", "password_test2", "LinkedIn")
