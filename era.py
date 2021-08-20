import os
import _process
import os.path
import random

if __name__ == '__main__':
    #_process.greet()
    while True:
        get_user = input('User: ')
        if get_user == "bye":
                print('Era: Ok goodbye.')
                os._exit(0)
        elif os.path.isfile("_data\\" + get_user + ".er"):
            file = open("_data\\" + get_user + ".er", "r")
            _content = file.read().splitlines()
            if os.stat("_data\\" + get_user + ".er").st_size == 0:
                print("Era: I don't know the ans...")
                _process.tellMe(get_user)
            else:
                ans = random.choice(_content)
                print("Era: " + ans)
                #_process.say(ans)
                
        else:
            _process.tellMe(get_user)
