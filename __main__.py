try:
    from . import *
except ImportError:
    from pathlib import Path
    from subprocess import run
    pth = Path(__file__).parent
    run(f'py -m {pth.name}', cwd=pth.parent)
    raise SystemExit


def main():
    ans = Messagebox.askquestion(title='Messagebox Example',
                                 message='Press "Yes" to play "Beep" or "No" to play "Hand"',
                                 buttons=('yes', 'no', 'cancel'))
    if ans == 'cancel':
        return

    PlaySound("Beep" if ans == 'yes' else "Hand")

    kwargs = InputDialog.multiinput(
        title='InputDialog Example',
        input_fields=(
            ('title', InputDialog._textbox(
                default='CreateBalloontip Example')),
            ('message', InputDialog._textbox(
                default='An example message')),
            ('timeout', InputDialog._spinbox(
                min=1, max=10, default=5))
        ))

    if kwargs:
        CreateBalloontip(**kwargs)


if __name__ == "__main__":
    main()
