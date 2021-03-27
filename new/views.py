from django.shortcuts import render, redirect
from django.template.loader import render_to_string,get_template
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

from django.core.mail import *





def email_message(request):
    '''
        This method is for sending the message to the user through email. 
        For the better look this method can send email combined with any html template.

    '''
    #demo values
    values={
        'name' : 'Imran',
        'email' : 'mkaf10imran@gmail.com',
        'template' : 'email_template.html',
        'subject' : 'Thank you for purchasing',
        'sender' : 'imranpassw0rd@gmail.com',
        'receiver': ['mkaf10imran@gmail.com']
    }

    company={
        'name' : 'Company Name',
        'logo' : 'logo_img_src',
        'banner' : 'banner_img_src',
        'subject' : 'Thank you for purchasing',
        'sender' : 'imranpassw0rd@gmail.com',
        'receiver': ['mkaf10imran@gmail.com']
    }
    backend = EmailBackend(host='smtp.gmail.com', port=587, username='imranpassw0rd@gmail.com', 
                       password='IM123456', use_tls=True, fail_silently=False)

    # email = EmailMessage(subject='subj', body='body', from_email=from_email, to=to, 
    #          connection=backend)

    template = render_to_string (values['template'],{'name': values['name'], 'user_email': values['email'] })
    text_content = strip_tags(template)
    email = EmailMultiAlternatives(
        subject= values['subject'],
        body=text_content,
        from_email=values['sender'],
        to=values['receiver'],
        connection=backend
        )
    email.attach_alternative(template, "text/html")
    email.send()

    try:
        email.send()
        return render(request,'index.html')
    except:
        return render(request,'error.html',{'error': 'Internal server'})
