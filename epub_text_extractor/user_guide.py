from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("دليل المستخدم")
        self.showFullScreen()
        self.الدليل=qt.QListWidget()
        self.الدليل.addItem("CTRL+Cنسخ جزء من النص, يجب تحديد الجزء المراد نسخه أولا")
        self.الدليل.addItem("CTRL+A نسخ النص كاملا")        
        self.الدليل.addItem("CTRL+T ترجمة النص")
        self.الدليل.addItem("CTRL+P طباعة النص")
        self.الدليل.addItem("CTRL+S حفظ النص كمستند نصي")
        self.الدليل.addItem("CTRL+- تصغير حجم الخط")
        self.الدليل.addItem("CTRL+= تكبير حجم الخط")
        self.الدليل.addItem("معلومة هامة, إستخراج النص يعمل بدون إنترنيت, لكن الترجمة تعمل بإنترنيت")
        l=qt.QVBoxLayout(self)
        l.addWidget(self.الدليل)                