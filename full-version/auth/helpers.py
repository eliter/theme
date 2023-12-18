from django.core.mail import EmailMessage
from django.urls import reverse
from django.conf import settings

def send_email(subject, email, message):
    try:
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        email = EmailMessage(subject, message, email_from, recipient_list)
        email.send()
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_verification_email(email, token):
    subject = "Verify your email"
    verification_url = reverse('verify-email', kwargs={'token': token})
    full_url = settings.BASE_URL + verification_url
    message = f"Hi,\n\nPlease verify your email using this link: {full_url}"
    send_email(subject, email, message)

def send_password_reset_email(email, token):
    subject = "Reset your password"
    reset_url = reverse('reset-password', kwargs={'token': token})
    full_url = settings.BASE_URL + reset_url
    message = f"Hi,\n\nPlease reset your password using this link: {full_url}"
    send_email(subject, email, message)
