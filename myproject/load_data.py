#Main function to render Data into application 

#Jonathan - I think this is where the API call is  gonna go. 
def data():
    from chatbox.models import Chatmessage,User,Response
  #Data Models imported 

    from datetime import datetime
    from django.utils import timezone
    

    # create sample users
    user = User.objects.create(name="Alice")
    user = User.objects.create(name="Bob")

    # create sample Chatmessage
    user_ = User.objects.get(name="Alice")
    userChatmessage = Chatmessage.objects.create(user=user_, message_text="Hi, Bob!",timestamp=timezone.make_aware(datetime.now()))
    user_ = User.objects.get(name="Bob")
    userChatmessage = Chatmessage.objects.create(user=user_, message_text="Hello, Alice!",timestamp=timezone.make_aware(datetime.now()))

    # create sample response
    message_ = Chatmessage.objects.get(message_text="Hi, Bob!")
    response1 = Response.objects.create(response_text="How are you?",timestamp=timezone.make_aware(datetime.now()),message=message_)

    message_ = Chatmessage.objects.get(message_text="Hello, Alice!")
    response2 = Response.objects.create( response_text="I'm fine, thanks!",timestamp=timezone.make_aware(datetime.now()),message=message_)

def delete():
    from chatbox.models import Chatmessage,User,Response
    print(Chatmessage.objects.all().delete())
    print(User.objects.all().delete())
    print(Response.objects.all().delete())
    print('\n>>> END <<<')
