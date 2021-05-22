try:
    from . import *
except ImportError:
    from pathlib import Path
    from subprocess import run
    pth = Path(__file__).parent
    run(f'py -m {pth.name}', cwd=pth.parent)
    raise SystemExit


if __name__ == "__main__":
    CreateBalloontip('title', 'message', 5)
    playSound()
