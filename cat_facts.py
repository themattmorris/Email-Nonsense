# -*- coding: utf-8 -*-
from __future__ import division
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from random import choice
import time

def send_mail(send_from, password, send_to, reply_to, subject, body, server="smtp.gmail.com:587"):
    assert type(send_to)==list
    
    msg = MIMEMultipart('alternative')
    msg.add_header('reply-to', reply_to)
    msg['From'] = send_from + ' <' + reply_to + '>'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(body, 'plain') )
    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(send_from, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

send_from = 'teddysbots@gmail.com'
password = 'goillini'
send_to = ['3097123420@vtext.com']
reply_to = '3097121597'
subject = ''

facts = [
        "Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.",
        "There are cats who have survived falls from over 32 stories (320 meters) onto concrete.",
        "A group of cats is called a clowder.",
        "Cats have over 20 muscles that control their ears.",
        "Cats sleep 70% of their lives.",
        "A cat has been mayor of Talkeetna, Alaska, for 15 years. His name is Stubbs.",
        "And one ran for mayor of Mexico City in 2013.",
        "In tigers and tabbies, the middle of the tongue is covered in backward-pointing spines, used for breaking off",
        "When cats grimace, they are usually \"taste-scenting.\" They have an extra organ that, with some breathing cont",
        "Cats can't taste sweetness.",
        "Owning a cat can reduce the risk of stroke and heart attack by a third.",
        "Wikipedia has a recording of a cat meowing because why not?",
        "The world's largest cat measured 48.5 inches long.",
        " Evidence suggests domesticated cats have been around since 3600 B.C., 2,000 years before Egypt's pharaohs.",
        "A cat's purr may be a form of self-healing, as it can be a sign of nervousness as well as contentment.",
        "Similarly, the frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
        "Adult cats only meow to communicate with humans.",
        "The world's richest cat is worth $13 million after his human passed away and left her fortune to him.",
        "Your cat recognizes your voice but just acts too cool to care (probably because they are).",
        "Cats are often lactose intolerant, so stop givin' them milk!",
        "Basically all cartoon cats lied to us: Raw fish is off the table for cats as well.",
        "The oldest cat video on YouTube dates back to 1894 (when it was made, not when it was uploaded, duh).",
        "In the 1960s, the CIA tried to turn a cat into a bonafide spy by implanting a microphone into her ear and a",
        "The technical term for \"hairball\" is \"bezoar.\"",
        "Female cats are typically right-pawed while male cats are typically left-pawed.",
        "Cats make more than 100 different sounds whereas dogs make around 10.",
        "A cat's brain is 90% similar to a human's — more similar than to a dog's.",
        "Cats and humans have nearly identical sections of the brain that control emotion.",
        "A cat's cerebral cortex (the part of the brain in charge of cognitive information processing) has 300 millio",
        "Cats have a longer-term memory than dogs, especially when they learn by actually doing rather than simply se",
        "Basically, cats have a lower social IQ than dogs but can solve more difficult cognitive problems when they f",
        "Cats have 1,000 times more data storage than an iPad.",
        "It was illegal to slay cats in ancient Egypt, in large part because they provided the great service of contr",
        "In the 15th century, Pope Innocent VIII began ordering the killing of cats, pronouncing them demonic.",
        "A cat has five toes on his front paws, and four on the back, unless he's a polydactyl.",
        "Polydactyl cats are also referred to as \"Hemingway cats\" because the author was so fond of them.",
        "There are 45 Hemingway cats living at the author's former home in Key West, Fla.",
        "Original kitty litter was made out of sand but it was replaced by more absorbent clay in 1948.",
        "Abraham Lincoln kept four cats in the White House.",
        "When asked if her husband had any hobbies, Mary Todd Lincoln is said to have replied \"cats.\"",
        "Isaac Newton is credited with inventing the cat door.",
        "One legend claims that cats were created when a lion on Noah's Ark sneezedand two kittens came out.",
        "A cat can jump up to six times its length.",
        "A house cat is faster than Usain Bolt.",
        "When cats leave their poop uncovered, it is a sign of aggression to let you know they don't fear you.",
        "Cats can change their meow to manipulate a human. They often imitate a human baby when they need food, for e",
        "Cats use their whiskers to detect if they can fit through a space.",
        "Cats only sweat through their foot pads.",
        "The first cat in space was French. She was named Felicette, or \"Astrocat.\" She survived the trip.",
        "Cats have free-floating clavicle bones that attach their shoulders to their forelimbs, which allows them to",
        " Hearing is the strongest of cat's senses: They can hear sounds as high as 64 kHz — compared with humans, who",
        "Cats can move their ears 180 degrees.",
        "They can also move their ears separately.",
        "A cat has detected his human's breast cancer.",
        "A cat's nose is ridged with a unique pattern, just like a human fingerprint.",
        "Cats have scent glands along their tail, their forehead, lips, chin, and the underside of their front paws.",
        "A cat rubs against people to mark its territory.",
        "Cats lick themselves to get your scent off.",
        "When a family cat died in ancient Egypt, family members would shave off their eyebrows as they mourned.",
        "They also had elaborate memorials that included mummifying the cat and either burying it in a family tomb or",
        "Cats were mythic symbols of divinity in ancient Egypt.",
        " Black cats are bad luck in the United States, but they are good luck in the United Kingdom and Australia.",
        "Most cats don't like water because their coats do not insulate them well enough.",
        "However, a cat called the Turkish Van does not have that insulation problem and LOVES it.",
        "The Egyptian Mau is the oldest breed of cat.",
        "This breed is also the fastest pedigreed cat.",
        "The Egyptian word for cat is, in fact, \"mau.\"",
        "Only 11.5% of people consider themselves \"cat people.\"",
        "Cat people are also 11% more likely to be introverted.",
        "Still, cat people are more open to new experiences than typical \"dog people.\"",
        "Cat owners who are male tend to be luckier in love, as they are perceived as more sensitive.",
        "Cat owners are 17% more likely to have a graduate degree.",
        "Cat people are 25% likely to pick George as their favorite Beatle.",
        "A cat's carbon footprint is similar to that of a VW Bug, whereas a dog's is more like a Hummer.",
        "When your cat brings home a dead mouse or bird, it may do so to show you that you suck at hunting.",
        "Cats have inferior daytime sight, but during the night they need seven times less light than humans to see.",
        "The largest litter of kittens produced 19 kittens.",
        "Eighty-eight percent of cats in the U.S. are spayed or neutered.",
        "Only 24% of cats who enter animal shelters are adopted."
        ]

used = []
body = "Meow! A friend subscribe you to Cat Facts!  You can respond with STOP if you'd like, but that won't stop you from receiving these awesome texts!  Enjoy :)"
send_mail(send_from, password, send_to, reply_to, subject, body)
texts = 10 # number of texts to be sent
wait_time = 5 # minutes
for x in range(texts):
    rand = choice([x for x in range(len(facts)) if x not in used])
    used.append(rand)
    body = facts[rand]
    send_mail(send_from, password, send_to, reply_to, subject, body)
    time.sleep(wait_time*60)