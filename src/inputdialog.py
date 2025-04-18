from sys import argv as sys_argv
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QDoubleSpinBox,
    QApplication,
    QFormLayout,
    QVBoxLayout,
    QScrollArea,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QSpinBox,
    QDialog,
    QLayout,
    QWidget,
    QLabel
)
from typing import Optional as O, Union as U

try:
    from .playsound import PlaySound
except ImportError:
    from playsound import PlaySound


class InputDialog:
    """-----
    Display a PyQt5.QDialog asking for input

    Class Methods
    ----------
    multiinput: Asks the user for multiple inputs and returns the responses in a dictionary

    textinput: Asks the user for a string input and returns the response

    comboinput: Asks the user to choose an option from a combobox and returns the response

    spininput: Asks the user to choose an integer or float and returns the response


    Builder Class
    ----------
    ChildWidget|ChWgt: Create a child widget for use with above methods. One of <checkbox>, <combobox>, <spinbox>, or <textbox>
    """

    __app__ = QApplication(sys_argv)
    _layout: QFormLayout
    _main_layout: QVBoxLayout
    _fields: list[U[QWidget, QLayout,
                    tuple[U[str, QWidget], U[QWidget, QLayout]]]]
    out: dict[str, U[str, int, bool]]

    def __init__(
        self,
        title: str,
        input_fields: list[
            U[QWidget, QLayout, tuple[U[str, QWidget], U[QWidget, QLayout]]]
        ],
        parent: QWidget = None,
        playsound: str = None,
        icon: QIcon = None,
    ):
        """-----
        Parameters
        ----------
        title (str): the window title

        input_fields (list[QWidget | QLayout | tuple[str | QWidget, QWidget | QLayout]]): the fields to display

        parent (QWidget, optional): [default=None] the parent widget

        playsound (str, optional): [default=None] whether to play a sound. One of None, "alert", or "error"

        icon (QIcon, optional): [default=None] an icon to set for the dialog window

        """
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle(title)
        self.dialog.setMinimumWidth(450)
        if icon:
            self.dialog.setWindowIcon(icon)
        # set defaults
        self.out = dict()
        self.dialog.setStyleSheet("QDialog {background-color: #202328;}\n"
                                  "QWidget {font-size: 11pt;}")
        # construct layouts
        self._main_layout = QVBoxLayout(self.dialog)
        scrollArea = QScrollArea(self.dialog)
        scrollArea.setWidgetResizable(True)
        scrollAreaContents = QWidget()
        scrollAreaContents.setStyleSheet("background-color: #2d3640;"
                                         "font-size: 10pt;")
        scrollArea.setWidget(scrollAreaContents)
        self._layout = QFormLayout(scrollAreaContents)
        self._layout.setVerticalSpacing(8)
        # construct widgets
        self._fields = list()
        for item in input_fields:
            if isinstance(item, (list, tuple)):
                self._fields.append(item)
                self._layout.addRow(*item)
            else:
                self._main_layout.addWidget(item)
        self._main_layout.addWidget(scrollArea)
        # construct buttonbox
        btnbox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btnbox.accepted.connect(self._submit)
        btnbox.rejected.connect(self._cancel)
        btnbox.setCenterButtons(True)
        self._main_layout.addWidget(btnbox)
        # run
        if playsound == "error":
            PlaySound("Hand")
        elif playsound == "alert":
            PlaySound("Beep")
        self.dialog.exec()

    def _submit(self):
        """called when the <Ok> button is pressed. Override this function to change the default action (default=set <self.out> to a dictionary where labelText=value, then close the input dialog)"""

        for lbl, wgt in self._fields:
            if isinstance(wgt, QLineEdit):
                val = wgt.text()
            elif isinstance(wgt, QComboBox):
                val = wgt.currentText()
            elif isinstance(wgt, (QSpinBox, QDoubleSpinBox)):
                val = wgt.value()
            elif isinstance(wgt, QCheckBox):
                val = wgt.isChecked()
            else:
                val = "ERROR"
            self.out[lbl] = val
        self.dialog.close()

    def _cancel(self):
        """called when the <Cancel> button is pressed. Override this function to change the default action (default=close input dialog)"""
        self.dialog.close()

    class ChildWidget:
        """Builder class for the dialog. Available methods are checkbox, combobox, spinbox, or textbox"""

        def checkbox(text: str = "", default: bool = False) -> QCheckBox:
            """-----
            Build a QCheckBox

            Parameters
            ----------
            text (str, optional): [default=""] the checkbox's text

            default (bool, optional): [default=False] the default state of the checkbox


            Returns:
            --------
            QCheckBox : the initialized QCheckBox
            """

            cbx = QCheckBox(text)
            cbx.setChecked(default)
            return cbx

        def combobox(options: list[str], default: U[str, int] = 0) -> QComboBox:
            """-----
            Build a QComboBox

            Parameters
            ----------
            options (list[str]): a list of options

            default (str | int, optional): [default=0] the option to have selected as a default. Either the index or value


            Returns:
            --------
            QComboBox : the initialized QComboBox
            """

            cbx = QComboBox()
            cbx.addItems(options)
            if default:
                i = cbx.findText(default) if isinstance(
                    default, str) else default
                cbx.setCurrentIndex(i)
            cbx.adjustSize()
            cbx.setMinimumHeight(round(cbx.height() * 1.7))
            return cbx

        def spinbox(
            from_: U[int, float],
            to: U[int, float],
            step: U[int, float] = 1,
            default: U[int, float] = None,
        ) -> U[QSpinBox, QDoubleSpinBox]:
            """-----
            Build a QSpinBox | QDoubleSpinBox

            Parameters
            ----------
            from_ (int | float): the minimum value

            to (int | float): the maximum value

            step (int | float, optional): [default=1] the step between values

            default (int | float, optional): [default=None] the value to set as default


            Returns:
            --------
            QSpinBox | QDoubleSpinBox : the initialized QSpinBox (if integers) or QDoubleSpinBox (if floats)
            """

            if isinstance(from_ + to + step, float):
                from_ = float(from_)
                to = float(to)
                step = float(step)
                sbx = QDoubleSpinBox()
            else:
                sbx = QSpinBox()
            sbx.setRange(from_, to)
            sbx.setSingleStep(step)
            sbx.setWrapping(True)
            sbx.adjustSize()
            sbx.setMinimumHeight(round(sbx.height() * 1.7))
            if isinstance(default, (int, float)):
                sbx.setValue(default)
            return sbx

        def textbox(hint: str = None, default: str = None) -> QLineEdit:
            """-----
            Build a QLineEdit

            Parameters
            ----------
            hint (str, optional): [default=None] the textbox's placeholder text

            default (str, optional): [default=None] the text to place in the textbox. This will overwrite the hint if both are provided


            Returns:
            --------
            QLineEdit : the initialized widget
            """

            txt = QLineEdit()
            txt.adjustSize()
            txt.setMinimumHeight(round(txt.height() * 1.7))
            if default:
                txt.setText(default)
            elif hint:
                txt.setPlaceholderText(hint)
            return txt

    ChWgt = ChildWidget

    @classmethod
    def multiinput(
        cls,
        title: str,
        input_fields: list[tuple[str, U[QLineEdit, QComboBox, QSpinBox, QCheckBox]]],
        message: str = None,
        parent: QWidget = None,
        playsound: str = None,
        icon: QIcon = None,
    ) -> dict[str, U[str, int, bool]]:
        """-----
        Asks the user for multiple inputs and returns the responses in a dictionary

        Parameters
        ----------
        title (str): the window title

        input_fields (list[tuple[str, QWidget], ...]): a sequence of tuples (labelText, QWidget). Use the InputDialog.ChildWidget functions to create the QWidgets

        message (str, optional): [default=None] the message to put above all other inputs

        parent (QWidget, optional): [default=None] the parent of the window

        playsound (str, optional): [default=None] a sound to play. One of None, "alert", or "error"

        icon (QIcon, optional): [default=None] an icon to set for the dialog window


        Returns:
        --------
        None : The user pressed <Cancel> or the window was closed

        dict[str, str | int | bool] : The user's responses {labelText: responseValue, ...}
        """

        if isinstance(message, str):
            msg = QLabel(message)
            msg.setWordWrap(True)
            input_fields = list(input_fields)
            input_fields.insert(0, msg)
        return (
            cls(
                title=title,
                parent=parent,
                input_fields=input_fields,
                playsound=playsound,
                icon=icon,
            ).out
            or None
        )

    @classmethod
    def textinput(
        cls,
        title: str,
        label: str,
        default: str = None,
        message: str = None,
        parent: QWidget = None,
        playsound: str = None,
        icon: QIcon = None,
    ) -> O[str]:
        """-----
        Asks the user for a string input and returns the response

        Parameters
        ----------
        title (str): the window title

        label (str): the input label

        default (str, optional): [default=None] the input's default string

        message (str, optional): [default=None] the message to put above all other inputs

        parent (QWidget, optional): [default=None] the parent of the window

        playsound (str, optional): [default=None] a sound to play. One of None, "alert", or "error"

        icon (QIcon, optional): [default=None] an icon to set for the dialog window


        Returns:
        --------
        None : The user pressed <Cancel> or the window was closed

        str : The user's string
        """

        wgt = cls.ChWgt.textbox(default)
        if isinstance(message, str):
            msg = QLabel(message)
            msg.setWordWrap(True)
            in_f = [msg, (label, wgt)]
        else:
            in_f = [(label, wgt)]
        return cls(
            title=title,
            parent=parent,
            input_fields=in_f,
            playsound=playsound,
            icon=icon,
        ).out.get(label)

    @classmethod
    def comboinput(
        cls,
        title: str,
        label: str,
        options: list[str],
        default: U[str, int] = 0,
        message: str = None,
        parent: QWidget = None,
        playsound: str = None,
        icon: QIcon = None,
    ) -> O[str]:
        """-----
        Asks the user to choose an option from a combobox and returns the response

        Parameters
        ----------
        title (str): the window title

        label (str): the input's label

        options (list[str]): the available options

        default (str | int, optional): [default=0] the default index or value

        message (str, optional): [default=None] the message to put above all other inputs

        parent (QWidget, optional): [default=None] the parent of the window

        playsound (str, optional): [default=None] a sound to play. One of None, "alert", or "error"

        icon (QIcon, optional): [default=None] an icon to set for the dialog window


        Returns:
        --------
        None : The user pressed <Cancel> or the window was closed

        str : The user's chosen option
        """

        wgt = cls.ChWgt.combobox(options, default)
        fields = [(label, wgt)]
        if isinstance(message, str):
            msg = QLabel(message)
            msg.setWordWrap(True)
            fields.insert(0, msg)
        return cls(
            title=title,
            parent=parent,
            input_fields=fields,
            playsound=playsound,
            icon=icon,
        ).out.get(label)

    @classmethod
    def spininput(
        cls,
        title: str,
        label: str,
        from_: U[int, float],
        to: U[int, float],
        step: U[int, float] = 1,
        default: U[int, float] = None,
        message: str = None,
        parent: QWidget = None,
        playsound: str = None,
        icon: QIcon = None,
    ) -> O[U[int, float]]:
        """-----
        Asks the user to choose a number (integer or float) and returns the response

        Parameters
        ----------
        title (str): the window title

        label (str): the input's label

        from_ (int | float): the minimum value

        to (int | float): the maximum value

        step (int | float, optional): [default=1] the step between values

        default (int | float, optional): [default=None] the default value

        message (str, optional): [default=None] the message to put above all other inputs

        parent (QWidget, optional): [default=None] the parent of the window

        playsound (str, optional): [default=None] a sound to play. One of None, "alert", or "error"

        icon (QIcon, optional): [default=None] an icon to set for the dialog window


        Returns:
        --------
        None : The user pressed <Cancel> or the window was closed

        int | float : The user's selected value
        """

        wgt = cls.ChWgt.spinbox(from_, to, step, default)
        fields = [(label, wgt)]
        if isinstance(message, str):
            msg = QLabel(message)
            msg.setWordWrap(True)
            fields.insert(0, msg)
        return cls(
            title=title,
            parent=parent,
            input_fields=fields,
            playsound=playsound,
            icon=icon,
        ).out.get(label)


def test():
    from PyQt5.QtWidgets import QMessageBox

    fields = [
        ("This is a checkbox", InputDialog.ChildWidget.checkbox(default=True)),
        (
            "This is a combobox",
            InputDialog.ChildWidget.combobox(
                options=["option 1", "option 2", "option 3"], default="option 2"
            ),
        ),
        ("This is a spinbox", InputDialog.ChildWidget.spinbox(from_=0, to=5, step=0.5)),
        ("This is a textbox", InputDialog.ChildWidget.textbox()),
    ]
    ans = InputDialog.multiinput(
        title="test", input_fields=fields, message="An example multiinput InputDialog."
    )
    mbox = QMessageBox()
    mbox.setWindowTitle("Result")
    mbox.setText(str(ans))
    mbox.exec()


if __name__ == "__main__":
    test()
