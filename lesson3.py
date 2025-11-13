import os
from dotenv import load_dotenv
import smtplib

email_from = "pitonpav@yandex.ru"
my_name = "Павел"
email_to = "spounjkeee@gmail.com"
friend_name = "Антон"
website = "https://dvmn.org/profession-ref-program/spounjkeee/B3i0c/"

letter = """\
From: {from_email}
To: {to_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" .format(from_email=email_from, to_email=email_to)

letter = letter.replace('%website%', website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)

letter = letter.encode("UTF-8")

print(letter)

load_dotenv()

server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))
server.sendmail(email_from, email_to, letter)
server.quit()