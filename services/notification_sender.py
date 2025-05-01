from abc import ABC, abstractmethod
from ..models import Customer

class NotificationSenderInterface(ABC):
    @abstractmethod
    def send(self, message, recipient: Customer) -> bool:
        pass
