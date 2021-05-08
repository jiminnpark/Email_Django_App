from email.message import EmailMessage
import smtplib
# from decouple import config
import imghdr
from django.conf import settings


def send_email(To, Subject, Message, filename):

    email = "testmailtesting17@gmail.com"
    password = "Testmail#12345"
    # contact-list
    contacts = []
    contacts.append(To)
    image_file = []
    doc_file = []
    # subject
    subject = Subject

    # Mail sending initiator

    def start_service(msg):
        # Context manager to start SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            # Login to server
            smtp.login(email, password)

            # sending email
            smtp.send_message(msg)

    # setting up msg content

    def msg_content(file_name):

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = ','.join(contacts)
        msg.set_content(Message)

        # msg.add_alternative("""\
        # <!DOCTYPE html>
        #     <html>
        #         <body>
        #             <h1>Hello</h1>
        #         </body>
        #     </html>
        # """, subtype='html')

        def upload_img(image_file):
            print('hi')
            # uploading files (Images)

            for file in image_file:
                # opening attachment file
                with open(file, 'rb') as f:
                    file_data = f.read()

                    # file type (Image type )
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                msg.add_attachment(file_data, maintype='image',
                                   subtype=file_type, filename=file_name)

        def upload_docs(doc_file):
            print('hello')
            # uploading files (octet-stream)
            for file in doc_file:
                # opening attachment file
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                    file_type = "octet-stream"

                msg.add_attachment(file_data, maintype='application',
                                   subtype=file_type, filename=file_name)

        file_path = r'media/'+file_name
        if file_path[-1] == 'g':
            image_file.append(file_path)
            upload_img(image_file)
        else:
            doc_file.append(file_path)
            upload_docs(doc_file)
        start_service(msg)

    msg_content(filename)
