from email.message import EmailMessage
import smtplib

from email_validator import EmailNotValidError, ValidatedEmail
from fastapi    import APIRouter, BackgroundTasks, Response, status

from user_app.configs import settings

user = APIRouter()

@user.get()
def get():
    pass


@user.post()
def post():
    pass


@user.put()
def put():
    pass



@user.post("/mail")
def mail_send(send_to:str,
              rsps:Response,
              bts: BackgroundTasks):
    try:
        # check email addr.
        emailinfo = ValidatedEmail(send_to, 
                                   check_deliverability=False)
        email_norm = emailinfo.normalized


        # create email
        emsg = EmailMessage()
        emsg['Subject'] = "mailing test"
        emsg['From'] = settings.SMTP_address
        emsg['To'] = email_norm # type Email
        emsg.set_content(f"message from {emsg['From']} to {email_norm} for a test.")
        # send email
        def task_smtp():
            with smtplib.SMTP_SSL(settings.SMTP_server, settings.SMTP_port_SSL) as smtp:
                smtp.login(settings.SMTP_address, settings.SMTP_password)
                smtp.send_message(emsg)
        bts.add_task(task_smtp) 

    except EmailNotValidError as e:
        rsps.status_code = status.HTTP_400_BAD_REQUEST
        return str(e)
    
    return "sending... maybe..."
