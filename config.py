from configparser import ConfigParser

def config_read():
    config=ConfigParser()
    config.read("config.ini")
    return config


site_ip=config_read()['site']['ip']
site_port=config_read()['site']['port']
base_ip=config_read()['base']['ip']
base_port=config_read()['base']['port']
base_name=config_read()['base']['name']
base_user=config_read()['base']['user']
base_passw=config_read()['base']['passw']
table_users=config_read()['table']['users']
table_message=config_read()['table']['message']