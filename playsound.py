from subprocess import (Popen,
                        CREATE_NO_WINDOW
                        )
from pathlib import Path


def PlaySound(sound: str = "Hand"):
    """-----
    Play a default Windows 10 sound

    Parameters
    ----------
    sound (str, optional): [default="Hand"] Which sound to play. One of "Asterisk", "Beep", "Exclamation", "Hand", "Question", or a "Windows [__].wav" file from C:\\WINDOWS\\Media
    """

    syssounds = ["Asterisk", "Beep", "Exclamation", "Hand", "Question"]
    winsounds = [p for p in Path('C:\\WINDOWS\\Media').glob('Windows *.wav')
                 if sound in p.stem]
    Sound = sound.title()
    if Sound in syssounds:
        cmd = f'[system.media.systemsounds]::{Sound}.play()'
    elif winsounds:
        cmd = f'(new-object Media.SoundPlayer "{winsounds[0]}").play()'
    else:
        raise ValueError('< sound > parameter must be one of "Asterisk", "Beep", "Exclamation", '
                         '"Hand", "Question", or a "Windows *.wav" file from C: \\WINDOWS\\Media')
    Popen(['powershell', cmd], creationflags=CREATE_NO_WINDOW)
