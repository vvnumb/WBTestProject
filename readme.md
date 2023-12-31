# Тестовое задание в Wildberries


## ТЗ
Написать простейший HTTP сервер на Python >=3.7 версии, который принимает запросы на:\
    - сохранение записи\
    - выдачу записи по уникальному идентификатору\
    - выдачу множества записей\

Запись представляет собой объект из 2 полей:\
    - id: уникальный идентификатор записи\
    - data: данные в свободном формате на ваше усмотрение\

Между запусками сервер должен сохранять все ранее сохранённые записи.\
Использовать готовые базы данных нельзя.\

Пожелания:
    - чем меньше зависимостей будет у проекта тем лучше\
    - скрипт оценивающий производительность сервера на какой-либо выборке/выборках (на ваше 
усмотрение)\
    - если вы сможете написать несколько вариантов реализаций то это будет большой плюс\


## Реализация

Было выполнено 2 реализации HTTP сервера: 
1) Собственный сервер на базе стандарного пакета http. Установка дополнительных зависимостей 
   не требуется
2) Реализация на FastApi. Для запуска требуется поменять ключ в файле config.settings и 
   установить зависимости из файла ```fastapi_impl_requirements.txt```

Для хранения данных был выбран обычный txt-файл

В качестве подхода был использован подход DDD, что позволило единообразно использовать 
сущности/доступы к "БАЗЕ"/сервисы

Тесты и бенчмарки не были реализованы из-за нехватки времени

По проекту есть комментарии с тегом ```note: ```, в них я обозначал то, что можно было бы 
имплементировать в свое решение, но на что у меня не было времени/цели в ТЗ. 