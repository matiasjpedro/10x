#------------------------------------------------------------------------
import os
import N10X

#------------------------------------------------------------------------
# This script tries to simulate vim's "vsplit" and "only" commands
# for 2 panes. I.e. "split current window into 2 panes and duplicate current
# buffer to the other pane" and "only one pane, with current buffer"

# Stick this file in your 10x PythonScripts folder,
# typically \users\USERNAME\AppData\Roaming\10x\PythonScripts
# For this to work, please map two keys to QuickPane1() and QuickPane2() in
# key bindings (KeyMappings.10x_settings). F1 and F2 are recommended,
# but they need to be unmapped from other uses first!

#------------------------------------------------------------------------
# Switches to single column
def QuickPane():
    x, y = N10X.Editor.GetCursorPos()
    if (N10X.Editor.GetColumnCount() == 2):
        N10X.Editor.ExecuteCommand("MovePanelLeft")
        N10X.Editor.ExecuteCommand("SetRowCount1")
        N10X.Editor.ExecuteCommand("SetColumnCount1")
        N10X.Editor.SetFocusedTab(100)
        N10X.Editor.CloseFile()
    else:
        N10X.Editor.ExecuteCommand("SetColumnCount2")
        N10X.Editor.ExecuteCommand("DuplicatePanelRight")

    N10X.Editor.SetCursorPos((x, y))