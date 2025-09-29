import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#


def multiline_dice_result(result):
  if result["qty"] == 1 and result["modifier"] == 0:
    return result["value"]
  else:
    return (
      ", ".join(str(r["value"]) for r in result["rolls"])
      + (f"\n + {result['modifier']}" if result['modifier'] else "")
      + "\n = " + str(result["value"])
    )
