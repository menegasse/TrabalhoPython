import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtp.login('menegassehugo12@gmail.com', '36380170h')

de = 'menegassehugo12@gmail.com'
para = ['menegassehugo@gmail.com']
msg = """From: %s
To: %s
Subject: Buteco Open Source

Email de teste do Buteco Open Source.""" % (de, ', '.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()