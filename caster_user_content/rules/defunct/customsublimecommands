from dragonfly import (Grammar, AppContext, Dictation, Key, Pause)
from dragonfly.actions.action_key import Key
from dragonfly.actions.action_text import Text

from castervoice.lib import settings
from castervoice.lib import control
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge import gfilter
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.state.short import R


class CustomSublimeCommands(MergeRule):
    pronunciation = "custom sublime commands"
    mapping = {
        # my custom overrides
        "save file as":
            R(Key("cs-s"), rdescript="Sublime: Save As"),
        "grab it":
            R(Key("c-d"), rdescript="Sublime: Ctrl + d"),
        "skip it":
            R(Key("c-k,c-d"), rdescript="Sublime: Ctrl + d, k"),
        "execute":
            R(Key("c-b"), rdescript="Sublime: Ctrl + b"),
        "[go to] group [<n2>]":
            R(Key("c-%(n2)s"), rdescript="Sublime: Go to Group #"),
        "spring <n>":
            R(Key("c-g") + Pause("10") + Text("%(n)s") + Key("enter"),
              rdescript="Sublime: Go to Line #"),
        "crew [<text>]":
            R(Key("c-i") + Pause("10") + Text("%(text)s") + Key("enter") + Key("escape"),
              rdescript="Sublime: Get Next"),
        "trail [<text>]":
            R(Key("cs-i") + Pause("10") + Text("%(text)s") + Key("enter") + Key("escape"),
              rdescript="Sublime: Get Next"),
        "expand|fill quotes":
            R(Key("cs-space"), rdescript="Atom: Expand Selection to Quotes"),
        # SymbolSpecs.FUNCTION:                       R(Text("fu\\") + Key("tab"), rdescript="CustomSublime: Function"),
        # SymbolSpecs.IF:                             R(Text("if\\") + Key("tab"), rdescript="ColdFusion: If"),
        # my custom overrides
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


#---------------------------------------------------------------------------

context = AppContext(executable="sublime_text")
grammar = Grammar("Sublime", context=context)

if settings.SETTINGS["apps"]["sublime"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CustomSublimeCommands())
    else:
        rule = CustomSublimeCommands(name="sublime")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
