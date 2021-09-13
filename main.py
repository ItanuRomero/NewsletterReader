import pyttsx3
import easyimap as ei
import re


def get_email(sender):
    user = "newsletterreaderbot@gmail.com"
    password = "ImARobotWhoReadsNewsletters"
    inbox = ei.connect("imap.gmail.com", user, password)
    for email_id in range(0, len(inbox.listids())):
        email = inbox.mail(inbox.listids()[email_id])
        if sender in email.from_addr:
            newsletter_txt = open('newsLetterText.txt', 'w', encoding='utf8')
            newsletter_txt.write(email.title)
            body = email.body.split('Cancelar inscrição')[0]
            warning = ". Aqui estava um link, acesse a newsletter para clicar."
            body = warning.join(re.split("\(|\)|\[|\]", body)[::2])
            newsletter_txt.write(body)
            newsletter_txt.close()
    inbox.quit()


def say_and_save(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25)
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text, 'NewsletterSpeaked.mp3')
    engine.runAndWait()
    engine.stop()


newsletter = 'newsletter@filipedeschamps.com.br'
get_email(newsletter)
file = open("./newsLetterText.txt", 'r', encoding='utf8')
text_from_file = file.read()
say_and_save(text_from_file)
