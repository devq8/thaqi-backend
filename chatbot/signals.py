from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from chatbot.models import Message
from chatbot.views import generate_answer

@receiver(pre_save, sender=Message)
def save_response(sender, instance, *args, **kwargs):
    if instance.message:
        try:
            print('Me:')
            print(instance.message)
            print('Thaqi:')
            response = generate_answer(instance.message)
            print(response[2:])
            instance.response = response[2:]
            
        except Exception as e:
            print(e)
            raise ValueError(e)
    else:
        print('You should ask a question')
        raise ValueError('No message provided!')