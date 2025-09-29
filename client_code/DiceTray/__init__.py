from ._anvil_designer import DiceTrayTemplate
from anvil import *
import anvil.server
import anvil.js
from ..DiceResult import multiline_dice_result


class DiceTray(DiceTrayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.dice = None
    self.dice_box_module = anvil.js.import_from("https://unpkg.com/@3d-dice/dice-box@1.1.3/dist/dice-box.es.min.js").default
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.dice:
      self.DiceBox.add_component(anvil.XYPanel(
        width=400, height=400,
        margin=40,
      ))
      
      dice_options = {
        "assetPath": "assets/",
        "origin": "https://unpkg.com/@3d-dice/dice-box@1.1.3/dist/",
        "container": ".xypanel-1",
        "theme": "diceOfRolling",
        "themeColor": "#008080",
        "externalThemes": {
          "diceOfRolling": "https://www.unpkg.com/@3d-dice/theme-dice-of-rolling@0.2.1",
        },
        "startingHeight": 8,
        "throwForce": 6,
        "spinForce": 5,
        "lightIntensity": 0.9,
        "scale": 6,
        "offscreen": False,
        "onRollComplete": self.update_roll_result,
      }
      self.dice = self.dice_box_module(dice_options)
  
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
    # anvil.alert(f"{results[0]}")
    self.label_2.text = multiline_dice_result(results[0])
    