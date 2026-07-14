APP_STYLE = """
/* ===========================
   Main Window
=========================== */

QMainWindow {
    background-color: #1e1e2f;
}

/* ===========================
   Group Boxes
=========================== */

QGroupBox {
    background-color: #2a2d3e;
    color: white;

    border: 1px solid #3d4258;
    border-radius: 10px;

    margin-top: 14px;
    padding: 14px;

    font-size: 16px;
    font-weight: 600;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
}

/* ===========================
   Labels
=========================== */

QLabel {
    color: #ececec;
    font-size: 14px;
}

/* ===========================
   Text Inputs
=========================== */

QLineEdit {
    background: #3a3f58;
    color: white;

    border: 1px solid #555;
    border-radius: 6px;

    padding: 8px;
    font-size: 14px;
}

/* ===========================
   Text Area
=========================== */

QTextEdit {
    background: #232634;
    color: #dddddd;

    border: 1px solid #444;
    border-radius: 6px;

    padding: 8px;
    font-size: 14px;
}

/* ===========================
   General Buttons
=========================== */

QPushButton {
    background-color: #3b82f6;
    color: white;

    border: none;
    border-radius: 6px;

    padding: 6px 14px;

    min-height: 18px;

    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #2563eb;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

/* ===========================
   Quantity Buttons
=========================== */

QPushButton#quantityButton {
    min-width: 30px;
    max-width: 30px;

    min-height: 30px;
    max-height: 30px;

    padding: 0;

    border-radius: 15px;

    font-size: 16px;
}

QPushButton#quantityButton:hover {
    background-color: #2563eb;
}

/* ===========================
   Quantity Label
=========================== */

QLabel#quantityLabel {
    font-size: 15px;
    font-weight: bold;
    min-width: 24px;
}
QLabel#appTitle {
    color: white;
    font-size: 26px;
    font-weight: bold;
    padding: 10px;
}
"""