from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation admin definition """

    list_display = ('__str__', 'count_participants', 'count_messages')
    filter_horizontal = ('participants',) 
 


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Conversation admin definition """

    list_display = ('__str__', 'created')