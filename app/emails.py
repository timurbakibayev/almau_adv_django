from mailersend import emails
from celery import shared_task


mailersend_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNDk1ZjA5Zjg0YTgxYzk5NWVkNWNkMWYyY2JkNWFhMzhlMTU0Y2Y4YzRkNmEwN2RlYjc4YTgyNjUzZGEyOWEyMTQzNTY2OWRkZDI5NTI3N2EiLCJpYXQiOjE2NDY4OTUzNDIuMzQzMDE1LCJuYmYiOjE2NDY4OTUzNDIuMzQzMDE4LCJleHAiOjQ4MDI1Njg5NDIuMzM5NjQ2LCJzdWIiOiIyMTcwNCIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCJdfQ.gvLP5pmkAfFupnbtaF3pH40IlJYt-pD0dzC_9zH6_-AOaC7m7FoCe0Id4jAZ26sCYnWc40NFg4Xg5TrPmRn46Uib6TRFdFYcWyMtWF4uxsyD-gjCLAbRVQURLY7cSeO8qmofo6ytQDG7PpJT-JmM8ctCAjLksSCmsclmh7OzooXFSlI31z1I04ZitW2X0tbqm8lnCsEjt1pK0DjIlSfpTaZEclnaiIWoThLfWnWKxDPIzaiF4YO9S7SXTnL47MnXDS8l1J4ciE_zD6qpy1eoxOCSAb9hRww7eLghpMkgz1PTcO1ZvAihcb8iIgRP98MOzA-bp6UZpchj9VN9IMFzKbRTDY_O2SpzBiKw8-VwKF5pGfjaiRkLAEa_30YKeU9nUpnNNn5map3DwnpE9WWS8EcKtk6wmuWlc71VgRnThAANU3mXJOxL1-1I12EqNtx1q0tuUj-ky5POOTxsa55BufqVT0eTSfyIl5pwdxC9yvdRjKr1vnwnqaYeeT6IeZy8vDnt14qj_6BwNF-zHmudJHgHOg8BJbgdJTTF6xqKiG4mrP_zMJMGKmBJZJ_7SNZM8GTitqSa_YHhKmhnRx5HOXtqTXY1fC0flSzSwEr90TlsQ7I_s_6jVMKjU7ccwhxbOOtxJI7vmNgMMO310ZVgaEaKpziQuhmQQQmIAyYF2Ew"


@shared_task(name="send_email_with_mailersend")
def send_email(email: str, subject: str, text: str) -> None:
    mailer = emails.NewEmail(mailersend_token)

    mail_body = {}

    mail_from = {
        "name": "Data Science Academy",
        "email": "info@dsacademy.kz",
    }

    recipients = [
        {
            "name": "Your Client",
            "email": email,
        }
    ]

    reply_to = [
        {
            "name": "Data Science Academy",
            "email": "info@dsacademy.kz",
        }
    ]

    html = f"""
    <HTML>
      <body>
         <h3>{text}</h3>
      </body>
    </HTML>
    """

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject(subject, mail_body)
    mailer.set_html_content(html, mail_body)
    mailer.set_plaintext_content(text, mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    print("Sending email to:", email)
    return mailer.send(mail_body)
