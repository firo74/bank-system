from .notification_sender import NotificationSenderInterface

class EmailSender(NotificationSenderInterface):
    def __init__(self, path):
        self.emails_file = open(path, 'a')
    
    def send(self, message, recipient):
        self.emails_file.write(f'TO: {recipient}, MSG: {message}\n\n')
    
    def __del__(self):
        self.emails_file.close()