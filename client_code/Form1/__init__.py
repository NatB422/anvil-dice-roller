from ._anvil_designer import Form1Template
from anvil import *
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    if self.dice:
      self.dice.clear()
      self.dice.roll("1d6", {"theme": "rust"})
      self.dice.show()

  def DiceBox_show(self, **event_args):
    """This method is called when the X-Y panel is shown on the screen"""
    dice_box_module = anvil.js.import_from("https://cdn.jsdelivr.net/npm/@3d-dice/dice-box@1.1.4/dist/dice-box.es.min.js")
    dice_box = dice_box_module.default

    asset_folder = f"{anvil.server.get_app_origin()}/_/theme/themes/"
    print(asset_folder)
    self.dice = dice_box({
      "target": '#DiceBox',
      "themes": ["rust"],
      "assetPath": asset_folder,
    })
    self.dice.init()
    # dice.roll("1d6")
    
    
