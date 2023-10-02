from qtpy.QtWidgets import QApplication
from pymmcore_widgets._mda._simple_mda import SimpleMDAWidget
from pymmcore_plus import CMMCorePlus


mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

if __name__ == "__main__":
    app = QApplication([])
    frame = SimpleMDAWidget()
    frame.show()
    frame.get_state()
    app.exec_()