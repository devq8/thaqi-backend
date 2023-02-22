from django.dispatch import receiver
from django.db.models.signals import pre_save
from chatbot.models import Message
from chatbot.views import generate_answer

@receiver(pre_save, sender=Message)
def save_response(sender, instance, *args, **kwargs):
    if instance.message:
        try:
            response = generate_answer(instance.chat, instance.message)
            print(response)
            instance.response = response
            
        except Exception as e:
            print(e)
            raise ValueError(e)
    else:
        print('You should ask a question')
        raise ValueError('No message provided!')