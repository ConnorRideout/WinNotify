# [WinNotify](https://github.com/Cryden13/WinNotify)

A collection of methods that simplify a couple small Windows UI elements.

## Methods

### `CreateBalloontip`

Creates a popup balloontip on Windows 10

**Parameters:**

- *title* (str): The text to display at the top of the balloontip
- *msg* (str): The text to display as the body of the balloontip
- *timeout* (int|float, optional): [default=6] Seconds to keep the balloontip active. After ~4 seconds it is put into the action center
- *icon* (str, optional): [default="default"] The balloontip's icon. One of "default", "info", "warning", "error", or an *.ico image file path
- *silent* (bool, optional): [default=False] Whether to play a sound when the balloontip is displayed

### `Messagebox`

Display a PyQt5.QMessageBox

#### **Class Methods**

`askquestion`

Asks the user a question and waits for the response.  

**Parameters:**

- *title* (str): The messagebox window title
- *message* (str): The question to ask in the body of the messagebox
- *buttons* (tuple[str], optional): [default=("yes", "no")] The buttons to show. The first item listed will be set as the default button, the last will be the 'escape' button if listed. Any combination of: ok, open, save, cancel, close, discard, apply, reset, restoredefaults, help, saveall, yes, yestoall, no, notoall, abort, retry, ignore
- *icon* (str, optional): [default="question"] The messagebox icon. One of: noicon, question, info, warning, critical
- *sound* (str, optional): [default="silent"] The sound to play with the messagebox. One of: silent, info, error

**Returns:**

- str : The lowercase text of the pressed button

**`showinfo`**

Shows the user an infobox.

**Parameters:**

- *title* (str): The messagebox window title
- *message* (str): The info message in the body of the messagebox

**`showwarning`**

Shows the user a warning message.

**Parameters:**

- *title* (str): The messagebox window title
- *message* (str): The warning message in the body of the messagebox

**`showerror`**

Shows the user an error message.

**Parameters:**

- *title* (str): The messagebox window title
- *message* (str): The warning message in the body of the messagebox

### `PlaySound`

Play a default Windows 10 sound

**Parameters:**

- *sound* (str, optional): [default="Hand"] Which sound to play. One of "Asterisk", "Beep", "Exclamation", "Hand", "Question", or a "Windows [__].wav" file from C:\\WINDOWS\\Media

## Changelog

<table>
    <tbody>
        <tr>
            <th align="center">Version</th>
            <th align="left">Changes</th>
        </tr>
        <tr>
            <td align="center">1.0</td>
            <td>Initial release</td>
        </tr>
        <tr>
            <td align="center">1.1</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>condensed code</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed messages not showing</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">2.0</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>added overrideable clicking methods</li>
                        <li>added more notations</li>
                        <li>added type hints</li>
                        <li>updated built-in icon list</li>
                    </ul>
                    <dt>bugfixes</dt>
                    <ul>
                        <li>fixed timeout errors</li>
                        <li>fixed error messages</li>
                    </ul>
                </dl>
            </td>
        </tr>
        <tr>
            <td align="center">3.0</td>
            <td>
                <dl>
                    <dt>new</dt>
                    <ul>
                        <li>changed package name to winnotify</li>
                        <li>added Messagebox method</li>
                        <li>added PlaySound method</li>
                    </ul>
                </dl>
            </td>
        </tr>
    </tbody>
</table>
