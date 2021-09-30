from dragonfly import Grammar, AppContext
from dragonfly.actions.action_text import Text

from caster.lib import control, settings
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter


class YarnCommands(MergeRule):
    pronunciation = "yarn commands"
    mapping = {
        "yarn":
            R(Text("yarn"), rdescript="Yarn: yarn"),
        "yarn global add":
            R(Text("yarn global add"), rdescript="Yarn: yarn global add"),
        "build my client":
            R(Text("yarn build client --env api-ashley"),
              rdescript="Yarn: yarn global add"),
        "build my API":
            R(Text("yarn build api --env api-ashley"), rdescript="Yarn: yarn global add"),
        "yarn client":
            R(Text("yarn client"), rdescript="Yarn: yarn global add"),
        "API ashley":
            R(Text("api-ashley"), rdescript="Yarn: yarn global add"),
    }
    extras = [
        IntegerRefST("n", 1, 10),
    ]
    defaults = {"n": 1}


control.nexus().merger.add_global_rule(YarnCommands())

context = AppContext(executable="\\sh.exe")
context2 = AppContext(executable="\\bash.exe")
context3 = AppContext(executable="\\mintty.exe")
context4 = AppContext(executable="\\ConEmu64.exe")

grammar = Grammar("MINGW32", context=(context | context2 | context3 | context4))

if settings.SETTINGS["apps"]["gitbash"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(YarnCommands())
    else:
        rule = YarnCommands(name="custom git bash")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
