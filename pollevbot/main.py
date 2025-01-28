from pollevbot import PollBot


def main():
    user='loganoscsher222'
    password='Daisy135!'
    host='profprairie'
    login_type='pollev'
    with PollBot(user, password, host) as bot:
        bot.run()


if __name__ == '__main__':
    main()
