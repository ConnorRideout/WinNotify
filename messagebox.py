from typing import Union as U
from sys import argv

from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QAbstractButton
)


class Messagebox(QMessageBox):
    """-----
    Display a PyQt5.QMessageBox

    Class Methods
    ----------
    askquestion: Asks the user a question and returns the response

    showinfo: Show the user a simple info dialog

    showwarning: Show the user a simple warning dialog

    showerror: Show the user a simple error dialog
    """

    _icons = dict(noicon=QMessageBox.NoIcon,
                  question=QMessageBox.Question,
                  info=QMessageBox.Information,
                  warning=QMessageBox.Warning,
                  critical=QMessageBox.Critical)
    _buttons = dict(ok=QMessageBox.Ok,
                    open=QMessageBox.Open,
                    save=QMessageBox.Save,
                    cancel=QMessageBox.Cancel,
                    close=QMessageBox.Close,
                    discard=QMessageBox.Discard,
                    apply=QMessageBox.Apply,
                    reset=QMessageBox.Reset,
                    restoredefaults=QMessageBox.RestoreDefaults,
                    help=QMessageBox.Help,
                    saveall=QMessageBox.SaveAll,
                    yes=QMessageBox.Yes,
                    yestoall=QMessageBox.YesToAll,
                    no=QMessageBox.No,
                    notoall=QMessageBox.NoToAll,
                    abort=QMessageBox.Abort,
                    retry=QMessageBox.Retry,
                    ignore=QMessageBox.Ignore)
    out: str
    _ = QApplication(argv[:1])

    def __init__(self,
                 title: str,
                 message: str,
                 icon: QMessageBox.Icon = QMessageBox.NoIcon,
                 buttons: U[QMessageBox.StandardButton,
                            QMessageBox.StandardButtons] = QMessageBox.Ok,
                 default: QMessageBox.StandardButton = QMessageBox.NoButton,
                 escape: QMessageBox.StandardButton = QMessageBox.NoButton):
        QMessageBox.__init__(self)
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(icon)
        self.setStandardButtons(buttons)
        self.setDefaultButton(default)
        self.setEscapeButton(escape)
        self.buttonClicked.connect(self._btnclick)
        self.exec()

    def _btnclick(self, btn: QAbstractButton):
        self.out = btn.text().lstrip("&").replace(' ', '').lower()

    @classmethod
    def askquestion(cls, title: str, message: str, buttons: tuple[str] = ("yes", "no"), icon: str = "question") -> str:
        """-----
        Ask the user a question

        Parameters
        ----------
        title (str): The messagebox window title

        message (str): The question to ask in the body of the messagebox

        buttons (tuple[str], optional): [default=("yes", "no")] The buttons to show. The first item listed will be set as the \
default button, the last will be the 'escape' button if listed. Any combination of: ok, open, save, cancel, close, discard, \
apply, reset, restoredefaults, help, saveall, yes, yestoall, no, notoall, abort, retry, ignore

        icon (str, optional): [default="question"] The messagebox icon. One of: noicon, question, info, warning, critical

        sound (str, optional): [default="silent"] The sound to play with the messagebox. One of: silent, info, error


        Returns:
        --------
        str : The lowercase text of the pressed button
        """

        btnlst = [cls._buttons.get(btnstr.lower(), QMessageBox.NoButton)
                  for btnstr in buttons]
        btns = QMessageBox.NoButton
        for btn in btnlst:
            btns |= btn
        return cls(title=title,
                   message=message,
                   icon=cls._icons.get(icon.lower(), QMessageBox.NoIcon),
                   buttons=btns,
                   default=btnlst[0],
                   escape=btnlst[-1]).out

    @classmethod
    def showinfo(cls, title: str, message: str) -> None:
        """-----
        Show an infobox

        Parameters
        ----------
        title (str): The messagebox window title

        message (str): The info message in the body of the messagebox
        """

        cls(title=title,
            message=message,
            icon=QMessageBox.Information)

    @classmethod
    def showwarning(cls, title: str, message: str) -> None:
        """-----
        Show a warning

        Parameters
        ----------
        title (str): The messagebox window title

        message (str): The warning message in the body of the messagebox
        """

        cls(title=title,
            message=message,
            icon=QMessageBox.Warning)

    @classmethod
    def showerror(cls, title: str, message: str) -> None:
        """-----
        Show an error

        Parameters
        ----------
        title (str): The messagebox window title

        message (str): The error message in the body of the messagebox
        """

        cls(title=title,
            message=message,
            icon=QMessageBox.Critical)


if __name__ == '__main__':
    answer = Messagebox.askquestion("Ask Question",
                                    "This is Messagebox.askquestion. The output is saved")
    Messagebox.showinfo("Show Info",
                        f"This is Messagebox.showinfo. On the previous popup, you answered '{answer}'")
    Messagebox.showwarning("Show Warning",
                           "This is Messagebox.showwarning")
    Messagebox.showerror("Show Error",
                         "This is Messagebox.showerror")
