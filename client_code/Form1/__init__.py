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
        "onRollComplete": self.update_roll_result,
      }
      self.dice = dice_box(dice_options)
      image_asset = f"{anvil.server.get_app_origin()}/_/theme/DiceTray.png"
  
      # Set the background property of the XYPanel
      # self.DiceBox.background = image_asset
  
      anvil.js.await_promise(self.dice.init())
    
    self.dice.clear()

    roll_arg = self.text_box_1.text or "1d6"
    self.label_2.text = ""
    
    try:
      self.dice.roll(roll_arg)
      self.dice.show()
    except Exception:
      self.dice.clear()
      anvil.alert(f"{roll_arg} is not a valid roll argument")

  def update_roll_result(self, results):
    #dice_outcomes = results[0]["rolls"]
    #total = sum(d["value"] for d in dice_outcomes)
    # anvil.alert(f"{results[0]['value']}")
    self.label_2.text = results[0]["value"]
    
    