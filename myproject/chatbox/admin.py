from django.contrib import admin

#models must be registered under for the django-admin page


from .models import User,Chatmessage, Response 

admin.site.register(User)

admin.site.register(Chatmessage)

admin.site.register(Response)
