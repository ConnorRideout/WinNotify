try:
    from .src import *
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
        input_fields=[
            ('title', InputDialog.ChWgt.textbox(
                hint='CreateBalloontip Example')),
            ('message', InputDialog.ChWgt.textbox(
                hint='An example message')),
            ('timeout', InputDialog.ChWgt.spinbox(
                from_=1, to=10, default=5))
        ])

    if kwargs:
        CreateBalloontip(**kwargs)


if __name__ == "__main__":
    main()
