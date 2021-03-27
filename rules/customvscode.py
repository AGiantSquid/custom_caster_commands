from castervoice.lib.actions import Key
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R
from castervoice.lib.merge.mergerule import MergeRule
from dragonfly import Pause, Dictation, ShortIntegerRef
from dragonfly.actions.action_text import Text


class CustomVSCode(MergeRule):
    pronunciation = "custom visual studio code"
    mapping = {
        "save file as":
            R(Key("cs-s"), rdescript="VS Code: Save As"),
        "uppercase":
            R(Key("csa-u"), rdescript="VS Code: uppercase"),
        "lowercase":
            R(Key("csa-l"), rdescript="VS Code: lowercase"),
        "execute":
            R(Key("s-enter"), rdescript="VS Code: Ctrl + b"),
        "[go to] group [<n2>]":
            R(Key("c-%(n2)s"), rdescript="VS Code: Go to Group #"),
        "spring <n>":
            R(Key("c-g") + Pause("10") + Text("%(n)s") + Key("enter"),
              rdescript="VS Code: Go to Line #"),
        "crew [<text>]":
            R(Key("c-f") + Pause("10") + Text("%(text)s") + Pause("10") +
              Key("escape"),
              rdescript="VS Code: Get Next"),
        "trail [<text>]":
            R(Key("c-f") + Pause("10") + Text("%(text)s") + Pause("10") +
                Key("s-enter") + Key("escape"),
              rdescript="VS Code: Get Next"),
        "expand|fill quotes":
            R(Key("cs-space"), rdescript="VS Code: Expand Selection to Quotes"),
        "(cellaring | sell rang) <n> <n3>":
            R(
                Key("c-g") + Pause("5") + Text("%(n)s") + Key("enter") + Pause("5") +
                Key("c-k") + Key("c-b") + Pause("5") + Key("c-g") + Pause("10") +
                Text("%(n3)s") + Key("enter") + Key("end") + Key("c-k") + Key("c-k")),

        # The following commands of been enabled via words.txt
        # If Caster gets rid of transformers, reenable these words
        # "grab it":
        #     R(Key("c-d"), rdescript="VS Code: Ctrl + d"),
        # "skip it":
        #     R(Key("c-k,c-d"), rdescript="VS Code: Ctrl + d, k"),
        # "cue jeep":
        #     R(Key("a-up"), rdescript="VS Code: uppercase"),
        # "cue doom":
        #     R(Key("a-down"), rdescript="VS Code: uppercase"),
    }

    extras = [
        Dictation("text"),
        Dictation("mim"),
        ShortIntegerRef("n", 1, 1000),
        ShortIntegerRef("n2", 1, 9),
        ShortIntegerRef("n3", 1, 999),
    ]
    defaults = {"n": 1, "mim": "", "text": ""}


def get_rule():
    details = RuleDetails(executable="code",
                          title="Visual Studio Code",
                          ccrtype=CCRType.APP)
    return CustomVSCode, details
