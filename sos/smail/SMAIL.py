
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
from src.layout import first_frame



if __name__ == '__main__':

    # check_logfile()
    config_path = os.path.join(os.getcwd().split("smail")[0], "sconf/")

    try:
        # # Generating global configuration file
        # config = act.configExistCheck()
        #
        # if not os.path.exists(os.path.join(config_path, "SMAIL_config.json")):
        #     smail_config_default(os.path.join(config_path))
        #     logging.info("Generating SMAIL configuration file.")

        app = QApplication([])
        window = QMainWindow()
        window.setWindowTitle("SMAIL App")
        # window.showFullScreen()
        window.setGeometry(100, 100, 1280, 720)
        layout = first_frame(window)
        window.setCentralWidget(layout)
        window.show()
        app.exec()

    except Exception as e:
        print(f"Could not start SMAIL app, error loading configuration. {e}" )

