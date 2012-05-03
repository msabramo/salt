'''
Commands for OS X

Some of these may be possible with other operating systems using other commands
and thus could be abstracted.
'''

import os


def screensaver():
    '''
    Launch the screensaver
    '''

    cmd = 'open /System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app'

    return __salt__['cmd.run'](cmd)


def lock():
    '''
    Lock the screen
    '''

    cmd = '/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend'

    return __salt__['cmd.run'](cmd)


def set_volume(volume):
    '''
    Set the volume of sound
    '''

    cmd = 'osascript -e "set Volume {0}"'.format(volume)

    return __salt__['cmd.run'](cmd)


def launchctl_list():
    '''
    Do launchctl list
    '''

    cmd = 'launchctl list'

    return [line.split("\t") for line in __salt__['cmd.run'](cmd).splitlines()]


def launchctl_stop(job_label):
    '''
    Do launchctl stop

    @todo: Not working for some reason
    launchctl stop error: No such process
    '''

    cmd = 'launchctl stop {0}'.format(job_label)

    return __salt__['cmd.run'](cmd)


def launchctl_start(job_label):
    '''
    Do launchctl start

    @todo: Not working for some reason
    launchctl start error: No such process
    '''

    cmd = 'launchctl start {0}'.format(job_label)

    return __salt__['cmd.run'](cmd)


def itunes_pause():
    '''
    Do itunes pause
    '''

    cmd = """osascript -e 'tell application "iTunes" to pause'"""

    return __salt__['cmd.run'](cmd)


def itunes_play():
    '''
    Do itunes play
    '''

    cmd = """osascript -e 'tell application "iTunes" to play'"""

    return __salt__['cmd.run'](cmd)
