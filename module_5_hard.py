from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'User: {self.nickname}, password: {self.password}, age: {self.age}'

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'title: {self.title}, duration: {self.duration}, time_now: {self.time_now}, adult_mode: {self.adult_mode}'

class UrTube:
    users = []
    videos = []
    current_user = None

    def __init__(self):
        pass

    def __str__(self):
        return f'users: {self.users} and video: {self.videos}, current_user: {self.current_user}'

    def add(self, *args):
        flag = False

        for i in args:
            for j in self.videos:
                if j[0] == i.title:
                    flag = True
                    # print(f'Видео с именем {i.title} уже есть в базе')
                    break
                else:
                    flag = False

            if not flag:
                self.videos.append([i.title, i.duration, i.time_now, i.adult_mode])
                # print(f'Видео с именем {i.title} успешно сохранено в базу')



    def log_in(self, nickname, password):
        for i in self.users:
            if nickname.lower() == i[0] and hash(password) == i[1]:
                self.current_user = nickname
                break

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        count = len(self.users)
        i = 0
        while i < count:
            el = self.users[i]
            if nickname.lower() == el[0]:
                # print()
                print(f'Пользователь {nickname} уже существует')
                self.log_in(nickname, password)
                # print(f'Вход успешно выполнен под именем {self.current_user}')
                break
            elif i == count - 1:
                # print()
                # print(f'Пользователя с логином {nickname} не существует')
                new_user = User(nickname, password, age)
                self.users.append([new_user.nickname, new_user.password, age])
                # print(f'Пользователь с логином {nickname} успешно создан')
                self.log_in(nickname, password)
                # print(f'Вход успешно выполнен под именем {self.current_user}')
                break
            else:
                 i += 1

        if count == 0:
            # print()
            # print('База пользователей пуста, создаем первого пользователя')
            self.users.append([nickname, hash(password), age])
            # print(f'Пользователь с логином {nickname} успешно создан')
            self.log_in(nickname, password)
            # print(f'Вход успешно выполнен под именем {self.current_user}')
            return self

    def get_videos(self, title):
        result = []
        for i in self.videos:
            value = i[0].lower()
            if title.lower() in value:
                result.append(i[0])

        return result

    def watch_video(self, title):
        video = []
        user = []
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.users:
                if self.current_user == i[0]:
                    user = i
                    break

            for j in self.videos:
                if title == j[0]:
                    video = j
                    break
                else:
                    # print('Видео не найдено')
                    continue

            if video == []:
                return False
            elif video[3] == True and user[2] < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for k in range(1, video[1] + 1):
                    if k != video[1]:
                        sleep(1)
                        print(k, end=' ')
                    else:
                        sleep(1)
                        print(k, 'Конец видео')






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')