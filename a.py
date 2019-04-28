import os
# from Check_Attack import check_attack


def launch_attack():
    os.system('sudo mkdir /home/victim/Desktop/Launch attack')
    fo = open('/home/victim/Desktop/Launch attack/test.txt')

    fo.write('hey')

    fo.close()

    return


if __name__ == '__main__':
    launch_attack()
