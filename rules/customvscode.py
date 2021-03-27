from dragonfly import (Grammar, AppContext, Dictation, Key, Pause)

Enable custom Visual Studio codefrom castervoice.lib.actions import Key
from dragonfly.actions.action_text import Text
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails

# from caster.lib import settings
# from caster.lib import control
# from caster.lib.dfplus.additions import IntegerRefST
# from caster.lib.dfplus.merge import gfilter
# from caster.lib.dfplus.merge.mergerule import MergeRule
# from caster.lib.dfplus.state.short import R


class CustomVSCode(MergeRule):
    pronunciation = "custom visual studio code"
    mapping = {
        # my custom overrides
        "save file as":
            R(Key("cs-s"), rdescript="VS Code: Save As"),
        "grab it":
            R(Key("c-d"), rdescript="VS Code: Ctrl + d"),
        "skip it":
            R(Key("c-k,c-d"), rdescript="VS Code: Ctrl + d, k"),
        "uppercase":
            R(Key("csa-u"), rdescript="VS Code: uppercase"),
        "lowercase":
            R(Key("csa-l"), rdescript="VS Code: uppercase"),
        "cue jeep":
            R(Key("a-up"), rdescript="VS Code: uppercase"),
        "cue doom":
            R(Key("a-down"), rdescript="VS Code: uppercase"),
        "execute":
            R(Key("s-enter"), rdescript="VS Code: Ctrl + b"),
        "[go to] group [<n2>]":
            R(Key("c-%(n2)s"), rdescript="VS Code: Go to Group #"),
        "spring <n>":
            R(Key("c-g") + Pause("10") + Text("%(n)s") + Key("enter"),
              rdescript="VS Code: Go to Line #"),
        "crew [<text>]":
            R(Key("c-i") + Pause("10") + Text("%(text)s") + Pause("10") + Key("enter") +
              Key("escape"),
              rdescript="VS Code: Get Next"),
        "trail [<text>]":
            R(Key("c-u") + Pause("10") + Text("%(text)s") + Pause("10") + Key("enter") +
              Key("escape"),
              rdescript="VS Code: Get Next"),
        "expand|fill quotes":
            R(Key("cs-space"), rdescript="VS Code: Expand Selection to Quotes"),
        "double quotes":
            R(Key("dquote"), rdescript="Quotation Marks"),
        "Quach it":
            R(Key("apostrophe"), rdescript="Thin Quotation Marks"),
        "(cellaring | sell rang) <n> <n3>":
            R(
                Key("c-g") + Pause("5") + Text("%(n)s") + Key("enter") + Pause("5") +
                Key("c-k") + Key("c-space") + Pause("5") + Key("c-g") + Pause("10") +
                Text("%(n3)s") + Key("enter") + Key("end") + Key("c-k") + Key("c-a")),
    }

    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 1000),
        IntegerRefST("n2", 1, 9),
        IntegerRefST("n3", 1, 999),
    ]
    defaults = {"n": 1, "mim": "", "text": ""}


context = AppContext(executable="code")
grammar = Grammar("Visual Studio Code", context=context)

if settings.SETTINGS["apps"]["visualstudiocode"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CustomVSCode())
    else:
        rule = CustomVSCode(name="sublime")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()


def get_rule():
    details = RuleDetails(executable="code",
                          title="Visual Studio Code",
                          ccrtype=CCRType.APP)
    return VSCodeCcrRule, details
