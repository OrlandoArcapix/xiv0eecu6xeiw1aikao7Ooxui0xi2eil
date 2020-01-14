import distutils, salt

postconf = distutils.spawn.find_executable("postconf")

def setconfig(setting, value):
    """Sets a postfix configuration setting.

    Parameters:
        setting (str): setting
        value (str): value to set
    """
    __salt__['cmd.run'](postconf + ' ' + setting + '=' + value)

