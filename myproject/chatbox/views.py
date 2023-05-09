# This PY file - Allows us to render the HTML page with defined Python models passing dynamic Information into them

from django.shortcuts import render, redirect

from .models import Chatmessage, User, Response


# Index Render - this is where the API call will be made

from django.shortcuts import render, redirect

from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

def index(request):
    responses = []
    if request.method == "POST":
        user_name = request.POST["user_name"]
        message_text = request.POST["message_text"]

        # Retrieve or create the User
        user, _ = User.objects.get_or_create(name=user_name)

        # Save the Chatmessage
        message = Chatmessage(message_text=message_text, user=user)
        message.save()

        # Set the OpenAI API key
        openai.api_key = settings.OPENAI_API_KEY

        # Call the OpenAI API
        # Call the OpenAI API
        response = openai.Completion.create(
        engine="text-davinci-002",  # You can replace this with the desired GPT-3 engine
        prompt=message_text,
        max_tokens=100,
        n=1,
        temperature=0.5,
        )


        # Save the Response
        response_text = response.choices[0].text.strip()
        chat_response = Response(response_text=response_text, message=message)
        chat_response.save()

        # Add the response to the list
        responses.append({"response_text": response_text})

    context = {
        "responses": responses,
    }
    return render(request, "chatbox/base.html", context)



def chat_history(request):
    chats = Chatmessage.objects.all()
    chats_list = []
    for chat in chats:
        chats_list.append({"chat": chat})

    context = {
        "chats_list": chats_list
    }
    return render(request, "chatbox/chat_history.html", context)


def user_list(request):
    users = User.objects.all()
    users_list = []
    for user in users:
        users_list.append({"user": user})

    context = {
        "users_list": users_list
    }
    return render(request, "chatbox/user_list.html", context)


def response_history(request):
    responses = Response.objects.all()
    responses_list = []
    for response in responses:
        responses_list.append({"response": response})

    context = {
        "responses_list": responses_list
    }
    return render(request, "chatbox/response_history.html", context)
