QT += widgets
QT += gui-private
QT += widgets-private
QT += core-private

HEADERS       = \
                widgetgallery.h \
    qflatstyle.h \
    form.h
SOURCES       = main.cpp \
                widgetgallery.cpp \
    qflatstyle.cpp \
    form.cpp \
    qstylehelper.cpp

FORMS += \
    form.ui
