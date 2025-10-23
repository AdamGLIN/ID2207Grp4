from src.view import SEPView
from src.controller import SEPController
from src.model import SEPModel

model = SEPModel()
controller = SEPController(model)
view = SEPView(controller)
