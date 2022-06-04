import vk_api
import Image
import sys
from random import randint, randrange
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
sys.setrecursionlimit(15000)
attachments = []
ban = [i for i in range(1, 99)]
score = 0
b = []
a = 0
c = -2


def error():
    write_msg(event.user_id, "Не понял вашего ответа...")


def write_msg(user_id, message, keyboard=None):
    global attachments
    post = {'user_id': user_id,
            'random_id': 0,
            'message': message,
            'attachment': ','.join(attachments)}
    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        post = post

    vk.method('messages.send', post)
    attachments = []


def randph():
    global ban
    global a
    global b
    a = ban.pop(randrange(len(ban)))
    b.append(a)
    return int(a)


# API-ключ созданный ранее
token = "2d2e9dfb64c1f3ed4fd8be33023a4f29356a92ebb915df6d7f8bb1deb467a2a4b9a077391bf3c3308c034"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
upload = VkUpload(vk)
keyboard = VkKeyboard(one_time=True)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            if c > -1 and request.isnumeric() and request == f"{c+1}":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button(f"Ещё", VkKeyboardColor.POSITIVE)
                score += 3
                write_msg(
                    event.user_id, f"Вы получили 3 очка. Ваш счёт: {score}!", keyboard)
                c = -2
            elif c > -1 and request.isnumeric() and request != f"{c+1}":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button(f"Ещё", VkKeyboardColor.POSITIVE)
                write_msg(
                    event.user_id, f"Вы не угадали, правильный ответ {c+1}. Ваш счёт: {score}!", keyboard)
                c = -2
            else:
                if request.upper() == "СТАРТ" or request.upper() == "ЕЩЁ":
                    image1 = f"Image/{randph()}.jpg"
                    image2 = f"Image/{randph()}.jpg"
                    image3 = f"Image/{randph()}.jpg"
                    image4 = f"Image/{randph()}.jpg"
                    image5 = f"Image/{randph()}.jpg"
                    upload_image = upload.photo_messages(photos=image1)[0]
                    attachments.append(
                        f"photo{upload_image['owner_id']}_{upload_image['id']}")
                    upload_image = upload.photo_messages(photos=image2)[0]
                    attachments.append(
                        f"photo{upload_image['owner_id']}_{upload_image['id']}")
                    upload_image = upload.photo_messages(photos=image3)[0]
                    attachments.append(
                        f"photo{upload_image['owner_id']}_{upload_image['id']}")
                    upload_image = upload.photo_messages(photos=image4)[0]
                    attachments.append(
                        f"photo{upload_image['owner_id']}_{upload_image['id']}")
                    upload_image = upload.photo_messages(photos=image5)[0]
                    attachments.append(
                        f"photo{upload_image['owner_id']}_{upload_image['id']}")
                    write_msg(event.user_id, f"")
                    c = randint(0, 4)
                    with open("words.txt") as file:
                        d = file.readlines()[b[c]-1].split()

                    e = d[randrange(len(d))]
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button(f"1", VkKeyboardColor.POSITIVE)
                    keyboard.add_button(f"2", VkKeyboardColor.POSITIVE)
                    keyboard.add_button(f"3", VkKeyboardColor.POSITIVE)
                    keyboard.add_button(f"4", VkKeyboardColor.POSITIVE)
                    keyboard.add_button(f"5", VkKeyboardColor.POSITIVE)
                    write_msg(event.user_id, f"{e.capitalize()}", keyboard)
                    print(b, c, d, e)
                    b = []

                else:
                    error()
