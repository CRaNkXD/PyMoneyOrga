from PySide2 import QtWidgets, QtCore


class FloatDelegate(QtWidgets.QStyledItemDelegate):
    """
    ItemDelegate class for float values.
    Can be used to specify the decimal precision shown in a table.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

    def displayText(self, value, locale):
        try:
            number = float(value)
        except ValueError:
            return super(FloatDelegate, self).displayText(value, locale)
        else:
            return f"{number:.2f}".replace(".", ",")

        # There seems to be a bug in Pyside. If the parameter f or prec are used
        # the toString methods always uses scientific notation.
        # The precision is not applied to the decimals but to the whole number.

        # return locale.toString(number, f="f", prec=2)
