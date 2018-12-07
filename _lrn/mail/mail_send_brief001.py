# NOT WORKS
import yagmail

contents = [
    '<h1>This is a big title!</h1>', 'Body text, and here is an embedded image:',
    {'/attachment/scrn001.png': 'opa'}  # this is out of works,
    ]                                   # all other stuff is good. Just need to set a keyring log/pass

yagmail.SMTP('sm.mail.auto@gmail.com').send('mahnosam@gmail.com', 'ololo', contents=contents)
