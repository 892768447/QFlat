/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QFLATSTYLE_H
#define QFLATSTYLE_H

#include <QProxyStyle>
#include <QtWidgets/qcommonstyle.h>
#include <QtWidgets/qproxystyle.h>

QT_BEGIN_NAMESPACE

//! [0]
class QFlatStyle : public QProxyStyle
{
    Q_OBJECT

public:
    QFlatStyle();
    ~QFlatStyle();

    void drawControl(ControlElement element, const QStyleOption *option, QPainter *painter,
                         const QWidget *widget) const Q_DECL_OVERRIDE;
    void drawComplexControl(ComplexControl control, const QStyleOptionComplex *option,
                                QPainter *painter, const QWidget *widget) const Q_DECL_OVERRIDE;

    // Used for grip handles
    QColor lightShade() const {
        return QColor(255, 255, 255, 90);
    }
    QColor darkShade() const {
        return QColor(0, 0, 0, 60);
    }

    QColor topShadow() const {
        return QColor(0, 0, 0, 18);
    }

    QColor innerContrastLine() const {
        return QColor(255, 255, 255, 30);
    }

    // On mac we want a standard blue color used when the system palette is used
    bool isMacSystemPalette(const QPalette &pal) const {
        Q_UNUSED(pal);
#if defined(Q_OS_MACX)
        const QPalette *themePalette = QGuiApplicationPrivate::platformTheme()->palette();
        if (themePalette && themePalette->color(QPalette::Normal, QPalette::Highlight) ==
                pal.color(QPalette::Normal, QPalette::Highlight) &&
            themePalette->color(QPalette::Normal, QPalette::HighlightedText) ==
                pal.color(QPalette::Normal, QPalette::HighlightedText))
            return true;
#endif
        return false;
    }

    QColor highlight(const QPalette &pal) const {
        if (isMacSystemPalette(pal))
            return QColor(60, 140, 230);
        return pal.color(QPalette::Highlight);
    }

    QColor highlightedText(const QPalette &pal) const {
        if (isMacSystemPalette(pal))
            return Qt::white;
        return pal.color(QPalette::HighlightedText);
    }

    QColor outline(const QPalette &pal) const {
        if (pal.window().style() == Qt::TexturePattern)
            return QColor(0, 0, 0, 160);
        return pal.background().color().darker(140);
    }

    QColor highlightedOutline(const QPalette &pal) const {
        QColor highlightedOutline = highlight(pal).darker(125);
        if (highlightedOutline.value() > 160)
            highlightedOutline.setHsl(highlightedOutline.hue(), highlightedOutline.saturation(), 160);
        return highlightedOutline;
    }

    QColor tabFrameColor(const QPalette &pal) const {
        if (pal.window().style() == Qt::TexturePattern)
            return QColor(255, 255, 255, 8);
        return buttonColor(pal).lighter(104);
    }

    QColor buttonColor(const QPalette &pal) const {
        QColor buttonColor = pal.button().color();
        int val = qGray(buttonColor.rgb());
        buttonColor = buttonColor.lighter(100 + qMax(1, (180 - val)/6));
        buttonColor.setHsv(buttonColor.hue(), buttonColor.saturation() * 0.75, buttonColor.value());
        return buttonColor;
    }

    enum {
        menuItemHMargin      =  3, // menu item hor text margin
        menuArrowHMargin     =  6, // menu arrow horizontal margin
        menuRightBorder      = 15, // right border on menus
        menuCheckMarkWidth   = 12  // checkmarks width on menus
    };

    int animationFps         = 60;
};
//! [0]

QT_END_NAMESPACE

#endif
