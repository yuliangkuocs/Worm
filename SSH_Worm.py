import paramiko


def ssh_command(ip, user, password, command, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(ip, username=user, password=password, port=port)

    session = client.get_transport().open_session()

    if session.active:
        print('Session Active')
        session.exec_command(command)
    else:
        print('Session Failed')


if __name__ == '__main__':
    ssh_command('192.168.31.145', 'victim', 'victim', 'mkdir ~/Desktop/Mytest', 5555)



