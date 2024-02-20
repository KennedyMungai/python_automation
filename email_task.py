"""The script containing the logic to send emails"""
import argparse
import configparser
import smtplib
from email.message import EmailMessage


def main(to_email, server, port, from_email, password):
    """The main function for the script

    Args:
        to_email (email): Destination mail
        server (string): Server Address
        port (string): Port Address
        from_email (email): Source Email
        password (string): The password of the from_mail box
    """
    print(f'With love, from {from_email} to {to_email}')

    # Create the message
    subject = 'With love, from ME to YOU'
    text = '''This is an example test'''
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Open communication and send
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='Destination email')
    parser.add_argument(
        '-c', dest='config', type=argparse.FileType('r'), help='config file', default=None)

    args = parser.parse_args()

    if not args.config:
        print('Error, a config file is required')
        parser.print_help()
        exit(1)

    config = configparser.ConfigParser()
    config.read_file(args.config)

    main(
        args.mail,
        server=config['DEFAULT']['server'],
        port=config['DEFAULT']['port'],
        from_email=config['DEFAULT']['email'],
        password=config['DEFAULT']['password']
    )
