from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QSpinBox, QCheckBox, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from core.settings_manager import save_settings, load_settings

class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.setWindowTitle("⚙ Settings")

        self.settings = load_settings()  # ← make sure settings are loaded
        self.init_ui()                   # ← THIS was missing!
        if self.settings.get("dark_mode", True):
            self.apply_dark_theme()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel("LexiAI Settings")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Chunk Size
        self.chunk_size_spin = QSpinBox()
        self.chunk_size_spin.setRange(100, 2000)
        self.chunk_size_spin.setValue(self.settings.get("chunk_size", 500))
        form_layout.addRow("Chunk Size:", self.chunk_size_spin)

        # Overlap Size
        self.overlap_spin = QSpinBox()
        self.overlap_spin.setRange(0, 300)
        self.overlap_spin.setValue(self.settings.get("overlap", 50))
        form_layout.addRow("Chunk Overlap:", self.overlap_spin)

        # Dark Mode Toggle
        self.dark_mode_checkbox = QCheckBox("Enable Dark Mode")
        self.dark_mode_checkbox.setChecked(self.settings.get("dark_mode", True))
        form_layout.addRow(self.dark_mode_checkbox)

        # Model Selection
        self.model_combo = QComboBox()
        self.model_combo.addItems(["llama3", "mistral", "gemma", "llama2", "codellama"])
        self.model_combo.setCurrentText(self.settings.get("model_name", "llama3"))
        form_layout.addRow("Model:", self.model_combo)

        layout.addLayout(form_layout)

        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        self.save_button.setFixedHeight(40)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                font-size: 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
        """)
        layout.addWidget(self.save_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def save_settings(self):
        new_settings = {
            "chunk_size": self.chunk_size_spin.value(),
            "overlap": self.overlap_spin.value(),
            "dark_mode": self.dark_mode_checkbox.isChecked(),
            "model_name": self.model_combo.currentText(),
        }
        save_settings(new_settings)
        if self.main_window:
            self.main_window.apply_updated_settings()

        self.close()

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: 'Segoe UI';
                font-size: 16px;
            }
            QSpinBox, QComboBox {
                background-color: #2a2a3d;
                color: white;
                border: 1px solid #3b82f6;
                border-radius: 6px;
                padding: 4px;
            }
            QCheckBox {
                padding: 4px;
            }
        """)
