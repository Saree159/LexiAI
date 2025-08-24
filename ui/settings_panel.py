from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QSpinBox, QCheckBox, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from core.settings_manager import save_settings, load_settings

class SettingsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.settings = load_settings()
        self.setFixedWidth(300)
        self.setStyleSheet(self.load_styles())

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("⚙ Settings")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignTop)

        form_layout = QFormLayout()
       
        self.chunk_size_spin = QSpinBox()
        self.chunk_size_spin.setRange(100, 2000)
        self.chunk_size_spin.setValue(self.settings.get("chunk_size", 500))
        form_layout.addRow("Chunk Size:", self.chunk_size_spin)

        self.overlap_spin = QSpinBox()
        self.overlap_spin.setRange(0, 500)
        self.overlap_spin.setValue(self.settings.get("overlap", 50))
        form_layout.addRow("Chunk Overlap:", self.overlap_spin)

        self.dark_mode_checkbox = QCheckBox("Enable Dark Mode")
        self.dark_mode_checkbox.setChecked(self.settings.get("dark_mode", True))
        form_layout.addRow(self.dark_mode_checkbox)

        self.model_combo = QComboBox()
        self.model_combo.addItems(["llama3", "mistral", "gemma", "llama2", "codellama"])
        self.model_combo.setCurrentText(self.settings.get("model_name", "llama3"))
        form_layout.addRow("Model:", self.model_combo)
        self.role_combo = QComboBox()
        self.role_combo.addItems(["General", "Legal Advisor", "HR Assistant", "Technical Expert"])
        self.role_combo.setCurrentText(self.settings.get("role", "General"))
        form_layout.addRow("Bot Role:", self.role_combo)

        layout.addLayout(form_layout)

        save_button = QPushButton("Save & Close")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_settings(self):
        new_settings = {
            "chunk_size": self.chunk_size_spin.value(),
            "overlap": self.overlap_spin.value(),
            "dark_mode": self.dark_mode_checkbox.isChecked(),
            "model_name": self.model_combo.currentText(),
            "role": self.role_combo.currentText()
    }
        save_settings(new_settings)
        if self.main_window:
            self.main_window.apply_updated_settings()
        self.setVisible(False)

    def load_styles(self):
        return """
        QWidget {
            background-color: #1e1e2f;
            color: white;
            font-size: 16px;
            font-family: 'Segoe UI';
        }
        QSpinBox, QComboBox {
            background-color: #2a2a3d;
            color: white;
            border-radius: 6px;
            padding: 4px;
        }
        QPushButton {
            background-color: #3b82f6;
            color: white;
            border-radius: 6px;
            padding: 6px 12px;
        }
        QPushButton:hover {
            background-color: #2563eb;
        }
        QCheckBox {
            padding-top: 8px;
        }
        """
