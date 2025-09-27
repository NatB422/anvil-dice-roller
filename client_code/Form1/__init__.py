from ._anvil_designer import Form1Template
from anvil import *
import anvil.js


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.dice = None
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.dice:
      dice_box_module = anvil.js.import_from("https://unpkg.com/@3d-dice/dice-box@1.1.3/dist/dice-box.es.min.js")
      dice_box = dice_box_module.default
      
      dice_options = {
        "assetPath": "assets/",
        "origin": "https://unpkg.com/@3d-dice/dice-box@1.1.3/dist/",
        "container": ".xypanel-0",
        "theme": "diceOfRolling",
        "themeColor": "#feea03",
        "externalThemes": {
          "diceOfRolling": "https://www.unpkg.com/@3d-dice/theme-dice-of-rolling@0.2.1",
        },
        "startingHeight": 8,
        "throwForce": 6,
        "spinForce": 5,
        "lightIntensity": 0.9,
        "scale": 8,
        "offscreen": True,
      }
      self.dice = dice_box(dice_options)
  
      anvil.js.await_promise(self.dice.init())
    
    self.dice.clear()
    self.dice.roll("1d6")
    self.dice.show()
