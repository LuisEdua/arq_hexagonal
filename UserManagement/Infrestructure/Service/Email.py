from UserManagement.Domain.Entity.User import User
from UserManagement.Infrestructure.Service.EmailPort import EmailPort
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email(EmailPort):

    def run(self, user: User) -> None:
        msg = MIMEMultipart()
        msg['From'] = "correo@electronico"
        msg['To'] = user.email
        msg['Subject'] = "Verificacion"
        mensaje = (f"Usuario: {user.name} con el id {user.uuid} le enviamos su código de verificación acceda a esta "
                   f"ruta: \n http://127.0.0.1:5000//api/v1/users/{user.activation_token}/active")
        msg.attach(MIMEText(mensaje, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Usar 465 para SSL
            server.starttls()  # Activar la seguridad
            server.login("correo@electronico", "contraseña")
            text = msg.as_string()
            server.sendmail(msg['From'], msg['To'], text)
            server.quit()
        except Exception:
            print(f"Error al enviar el correo")
