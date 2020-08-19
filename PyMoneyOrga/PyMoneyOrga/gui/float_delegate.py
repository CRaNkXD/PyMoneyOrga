from PySide2 import QtWidgets, QtCore


class FloatDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def displayText(self, value, locale):
        try:
            number = float(value)
        except ValueError:
            return super(FloatDelegate, self).displayText(value, locale)
        else:
            return f"{number:.2f}".replace(".", ",")
