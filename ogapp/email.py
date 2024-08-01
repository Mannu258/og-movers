from django.core.mail import EmailMessage

def send_order_email(name, customer_email, price, date, mobile, froml, tol):
    email = EmailMessage(
        subject='Order Received',
        body=f"Name:\t{name}\nEmail:\t{customer_email}\nPrice:\t{price}\nDate:\t{date}\nMobile:\t{mobile}\nFrom:\t{froml}\nTo:\t{tol}\n\nRegards,\nOG Movers\n\nContact Us:\nPhone: +1 (123) 456-7890\nEmail: info@ogmovers.com",
        to=['mandeepkumarmannu123@gmail.com','ogmovers1@gmail.com','ogmovers2@gmail.com','priyanshuv007@gmail.com']
        # to=['mandeepkumarmannu123@gmail.com']
    )
    email.send()
    customer = EmailMessage(
    subject='Inquiry Received',
    body=(
        f"Hello {name},\n\nThank you for reaching us. We are working on your inquiry and "
          "will get back to you as soon as possible.\n\nIn the meantime, feel free to check our FAQ section.\n\n"
          "Thank you for your patience,\n OG Movers Support Team\n\n"
          "Regards,\nOG Movers\n\nContact Us:\nPhone: +1 (123) 456-7890\nEmail: ogmovers1@gmail.com"),
    to=[f'{customer_email}']
)

    customer.send()

# def send_inquiry_email(name, customer_email):
#     customer = EmailMessage(
#         subject='Inquiry Received',
#         body=f"Hello {name},\n\nThank you for reaching us. We are working on your inquiry and will get back to you as soon as possible.\n\nIn the meantime, feel free to check our FAQ section.\n\nThank you for your patience,\n OG Movers Support Team",
#         to=[f'{customer_email}']  # Use f-string to format the email address
#     )
#     customer.send()
