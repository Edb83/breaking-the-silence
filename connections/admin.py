from django.contrib import admin
from .models import Connection, Conversation, Message

class MessageAdminInline(admin.TabularInline):
    model = Message


class ConversationAdmin(admin.ModelAdmin):
    inlines = (MessageAdminInline, )


admin.site.register(Connection)
admin.site.register(Conversation, ConversationAdmin)
