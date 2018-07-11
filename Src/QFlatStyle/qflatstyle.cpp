#include <QtWidgets>
#include "qflatstyle.h"
#include <QtWidgets/private/qstylehelper_p.h>
#include <QtWidgets/private/qstyle_p.h>

#if QT_CONFIG(slider)
#include <qslider.h>
#endif

#include <QDebug>

using namespace QStyleHelper;

static const char *BackgroundColor     =  "backgroundColor";   // 背景颜色
static const char *BorderColor         =  "borderColor";       // 边框颜色
static const char *TextColor           =  "textColor";         // 文字颜色
static const char *BorderRadius        =  "borderRadius";      // 圆角

enum Direction {
    TopDown,
    FromLeft,
    BottomUp,
    FromRight
};

// from windows style
static const int windowsItemFrame        =  2; // menu item frame width
static const int windowsItemHMargin      =  3; // menu item hor text margin
static const int windowsItemVMargin      =  8; // menu item ver text margin
static const int windowsRightBorder      = 15; // right border on windows

static const int groupBoxBottomMargin    =  0;  // space below the groupbox
static const int groupBoxTopMargin       =  3;

#if QT_CONFIG(imageformat_xpm)
/* XPM */
static const char * const dock_widget_close_xpm[] = {
    "11 13 7 1",
    "  c None",
    ". c #D5CFCB",
    "+ c #8F8B88",
    "@ c #6C6A67",
    "# c #ABA6A3",
    "$ c #B5B0AC",
    "% c #A4A09D",
    "           ",
    " +@@@@@@@+ ",
    "+#       #+",
    "@ $@   @$ @",
    "@ @@@ @@@ @",
    "@  @@@@@  @",
    "@   @@@   @",
    "@  @@@@@  @",
    "@ @@@ @@@ @",
    "@ $@   @$ @",
    "+%       #+",
    " +@@@@@@@+ ",
    "           "};

static const char * const dock_widget_restore_xpm[] = {
    "11 13 7 1",
    " c None",
    ". c #D5CFCB",
    "+ c #8F8B88",
    "@ c #6C6A67",
    "# c #ABA6A3",
    "$ c #B5B0AC",
    "% c #A4A09D",
    "           ",
    " +@@@@@@@+ ",
    "+#       #+",
    "@   #@@@# @",
    "@   @   @ @",
    "@ #@@@# @ @",
    "@ @   @ @ @",
    "@ @   @@@ @",
    "@ @   @   @",
    "@ #@@@#   @",
    "+%       #+",
    " +@@@@@@@+ ",
    "           "};

static const char * const workspace_minimize[] = {
    "11 13 7 1",
    "  c None",
    ". c #D5CFCB",
    "+ c #8F8B88",
    "@ c #6C6A67",
    "# c #ABA6A3",
    "$ c #B5B0AC",
    "% c #A4A09D",
    "           ",
    " +@@@@@@@+ ",
    "+#       #+",
    "@         @",
    "@         @",
    "@         @",
    "@ @@@@@@@ @",
    "@ @@@@@@@ @",
    "@         @",
    "@         @",
    "+%       #+",
    " +@@@@@@@+ ",
    "           "};


static const char * const qt_titlebar_context_help[] = {
    "10 10 3 1",
    "  c None",
    "# c #000000",
    "+ c #444444",
    "  +####+  ",
    " ###  ### ",
    " ##    ## ",
    "     +##+ ",
    "    +##   ",
    "    ##    ",
    "    ##    ",
    "          ",
    "    ##    ",
    "    ##    "};
#endif // QT_CONFIG(imageformat_xpm)

static QColor mergedColors(const QColor &colorA, const QColor &colorB, int factor = 50)
{
    const int maxFactor = 100;
    QColor tmp = colorA;
    tmp.setRed((tmp.red() * factor) / maxFactor + (colorB.red() * (maxFactor - factor)) / maxFactor);
    tmp.setGreen((tmp.green() * factor) / maxFactor + (colorB.green() * (maxFactor - factor)) / maxFactor);
    tmp.setBlue((tmp.blue() * factor) / maxFactor + (colorB.blue() * (maxFactor - factor)) / maxFactor);
    return tmp;
}

// The default button and handle gradient
static QLinearGradient qt_fusion_gradient(const QRect &rect, const QBrush &baseColor, Direction direction = TopDown)
{
    int x = rect.center().x();
    int y = rect.center().y();
    QLinearGradient gradient;
    switch (direction) {
    case FromLeft:
        gradient = QLinearGradient(rect.left(), y, rect.right(), y);
        break;
    case FromRight:
        gradient = QLinearGradient(rect.right(), y, rect.left(), y);
        break;
    case BottomUp:
        gradient = QLinearGradient(x, rect.bottom(), x, rect.top());
        break;
    case TopDown:
    default:
        gradient = QLinearGradient(x, rect.top(), x, rect.bottom());
        break;
    }
    if (baseColor.gradient())
        gradient.setStops(baseColor.gradient()->stops());
    else {
        QColor gradientStartColor = baseColor.color().lighter(124);
        QColor gradientStopColor = baseColor.color().lighter(102);
        gradient.setColorAt(0, gradientStartColor);
        gradient.setColorAt(1, gradientStopColor);
        //          Uncomment for adding shiny shading
        //            QColor midColor1 = mergedColors(gradientStartColor, gradientStopColor, 55);
        //            QColor midColor2 = mergedColors(gradientStartColor, gradientStopColor, 45);
        //            gradient.setColorAt(0.5, midColor1);
        //            gradient.setColorAt(0.501, midColor2);
    }
    return gradient;
}

// 画左上右下方向的小三角形
static void qt_fusion_draw_arrow(Qt::ArrowType type, QPainter *painter, const QStyleOption *option, const QRect &rect, const QColor &color)
{
    const int arrowWidth = QStyleHelper::dpiScaled(14);
    const int arrowHeight = QStyleHelper::dpiScaled(8);

    const int arrowMax = qMin(arrowHeight, arrowWidth);
    const int rectMax = qMin(rect.height(), rect.width());
    const int size = qMin(arrowMax, rectMax);

    QPixmap cachePixmap;
    QString cacheKey = QStyleHelper::uniqueName(QLatin1String("fusion-arrow"), option, rect.size())
            % HexString<uint>(type)
            % HexString<uint>(color.rgba());
    if (!QPixmapCache::find(cacheKey, cachePixmap)) {
        cachePixmap = styleCachePixmap(rect.size());
        cachePixmap.fill(Qt::transparent);
        QPainter cachePainter(&cachePixmap);

        QRectF arrowRect;
        arrowRect.setWidth(size);
        arrowRect.setHeight(arrowHeight * size / arrowWidth);
        if (type == Qt::LeftArrow || type == Qt::RightArrow)
            arrowRect = arrowRect.transposed();
        arrowRect.moveTo((rect.width() - arrowRect.width()) / 2.0,
                         (rect.height() - arrowRect.height()) / 2.0);

        QPolygonF triangle;
        triangle.reserve(3);
        switch (type) {
        case Qt::DownArrow:
            triangle << arrowRect.topLeft() << arrowRect.topRight() << QPointF(arrowRect.center().x(), arrowRect.bottom());
            break;
        case Qt::RightArrow:
            triangle << arrowRect.topLeft() << arrowRect.bottomLeft() << QPointF(arrowRect.right(), arrowRect.center().y());
            break;
        case Qt::LeftArrow:
            triangle << arrowRect.topRight() << arrowRect.bottomRight() << QPointF(arrowRect.left(), arrowRect.center().y());
            break;
        default:
            triangle << arrowRect.bottomLeft() << arrowRect.bottomRight() << QPointF(arrowRect.center().x(), arrowRect.top());
            break;
        }

        cachePainter.setPen(Qt::NoPen);
        cachePainter.setBrush(color);
        cachePainter.setRenderHint(QPainter::Antialiasing);
        cachePainter.drawPolygon(triangle);

        QPixmapCache::insert(cacheKey, cachePixmap);
    }

    painter->drawPixmap(rect, cachePixmap);
}

static void qt_fusion_draw_mdibutton(QPainter *painter, const QStyleOptionTitleBar *option, const QRect &tmp, bool hover, bool sunken)
{
    QColor dark;
    dark.setHsv(option->palette.button().color().hue(),
                qMin(255, (int)(option->palette.button().color().saturation())),
                qMin(255, (int)(option->palette.button().color().value()*0.7)));

    QColor highlight = option->palette.highlight().color();

    bool active = (option->titleBarState & QStyle::State_Active);
    QColor titleBarHighlight(255, 255, 255, 60);

    if (sunken)
        painter->fillRect(tmp.adjusted(1, 1, -1, -1), option->palette.highlight().color().darker(120));
    else if (hover)
        painter->fillRect(tmp.adjusted(1, 1, -1, -1), QColor(255, 255, 255, 20));

    QColor mdiButtonGradientStartColor;
    QColor mdiButtonGradientStopColor;

    mdiButtonGradientStartColor = QColor(0, 0, 0, 40);
    mdiButtonGradientStopColor = QColor(255, 255, 255, 60);

    if (sunken)
        titleBarHighlight = highlight.darker(130);

    QLinearGradient gradient(tmp.center().x(), tmp.top(), tmp.center().x(), tmp.bottom());
    gradient.setColorAt(0, mdiButtonGradientStartColor);
    gradient.setColorAt(1, mdiButtonGradientStopColor);
    QColor mdiButtonBorderColor(active ? option->palette.highlight().color().darker(180): dark.darker(110));

    painter->setPen(QPen(mdiButtonBorderColor));
    const QLine lines[4] = {
        QLine(tmp.left() + 2, tmp.top(), tmp.right() - 2, tmp.top()),
        QLine(tmp.left() + 2, tmp.bottom(), tmp.right() - 2, tmp.bottom()),
        QLine(tmp.left(), tmp.top() + 2, tmp.left(), tmp.bottom() - 2),
        QLine(tmp.right(), tmp.top() + 2, tmp.right(), tmp.bottom() - 2)
    };
    painter->drawLines(lines, 4);
    const QPoint points[4] = {
        QPoint(tmp.left() + 1, tmp.top() + 1),
        QPoint(tmp.right() - 1, tmp.top() + 1),
        QPoint(tmp.left() + 1, tmp.bottom() - 1),
        QPoint(tmp.right() - 1, tmp.bottom() - 1)
    };
    painter->drawPoints(points, 4);

    painter->setPen(titleBarHighlight);
    painter->drawLine(tmp.left() + 2, tmp.top() + 1, tmp.right() - 2, tmp.top() + 1);
    painter->drawLine(tmp.left() + 1, tmp.top() + 2, tmp.left() + 1, tmp.bottom() - 2);

    painter->setPen(QPen(gradient, 1));
    painter->drawLine(tmp.right() + 1, tmp.top() + 2, tmp.right() + 1, tmp.bottom() - 2);
    painter->drawPoint(tmp.right() , tmp.top() + 1);

    painter->drawLine(tmp.left() + 2, tmp.bottom() + 1, tmp.right() - 2, tmp.bottom() + 1);
    painter->drawPoint(tmp.left() + 1, tmp.bottom());
    painter->drawPoint(tmp.right() - 1, tmp.bottom());
    painter->drawPoint(tmp.right() , tmp.bottom() - 1);
}

QFlatStyle::QFlatStyle() :
    QProxyStyle(QStyleFactory::create("fusion"))
{
    setObjectName(QLatin1String("Flat"));
}

void QFlatStyle::drawPrimitive(PrimitiveElement element,
                               const QStyleOption *option,
                               QPainter *painter, const QWidget *widget) const
{
    Q_ASSERT(option);

    QRect rect = option->rect;
    int state = option->state;

    QColor outline = this->outline(option->palette);
    QColor highlightedOutline = this->highlightedOutline(option->palette);

    QColor tabFrameColor = this->tabFrameColor(option->palette);

    switch (element) {
    case PE_Frame:
    {
        if (widget && widget->inherits("QComboBoxPrivateContainer")){
            QStyleOption copy = *option;
            copy.state |= State_Raised;
            proxy()->drawPrimitive(PE_PanelMenu, &copy, painter, widget);
            break;
        }
        painter->save();
        QPen thePen(outline.lighter(108));
        thePen.setCosmetic(false);
        painter->setPen(thePen);
        painter->drawRect(option->rect.adjusted(0, 0, -1, -1));
        painter->restore();
    }
        qDebug() << widget << "PE_Frame";
        break;
    case PE_FrameWindow:
        painter->save();
    {
        QRect rect= option->rect;
        painter->setPen(QPen(outline.darker(150)));
        painter->drawRect(option->rect.adjusted(0, 0, -1, -1));
        painter->setPen(QPen(option->palette.light(), 1));
        painter->drawLine(QPoint(rect.left() + 1, rect.top() + 1),
                          QPoint(rect.left() + 1, rect.bottom() - 1));
        painter->setPen(QPen(option->palette.background().color().darker(120)));
        painter->drawLine(QPoint(rect.left() + 1, rect.bottom() - 1),
                          QPoint(rect.right() - 2, rect.bottom() - 1));
        painter->drawLine(QPoint(rect.right() - 1, rect.top() + 1),
                          QPoint(rect.right() - 1, rect.bottom() - 1));
    }
        painter->restore();
        qDebug() << widget << "PE_FrameWindow";
        break;
    case PE_FrameLineEdit: // 输入框边框
    {
        QRect r = rect;
        bool hasFocus = option->state & State_HasFocus;

        painter->save();

        painter->setRenderHint(QPainter::Antialiasing, true);
        //  ### highdpi painter bug.
        painter->translate(0.5, 0.5);

        // 获取自定义的属性(边框颜色)
        QVariant color = widget->property(BorderColor);
        if (color != NULL && !color.isNull() && color.isValid()) {
            // 修改颜色为自定义的颜色
            outline = color.value<QColor>();
            highlightedOutline = QColor(outline.red() + 20, outline.green() + 20, outline.blue() + 20);
        }

        // Draw Outline //画外边框
        int radius = 4; //默认圆角
        QVariant pradius = widget->property(BorderRadius);
        if (pradius != NULL && !pradius.isNull() && pradius.isValid()) {
            // 自定义的圆角
            radius = pradius.value<int>();
        }

        painter->setPen( QPen(hasFocus ? highlightedOutline : outline));
        painter->setBrush(option->palette.base());
        painter->drawRoundedRect(r.adjusted(0, 0, -1, -1), radius, radius);

        if (hasFocus) {
            QColor softHighlight = highlightedOutline;
            softHighlight.setAlpha(40);
            painter->setPen(softHighlight);
            painter->drawRoundedRect(r.adjusted(1, 1, -2, -2), radius - 0.3, radius - 0.3);
        }
        // Draw inner shadow //画内阴影
        painter->setPen(this->topShadow());
        painter->drawLine(QPoint(r.left() + 2, r.top() + 1), QPoint(r.right() - 2, r.top() + 1));

        painter->restore();

    }
        break;
    case PE_IndicatorArrowUp: // 向上三角箭头
    case PE_IndicatorArrowDown: // 向下三角箭头
    case PE_IndicatorArrowRight: // 向右三角箭头
    case PE_IndicatorArrowLeft: // 向左三角箭头
    {
        if (option->rect.width() <= 1 || option->rect.height() <= 1)
            break;
        // 修改颜色为白色
        QColor arrowColor = Qt::white;//option->palette.foreground().color();
        arrowColor.setAlpha(160);
        Qt::ArrowType arrow = Qt::UpArrow;
        switch (element) {
        case PE_IndicatorArrowDown:
            arrow = Qt::DownArrow;
            break;
        case PE_IndicatorArrowRight:
            arrow = Qt::RightArrow;
            break;
        case PE_IndicatorArrowLeft:
            arrow = Qt::LeftArrow;
            break;
        default:
            break;
        }
        qt_fusion_draw_arrow(arrow, painter, option, option->rect, arrowColor);
    }
        break;
    default:
        baseStyle()->drawPrimitive(element, option, painter, widget);
        break;
    }
}

void QFlatStyle::drawControl(ControlElement element, const QStyleOption *option, QPainter *painter,
                             const QWidget *widget) const
{
    QRect rect = option->rect;
    QColor outline = this->outline(option->palette);
    QColor highlightedOutline = this->highlightedOutline(option->palette);
    QColor shadow = this->darkShade();
    switch (element) {
    case CE_PushButton:
        if (const QStyleOptionButton *btn = qstyleoption_cast<const QStyleOptionButton *>(option)) {
            QStyleOptionButton subopt = *btn;
            // 按钮背景颜色
            // 获取自定义的属性(背景颜色)
            QVariant color = widget->property(BackgroundColor);
            if (color != NULL && !color.isNull() && color.isValid()) {
                // 修改颜色为自定义的颜色
                subopt.palette.setBrush(QPalette::Button, color.value<QColor>());
            }

            proxy()->drawControl(CE_PushButtonBevel, &subopt, painter, widget);
            subopt.rect = subElementRect(SE_PushButtonContents, btn, widget);
            proxy()->drawControl(CE_PushButtonLabel, &subopt, painter, widget);
        }
        break;
    case CE_PushButtonLabel:
        if (const QStyleOptionButton *button = qstyleoption_cast<const QStyleOptionButton *>(option)) {
            QRect ir = button->rect;
            uint tf = Qt::AlignVCenter;
            if (styleHint(SH_UnderlineShortcut, button, widget))
                tf |= Qt::TextShowMnemonic;
            else
                tf |= Qt::TextHideMnemonic;

            // 图标
            if (!button->icon.isNull()) {
                //Center both icon and text
                QPoint point;

                QIcon::Mode mode = button->state & State_Enabled ? QIcon::Normal
                                                                 : QIcon::Disabled;
                if (mode == QIcon::Normal && button->state & State_HasFocus)
                    mode = QIcon::Active;
                QIcon::State state = QIcon::Off;
                if (button->state & State_On)
                    state = QIcon::On;

                QPixmap pixmap = button->icon.pixmap(button->iconSize, mode, state);
                int w = pixmap.width() / pixmap.devicePixelRatio();
                int h = pixmap.height() / pixmap.devicePixelRatio();

                if (!button->text.isEmpty())
                    w += button->fontMetrics.boundingRect(option->rect, tf, button->text).width() + 2;

                point = QPoint(ir.x() + ir.width() / 2 - w / 2,
                               ir.y() + ir.height() / 2 - h / 2);

                w = pixmap.width() / pixmap.devicePixelRatio();

                if (button->direction == Qt::RightToLeft)
                    point.rx() += w;

                painter->drawPixmap(visualPos(button->direction, button->rect, point), pixmap);

                if (button->direction == Qt::RightToLeft)
                    ir.translate(-point.x() - 2, 0);
                else
                    ir.translate(point.x() + w, 0);

                // left-align text if there is
                if (!button->text.isEmpty())
                    tf |= Qt::AlignLeft;

            } else {
                tf |= Qt::AlignHCenter;
            }

            if (button->features & QStyleOptionButton::HasMenu)
                ir = ir.adjusted(0, 0, -baseStyle()->pixelMetric(PM_MenuButtonIndicator, button, widget), 0);

            // 画文字
            // 获取自定义的属性(文字颜色)
            QVariant color = widget->property(TextColor);
            QPalette pal = button->palette;
            if (color != NULL && !color.isNull() && color.isValid()) {
                // 修改颜色为自定义的颜色
                pal.setColor(QPalette::ButtonText, color.value<QColor>());
            }

            baseStyle()->drawItemText(painter, ir, tf, pal, (button->state & State_Enabled),
                                      button->text, QPalette::ButtonText);
        }
        break;
    default:
        baseStyle()->drawControl(element,option,painter,widget);
        break;
    }
}

void QFlatStyle::drawComplexControl(ComplexControl control, const QStyleOptionComplex *option,
                                    QPainter *painter, const QWidget *widget) const
{

#if QT_CONFIG(spinbox) || QT_CONFIG(slider)
    QColor buttonColor = this->buttonColor(option->palette);
    QColor gradientStopColor = buttonColor;
#endif
#if QT_CONFIG(slider)
    QColor gradientStartColor = buttonColor.lighter(118);
#endif
    QColor outline = this->outline(option->palette);

    QColor alphaCornerColor;
    if (widget) {
        // ### backgroundrole/foregroundrole should be part of the style option
        alphaCornerColor = mergedColors(option->palette.color(widget->backgroundRole()), outline);
    } else {
        alphaCornerColor = mergedColors(option->palette.background().color(), outline);
    }

    switch (control) {
    case CC_Slider:
        if (const QStyleOptionSlider *slider = qstyleoption_cast<const QStyleOptionSlider *>(option)) {
            QRect groove = baseStyle()->subControlRect(CC_Slider, option, SC_SliderGroove, widget);
            QRect handle = baseStyle()->subControlRect(CC_Slider, option, SC_SliderHandle, widget);

            bool horizontal = slider->orientation == Qt::Horizontal;
            bool ticksAbove = slider->tickPosition & QSlider::TicksAbove;
            bool ticksBelow = slider->tickPosition & QSlider::TicksBelow;
            QColor activeHighlight = this->highlight(option->palette);
            QPixmap cache;
            QBrush oldBrush = painter->brush();
            QPen oldPen = painter->pen();
            QColor shadowAlpha(Qt::black);
            shadowAlpha.setAlpha(10);
            if (option->state & State_HasFocus && option->state & State_KeyboardFocusChange)
                outline = this->highlightedOutline(option->palette);


            if ((option->subControls & SC_SliderGroove) && groove.isValid()) {
                QColor grooveColor;
                grooveColor.setHsv(buttonColor.hue(),
                                   qMin(255, (int)(buttonColor.saturation())),
                                   qMin(255, (int)(buttonColor.value()*0.9)));
                QString groovePixmapName = QStyleHelper::uniqueName(QLatin1String("slider_groove"), option, groove.size());
                QRect pixmapRect(0, 0, groove.width(), groove.height());

                // draw background groove
                if (!QPixmapCache::find(groovePixmapName, cache)) {
                    cache = styleCachePixmap(pixmapRect.size());
                    cache.fill(Qt::transparent);
                    QPainter groovePainter(&cache);
                    groovePainter.setRenderHint(QPainter::Antialiasing, true);
                    groovePainter.translate(0.5, 0.5);
                    QLinearGradient gradient;
                    if (horizontal) {
                        gradient.setStart(pixmapRect.center().x(), pixmapRect.top());
                        gradient.setFinalStop(pixmapRect.center().x(), pixmapRect.bottom());
                    }
                    else {
                        gradient.setStart(pixmapRect.left(), pixmapRect.center().y());
                        gradient.setFinalStop(pixmapRect.right(), pixmapRect.center().y());
                    }
                    groovePainter.setPen(QPen(outline));
                    gradient.setColorAt(0, grooveColor.darker(110));
                    gradient.setColorAt(1, grooveColor.lighter(110));//palette.button().color().darker(115));
                    groovePainter.setBrush(gradient);
                    groovePainter.drawRoundedRect(pixmapRect.adjusted(1, 1, -2, -2), 1, 1);
                    groovePainter.end();
                    QPixmapCache::insert(groovePixmapName, cache);
                }
                painter->drawPixmap(groove.topLeft(), cache);

                // draw blue groove highlight
                QRect clipRect;
                groovePixmapName += QLatin1String("_blue");
                if (!QPixmapCache::find(groovePixmapName, cache)) {
                    cache = styleCachePixmap(pixmapRect.size());
                    cache.fill(Qt::transparent);
                    QPainter groovePainter(&cache);
                    QLinearGradient gradient;
                    if (horizontal) {
                        gradient.setStart(pixmapRect.center().x(), pixmapRect.top());
                        gradient.setFinalStop(pixmapRect.center().x(), pixmapRect.bottom());
                    }
                    else {
                        gradient.setStart(pixmapRect.left(), pixmapRect.center().y());
                        gradient.setFinalStop(pixmapRect.right(), pixmapRect.center().y());
                    }
                    QColor highlight = this->highlight(option->palette);
                    QColor highlightedoutline = highlight.darker(140);
                    if (qGray(outline.rgb()) > qGray(highlightedoutline.rgb()))
                        outline = highlightedoutline;


                    groovePainter.setRenderHint(QPainter::Antialiasing, true);
                    groovePainter.translate(0.5, 0.5);
                    groovePainter.setPen(QPen(outline));
                    gradient.setColorAt(0, activeHighlight);
                    gradient.setColorAt(1, activeHighlight.lighter(130));
                    groovePainter.setBrush(gradient);
                    groovePainter.drawRoundedRect(pixmapRect.adjusted(1, 1, -2, -2), 1, 1);
                    groovePainter.setPen(this->innerContrastLine());
                    groovePainter.setBrush(Qt::NoBrush);
                    groovePainter.drawRoundedRect(pixmapRect.adjusted(2, 2, -3, -3), 1, 1);
                    groovePainter.end();
                    QPixmapCache::insert(groovePixmapName, cache);
                }
                if (horizontal) {
                    if (slider->upsideDown)
                        clipRect = QRect(handle.right(), groove.top(), groove.right() - handle.right(), groove.height());
                    else
                        clipRect = QRect(groove.left(), groove.top(), handle.left(), groove.height());
                } else {
                    if (slider->upsideDown)
                        clipRect = QRect(groove.left(), handle.bottom(), groove.width(), groove.height() - handle.bottom());
                    else
                        clipRect = QRect(groove.left(), groove.top(), groove.width(), handle.top() - groove.top());
                }
                painter->save();
                painter->setClipRect(clipRect.adjusted(0, 0, 1, 1), Qt::IntersectClip);
                painter->drawPixmap(groove.topLeft(), cache);
                painter->restore();
            }

            // 画QSlider刻度条
            if (option->subControls & SC_SliderTickmarks) {
                painter->setPen(outline);
                int tickSize = baseStyle()->pixelMetric(PM_SliderTickmarkOffset, option, widget);
                int available = baseStyle()->pixelMetric(PM_SliderSpaceAvailable, slider, widget);
                int interval = slider->tickInterval;
                if (interval <= 0) {
                    interval = slider->singleStep;
                    if (QStyle::sliderPositionFromValue(slider->minimum, slider->maximum, interval,
                                                        available)
                            - QStyle::sliderPositionFromValue(slider->minimum, slider->maximum,
                                                              0, available) < 3)
                        interval = slider->pageStep;
                }
                if (interval <= 0)
                    interval = 1;

                int v = slider->minimum;
                int len = baseStyle()->pixelMetric(PM_SliderLength, slider, widget);
                while (v <= slider->maximum + 1) {
                    if (v == slider->maximum + 1 && interval == 1)
                        break;
                    const int v_ = qMin(v, slider->maximum);
                    int pos = sliderPositionFromValue(slider->minimum, slider->maximum,
                                                      v_, (horizontal
                                                           ? slider->rect.width()
                                                           : slider->rect.height()) - len,
                                                      slider->upsideDown) + len / 2;
                    int extra = 2 - ((v_ == slider->minimum || v_ == slider->maximum) ? 1 : 0);

                    if (horizontal) {
                        if (ticksAbove) {
                            painter->drawLine(pos, slider->rect.top() + extra,
                                              pos, slider->rect.top() + tickSize);
                        }
                        if (ticksBelow) {
                            painter->drawLine(pos, slider->rect.bottom() - extra,
                                              pos, slider->rect.bottom() - tickSize);
                        }
                    } else {
                        if (ticksAbove) {
                            painter->drawLine(slider->rect.left() + extra, pos,
                                              slider->rect.left() + tickSize, pos);
                        }
                        if (ticksBelow) {
                            painter->drawLine(slider->rect.right() - extra, pos,
                                              slider->rect.right() - tickSize, pos);
                        }
                    }
                    // in the case where maximum is max int
                    int nextInterval = v + interval;
                    if (nextInterval < v)
                        break;
                    v = nextInterval;
                }
            }
            // draw handle
            // QSlider中间的小滑块
            if ((option->subControls & SC_SliderHandle) ) {
                QString handlePixmapName = QStyleHelper::uniqueName(QLatin1String("slider_handle"), option, handle.size());
                // 查找缓存,没有则重新生成一个
                if (!QPixmapCache::find(handlePixmapName, cache)) {
                    // 生成一个和滑块一样大小的透明图
                    cache = styleCachePixmap(handle.size());
                    cache.fill(Qt::transparent);
                    // 滑块矩形
                    QRect pixmapRect(0, 0, handle.width(), handle.height());

                    QPainter handlePainter(&cache);
                    QRect gradRect = pixmapRect.adjusted(2, 2, -2, -2);

                    // gradient fill, 渐变填充
                    QRect r = pixmapRect.adjusted(1, 1, -2, -2);
                    QLinearGradient gradient = qt_fusion_gradient(gradRect, this->buttonColor(option->palette),horizontal ? TopDown : FromLeft);

                    handlePainter.setRenderHint(QPainter::Antialiasing, true);
                    handlePainter.translate(0.5, 0.5);

                    handlePainter.setPen(Qt::NoPen);
                    handlePainter.setBrush(QColor(0, 0, 0, 40));
                    handlePainter.drawRect(r.adjusted(-1, 2, 1, -2));

                    handlePainter.setPen(QPen(this->outline(option->palette)));
                    if (option->state & State_HasFocus && option->state & State_KeyboardFocusChange)
                        handlePainter.setPen(QPen(this->highlightedOutline(option->palette)));

                    handlePainter.setBrush(gradient);
                    handlePainter.drawRoundedRect(r, 2, 2);
                    handlePainter.setBrush(Qt::NoBrush);
                    handlePainter.setPen(this->innerContrastLine());
                    handlePainter.drawRoundedRect(r.adjusted(1, 1, -1, -1), 2, 2);

                    QColor cornerAlpha = outline.darker(120);
                    cornerAlpha.setAlpha(80);

                    //handle shadow
                    handlePainter.setPen(shadowAlpha);
                    handlePainter.drawLine(QPoint(r.left() + 2, r.bottom() + 1), QPoint(r.right() - 2, r.bottom() + 1));
                    handlePainter.drawLine(QPoint(r.right() + 1, r.bottom() - 3), QPoint(r.right() + 1, r.top() + 4));
                    handlePainter.drawLine(QPoint(r.right() - 1, r.bottom()), QPoint(r.right() + 1, r.bottom() - 2));

                    handlePainter.end();
                    QPixmapCache::insert(handlePixmapName, cache);
                }

                painter->drawPixmap(handle.topLeft(), cache);

            }
            painter->setBrush(oldBrush);
            painter->setPen(oldPen);
        }
        break;
    default:
        baseStyle()->drawComplexControl(control, option, painter, widget);
        break;
    }


}

QFlatStyle::~QFlatStyle()
{
}
