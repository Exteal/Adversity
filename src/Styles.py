endPageButtonStyle =  """QPushButton {
    background-color: red;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
}"""


namesListStyle = """QListWidget
    {
    border : 2px solid black;
    }
    QListWidget QScrollBar
    {
    background : lightblue;
    }
    QListView::item:selected
    {
    border : 2px solid black;
    background : green;
    }
    QListView::item
    {
    border : 1px solid grey;
    background : rgba(255, 255, 0, 0.5);
    }

    
}"""


recommandationTitleStyle = """QLabel
{
background: black;
color : lightgreen;
border : 2px solid green;
font-family : Onyx;
font-size : 25px;
}
"""
