import smtplib

class Email():
   
   def __init__(self,email='',senha=''):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    smtp.login('teste@gmail.com', 'passwordteste')

    de = 'menegassehugo12@gmail.com'
    para = [f'{email}']
    msg = """From: %s
    To: %s
    Subject: Recuperando Senha 

    Sua senha: %s.""" % (de, ', '.join(para),senha)

    smtp.sendmail(de, para, msg)

    smtp.quit()
