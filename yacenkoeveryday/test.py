import time
import vk_api
import schedule
import random
import requests
import threading
import os
from datetime import datetime


from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def write_msg(user_id,s):
    vk.method('messages.send', {'user_id': user_id, 'message': s, 'random_id':''})

def write_chat_msg(peer_id,s):
    vk.method('messages.send', {'peer_id': peer_id, 'message': s, 'random_id':''})

def job(arr,phr):
    print("I'm working...")
    #write_chat_msg(2000000000 + 1, 'hello world')
    photo4ka(random.randint(0, 8), 2000000000 + 2,arr,phr)
def photo4ka(i,id,arr,phr):
    session = requests.Session()
    attachments = []
    upload = vk_api.VkUpload(vk)
    image_url = arr[i]
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk2.messages.send(
        peer_id=id,
        attachment=','.join(attachments),
        message='Поздравляем нашего высокоуважаемого учителя с днём рождения!\n' + '\"'+phr[random.randint(0,9)] '\"',
        random_id=''
    )

def thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

os.environ["TZ"] = "Europe/Moscow"
time.tzset()

token = "paste_your_token_here"
vk = vk_api.VkApi(token=token)

vk._auth_token()
vk2=vk.get_api()
#try:
#    vk.auth()

#except vk_api.AuthError as error_msg:
#    print(error_msg)

#write_msg('175383048', 'hello world')

timeik="05:42"

arr=['paste_image_url_here'
    ]

phr=['Ёж - птица гордая, пока не пнёшь, не полетит',
    'Мемасик: нельзя так просто взять и создать Paper',
    'Как можно использовать программирование в обычной жизни? Ну, например, можно красиво и оригинально сказать человеку, что он лох!',
    'Программисты - они не для того, чтобы думать, они для того, чтобы код писать!',
    'Какой синоним в Java слову "дофига"? Правильно, for.',
    'И он делает какого-то макаронного монстра!',
    'У человека вон уже панда летает',
    'Сломайте ему руки, пусть они правильно срастутся!',
    'Тяжело в лечении, легко в раю',
    'И как бы все ни было на самом деле, важно помнить, что... \n Всё каефно :^)'
    ]


schedule.every().day.at(timeik).do(job,arr,phr)

x = threading.Thread(target=thread, args=())
x.start()



#write_chat_msg(2000000000 + 1,'Соня, как ты?')

longpoll = VkBotLongPoll(vk,186365852)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('yacenkoeveryday '+ str(datetime.now()))
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower().split(" ")[1] == "set":
                    hours,minutes= event.object.text.lower().split(" ")[2].split(":")
                    h=int(hours)
                    m=int(minutes)
                    if h<=24 and h>=0 and m>=0 and m<60 and len(hours)<=2 and len(minutes)<=2:
                        if h<10: hours='0'+hours
                        timeik=str(hours) + ":" + str(minutes)
                        print(timeik)
                        schedule.every().day.at(timeik).do(job,arr,phr)
                    else:
                        write_chat_msg(event.object.peer_id, "Неверный формат времени")
                # vk.method("messages.send", {"peer_id": event.object.peer_id, "message": 'Приём',
                #                                "random_id": 0})
                else:
                    photo4ka(random.randint(0,8),event.object.peer_id,arr,phr)
                print(event.object.peer_id)
            else:
                #if event.object.text.lower() == "привет":
                # vk.method("messages.send", {"user_id": event.object.from_id, "message": 'Приём',
                #                                 "random_id": 0})
                photo4ka(random.randint(0, 8),event.object.from_id,arr,phr)
