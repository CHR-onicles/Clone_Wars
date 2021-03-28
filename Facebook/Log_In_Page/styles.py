def login_widgets_styles():
    return """
    QFrame {
        border-radius: 5px;
        background-color: white;
    }
    
    QLineEdit {
        border: 1px solid gray;
        border-radius: 5px;
    }
    
    QLineEdit:focus {
        border: 1px solid #1877f2;
    }
    
    QPushButton {
        color: white;
        background-color: #1877f2;
        border-radius: 5px;
        border: 1px solid #1877f2;
    }
    """