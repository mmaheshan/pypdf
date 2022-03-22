# install PyQtWebEngine to get this working
# pip install PyQtWebEngine

import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl, QMarginsF
from PyQt5.QtGui import QPageLayout, QPageSize
from PyQt5.QtWidgets import QApplication
url = 'https://en.wikipedia.org/wiki/Illinois_Central_College'



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loader = QtWebEngineWidgets.QWebEngineView()
    loader.setZoomFactor(1)

    layout = QPageLayout()
    layout.setUnits(QPageLayout.Millimeter)
    layout.setMode(QPageLayout.FullPageMode)
    layout.setMargins(QMarginsF(12, 16, 12, 20))
    layout.setPageSize(QPageSize(QPageSize.A4))
    layout.setOrientation(QPageLayout.Portrait)
    loader.load(QUrl(url))
    loader.page().pdfPrintingFinished.connect(lambda *args: QApplication.exit())

    def emit_pdf(finished):
        loader.page().printToPdf("test.pdf", pageLayout=layout)

    loader.loadFinished.connect(emit_pdf)
    sys.exit(app.exec_())

