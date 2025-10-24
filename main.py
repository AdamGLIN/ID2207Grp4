import sys

from src.view import SEPView
from src.controller import SEPController
from src.model import SEPModel
from tests.tester import SEPTester

model = SEPModel()
controller = SEPController(model)
view = SEPView(controller)

if "-test" in sys.argv:
    tester = SEPTester(model, view, controller)
    tester.start()
else:
    view.show()