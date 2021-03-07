import apiai, json

def textMessage(s):
    # Токен API к Dialogflow
    request = apiai.ApiAI('AIzaSyCJtxEMS7U5nHO3DoktRWyDDOwj7zNM9x8').text_request()
    # На каком языке будет послан запрос
    request.lang = 'ru'
    # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.session_id = 'PyPro'
    # Посылаем запрос к ИИ с сообщением от юзера
    request.query = s
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # Разбираем JSON и вытаскиваем ответ
    #response=''
    response = responseJson['result']['fulfillment']['speech']
    # Если есть ответ от бота - выдаём его,
    # если нет - бот его не понял
    if response:
        return response
    else:
        return 'Я Вас не совсем понял!'

s=''
while(s!='Пока'):
    s=input('Введите ваше сообщение: ')
    print(textMessage(s))