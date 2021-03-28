def styles():
    return """
    QWidget#mainwindow {
        background-color: #f0f2f5;
    }
    
    QLabel#lbl_facebook {
        font: 50pt segoe UI;
        color: #1877f2;
        font-weight: bold;
        background-color:  #f0f2f5;
    }
    
    QLabel#description {
        font: 18pt segoe UI;
        background-color:  #f0f2f5;
    }
    
    QFrame {
        border-radius: 5px;
        background-color: white;
    }
    
    QLineEdit {
        font: 12pt solid segoe UI;
        border: 1px solid #d3d5d8;
        border-radius: 5px;
        padding: 20 20px;
    }
    
    QLineEdit:focus {
        border: 1px solid #1877f2;
    }
    
    QPushButton {
        color: white;
        background-color: #1877f2;
        border-radius: 5px;
        border: 1px solid #1877f2;
        font: 14pt segoe UI;
        font-weight: bold;
        padding-top: 15px;
        padding-bottom: 15px;
    }
    
    QPushButton:hover {
        background-color: 
        background-color: #1877f2;
        border: 1px solid #1877f2;
       /* # todo: darken these colors a bit */
    }
    
    QPushButton#new_account {
        background-color: #42b72a;
        border: 1px solid #42b72a;
    }
    """