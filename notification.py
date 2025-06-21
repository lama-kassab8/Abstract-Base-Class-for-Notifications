from abc import ABC, abstractmethod
# Abstract base class defining the interface for all notifications
class Notification(ABC):

    def __init__(self, name):
        self.name= name # Common attribute shared by all notifications

    @abstractmethod
    def send(self, message):
        # All subclasses must implement this method
        pass


# SMS subclass adds a specific attribute: carrier
class SMS(Notification):

    def __init__(self, name, carrier):
        super().__init__(name)
        self.carrier= carrier

    def send(self, message):
        print(f"Sending SMS via {self.carrier}: Dear {self.name}, {message}")


# Email subclass adds a specific attribute: email_provider
class Email(Notification):
    def __init__(self, name, email_provider):
        super().__init__(name)
        self.email_provider= email_provider

    def send(self, message):
        print(f"Sending Email via {self.email_provider}: Dear {self.name}, {message}")

# Push subclass adds a specific attribute: device_type
class Push(Notification):
    def __init__(self, name, device_type):
        super().__init__(name)
        self.device_type= device_type    

    def send(self, message):
        print(f"Sending Push to an {self.device_type} device: Dear {self.name}, {message}")


# --- Test cases ---
omar= SMS("Omar", "Du")
omar.send("Please, renew your subscription to enjoy our services.")

judy= Email("Judy", "Gmail")
judy.send("Your inbox is almost full. Please delete unnecessary emails.")

steven = Push("Steven", "Android")
steven.send("You have a new app update waiting. Tap to install.")