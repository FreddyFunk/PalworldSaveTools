from PySide6.QtWidgets import QTabBar
from PySide6.QtCore import Qt, QSize, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QColor, QFont, QPen, QBrush, QFontMetrics
class FloatingTabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDrawBase(False)
        self.is_dark_mode = True
        self._hovered_tab = -1
    def set_theme(self, is_dark):
        self.is_dark_mode = is_dark
        self.update()
    def tabSizeHint(self, index):
        size = super().tabSizeHint(index)
        return QSize(size.width() + 20, size.height() + 12)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for i in range(self.count()):
            self._draw_custom_tab(painter, i)
    def _draw_custom_tab(self, painter, index):
        rect = self.tabRect(index)
        is_selected = index == self.currentIndex()
        is_hovered = index == self._hovered_tab
        rect = rect.adjusted(4, 6, -4, -4)
        path = self._create_tab_path(rect)
        bg_color, border_color, text_color = self._get_colors(is_selected, is_hovered)
        self._draw_shadow(painter, path)
        painter.fillPath(path, QBrush(bg_color))
        painter.setPen(QPen(border_color, 1))
        painter.drawPath(path)
        painter.setPen(text_color)
        font = QFont('Segoe UI', 11, QFont.Bold if is_selected else QFont.DemiBold)
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignCenter, self.tabText(index))
    def _create_tab_path(self, rect):
        path = QPainterPath()
        radius = 10
        slant = 15
        path.moveTo(rect.left() + radius, rect.top())
        path.arcTo(rect.left(), rect.top(), radius * 2, radius * 2, 90, 90)
        path.lineTo(rect.left(), rect.bottom() - radius)
        path.arcTo(rect.left(), rect.bottom() - radius * 2, radius * 2, radius * 2, 180, 90)
        path.lineTo(rect.right() - radius, rect.bottom())
        path.arcTo(rect.right() - radius * 2, rect.bottom() - radius * 2, radius * 2, radius * 2, 270, 90)
        path.lineTo(rect.right(), rect.top() + slant)
        path.lineTo(rect.right() - slant, rect.top())
        path.closeSubpath()
        return path
    def _draw_shadow(self, painter, path):
        shadow_color = QColor(125, 211, 252, 25) if self.is_dark_mode else QColor(37, 150, 190, 25)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(shadow_color))
        painter.save()
        painter.translate(0, 2)
        painter.fillPath(path, shadow_color)
        painter.restore()
    def _get_colors(self, is_selected, is_hovered):
        if self.is_dark_mode:
            if is_selected:
                bg = QColor(125, 211, 252, 31)
                border = QColor(125, 211, 252, 76)
                text = QColor('#7DD3FC')
            elif is_hovered:
                bg = QColor(125, 211, 252, 13)
                border = QColor(125, 211, 252, 38)
                text = QColor('#E6EEF6')
            else:
                bg = QColor(30, 33, 40, 178)
                border = QColor(125, 211, 252, 26)
                text = QColor('#A6B8C8')
        elif is_selected:
            bg = QColor(37, 150, 190, 38)
            border = QColor(37, 150, 190, 102)
            text = QColor('#1A365D')
        elif is_hovered:
            bg = QColor(37, 150, 190, 20)
            border = QColor(37, 150, 190, 51)
            text = QColor('#2C3E50')
        else:
            bg = QColor(200, 215, 235, 128)
            border = QColor(180, 200, 220, 76)
            text = QColor('#2C3E50')
        return (bg, border, text)
    def mouseMoveEvent(self, event):
        old_hovered = self._hovered_tab
        self._hovered_tab = self.tabAt(event.pos())
        if old_hovered != self._hovered_tab:
            self.update()
        super().mouseMoveEvent(event)
    def leaveEvent(self, event):
        self._hovered_tab = -1
        self.update()
        super().leaveEvent(event)