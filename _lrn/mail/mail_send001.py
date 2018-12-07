import yagmail

contents = ['Body text, and here is an embedded image:', 'https://static.espreso.tv/uploads/article/2487043/images/im578x383-minob.jpg',
            'You can also find an audio file attached.', '_lrn/mail/attachment/scrn001.png']
yag = yagmail.SMTP('sm.mail.auto@gmail.com', 'gtkmvtyb')
yag.send('mahnosam@gmail.com', 'ololo', contents)

# adding creds for future use
# yagmail.register('sm.mail.auto@gmail.com', 'gtkmvtyb')
