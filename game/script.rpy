define a = Character("Антон")
define t = Character("Тлеужан")

# ---------------- ПЕРСОНАЖИ ----------------

# Антон
image anton neutral = "Anton neutral.png"
image anton happy = "Anton happy.png"
image anton sad = "Anton sad.png"
image anton angry = "Anton angry.png"
image anton tired = "Anton tired.png"

# Тлеужан
image tleuzhan neutral = "Tleuzhan neutral.png"
image tleuzhan smile = "Tleuzhan smile.png"
image tleuzhan shocked = "Tleuzhan shocked.png"
image tleuzhan tired = "Tleuzhan tired.png"
image tleuzhan laugh = "Tleuzhan laugh.png"

# ---------------- ФОНЫ ----------------

image bg hall = im.Scale("hallway.jpg", 1920, 1080)
image bg class = im.Scale("classroom.jpg", 1920, 1080)
image bg cafe = im.Scale("cafeteria.jpg", 1920, 1080)
image bg street = im.Scale("street.png", 1920, 1080)
image bg room = im.Scale("dorm room.png", 1920, 1080)
image bg pc = im.Scale("computer desk.png", 1920, 1080)
image bg evening = im.Scale("evening city.png", 1920, 1080)
image bg office = im.Scale("teacher office.png", 1920, 1080)
image bg entrance = im.Scale("college entrance.png", 1920, 1080)
image bg nightclass = im.Scale("classroom night.png", 1920, 1080)

# ---------------- НАЧАЛО ----------------

label start:

    play music "audio/music.mp3"

    # СЦЕНА 1
    scene bg entrance
    with fade

    "Раннее утро."

    show anton tired at left
    show tleuzhan tired at right

    a "Брат... сегодня защита проекта."

    t "Ты его доделал?"

    a "Я его даже не начинал."

    # СЦЕНА 2
    scene bg hall
    with fade

    show anton sad at left
    show tleuzhan neutral at right

    t "До дедлайна два часа."

    a "Это конец."

    t "Не паникуй."

    # СЦЕНА 3
    scene bg cafe
    with fade

    show anton neutral at left
    show tleuzhan laugh at right

    t "Может просто скачать готовую работу?"

    a "Плохая идея."

    # СЦЕНА 4
    scene bg street
    with fade

    show anton tired at left

    "После пар Антон пошел домой."

    # СЦЕНА 5
    scene bg room
    with fade

    show anton neutral at center

    a "Ладно. Надо решать."

    # СЦЕНА 6
    scene bg pc
    with fade

    show anton tired at center

    "Антон открыл ноутбук."

    "На часах было уже 2:34."

    # СЦЕНА 7
    scene bg evening
    with fade

    "За окном почти никого не осталось."

    # СЦЕНА 8
    scene bg nightclass
    with fade

    show anton angry at left

    a "Я не успеваю."

    # СЦЕНА 9
    scene bg room
    with fade

    show tleuzhan shocked at right

    t "Есть два варианта."

    menu:

        "Скачать готовый проект":
            jump bad_end

        "Сделать самому":
            jump good_end

# ---------------- ПЛОХАЯ КОНЦОВКА ----------------

label bad_end:

    # СЦЕНА 10
    scene bg class
    with fade

    show anton neutral at left

    a "Я скачал проект из интернета."

    # СЦЕНА 11
    scene bg office
    with fade

    show anton sad at left

    "Преподаватель быстро нашел копию."

    a "Похоже, меня раскрыли..."

    "Плохая концовка."

    return

# ---------------- ХОРОШАЯ КОНЦОВКА ----------------

label good_end:

    # СЦЕНА 12
    scene bg class
    with fade

    show anton happy at left
    show tleuzhan smile at right

    a "Я сделал всё сам."

    t "Красава."

    "Преподаватель похвалил Антона."

    a "Наконец-то получилось."

    "Хорошая концовка."

    return