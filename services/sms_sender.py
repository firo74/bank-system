from .notification_sender import NotificationSenderInterface

class SMSSender(NotificationSenderInterface):
    def __init__(self, provider_config: str):
        self.config = provider_config

    def send(self, message, recipient) -> bool:
        print(f'#{self.config}# TO: {recipient}\n MESSAGE: {message}')