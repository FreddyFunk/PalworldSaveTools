from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtGui import QFont, QColor
from i18n import t
try:
    from palworld_aio import constants
except ImportError:
    from .. import constants


class PlayerHoverOverlay(QWidget):
    """Hover overlay showing player information on the map."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('playerHoverOverlay')
        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self._setup_ui()
        self._hide_timer = QTimer(self)
        self._hide_timer.setSingleShot(True)
        self._hide_timer.timeout.connect(self._do_hide)

    def _setup_ui(self):
        self.container = QFrame(self)
        self.container.setObjectName('hoverOverlayContainer')
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.container)
        inner_layout = QVBoxLayout(self.container)
        inner_layout.setContentsMargins(12, 10, 12, 10)
        inner_layout.setSpacing(6)
        self.name_label = QLabel()
        self.name_label.setObjectName('hoverPlayerLabel')
        self.name_label.setFont(QFont(constants.FONT_FAMILY, 11, QFont.Bold))
        inner_layout.addWidget(self.name_label)
        self.level_label = QLabel()
        self.level_label.setObjectName('hoverDetailLabel')
        self.level_label.setFont(QFont(constants.FONT_FAMILY, 9))
        inner_layout.addWidget(self.level_label)
        self.uid_label = QLabel()
        self.uid_label.setObjectName('hoverDetailLabel')
        self.uid_label.setFont(QFont(constants.FONT_FAMILY, 9))
        inner_layout.addWidget(self.uid_label)
        self.coords_label = QLabel()
        self.coords_label.setObjectName('hoverDetailLabel')
        self.coords_label.setFont(QFont(constants.FONT_FAMILY, 9))
        inner_layout.addWidget(self.coords_label)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(2, 2)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.container.setGraphicsEffect(shadow)
        self.container.setStyleSheet('''
            QFrame#hoverOverlayContainer {
                background: rgba(18,20,24,0.95);
                border: 1px solid rgba(0, 255, 150, 0.3);
                border-radius: 8px;
            }
            QLabel#hoverPlayerLabel {
                color: #00FF96;
            }
            QLabel#hoverDetailLabel {
                color: #a0aec0;
            }
        ''')

    def show_for_player(self, player_data: dict, global_pos: QPoint):
        self._hide_timer.stop()
        nickname = player_data.get('nickname', 'Unknown')
        level = player_data.get('level', '?')
        uid = player_data.get('uid', '')
        coords = player_data.get('coords', (0, 0))

        self.name_label.setText(nickname)
        self.level_label.setText(f"{(t('map.info.player_level') if t else 'Level:')} {level}")
        self.uid_label.setText(f"{(t('map.info.player_name') if t else 'UID:')} {uid[:16]}...")
        self.coords_label.setText(f"{(t('map.info.player_location') if t else 'Location:')} X:{int(coords[0])},Y:{int(coords[1])}")
        self.adjustSize()
        offset_x = 20
        offset_y = -self.height() // 2
        new_pos = QPoint(global_pos.x() + offset_x, global_pos.y() + offset_y)
        self.move(new_pos)
        self.show()
        self.raise_()

    def hide_overlay(self):
        self._hide_timer.start(50)

    def _do_hide(self):
        self.hide()

    def cancel_hide(self):
        self._hide_timer.stop()
