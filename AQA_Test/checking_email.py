import imaplib
import email
class EmailBox():

    def check_an_email(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('look070907@gmail.com', 'Dart070907')

        mail.list()
        mail.select('inbox')

        result, data = mail.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        print(email_message['To'],
              email.utils.parseaddr(email_message['From']),
              email_message['Date'],
              email_message['Subject'],
              email_message['Message-Id'],
              sep='\n')

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
                print(body)
                assert "New Password" in body

        else:
            body = email_message.get_payload(decode=True).decode('utf-8')
            # print(body)
            assert "New Password" in body

        mail.logout()

