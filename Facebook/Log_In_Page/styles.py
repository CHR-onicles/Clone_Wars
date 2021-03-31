def styles():
    return """
    QWidget#mainwindow {
        background-color: #f0f2f5;
    }
    
    QWidget {
        font-family: segoe UI;
    }
    
    QLabel#lbl_facebook {
        font-size: 50pt;
        color: #1877f2;
        font-weight: bold;
        background-color:  #f0f2f5;
    }
    
    QLabel#description {
        font-size: 18pt;
        background-color:  #f0f2f5;
    }
    
    QFrame#big_frame {
        border-radius: 8px;
        background-color: white;
    }
    
    QLineEdit {
        font-size: 12pt;
        border: 1px solid #d3d5d8;
        border-radius: 8px;
        padding: 18 18px;
    }
    
    QLineEdit:focus {
        border: 1px solid #1877f2;
    }
    
    QPushButton {
        color: white;
        background-color: #1877f2;
        border-radius: 8px;
        border: 1px solid #1877f2;
        font-size: 15pt;
        font-weight: bold;
        padding-top: 12px;
        padding-bottom: 12px;
    }
    
    QPushButton:hover {
        background-color: #1466ca;
    }
    
    QPushButton#new_account {
        font-size: 14pt;
        background-color: #42b72a;
        border: 1px solid #42b72a;
        min-width: 250px;
    }
    
    QPushButton#new_account:hover {
        background-color: #399823;
    }
    """