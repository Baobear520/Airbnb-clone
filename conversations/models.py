from django.db import models
from core import models as core_models
# Create your models here.


class Conversation(core_models.TimeStampedModel):

    """ Conversation model definition """

    participants = models.ManyToManyField("users.User", blank=True, related_name='conversations')

    def __str__(self) -> str:
        usernames = [user.username for user in self.participants.all()]
        return f'{self.created.date()}' + " " + ", ".join(usernames)
    
    def count_messages(self):
        return self.messages.count()
    count_messages.short_description = 'Number of messages'
    
    def count_participants(self):
        return self.participants.count()
    count_participants.short_description = 'Number of participants'

class Message(core_models.TimeStampedModel):
    
    """ Message model definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='messages')
    conversation = models.ForeignKey("conversations.conversation", on_delete=models.CASCADE, related_name='messages')

    def __str__(self) -> str:
        return f'{self.user} says: "{self.message}"'